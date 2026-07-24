from __future__ import annotations

import json
import py_compile
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent


REQUIRED_FILES = [
    "index.html",
    "package.json",
    "build-static.js",
    "server.py",
    "README.md",
    "DEMO.md",
    "PRELAUNCH_REVIEW.md",
    "LEGAL.md",
    "LICENSE",
    "VERSION",
    "CHANGELOG.md",
    ".github/FUNDING.yml",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    ".github/ISSUE_TEMPLATE/data_source_request.md",
    ".github/workflows/ci.yml",
    "docs/screenshot-desktop.png",
    "docs/screenshot-mobile.png",
    "data/markets.json",
    "data/whales.json",
    "data/history.json",
    "data/wallet-alpha.json",
]

REQUIRED_README_TEXT = [
    "No wallet connection",
    "No order execution",
    "Donations are optional",
    "v0.1.0",
]


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        raise SystemExit("Missing required files: " + ", ".join(missing))

    py_compile.compile(str(ROOT / "server.py"), doraise=True)

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    missing_text = [text for text in REQUIRED_README_TEXT if text not in readme]
    if missing_text:
        raise SystemExit("Missing README text: " + ", ".join(missing_text))

    for data_file in ["data/markets.json", "data/whales.json"]:
        with (ROOT / data_file).open("r", encoding="utf-8-sig") as handle:
            parsed = json.load(handle)
        if not isinstance(parsed, list):
            raise SystemExit(f"{data_file} must contain a JSON array")

    sys.path.insert(0, str(ROOT))
    import server  # noqa: PLC0415

    changes = server.build_history_changes([
        {"capturedAt": 0, "markets": [{"key": "m1", "title": "Market 1", "prob": 40, "volume": 1000, "liquidity": 500}]},
        {"capturedAt": 82800, "markets": [{"key": "m1", "title": "Market 1", "prob": 45, "volume": 3000, "liquidity": 500}]},
        {"capturedAt": 86500, "markets": [{"key": "m1", "title": "Market 1", "prob": 60, "volume": 9000, "liquidity": 500}]},
        {"capturedAt": 87400, "markets": [{"key": "m1", "title": "Market 1", "prob": 70, "volume": 12000, "liquidity": 500}]},
    ])
    row = changes["markets"][0]
    if row["windows"]["15m"]["probDelta"] != 10:
        raise SystemExit("15m history delta calculation failed")
    if row["windows"]["1h"]["probDelta"] != 25:
        raise SystemExit("1h history delta calculation failed")
    if row["windows"]["24h"]["probDelta"] != 30:
        raise SystemExit("24h history delta calculation failed")

    print("Smoke test passed.")


if __name__ == "__main__":
    main()
