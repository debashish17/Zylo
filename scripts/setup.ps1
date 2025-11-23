# TescoCreate AI - Complete Setup Script (Windows)

Write-Host "TescoCreate AI - Complete Setup" -ForegroundColor Green
Write-Host ("=" * 60)

# Step 1: Install Node.js dependencies
Write-Host "`nStep 1: Installing Node.js dependencies..." -ForegroundColor Cyan
pnpm install

if ($LASTEXITCODE -ne 0) {
    Write-Host "Failed to install Node.js dependencies" -ForegroundColor Red
    exit 1
}

# Step 2: Set up Python virtual environments
Write-Host "`nStep 2: Setting up Python virtual environments..." -ForegroundColor Cyan

$services = @("compliance", "image", "creative")

foreach ($service in $services) {
    Write-Host "`n  Setting up $service service..." -ForegroundColor Yellow

    $servicePath = "services/$service"

    # Create virtual environment
    if (-not (Test-Path "$servicePath/.venv")) {
        Write-Host "    Creating virtual environment..." -ForegroundColor Gray
        python -m venv "$servicePath/.venv"
    }

    # Activate and install dependencies
    Write-Host "    Installing dependencies..." -ForegroundColor Gray
    & "$servicePath/.venv/Scripts/Activate.ps1"
    pip install --upgrade pip
    pip install -r "$servicePath/requirements.txt"
    deactivate

    Write-Host "    $service ready" -ForegroundColor Green
}

# Step 3: Set up environment variables
Write-Host "`nStep 3: Setting up environment variables..." -ForegroundColor Cyan

if (-not (Test-Path "apps/web/.env.local")) {
    Write-Host "    Creating apps/web/.env.local from example..." -ForegroundColor Gray
    Copy-Item ".env.example" "apps/web/.env.local"
    Write-Host "    Please edit apps/web/.env.local with your Supabase credentials" -ForegroundColor Yellow
}

# Step 4: Create uploads directory
Write-Host "`nStep 4: Creating uploads directory..." -ForegroundColor Cyan
if (-not (Test-Path "uploads")) {
    New-Item -ItemType Directory -Path "uploads" | Out-Null
    Write-Host "    uploads/ created" -ForegroundColor Green
}

# Step 5: Test GPU (optional)
Write-Host "`nStep 5: Testing GPU..." -ForegroundColor Cyan
python scripts/test-gpu.py

# Done!
Write-Host "`n$("=" * 60)"
Write-Host "Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "  1. Configure Supabase credentials in apps/web/.env.local"
Write-Host "  2. Get API keys:"
Write-Host "     - Gemini: https://makersuite.google.com/app/apikey"
Write-Host "     - NVIDIA NIM: https://build.nvidia.com/"
Write-Host "  3. Set up Supabase database:"
Write-Host "     cd apps/web && pnpm prisma db push"
Write-Host "  4. Start development:"
Write-Host "     .\scripts\dev.ps1"
Write-Host ""
