#!/bin/bash

# Prompt Optimizer MCP - Smithery Deployment Script
# This script automates the deployment process to Smithery

set -e  # Exit on any error

echo "🚀 Starting Prompt Optimizer MCP deployment to Smithery..."
echo "=================================================="

# Check if smithery CLI is installed
if ! command -v smithery &> /dev/null; then
    echo "❌ Smithery CLI not found. Please install it first:"
    echo "   npm install -g @smithery/cli"
    echo "   or visit: https://smithery.ai/docs/installation"
    exit 1
fi

# Check if user is logged in
if ! smithery auth status &> /dev/null; then
    echo "🔐 Please log in to Smithery first:"
    echo "   smithery auth login"
    exit 1
fi

# Validate configuration
echo "📋 Validating configuration..."
if [ ! -f "smithery.yaml" ]; then
    echo "❌ smithery.yaml not found!"
    exit 1
fi

if [ ! -f "Dockerfile" ]; then
    echo "❌ Dockerfile not found!"
    exit 1
fi

if [ ! -f "server.py" ]; then
    echo "❌ server.py not found!"
    exit 1
fi

echo "✅ Configuration validated"

# Build and deploy
echo "🔨 Building and deploying to Smithery..."
smithery deploy

echo "✅ Deployment completed!"
echo ""
echo "🌐 Your MCP server should now be available at:"
echo "   https://prompt-optimizer-mcp.smithery.ai"
echo ""
echo "📊 To check deployment status:"
echo "   smithery status"
echo ""
echo "📝 To view logs:"
echo "   smithery logs"
echo ""
echo "🔄 To update deployment:"
echo "   smithery deploy --force" 