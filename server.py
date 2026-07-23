from __future__ import annotations

import json
import mimetypes
import re
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, urlparse


ROOT = Path(__file__).resolve().parent
HTML = ROOT / "index.html"

UPSTREAMS = {
    "/api/markets": "https://gamma-api.polymarket.com/markets?active=true&closed=false&limit=80&order=volume24hr&ascending=false",
    "/api/leaderboard": "https://data-api.polymarket.com/v1/leaderboard?timePeriod=WEEK&orderBy=PNL&limit=10",
}

CACHE_FILES = {
    "/api/markets": ROOT / "data" / "markets.json",
    "/api/leaderboard": ROOT / "data" / "leaderboard.json",
    "/api/whales": ROOT / "data" / "whales.json",
}

WALLET_ENDPOINTS = {
    "/api/positions": "positions",
    "/api/closed-positions": "closed-positions",
    "/api/activity": "activity",
}

WALLET_RE = re.compile(r"^0x[a-fA-F0-9]{40}$")


class Handler(BaseHTTPRequestHandler):
    server_version = "PredictionMarketRadar/0.1"

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path in UPSTREAMS:
            self.proxy_json(UPSTREAMS[parsed.path], CACHE_FILES.get(parsed.path))
            return
        if parsed.path == "/api/whales":
            self.proxy_whales(parsed.query)
            return
        if parsed.path in WALLET_ENDPOINTS:
            self.proxy_wallet_json(parsed.path, parsed.query)
            return
        if parsed.path in {"/", "/index.html"}:
            self.send_file(HTML)
            return

        candidate = (ROOT / parsed.path.lstrip("/")).resolve()
        if ROOT in candidate.parents and candidate.is_file():
            self.send_file(candidate)
            return
        self.send_error(404, "Not found")

    def proxy_wallet_json(self, path: str, query: str) -> None:
        params = parse_qs(query)
        user = params.get("user", [""])[0]
        if not WALLET_RE.match(user):
            self.send_json({"error": "Invalid wallet address"}, status=400)
            return

        limit = params.get("limit", ["40"])[0]
        if not limit.isdigit() or not (1 <= int(limit) <= 100):
            limit = "40"

        endpoint = WALLET_ENDPOINTS[path]
        url = f"https://data-api.polymarket.com/{endpoint}?user={quote(user)}&limit={limit}"
        self.proxy_json(url, None)

    def proxy_whales(self, query: str) -> None:
        params = parse_qs(query)
        limit = params.get("limit", ["12"])[0]
        if not limit.isdigit() or not (1 <= int(limit) <= 50):
            limit = "12"
        threshold = params.get("threshold", ["1000"])[0]
        try:
            threshold_value = max(0.0, float(threshold))
        except ValueError:
            threshold_value = 1000.0

        try:
            trades = self.fetch_json("https://data-api.polymarket.com/trades?limit=300&takerOnly=false")
            rows = []
            for trade in trades if isinstance(trades, list) else []:
                size = float(trade.get("size") or 0)
                price = float(trade.get("price") or 0)
                usdc = float(trade.get("usdcSize") or (size * price))
                if usdc < threshold_value:
                    continue
                rows.append({
                    "proxyWallet": trade.get("proxyWallet", ""),
                    "side": trade.get("side", ""),
                    "outcome": trade.get("outcome", ""),
                    "title": trade.get("title", ""),
                    "slug": trade.get("slug", ""),
                    "timestamp": trade.get("timestamp", 0),
                    "name": trade.get("name", ""),
                    "pseudonym": trade.get("pseudonym", ""),
                    "price": price,
                    "size": size,
                    "usdcSize": usdc,
                    "transactionHash": trade.get("transactionHash", ""),
                })

            rows.sort(key=lambda item: item["usdcSize"], reverse=True)
            if not rows and CACHE_FILES["/api/whales"].exists():
                self.send_json_file(CACHE_FILES["/api/whales"])
                return
            self.send_json(rows[: int(limit)])
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            cache = CACHE_FILES["/api/whales"]
            if cache.exists():
                self.send_json_file(cache)
                return
            self.send_json({"error": str(exc)}, status=502)

    def proxy_json(self, url: str, cache: Path | None) -> None:
        try:
            body = json.dumps(self.fetch_json(url), ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            if cache and cache.exists():
                self.send_json_file(cache)
                return
            self.send_json({"error": str(exc)}, status=502)

    def fetch_json(self, url: str):
        req = urllib.request.Request(url, headers={"User-Agent": "PredictionMarketRadar/0.1"})
        with urllib.request.urlopen(req, timeout=12) as response:
            return json.loads(response.read().decode("utf-8"))

    def send_json(self, data, status: int = 200) -> None:
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def send_json_file(self, path: Path) -> None:
        body = path.read_bytes()
        if body.startswith(b"\xef\xbb\xbf"):
            body = body[3:]
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def send_file(self, path: Path) -> None:
        content_type = mimetypes.guess_type(str(path))[0] or "application/octet-stream"
        body = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        return


def main() -> None:
    server = ThreadingHTTPServer(("0.0.0.0", 8765), Handler)
    print("Prediction Market Radar running at http://127.0.0.1:8765", flush=True)
    print("From another device on the same network, open http://YOUR_PC_IP:8765", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
