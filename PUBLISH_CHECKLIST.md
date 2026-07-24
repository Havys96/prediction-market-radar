# Publish Checklist

## Before Creating The GitHub Repo

- [ ] Choose repository name: `prediction-market-radar`
- [ ] Set description:
  `Read-only prediction-market research dashboard for movers, anomalies, public whale trades, wallet analysis, local alerts, and reports.`
- [ ] Add topics:
  `polymarket`, `prediction-market`, `dashboard`, `wallet-analyzer`, `whale-tracker`, `pnl`, `market-intelligence`, `alerts`, `open-source`
- [ ] Confirm README screenshot renders
- [ ] Confirm `DEMO.md` and `PRELAUNCH_REVIEW.md` match the current interface
- [ ] Confirm no private keys, API keys, wallet secrets, or `.env` files exist
- [ ] Confirm safety boundary is visible in README
- [ ] Confirm `LEGAL.md` is visible and linked from README
- [ ] Confirm GitHub Actions CI passes
- [ ] Configure `.github/FUNDING.yml` only after GitHub Sponsors / creator-support links are ready
- [ ] Do not publish a personal crypto wallet address at launch

## Local Test

Run:

```bash
python smoke_test.py
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
- [ ] Reports tab shows README hook, Markdown/HTML export, and CSV export
- [ ] Alerts tab stores local descriptive observations only
- [ ] Refresh button does not request wallet permissions
- [ ] Support section does not imply payment for profit, entries, signals, or restricted access

## Launch Steps

1. Create GitHub repository.
2. Upload all files in this folder.
3. Add screenshots from `docs/`.
4. Push release tag `v0.1.0`.
5. Create first GitHub release from tag `v0.1.0` using `RELEASE_NOTES_v0.1.0.md`.
6. Confirm GitHub Actions CI passes.
7. Use `FIRST_POST.md` or `LAUNCH.md` for X, Reddit, Discord, and release notes.
8. Pin the repo on GitHub profile if the initial response is good.

Shortcut:

```powershell
.\publish.ps1 -RepoUrl "https://github.com/YOUR_NAME/prediction-market-radar.git"
```

The shortcut pushes `main` and the `v0.1.0` tag.

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
