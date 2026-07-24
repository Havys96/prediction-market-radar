# Changelog

## v0.1.0 - Local MVP

Initial public-ready MVP.

### Added

- Single-page read-only dashboard
- Local Python proxy server
- Polymarket public market data view
- Radar Score ranking
- Recent public large-trade watch
- Public wallet scorecard
- Public wallet recent activity table
- Snapshot cache fallback under `data/`
- Desktop and mobile screenshots
- GitHub-ready README
- Launch copy for X, Reddit, Discord, and release notes
- Publish checklist
- Funding guide and `.github/FUNDING.yml`
- Security policy
- Contributing guide
- GitHub issue templates
- Windows `run.bat`
- Windows `publish.ps1`
- Windows `update_snapshot.ps1`
- Legal and safety notice
- GitHub Actions smoke test
- Local `smoke_test.py`
- Higher-conversion README intro with badges, feature table, and clearer positioning
- Launch playbook with first-week feedback plan
- Publish script now pushes the `v0.1.0` tag
- GitHub pull request template and data-source issue template
- Market Anomaly Detector
- Narrative Tracker
- Watchlist and Daily Digest
- Before/After Movement Log
- Wallet Alpha Score
- Server-side market history snapshots under `data/history.json`
- Wallet Alpha Ranking from recent public trade activity
- History-backed anomaly scoring with probability and volume deltas

### Safety Boundary

- No wallet connection
- No private key input
- No order execution
- No copy-trading
- No financial advice
- No betting advice
- No geographic restriction bypass
- No profit-sharing donation language

### Known Limitations

- Probability-change history is approximate and depends on public API fields.
- Watchlists are not persisted yet.
- Telegram and Discord alerts are documented but not implemented.
- Wallet analysis depends on public Data API availability.
- Snapshot cache can become stale until refreshed.
