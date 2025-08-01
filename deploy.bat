@echo off
REM Prompt Optimizer MCP - Smithery Deployment Script for Windows
REM This script automates the deployment process to Smithery

echo 🚀 Starting Prompt Optimizer MCP deployment to Smithery...
echo ==================================================

REM Check if smithery CLI is installed
where smithery >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Smithery CLI not found. Please install it first:
    echo    npm install -g @smithery/cli
    echo    or visit: https://smithery.ai/docs/installation
    pause
    exit /b 1
)

REM Check if user is logged in
smithery auth status >nul 2>nul
if %errorlevel% neq 0 (
    echo 🔐 Please log in to Smithery first:
    echo    smithery auth login
    pause
    exit /b 1
)

REM Validate configuration
echo 📋 Validating configuration...
if not exist "smithery.yaml" (
    echo ❌ smithery.yaml not found!
    pause
    exit /b 1
)

if not exist "Dockerfile" (
    echo ❌ Dockerfile not found!
    pause
    exit /b 1
)

if not exist "server.py" (
    echo ❌ server.py not found!
    pause
    exit /b 1
)

echo ✅ Configuration validated

REM Build and deploy
echo 🔨 Building and deploying to Smithery...
smithery deploy

echo ✅ Deployment completed!
echo.
echo 🌐 Your MCP server should now be available at:
echo    https://prompt-optimizer-mcp.smithery.ai
echo.
echo 📊 To check deployment status:
echo    smithery status
echo.
echo 📝 To view logs:
echo    smithery logs
echo.
echo 🔄 To update deployment:
echo    smithery deploy --force
echo.
pause 