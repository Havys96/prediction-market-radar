# Upload Steps

Use this after creating an empty GitHub repository.

## 1. Create Empty GitHub Repo

Recommended:

- Repository name: `prediction-market-radar`
- Description: `Read-only prediction-market research dashboard for movers, anomalies, public whale trades, wallet analysis, local alerts, and reports.`
- Visibility: public
- Do not add README
- Do not add `.gitignore`
- Do not add license

This project already includes those files.

## 2. Copy Repo URL

Example:

```text
https://github.com/YOUR_NAME/prediction-market-radar.git
```

## 3. Publish From PowerShell

From this folder:

```powershell
.\publish.ps1 -RepoUrl "https://github.com/YOUR_NAME/prediction-market-radar.git"
```

If Git asks for login, use your GitHub browser login or a GitHub personal access token.

The script pushes:

- `main`
- tag `v0.1.0`

## 4. Configure Funding

After GitHub Sponsors or creator-support links are ready, edit:

```text
.github/FUNDING.yml
```

Recommended first version:

```yaml
github: [YOUR_GITHUB_USERNAME]
```

Keep crypto wallet addresses out of the first launch.

## 5. After Upload

Check:

- README screenshot renders
- Sponsor button appears only after funding is configured
- No secret files exist
- Repo description is set
- Topics are set
- Release `v0.1.0` is created
- Release notes use `RELEASE_NOTES_v0.1.0.md` and match `CHANGELOG.md`
- GitHub Actions CI passes
- `v0.1.0` tag is visible on GitHub

## 6. First Public Post

Use `FIRST_POST.md` for the first short post, or `LAUNCH.md` for longer variants.
