# Security Policy

## Scope

Prediction Market Radar is a local, read-only dashboard for public prediction-market data.

The project should never request:

- private keys
- seed phrases
- wallet signatures
- exchange credentials
- API secrets
- browser wallet permissions

## Reporting Issues

Please open a GitHub issue for:

- accidental secret exposure
- unsafe dependency behavior
- incorrect wallet handling
- data endpoint misuse
- privacy-sensitive logging

Do not include real private keys, seed phrases, or sensitive wallet information in public issues.

## Safety Boundary

Security fixes should preserve the read-only boundary:

- no order execution
- no wallet connection
- no copy-trading
- no geo-bypass instructions
- no financial or betting advice

