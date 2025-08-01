#!/usr/bin/env python3
"""
Startup script for Prompt Optimizer MCP Server

This script determines whether to run in STDIO mode (for local development)
or HTTP mode (for deployment) based on environment variables.
"""

import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Main startup function."""
    # Check if we should run in HTTP mode (for deployment)
    if os.getenv("DEPLOYMENT_MODE", "").lower() == "http":
        logger.info("Starting in HTTP deployment mode")
        from http_server import app
        import uvicorn
        
        port = int(os.getenv("PORT", 8000))
        host = os.getenv("HOST", "0.0.0.0")
        
        logger.info(f"Starting HTTP server on {host}:{port}")
        uvicorn.run(app, host=host, port=port)
    else:
        # Default to STDIO mode (for local development and MCP clients)
        logger.info("Starting in STDIO mode")
        from server import app
        app.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Server failed to start: {e}")
        sys.exit(1) 