#!/usr/bin/env python3
"""
Smithery Deployment Script for Prompt Optimizer MCP
"""

import subprocess
import sys
import os
import json
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return None

def check_prerequisites():
    """Check if all prerequisites are met."""
    print("🔍 Checking prerequisites...")
    
    # Check Python
    if not run_command("python --version", "Checking Python"):
        return False
    
    # Check if required files exist
    required_files = ["server.py", "requirements.txt", "smithery.yaml", "Dockerfile"]
    for file in required_files:
        if not Path(file).exists():
            print(f"❌ Required file {file} not found")
            return False
    
    print("✅ All prerequisites met")
    return True

def build_and_deploy():
    """Build and deploy to Smithery."""
    print("🚀 Starting Smithery deployment...")
    
    # Step 1: Build the project
    build_output = run_command("npx @smithery/cli build server.py", "Building MCP server")
    if not build_output:
        return False
    
    # Step 2: Deploy to Smithery
    deploy_output = run_command("npx @smithery/cli deploy", "Deploying to Smithery")
    if not deploy_output:
        return False
    
    print("✅ Deployment completed successfully!")
    return True

def main():
    """Main deployment function."""
    print("🚀 Prompt Optimizer MCP - Smithery Deployment")
    print("=" * 50)
    
    # Check prerequisites
    if not check_prerequisites():
        print("❌ Prerequisites check failed. Please fix the issues above.")
        sys.exit(1)
    
    # Build and deploy
    if not build_and_deploy():
        print("❌ Deployment failed. Please check the error messages above.")
        sys.exit(1)
    
    print("\n🎉 Deployment completed successfully!")
    print("Your MCP server should now be available on Smithery.")
    print("Check the Smithery dashboard for the deployment status.")

if __name__ == "__main__":
    main() 