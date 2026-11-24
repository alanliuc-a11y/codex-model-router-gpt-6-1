[CmdletBinding()]
param(
    [string]$CodexHome,
    [switch]$Disable,
    [switch]$Preview
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($CodexHome)) {
    $CodexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
}

$scriptDirectory = Split-Path -Parent $PSCommandPath
$skillDirectory = Split-Path -Parent $scriptDirectory
$fragmentPath = Join-Path $skillDirectory 'GLOBAL-ROUTING.md'
$agentsPath = Join-Path $CodexHome 'AGENTS.md'
$startMarker = '<!-- model-router:global-start -->'
$endMarker = '<!-- model-router:global-end -->'
$blockPattern = '(?s)<!-- model-router:global-start -->.*?<!-- model-router:global-end -->'

if (-not (Test-Path -LiteralPath $fragmentPath -PathType Leaf)) {
    throw "Missing routing fragment: $fragmentPath"
}

$existing = if (Test-Path -LiteralPath $agentsPath -PathType Leaf) {
    Get-Content -LiteralPath $agentsPath -Raw -Encoding utf8
} else {
    ''
}

$hasStart = $existing.Contains($startMarker)
$hasEnd = $existing.Contains($endMarker)
if ($hasStart -xor $hasEnd) {
    throw "Refusing to edit $agentsPath because its Model Router markers are incomplete. Repair the file manually first."
}

if ($Disable) {
    if (-not $hasStart) {
        Write-Output "Model Router global workflow is not enabled in $agentsPath."
        exit 0
    }
    $updated = [regex]::Replace($existing, $blockPattern, '').Trim()
    $action = 'remove the managed Model Router block from'
} else {
    $fragment = (Get-Content -LiteralPath $fragmentPath -Raw -Encoding utf8).Trim()
    $updated = if ($hasStart) {
        [regex]::Replace($existing, $blockPattern, [System.Text.RegularExpressions.MatchEvaluator]{ param($match) $fragment })
    } elseif ([string]::IsNullOrWhiteSpace($existing)) {
        $fragment + [Environment]::NewLine
    } else {
        $existing.TrimEnd() + [Environment]::NewLine + [Environment]::NewLine + $fragment + [Environment]::NewLine
    }
    $action = if ($hasStart) { 'update the managed Model Router block in' } else { 'add the managed Model Router block to' }
}

if ($Preview) {
    Write-Output "Would $action $agentsPath"
    exit 0
}

New-Item -ItemType Directory -Force -Path $CodexHome | Out-Null
if (Test-Path -LiteralPath $agentsPath -PathType Leaf) {
    $backupPath = "$agentsPath.model-router-backup-$([DateTime]::UtcNow.ToString('yyyyMMddHHmmssfff'))"
    Copy-Item -LiteralPath $agentsPath -Destination $backupPath
    Write-Output "Backup: $backupPath"
}

[System.IO.File]::WriteAllText($agentsPath, $updated, [System.Text.UTF8Encoding]::new($false))
Write-Output "Completed: $action $agentsPath"
