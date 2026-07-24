# GitHub Setup

## Recommended Repository

Name:

```text
prediction-market-radar
```

Description:

```text
Read-only prediction-market research dashboard for movers, anomalies, public whale trades, wallet analysis, local alerts, and reports.
```

Topics:

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
git remote add origin https://github.com/Havys96/prediction-market-radar.git
git push -u origin main
```

On Windows, you can use the included helper:

```powershell
.\publish.ps1 -RepoUrl "https://github.com/Havys96/prediction-market-radar.git"
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
Initial local MVP with read-only public market data, Radar Score, anomaly detection, 15m/1h/24h history deltas, whale trade observations, wallet scorecard, Wallet Alpha Ranking, local alerts, Markdown/HTML/CSV exports, snapshot cache, and GitHub-ready documentation.
```

Release notes are also available in `RELEASE_NOTES_v0.1.0.md` and `CHANGELOG.md`.

## Profile Pin

If early response is good, pin the repo on your GitHub profile.

## First Public Post

Use `FIRST_POST.md` with the live GitHub URL:

```text
https://github.com/Havys96/prediction-market-radar
```

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
