# Funding Guide

This project should use funding links that look like open-source support, not trading compensation.

## Recommended Order

1. GitHub Sponsors
2. Buy Me a Coffee
3. Ko-fi

Avoid putting a personal crypto wallet address in the README at launch.

## Why Not A Wallet Address First?

A public wallet address creates extra issues:

- every donation is publicly traceable
- donors can be linked to transactions
- the address can be associated with other wallets
- it may look like payment for prediction-market profit, signals, or access
- tax and accounting explanations can become harder

If a crypto donation address is ever added, use a fresh donation-only wallet and keep the wording strict.

## Safe Donation Copy

Use:

```text
If this project saved you time, you can support open-source development.
Donations are optional and are not payment for trading signals, betting advice,
investment advice, order execution, restricted access, or profit-sharing.
```

Avoid:

```text
If you made money with this, send me a cut.
Support me if this helped you profit.
Donate for better signals.
Premium wallets and entries for sponsors.
```

## GitHub Sponsors Setup

1. Open GitHub Sponsors.
2. Enable sponsorship for your GitHub account if eligible.
3. Edit `.github/FUNDING.yml`.
4. Replace:

```yaml
# github: [your-github-username]
```

with:

```yaml
github: [YOUR_USERNAME]
```

5. Commit and push.
6. Confirm the Sponsor button appears on the GitHub repository.

## Buy Me a Coffee / Ko-fi

If using creator-support links, keep them secondary.

Example:

```yaml
custom:
  - https://www.buymeacoffee.com/YOUR_NAME
```

or:

```yaml
ko_fi: YOUR_KOFI_NAME
```

## README Placement

Keep the support section below the safety boundary, not at the top.

Good:

```text
This is a free, read-only research dashboard.
If it saved you time, optional support links are available.
```

Bad:

```text
Use this to find profitable opportunities. Support me with a share of profits.
```

