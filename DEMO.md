# Demo Walkthrough

This walkthrough shows what to check when reviewing Prediction Market Radar for the first time.

The app is a read-only research dashboard. It does not connect a wallet, request private keys, place orders, provide financial advice, provide betting advice, or bypass geographic restrictions.

## 1. Start The Local App

```bash
python smoke_test.py
python server.py
```

Open:

```text
http://127.0.0.1:8765
```

On Windows, `run.bat` starts the same local server.

## 2. Radar Tab

Use this tab to review public market activity.

Check:

- `Radar Score` ranking
- probability movement
- volume and liquidity
- anomaly count
- narrative clusters
- before/after movement log
- watchlist and local daily digest

Radar Score is a research-priority score. It is not a trading recommendation.

## 3. Wallets Tab

Use this tab to review public wallet activity.

Check:

- estimated public PnL
- win rate
- risk grade
- category breakdown
- recent public activity
- Wallet Alpha Ranking

Wallet data is public-data research only. The app does not connect to the wallet or control funds.

## 4. Alerts Tab

Use this tab to create local descriptive observation rules.

Available local rules:

- probability movement threshold
- anomaly score threshold
- large public trade threshold
- watchlist focus
- optional browser notification permission

Alerts are stored in the browser and are descriptive observations only. They are not signal alerts, entry instructions, copy-trade actions, or profit claims.

## 5. Reports Tab

Use this tab to export the current browser state.

Available exports:

- Markdown preview
- copy Markdown
- download Markdown
- download HTML

The exported report includes top markets, anomaly watch, watchlist focus, large public trades, Wallet Alpha candidates, and local alert observations.

## Review Checklist

- The app runs locally without an API key.
- The dashboard loads snapshot data even if live public APIs are unavailable.
- No wallet connection button exists.
- No private key input exists.
- No order execution exists.
- No copy-trading or betting instruction exists.
- The report export keeps the same research-only boundary.

