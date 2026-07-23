$ErrorActionPreference = "Stop"

param(
  [Parameter(Mandatory = $true)]
  [string]$RepoUrl
)

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

if (-not (Test-Path -LiteralPath ".git")) {
  git init -b main
}

$remote = git remote get-url origin 2>$null
if ($LASTEXITCODE -ne 0) {
  git remote add origin $RepoUrl
} elseif ($remote -ne $RepoUrl) {
  Write-Output "Existing origin: $remote"
  Write-Output "Updating origin to: $RepoUrl"
  git remote set-url origin $RepoUrl
}

$status = git status --short
if ($status) {
  Write-Output "Uncommitted changes found:"
  Write-Output $status
  Write-Output "Commit or discard changes before publishing."
  exit 1
}

git branch -M main
git push -u origin main

Write-Output "Published to $RepoUrl"

