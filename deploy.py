#!/usr/bin/env python3
"""
Deployment script for Prompt Optimizer MCP Server.
"""

import os
import sys
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_command(command, description):
    """Run a command and log the result."""
    logger.info(f"Running: {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        logger.info(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"✗ {description} failed: {e}")
        logger.error(f"stdout: {e.stdout}")
        logger.error(f"stderr: {e.stderr}")
        return False

def main():
    """Main deployment function."""
    logger.info("Starting deployment process...")
    
    # Check if we're in the right directory
    if not os.path.exists("server.py"):
        logger.error("server.py not found. Please run this script from the project root.")
        sys.exit(1)
    
    # Step 1: Run tests
    logger.info("Step 1: Running tests...")
    if not run_command("python test_server.py", "Server tests"):
        logger.error("Tests failed. Deployment aborted.")
        sys.exit(1)
    
    # Step 2: Install dependencies
    logger.info("Step 2: Installing dependencies...")
    if not run_command("pip install -r requirements.txt", "Install dependencies"):
        logger.error("Dependency installation failed. Deployment aborted.")
        sys.exit(1)
    
    # Step 3: Run linting
    logger.info("Step 3: Running linting...")
    try:
        import flake8
        if not run_command("flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics", "Flake8 syntax check"):
            logger.warning("Flake8 syntax check failed, but continuing...")
    except ImportError:
        logger.info("Flake8 not available, skipping linting...")
    
    # Step 4: Build Docker image (if Docker is available)
    logger.info("Step 4: Building Docker image...")
    try:
        if not run_command("docker build -t prompt-optimizer-mcp:latest .", "Docker build"):
            logger.warning("Docker build failed, but continuing...")
        else:
            # Test the Docker image
            if run_command("docker run --rm prompt-optimizer-mcp:latest python -c 'from tools.optimize import optimize_prompt; print(\"Docker test passed\")'", "Docker test"):
                logger.info("✓ Docker image built and tested successfully")
            else:
                logger.warning("Docker test failed")
    except FileNotFoundError:
        logger.info("Docker not available, skipping Docker build...")
    
    # Step 5: Create deployment package
    logger.info("Step 5: Creating deployment package...")
    deployment_files = [
        "server.py",
        "http_server.py", 
        "start.py",
        "requirements.txt",
        "tools/",
        "tests/",
        "Dockerfile",
        "README.md"
    ]
    
    # Create a simple deployment package
    if os.name == 'nt':  # Windows
        if not run_command("powershell -Command \"Compress-Archive -Path " + ",".join(deployment_files) + " -DestinationPath deployment.zip -Force\"", "Create deployment package"):
            logger.warning("Failed to create deployment package")
    else:  # Unix/Linux
        if not run_command("tar -czf deployment.tar.gz " + " ".join(deployment_files), "Create deployment package"):
            logger.warning("Failed to create deployment package")
    
    logger.info("✓ Deployment process completed successfully!")
    logger.info("The server is ready for deployment.")
    logger.info("You can now:")
    logger.info("  1. Push to GitHub to trigger CI/CD")
    logger.info("  2. Deploy the Docker image to your preferred platform")
    logger.info("  3. Run the server locally with: python start.py")

if __name__ == "__main__":
    main() 