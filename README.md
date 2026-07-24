# Prediction Market Radar

![Version](https://img.shields.io/badge/version-v0.1.0-5db7ff)
![License](https://img.shields.io/badge/license-MIT-33c481)
![Wallet](https://img.shields.io/badge/wallet_connection-none-f0bd45)
![Execution](https://img.shields.io/badge/order_execution-none-f25d5d)

Read-only intelligence dashboard for prediction-market research.

Prediction Market Radar gives you one local screen for market movers, probability shifts, whale-sized public trades, and public wallet research without connecting a wallet or placing trades.

Prediction Market Radar helps you answer:

- What markets are moving right now?
- Where are large public trades appearing?
- Which public wallets are active or profitable?
- Which markets deserve research attention first?
- Is a wallet actually useful to study, or just noisy?

> Research dashboard only. No wallet connection, no private keys, no order execution, no trading or betting advice.

## Demo Path

1. Open the Radar tab to review market movers, anomaly cards, narrative clusters, and the local watchlist.
2. Open the Wallets tab to inspect public wallet PnL, activity, and Wallet Alpha Ranking.
3. Open the Alerts tab to configure local descriptive observation rules.
4. Open the Reports tab to export the current research snapshot as Markdown, HTML, or CSV.

See `DEMO.md` for the full review checklist.

See `PRELAUNCH_REVIEW.md` before publishing the repo.

## Why People Might Use It

Prediction markets are fragmented. A researcher often has to open market pages, wallet pages, leaderboards, trade feeds, and notes just to understand what changed.

This project compresses that loop into a small local dashboard:

| Problem | What the dashboard shows |
| --- | --- |
| Too many markets | Ranked market list with Radar Score |
| Hard to spot momentum | Probability, volume, liquidity, and close-time signals |
| Whale trades are noisy | Recent large public trades in one panel |
| Wallets are hard to judge | Public wallet PnL, win rate, risk grade, positions, and activity |
| Notes are scattered | Markdown, HTML, and CSV research export |
| API outages happen | Snapshot cache fallback under `data/` |

It is built as a public-data research tool, not a bot, not a signal service, and not a betting product.

## Screenshot

Desktop radar view:

![Prediction Market Radar desktop screenshot](docs/screenshot-desktop.png)

Mobile reports view:

![Prediction Market Radar mobile screenshot](docs/screenshot-mobile.png)

## Features

| Area | Included |
| --- | --- |
| Markets | active Polymarket markets, probability, volume, liquidity, Radar Score |
| Anomalies | anomaly detector, 15m/1h/24h server-history deltas, before/after movement log |
| Narratives | category-level attention clusters and top market summaries |
| Watchlist | browser-stored watchlist and local daily digest |
| Public trades | recent large public trade observations |
| Wallets | public wallet positions, closed positions, activity, estimated PnL, win rate, risk grade |
| Wallet Alpha | public wallet activity scoring and candidate ranking |
| Alerts | local rules, local observation log, optional browser notifications |
| Reports | Markdown, HTML, and CSV research snapshot export |
| Operations | local Python proxy, JSON snapshot fallback, smoke test, GitHub Actions CI |

Requires no API key.

## What It Does Not Do

- No order execution
- No private key input
- No wallet connection
- No copy-trading
- No financial advice
- No betting advice
- No geographic restriction bypass
- No guaranteed-profit claims

## Quick Start

Requirements:

- Python 3.10+
- Internet connection

Run:

```bash
python smoke_test.py
python server.py
```

Open:

```text
http://127.0.0.1:8765
```

On Windows, you can also run:

```text
run.bat
```

Demo checklist:

```text
DEMO.md
```

## Optional Snapshot Cache

The app includes cached JSON files under `data/` so the dashboard can still load a recent snapshot if the local Python process cannot reach the public APIs.

To refresh the snapshot on Windows:

```powershell
.\update_snapshot.ps1
```

The snapshot contains:

- `data/markets.json`
- `data/leaderboard.json`
- `data/whales.json`

## Data Sources

Public endpoints used:

- `https://gamma-api.polymarket.com/markets`
- `https://data-api.polymarket.com/trades`
- `https://data-api.polymarket.com/positions`
- `https://data-api.polymarket.com/closed-positions`
- `https://data-api.polymarket.com/activity`

The local server only proxies read-only public data and validates wallet address format before forwarding wallet-analysis requests.

## Radar Score

Radar Score is a research-priority score from 0 to 100.

It combines:

- probability movement
- 24h volume
- liquidity
- time to market close
- descriptive signals such as whale, news, or volume activity

Radar Score is not a trading recommendation.

## Project Status

MVP:

- live market list
- public large-trade radar
- market anomaly detector
- narrative tracker
- local watchlist and daily digest
- 15m/1h/24h probability-change history
- before/after movement log
- server-side market history file
- wallet scorecard
- wallet alpha ranking
- recent activity table
- local descriptive alerts
- Markdown, HTML, and CSV research exports
- local snapshot fallback

Current version:

```text
v0.1.0
```

Planned:

- Telegram and Discord alerts
- demo GIF or short video

## Safety Boundary

This project is for research and education only.

It does not place trades, connect wallets, provide financial advice, encourage betting, or bypass geographic restrictions.

See `LEGAL.md` for the full legal and safety notice.

## Support

If this project saves you time, you can support open-source development through GitHub Sponsors, Buy Me a Coffee, or Ko-fi.

Donations are optional and are not payment for signals, investment advice, betting advice, trading access, or restricted functionality.

See `FUNDING_GUIDE.md` before adding any funding links. The safest default is GitHub Sponsors first, creator-support links second, and no public personal crypto wallet address at launch.

## Suggested GitHub Topics

```text
polymarket
prediction-market
market-research
dashboard
wallet-analysis
whale-watcher
market-intelligence
alerts
open-source
```

## License

MIT
