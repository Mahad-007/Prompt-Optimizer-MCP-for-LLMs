#!/usr/bin/env python3
"""
Prompt Optimizer MCP Server

A Model Context Protocol server that provides tools for optimizing and scoring LLM prompts.
"""

import asyncio
import json
import logging
import sys
from typing import List, Literal, Any, Dict
from mcp import ServerSession, StdioServerParameters
from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from tools.optimize import optimize_prompt, score_prompt

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create MCP server
server = Server("prompt-optimizer")

@server.list_tools()
async def handle_list_tools() -> List[Dict[str, Any]]:
    """List available tools."""
    return [
        {
            "name": "optimize_prompt_tool",
            "description": "Generate 3 optimized variants of the raw LLM prompt in the specified style.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "raw_prompt": {
                        "type": "string",
                        "description": "The original prompt to optimize"
                    },
                    "style": {
                        "type": "string",
                        "enum": ["creative", "precise", "fast"],
                        "description": "The optimization style - 'creative' for imaginative variants, 'precise' for concise and focused variants, 'fast' for quick and direct variants"
                    }
                },
                "required": ["raw_prompt", "style"]
            }
        },
        {
            "name": "score_prompt_tool",
            "description": "Evaluate the effectiveness of an improved prompt relative to the original.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "raw_prompt": {
                        "type": "string",
                        "description": "The original prompt"
                    },
                    "improved_prompt": {
                        "type": "string",
                        "description": "The optimized version to evaluate"
                    }
                },
                "required": ["raw_prompt", "improved_prompt"]
            }
        }
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Handle tool calls."""
    try:
        if name == "optimize_prompt_tool":
            raw_prompt = arguments["raw_prompt"]
            style = arguments["style"]
            
            logger.info(f"Optimizing prompt with style: {style}")
            result = optimize_prompt(raw_prompt, style)
            logger.info(f"Successfully generated {len(result)} variants")
            
            return [
                {
                    "type": "text",
                    "text": f"Generated {len(result)} optimized variants:\n\n" + "\n\n".join(f"Variant {i+1}: {variant}" for i, variant in enumerate(result))
                }
            ]
            
        elif name == "score_prompt_tool":
            raw_prompt = arguments["raw_prompt"]
            improved_prompt = arguments["improved_prompt"]
            
            logger.info("Scoring prompt improvement")
            result = score_prompt(raw_prompt, improved_prompt)
            logger.info(f"Score: {result}")
            
            return [
                {
                    "type": "text",
                    "text": f"Effectiveness score: {result:.3f} (0.0 to 1.0 scale)"
                }
            ]
        else:
            raise ValueError(f"Unknown tool: {name}")
            
    except Exception as e:
        logger.error(f"Error in tool call {name}: {e}")
        raise

async def main():
    """Main function to run the MCP server."""
    try:
        logger.info("Starting Prompt Optimizer MCP Server...")
        
        # Run the server with stdio transport
        async with stdio_server() as (read_stream, write_stream):
            await server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="prompt-optimizer",
                    server_version="1.0.0",
                    capabilities=server.get_capabilities(
                        notification_options=NotificationOptions(),
                        experimental_capabilities={},
                    ),
                ),
            )
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Server failed to start: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main()) 