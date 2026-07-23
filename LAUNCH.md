# Launch Kit

## One-Line Description

Prediction Market Radar is a read-only Polymarket intelligence dashboard for market movers, public whale trades, and wallet PnL analysis.

## Short GitHub Description

Read-only prediction-market intelligence dashboard. Track Polymarket movers, whale trades, wallet PnL, and public activity without connecting a wallet or placing trades.

## X Post

I built Prediction Market Radar.

A read-only dashboard for Polymarket public data:

- market movers
- Radar Score
- recent large trades
- public wallet PnL
- category breakdown
- recent activity

No wallet connection.
No private keys.
No order execution.
No trading advice.

Open-source MVP:
<repo link>

## Longer X Thread

1/ I built an open-source prediction-market research dashboard: Prediction Market Radar.

It helps track public Polymarket data without connecting a wallet or placing trades.

2/ Current MVP:

- active market list
- Radar Score
- public large-trade feed
- wallet PnL scorecard
- category breakdown
- recent activity table
- local snapshot fallback

3/ The boundary is intentional:

- no private keys
- no wallet connection
- no order execution
- no copy-trading
- no financial or betting advice
- no geo-bypass features

4/ Why?

Prediction markets are noisy. Before making any judgment, you usually need market pages, wallet pages, leaderboards, trade feeds, and news tabs.

This compresses the research loop into one local dashboard.

5/ Built with:

- HTML/CSS/JS frontend
- tiny Python local proxy
- public Polymarket Gamma API
- public Polymarket Data API
- optional JSON snapshot cache

Repo:
<repo link>

## Reddit / Discord Post

I made a small open-source dashboard for Polymarket public data.

It is read-only and runs locally. It does not connect a wallet, ask for private keys, or place trades.

Current features:

- active market dashboard
- Radar Score ranking
- public large-trade detection
- wallet PnL scorecard
- recent public activity
- local snapshot cache

I built it as a research tool, not a trading bot. Feedback on data sources, scoring, and UX would be useful.

Repo:
<repo link>

## GitHub Release Notes

v0.1.0 - Local MVP

Initial release:

- single-page dashboard
- local Python server
- public market data proxy
- large-trade scanner
- wallet scorecard
- Radar Score
- snapshot cache fallback
- README safety boundary

Known limitations:

- probability-change history is approximate
- no persistent watchlist yet
- no browser/Telegram/Discord alerts yet
- wallet analysis depends on public Data API availability

## Launch Order

1. Publish the GitHub repo.
2. Confirm README screenshots render.
3. Confirm CI passes.
4. Create release `v0.1.0` from the pushed tag.
5. Add a short post on X.
6. Share in one relevant builder or data-analysis community.
7. Wait for feedback before adding execution, alerts, or paid features.

Do not launch it as a money-making tool. Launch it as a public-data research dashboard.

## First 7 Days

Day 1:

- Publish repo
- Pin repo on profile
- Post one short X post
- Ask for feedback on scoring, data sources, and UX

Day 2-3:

- Reply to every setup question
- Turn repeated questions into README fixes
- Label issues as `bug`, `data-source`, `ux`, or `feature`

Day 4-5:

- Ship one small improvement based on real feedback
- Avoid adding risky trading/betting language
- Keep the read-only safety boundary visible

Day 6-7:

- Write a short update post with what changed
- Ask users which feature matters most:
  - watchlist persistence
  - browser notifications
  - CSV export
  - better probability-change history
  - Telegram/Discord descriptive alerts

## Feedback Questions

Use these when posting or replying:

- Which panel is most useful: Market Radar, Whale Watch, or Wallet Scorecard?
- What data source should be added next?
- Is Radar Score easy to understand?
- What would make this worth starring?
- What would make this worth sponsoring as an open-source tool?

## Feature Priority After Launch

Do first if users ask for it:

1. Watchlist persistence
2. CSV export
3. Better probability-change history
4. Browser notifications
5. Telegram/Discord descriptive alerts

Do not add:

- order execution
- copy trading
- wallet connection
- private groups selling entries
- profit-sharing donation language
- geo-bypass instructions

## Donation Copy

If this project saved you time, you can support open-source development.

Donations are optional and are not payment for trading signals, betting advice, investment advice, order execution, restricted access, or profit-sharing.

Recommended funding order:

1. GitHub Sponsors
2. Buy Me a Coffee
3. Ko-fi

Avoid posting a personal crypto wallet address in the initial launch.
