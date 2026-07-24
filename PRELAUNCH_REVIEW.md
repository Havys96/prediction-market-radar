# Prelaunch Review

Last reviewed for `v0.1.0`.

## Current Positioning

Prediction Market Radar is a read-only prediction-market research dashboard.

It is positioned as:

- public-data research dashboard
- market movement review tool
- wallet activity analysis tool
- local observation and report export tool
- open-source MVP

It is not positioned as:

- trading bot
- betting product
- signal service
- copy-trading tool
- geo-bypass tool
- profit product

## Implemented In v0.1.0

- Radar Score market ranking
- Market Anomaly Detector
- 15m/1h/24h probability-change history
- Narrative Tracker
- Watchlist and local daily digest
- Before/After Movement Log
- public large-trade observations
- public wallet scorecard
- Wallet Alpha Ranking
- local descriptive alert rules
- optional browser notifications
- Markdown report export
- HTML report export
- CSV exports for markets, trades, Wallet Alpha, and alerts
- local snapshot fallback
- GitHub-ready docs, CI, funding guide, security policy, and launch kit

## Final Local Checks

Run before publishing:

```bash
python smoke_test.py
python -m py_compile server.py smoke_test.py
```

Optional frontend check:

```bash
node build-static.js
```

Manual checks:

- README screenshots render.
- `DEMO.md` matches the current interface.
- Reports tab exports Markdown, HTML, and CSV.
- Alerts tab remains descriptive and local.
- No wallet connection or order execution exists.
- `.github/FUNDING.yml` still contains placeholders unless funding accounts are ready.
- No private keys, API keys, `.env`, wallet secrets, or personal crypto wallet addresses are committed.

## Launch Recommendation

Publish as a research dashboard first.

Do not market it as a way to profit, trade, bet, copy wallets, or access restricted markets.

