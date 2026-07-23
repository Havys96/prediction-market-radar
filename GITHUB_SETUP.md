# GitHub Setup

## Recommended Repository

Name:

```text
prediction-market-radar
```

Description:

```text
Read-only prediction-market intelligence dashboard for Polymarket movers, whale trades, wallet PnL, and public activity.
```

Topics:

```text
polymarket
prediction-market
prediction-markets
dashboard
wallet-analyzer
whale-tracker
pnl
market-intelligence
open-source
```

## Create Local Git Repo

From this folder:

```bash
git init
python smoke_test.py
git add .
git commit -m "Initial Prediction Market Radar MVP"
```

Then create a GitHub repo and connect it:

```bash
git branch -M main
git remote add origin https://github.com/YOUR_NAME/prediction-market-radar.git
git push -u origin main
```

On Windows, you can use the included helper:

```powershell
.\publish.ps1 -RepoUrl "https://github.com/YOUR_NAME/prediction-market-radar.git"
```

## First Release

Tag:

```text
v0.1.0
```

Title:

```text
Prediction Market Radar v0.1.0
```

Release summary:

```text
Initial local MVP with read-only public market data, Radar Score, whale trade detection, wallet scorecard, snapshot cache, and GitHub-ready documentation.
```

Release notes are also available in `CHANGELOG.md`.

## Profile Pin

If early response is good, pin the repo on your GitHub profile.

## Important

Do not market this as:

- auto-trading
- betting signals
- profit tool
- copy-trading
- bypass tool

Market it as:

- public-data dashboard
- research terminal
- wallet analytics
- market intelligence
- open-source starter
