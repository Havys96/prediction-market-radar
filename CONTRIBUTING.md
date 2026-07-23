# Contributing

Thanks for helping improve Prediction Market Radar.

This project is intentionally read-only. Contributions should keep that boundary.

## Good Contributions

- better public-data parsing
- better Radar Score formulas
- cleaner UI/UX
- watchlist persistence
- browser notifications
- Telegram or Discord descriptive alerts
- CSV or image export
- documentation improvements
- bug reports with API response examples

## Out Of Scope

Please do not add:

- order execution
- wallet connection
- private key input
- copy-trading
- betting recommendations
- financial advice
- profit guarantees
- geographic restriction bypasses

## Local Development

Run:

```bash
python server.py
```

Open:

```text
http://127.0.0.1:8765
```

Refresh snapshot data on Windows:

```powershell
.\update_snapshot.ps1
```

## Pull Request Checklist

- [ ] No secrets, private keys, API keys, or wallet credentials
- [ ] No trading/order execution behavior
- [ ] README safety boundary still applies
- [ ] App still runs with `python server.py`
- [ ] Screenshot or docs updated if UI changed

