# TescoCreate AI - Development Environment Launcher (Windows)
# Interactive script to start selected services

Write-Host "🚀 TescoCreate AI Development Environment" -ForegroundColor Green
Write-Host ""

# Function to check if command exists
function Test-Command($command) {
    try {
        Get-Command $command -ErrorAction Stop | Out-Null
        return $true
    }
    catch {
        return $false
    }
}

# Check prerequisites
Write-Host "📋 Checking prerequisites..." -ForegroundColor Yellow

$allGood = $true

if (-not (Test-Command node)) {
    Write-Host "❌ Node.js not found. Please install Node.js 20+"-ForegroundColor Red
    $allGood = $false
} else {
    $nodeVersion = node --version
    Write-Host "✅ Node.js: $nodeVersion" -ForegroundColor Green
}

if (-not (Test-Command pnpm)) {
    Write-Host "❌ pnpm not found. Install with: npm install -g pnpm" -ForegroundColor Red
    $allGood = $false
} else {
    $pnpmVersion = pnpm --version
    Write-Host "✅ pnpm: $pnpmVersion" -ForegroundColor Green
}

if (-not (Test-Command python)) {
    Write-Host "❌ Python not found. Please install Python 3.11+" -ForegroundColor Red
    $allGood = $false
} else {
    $pythonVersion = python --version
    Write-Host "✅ Python: $pythonVersion" -ForegroundColor Green
}

if (-not $allGood) {
    Write-Host "`n⚠️  Please install missing prerequisites and try again." -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# Check if .env.local exists
if (-not (Test-Path "apps/web/.env.local")) {
    Write-Host "⚠️  apps/web/.env.local not found" -ForegroundColor Yellow
    Write-Host "   Copy .env.example and fill in your Supabase credentials" -ForegroundColor Yellow
    Write-Host ""
}

# Interactive service selection
Write-Host "Select services to start:" -ForegroundColor Cyan
Write-Host ""

$startNext = Read-Host "Start Next.js (Frontend)? [Y/n]"
$startNext = if ($startNext -eq "" -or $startNext -eq "Y" -or $startNext -eq "y") { $true } else { $false }

$startCompliance = Read-Host "Start Compliance API (Python)? [Y/n]"
$startCompliance = if ($startCompliance -eq "" -or $startCompliance -eq "Y" -or $startCompliance -eq "y") { $true } else { $false }

$startImage = Read-Host "Start Image AI (Python)? [Y/n]"
$startImage = if ($startImage -eq "" -or $startImage -eq "Y" -or $startImage -eq "y") { $true } else { $false }

$startCreative = Read-Host "Start Creative AI (Python)? [y/N]"
$startCreative = if ($startCreative -eq "Y" -or $startCreative -eq "y") { $true } else { $false }

Write-Host ""
Write-Host "🚀 Starting selected services..." -ForegroundColor Green
Write-Host ""

# Start Next.js
if ($startNext) {
    Write-Host "▶️  Starting Next.js..." -ForegroundColor Cyan
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD\apps\web'; Write-Host '🌐 Next.js Dev Server' -ForegroundColor Blue; pnpm dev"
    Start-Sleep -Seconds 1
}

# Start Compliance API
if ($startCompliance) {
    Write-Host "▶️  Starting Compliance API..." -ForegroundColor Cyan
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD\services\compliance'; Write-Host '🔒 Compliance API' -ForegroundColor Blue; if (Test-Path '.venv\Scripts\Activate.ps1') { .\.venv\Scripts\Activate.ps1 } else { Write-Host '⚠️  Virtual environment not found. Run setup.ps1 first' -ForegroundColor Yellow }; python -m uvicorn app.main:app --reload --port 8000"
    Start-Sleep -Seconds 1
}

# Start Image AI
if ($startImage) {
    Write-Host "▶️  Starting Image AI..." -ForegroundColor Cyan
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD\services\image'; Write-Host '🖼️  Image AI' -ForegroundColor Blue; if (Test-Path '.venv\Scripts\Activate.ps1') { .\.venv\Scripts\Activate.ps1 } else { Write-Host '⚠️  Virtual environment not found. Run setup.ps1 first' -ForegroundColor Yellow }; python -m uvicorn app.main:app --reload --port 8001"
    Start-Sleep -Seconds 1
}

# Start Creative AI
if ($startCreative) {
    Write-Host "▶️  Starting Creative AI..." -ForegroundColor Cyan
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD\services\creative'; Write-Host '✨ Creative AI' -ForegroundColor Blue; if (Test-Path '.venv\Scripts\Activate.ps1') { .\.venv\Scripts\Activate.ps1 } else { Write-Host '⚠️  Virtual environment not found. Run setup.ps1 first' -ForegroundColor Yellow }; python -m uvicorn app.main:app --reload --port 8002"
    Start-Sleep -Seconds 1
}

Write-Host ""
Write-Host "✅ Services started!" -ForegroundColor Green
Write-Host ""
Write-Host "📊 Service URLs:" -ForegroundColor Cyan
if ($startNext) { Write-Host "   Frontend:    http://localhost:3000" }
if ($startCompliance) { Write-Host "   Compliance:  http://localhost:8000/docs" }
if ($startImage) { Write-Host "   Image AI:    http://localhost:8001/docs" }
if ($startCreative) { Write-Host "   Creative AI: http://localhost:8002/docs" }
Write-Host ""
Write-Host "💡 Tips:" -ForegroundColor Yellow
Write-Host "   - GPU usage: nvidia-smi" -ForegroundColor Gray
Write-Host "   - Close all: Close PowerShell windows" -ForegroundColor Gray
Write-Host ""
