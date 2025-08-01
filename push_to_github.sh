#!/bin/bash

# Prompt Optimizer MCP - GitHub Push Script
# This script helps you push your project to GitHub

set -e  # Exit on any error

echo "🚀 Setting up GitHub repository for Prompt Optimizer MCP..."
echo "=================================================="

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git not found. Please install Git first."
    exit 1
fi

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
else
    echo "✅ Git repository already initialized"
fi

# Add all files
echo "📝 Adding files to Git..."
git add .

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "ℹ️  No changes to commit"
else
    echo "💾 Making initial commit..."
    git commit -m "Initial commit: Prompt Optimizer MCP server

- Add MCP server with optimize_prompt and score_prompt tools
- Implement three optimization styles: creative, precise, fast
- Add comprehensive test suite with 14 test cases
- Include Docker containerization and Smithery deployment
- Add GitHub Actions CI/CD pipeline
- Include comprehensive documentation and contributing guidelines
- MIT License and proper Python packaging"
fi

# Check if remote origin exists
if ! git remote get-url origin &> /dev/null; then
    echo "🌐 No remote origin found."
    echo ""
    echo "To add a GitHub repository:"
    echo "1. Create a new repository on GitHub: https://github.com/new"
    echo "2. Name it: prompt-optimizer-mcp"
    echo "3. Make it public or private"
    echo "4. Don't initialize with README (we already have one)"
    echo "5. Copy the repository URL"
    echo ""
    echo "Then run:"
    echo "  git remote add origin https://github.com/YOUR_USERNAME/prompt-optimizer-mcp.git"
    echo "  git branch -M main"
    echo "  git push -u origin main"
    echo ""
    echo "Or if you want to use SSH:"
    echo "  git remote add origin git@github.com:YOUR_USERNAME/prompt-optimizer-mcp.git"
    echo "  git branch -M main"
    echo "  git push -u origin main"
else
    echo "✅ Remote origin already configured"
    echo "Current remote URL: $(git remote get-url origin)"
    echo ""
    echo "To push to GitHub:"
    echo "  git push -u origin main"
fi

echo ""
echo "📋 Next steps:"
echo "1. Create GitHub repository (if not done)"
echo "2. Add remote origin (if not done)"
echo "3. Push to GitHub: git push -u origin main"
echo "4. Enable GitHub Actions in repository settings"
echo "5. Set up branch protection rules"
echo "6. Configure repository topics: mcp, prompt-engineering, ai, llm"
echo ""
echo "🎉 Your Prompt Optimizer MCP is ready for GitHub!" 