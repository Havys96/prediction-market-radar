# Prediction Market Radar

![Version](https://img.shields.io/badge/version-v0.1.0-5db7ff)
![License](https://img.shields.io/badge/license-MIT-33c481)
![Wallet](https://img.shields.io/badge/wallet_connection-none-f0bd45)
![Execution](https://img.shields.io/badge/order_execution-none-f25d5d)

Read-only intelligence dashboard for prediction markets.

Prediction Market Radar gives you one local screen for market movers, probability shifts, whale-sized public trades, and public wallet research without connecting a wallet or placing trades.

Prediction Market Radar helps you answer:

- What markets are moving right now?
- Where are large public trades appearing?
- Which public wallets are active or profitable?
- Which markets deserve research attention first?
- Is a wallet actually useful to study, or just noisy?

> Research dashboard only. No wallet connection, no private keys, no order execution, no trading or betting advice.

## Why People Might Use It

Prediction markets are fragmented. A researcher often has to open market pages, wallet pages, leaderboards, trade feeds, and notes just to understand what changed.

This project compresses that loop into a small local dashboard:

| Problem | What the dashboard shows |
| --- | --- |
| Too many markets | Ranked market list with Radar Score |
| Hard to spot momentum | Probability, volume, liquidity, and close-time signals |
| Whale trades are noisy | Recent large public trades in one panel |
| Wallets are hard to judge | Public wallet PnL, win rate, risk grade, positions, and activity |
| API outages happen | Snapshot cache fallback under `data/` |

It is built as a public-data research tool, not a bot, not a signal service, and not a betting product.

## Screenshot

Desktop:

![Prediction Market Radar desktop screenshot](docs/screenshot-desktop.png)

Mobile:

![Prediction Market Radar mobile screenshot](docs/screenshot-mobile.png)

## Features

- Shows active Polymarket markets from the public Gamma API
- Ranks markets by Radar Score
- Tracks recent large public trades
- Analyzes public wallet positions, closed positions, and activity
- Displays estimated PnL, win rate, category breakdown, and recent trades
- Detects unusual market activity with Market Anomaly Detector
- Tracks category-level narratives and attention clusters
- Stores a local watchlist and daily digest in the browser
- Logs before/after market movement from server snapshots, with browser fallback
- Scores public wallets with an Alpha Score research metric
- Ranks public wallet activity candidates with Wallet Alpha Ranking
- Keeps a small local `data/history.json` market history when run with `python server.py`
- Includes local snapshot fallback data
- Includes a local smoke test and GitHub Actions CI
- Works locally with a tiny Python proxy server
- Requires no API key

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
- before/after movement log
- server-side market history file
- wallet scorecard
- wallet alpha ranking
- recent activity table
- local snapshot fallback

Current version:

```text
v0.1.0
```

Planned:

- better probability-change history
- watchlist persistence
- browser notifications
- Telegram and Discord alerts
- exportable research reports
- screenshots and demo GIF

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
prediction-markets
prediction-market-dashboard
polymarket-analytics
whale-tracker
wallet-analyzer
pnl
market-intelligence
alerts
open-source
```

## License

MIT
