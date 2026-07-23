# Prediction Market Radar

Read-only intelligence dashboard for prediction markets.

Find where probability, volume, and public wallet activity are moving without connecting a wallet or placing trades.

Prediction Market Radar helps you answer:

- What markets are moving right now?
- Which public wallets are active?
- Where are large trades appearing?
- Which markets deserve research attention first?
- Is a wallet actually profitable, or just noisy?

> Research dashboard only. No wallet connection, no private keys, no order execution, no trading or betting advice.

## Screenshot

Desktop:

![Prediction Market Radar desktop screenshot](docs/screenshot-desktop.png)

Mobile:

![Prediction Market Radar mobile screenshot](docs/screenshot-mobile.png)

## What It Does

- Shows active Polymarket markets from the public Gamma API
- Ranks markets by Radar Score
- Tracks recent large public trades
- Analyzes public wallet positions, closed positions, and activity
- Displays estimated PnL, win rate, category breakdown, and recent trades
- Works locally with a tiny Python proxy server
- Requires no API key

## Why This Exists

Prediction markets are noisy. A user often needs to open market pages, wallet pages, leaderboards, trade feeds, and news tabs just to understand what changed.

This project compresses that research loop into one local dashboard.

The goal is not to tell users what to buy. The goal is to surface public information faster and more clearly.

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
python server.py
```

Open:

```text
http://127.0.0.1:8765
```

Optional local check:

```bash
python smoke_test.py
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
- wallet scorecard
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
