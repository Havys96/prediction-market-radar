# Publish Checklist

## Before Creating The GitHub Repo

- [ ] Choose repository name: `prediction-market-radar`
- [ ] Set description:
  `Read-only prediction-market intelligence dashboard for Polymarket movers, whale trades, wallet PnL, and public activity.`
- [ ] Add topics:
  `polymarket`, `prediction-market`, `dashboard`, `wallet-analyzer`, `whale-tracker`, `pnl`, `market-intelligence`
- [ ] Confirm README screenshot renders
- [ ] Confirm no private keys, API keys, wallet secrets, or `.env` files exist
- [ ] Confirm safety boundary is visible in README
- [ ] Configure `.github/FUNDING.yml` only after GitHub Sponsors / creator-support links are ready
- [ ] Do not publish a personal crypto wallet address at launch

## Local Test

Run:

```bash
python server.py
```

Open:

```text
http://127.0.0.1:8765
```

Check:

- [ ] Dashboard loads
- [ ] Market rows render
- [ ] Whale Watch renders
- [ ] Wallet Scorecard works with a public 0x address
- [ ] README Angle page shows safety text
- [ ] Refresh button does not request wallet permissions
- [ ] Support section does not imply payment for profit, entries, signals, or restricted access

## Launch Steps

1. Create GitHub repository.
2. Upload all files in this folder.
3. Add screenshots from `docs/`.
4. Create first release: `v0.1.0`.
5. Use `LAUNCH.md` for X, Reddit, Discord, and release notes.
6. Pin the repo on GitHub profile if the initial response is good.

Shortcut:

```powershell
.\publish.ps1 -RepoUrl "https://github.com/YOUR_NAME/prediction-market-radar.git"
```

## First 30-Day Goal

- 50 GitHub stars
- 5 issues or feature requests
- 3 users asking for setup help
- 1 sponsor/donation
- 1 useful external share

## Safe Support Copy

Use:

> If this project saved you time, you can support open-source development. Donations are optional and are not payment for trading signals, betting advice, investment advice, order execution, restricted access, or profit-sharing.

Avoid:

- "If you made money, send me a cut"
- "Use this to profit"
- "Trading signals"
- "Copy profitable wallets"
- "Auto-bet"
- "Bypass restrictions"
