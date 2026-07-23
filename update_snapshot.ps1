$ErrorActionPreference = "Stop"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$data = Join-Path $root "data"
if (-not (Test-Path -LiteralPath $data)) {
  New-Item -ItemType Directory -Path $data | Out-Null
}

$marketsUrl = "https://gamma-api.polymarket.com/markets?active=true&closed=false&limit=80&order=volume24hr&ascending=false"
$leaderboardUrl = "https://data-api.polymarket.com/v1/leaderboard?timePeriod=WEEK&orderBy=PNL&limit=10"
$tradesUrl = "https://data-api.polymarket.com/trades?limit=300&takerOnly=false"

$markets = Invoke-RestMethod -Uri $marketsUrl
$leaderboard = Invoke-RestMethod -Uri $leaderboardUrl
$trades = Invoke-RestMethod -Uri $tradesUrl

$whales = $trades |
  ForEach-Object {
    $size = 0.0
    $price = 0.0
    if ($_.PSObject.Properties.Name -contains "size") { $size = [double]$_.size }
    if ($_.PSObject.Properties.Name -contains "price") { $price = [double]$_.price }
    $usdc = if ($_.PSObject.Properties.Name -contains "usdcSize") { [double]$_.usdcSize } else { $size * $price }
    if ($usdc -ge 1000) {
      [PSCustomObject]@{
        proxyWallet = $_.proxyWallet
        side = $_.side
        outcome = $_.outcome
        title = $_.title
        slug = $_.slug
        timestamp = $_.timestamp
        name = $_.name
        pseudonym = $_.pseudonym
        price = $price
        size = $size
        usdcSize = $usdc
        transactionHash = $_.transactionHash
      }
    }
  } |
  Sort-Object -Property usdcSize -Descending |
  Select-Object -First 50

$markets | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath (Join-Path $data "markets.json") -Encoding UTF8
$leaderboard | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath (Join-Path $data "leaderboard.json") -Encoding UTF8
$whales | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath (Join-Path $data "whales.json") -Encoding UTF8

Write-Output "Snapshot updated:"
Get-ChildItem -LiteralPath $data | Select-Object Name, Length, LastWriteTime
