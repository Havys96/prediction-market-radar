from __future__ import annotations

import json
import py_compile
from pathlib import Path


ROOT = Path(__file__).resolve().parent


REQUIRED_FILES = [
    "index.html",
    "server.py",
    "README.md",
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

    print("Smoke test passed.")


if __name__ == "__main__":
    main()
