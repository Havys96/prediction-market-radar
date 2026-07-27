# Community Feedback Drafts

These drafts are for the next visibility test after the first X / Instagram posts.

The goal is to ask for feedback, not to sell, promise profits, or present the project as a trading product.

Repo:

```text
https://github.com/Havys96/prediction-market-radar
```

Recommended image:

```text
docs/demo-preview.gif
```

Fallback image:

```text
docs/social-preview.png
```

## Hacker News

Title:

```text
Show HN: A local radar for prediction-market public data
```

Body:

```text
I built a small open-source dashboard for reviewing prediction-market public data locally.

The problem I was trying to solve: prediction-market research often means jumping between market pages, trade feeds, wallet pages, notes, and exports just to understand what moved.

Prediction Market Radar puts that review loop into one local read-only screen:

- market movers
- probability shifts
- anomaly watch
- large public trade observations
- public wallet research
- local alerts
- Markdown / HTML / CSV exports

It does not connect wallets, request private keys, place orders, automate trades, provide signals, or give trading/betting advice.

I would appreciate feedback on the scoring logic, data sources, and whether the dashboard layout is useful.

Repo:
https://github.com/Havys96/prediction-market-radar
```

## Reddit

Suggested subreddits to evaluate first:

```text
r/opensource
r/SideProject
r/webdev
r/datasets
r/PredictionMarkets
```

Do not spam all of them at once. Pick one, wait, then decide.

Title:

```text
I built a local read-only dashboard for prediction-market public data. Looking for feedback.
```

Body:

```text
I built an open-source MVP called Prediction Market Radar.

It is a local dashboard for reviewing prediction-market public data without connecting a wallet or placing any orders.

What it currently shows:

- market movers
- probability shifts
- anomaly watch
- large public trade observations
- public wallet research
- local descriptive alerts
- Markdown / HTML / CSV exports

The main goal is to reduce the "open 20 tabs" research loop into one screen.

Important boundary:

- no wallet connection
- no private keys
- no order execution
- no copy-trading
- no financial advice
- no betting advice
- no geo-bypass features

I am looking for feedback on:

- whether the scoring model is understandable
- better public data sources
- dashboard UX
- what should be removed before adding more features

Repo:
https://github.com/Havys96/prediction-market-radar
```

## GitHub Issue Drafts

Create these as public issues if the repo needs clearer contribution paths.

### Issue 1

Title:

```text
Feedback wanted: scoring model and dashboard layout
```

Body:

```text
Prediction Market Radar v0.1.0 includes a first version of Radar Score and anomaly ranking.

Feedback wanted:

- Is the Radar Score explanation clear?
- Which signals should carry more or less weight?
- Are the anomaly cards useful?
- Which dashboard panels feel unnecessary?

Boundary: this project is read-only public-data research. It should not become a signal service, copy-trading tool, or order execution bot.
```

### Issue 2

Title:

```text
Data source ideas for public prediction-market research
```

Body:

```text
Looking for public data source ideas that could improve the dashboard without requiring private keys, wallet connection, paid APIs, or restricted access.

Useful categories:

- market metadata
- public trade observations
- public wallet activity
- liquidity / volume context
- news or event context
- historical probability movement

Please avoid requests for order execution, copy-trading, betting signals, or geo-bypass features.
```

### Issue 3

Title:

```text
Roadmap: make the research loop faster
```

Body:

```text
Possible next steps:

- clearer Radar Score explanation
- improved demo data
- better wallet alpha ranking notes
- Telegram / Discord descriptive alerts
- export polish
- live hosted read-only demo
- onboarding checklist for first-time users

The main product goal is to make public prediction-market research faster without connecting wallets, requesting keys, or placing orders.
```

## Avoid

- profit claims
- trading signal wording
- betting signal wording
- arbitrage bot wording
- auto-betting wording
- copy-trading wording
- geo-bypass wording
- "this will make money" framing
