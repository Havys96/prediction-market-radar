# Prediction Market Radar v0.1.0

Initial public-ready local MVP.

Prediction Market Radar is a read-only prediction-market research dashboard for public Polymarket data. It is built for market review, wallet activity research, descriptive local alerts, and exportable research snapshots.

## Highlights

- Single-page local dashboard
- Tiny Python proxy server
- Public market data view
- Radar Score ranking
- Market Anomaly Detector
- 15m/1h/24h probability-change history
- Narrative Tracker
- public large-trade observations
- public wallet scorecard
- Wallet Alpha Ranking
- local watchlist and daily digest
- local descriptive alert rules
- optional browser notifications
- Markdown report export
- HTML report export
- CSV exports for markets, trades, Wallet Alpha, and alerts
- local snapshot fallback
- GitHub-ready docs, screenshots, issue templates, funding guide, and CI

## Safety Boundary

This project is for research and education only.

It does not:

- connect wallets
- request private keys
- place orders
- provide financial advice
- provide betting advice
- copy-trade wallets
- bypass geographic restrictions
- promise profits

## Known Limitations

- Probability-change history depends on the local server collecting enough snapshots.
- Browser notifications require explicit browser permission.
- Telegram and Discord alerts are not implemented.
- Wallet analysis depends on public Data API availability.
- Snapshot cache can become stale until refreshed.

## Local Start

```bash
python smoke_test.py
python server.py
```

Open:

```text
http://127.0.0.1:8765
```

