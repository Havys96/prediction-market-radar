from __future__ import annotations

import json
import mimetypes
import re
import threading
import time
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

HISTORY_FILE = ROOT / "data" / "history.json"
HISTORY_LOCK = threading.Lock()
MAX_HISTORY_SNAPSHOTS = 96

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
        if parsed.path == "/api/history":
            self.send_history(parsed.query)
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
            data = self.fetch_json(url)
            if cache == CACHE_FILES.get("/api/markets"):
                append_market_history(data)
            body = json.dumps(data, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            if cache and cache.exists():
                data = read_json_file(cache)
                if cache == CACHE_FILES.get("/api/markets"):
                    append_market_history(data)
                self.send_json(data)
                return
            self.send_json({"error": str(exc)}, status=502)

    def send_history(self, query: str) -> None:
        params = parse_qs(query)
        limit = params.get("limit", ["12"])[0]
        if not limit.isdigit() or not (1 <= int(limit) <= MAX_HISTORY_SNAPSHOTS):
            limit = "12"
        history = read_history()
        self.send_json(history[-int(limit):])

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


def parse_json_array(value):
    if isinstance(value, list):
        return value
    if not isinstance(value, str):
        return []
    try:
        parsed = json.loads(value)
        return parsed if isinstance(parsed, list) else []
    except ValueError:
        return []


def first_number(*values: object) -> float:
    for value in values:
        try:
            number = float(value)
        except (TypeError, ValueError):
            continue
        if number == number and number not in {float("inf"), float("-inf")}:
            return number
    return 0.0


def normalize_market_snapshot(markets) -> list[dict[str, object]]:
    rows = []
    for market in markets if isinstance(markets, list) else []:
        if not isinstance(market, dict):
            continue
        title = market.get("question") or market.get("title")
        if not title:
            continue
        outcomes = parse_json_array(market.get("outcomes"))
        prices = [first_number(price) for price in parse_json_array(market.get("outcomePrices"))]
        yes_index = 0
        for index, outcome in enumerate(outcomes):
            if str(outcome).lower() == "yes":
                yes_index = index
                break
        yes_price = prices[yes_index] if yes_index < len(prices) else first_number(market.get("lastTradePrice"), market.get("bestBid"))
        rows.append({
            "key": str(market.get("conditionId") or market.get("slug") or title)[:140],
            "title": title,
            "prob": round(max(0.0, min(1.0, yes_price)) * 100, 2),
            "volume": first_number(market.get("volume24hr"), market.get("volume24hrClob"), market.get("volumeNum"), market.get("volume")),
            "liquidity": first_number(market.get("liquidityNum"), market.get("liquidityClob"), market.get("liquidity")),
            "endDate": market.get("endDate"),
        })
    return rows[:80]


def read_history() -> list[dict[str, object]]:
    data = read_json_file(HISTORY_FILE)
    return data if isinstance(data, list) else []


def read_json_file(path: Path):
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, ValueError):
        return []


def append_market_history(markets) -> None:
    snapshot = normalize_market_snapshot(markets)
    if not snapshot:
        return
    entry = {
        "capturedAt": int(time.time()),
        "markets": snapshot,
    }
    with HISTORY_LOCK:
        history = read_history()
        if history and int(history[-1].get("capturedAt", 0)) > entry["capturedAt"] - 45:
            history[-1] = entry
        else:
            history.append(entry)
        HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
        HISTORY_FILE.write_text(
            json.dumps(history[-MAX_HISTORY_SNAPSHOTS:], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )


def main() -> None:
    server = ThreadingHTTPServer(("0.0.0.0", 8765), Handler)
    print("Prediction Market Radar running at http://127.0.0.1:8765", flush=True)
    print("From another device on the same network, open http://YOUR_PC_IP:8765", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
