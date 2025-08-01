#!/usr/bin/env python3
"""
Prompt Optimizer MCP Server

A Model Context Protocol server that provides tools for optimizing and scoring LLM prompts.
"""

import logging
import sys
from typing import List, Literal
from fastmcp import FastMCP
from tools.optimize import optimize_prompt, score_prompt

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize the FastMCP server
app = FastMCP("prompt-optimizer")

@app.tool()
def optimize_prompt_tool(raw_prompt: str, style: Literal['creative', 'precise', 'fast']) -> List[str]:
    """
    Generate 3 optimized variants of the raw LLM prompt in the specified style.
    
    Args:
        raw_prompt: The original prompt to optimize
        style: The optimization style - 'creative' for imaginative variants, 
               'precise' for concise and focused variants, 'fast' for quick and direct variants
    
    Returns:
        List[str]: 3 optimized prompt variants
    """
    try:
        logger.info(f"Optimizing prompt with style: {style}")
        result = optimize_prompt(raw_prompt, style)
        logger.info(f"Successfully generated {len(result)} variants")
        return result
    except Exception as e:
        logger.error(f"Error optimizing prompt: {e}")
        raise

@app.tool()
def score_prompt_tool(raw_prompt: str, improved_prompt: str) -> float:
    """
    Evaluate the effectiveness of an improved prompt relative to the original.
    
    Returns a score from 0.0 to 1.0 based on:
    - Length optimization (shorter is better for most use cases)
    - Keyword preservation (maintaining important terms)
    - Clarity improvement (reduced redundancy)
    
    Args:
        raw_prompt: The original prompt
        improved_prompt: The optimized version to evaluate
    
    Returns:
        float: Effectiveness score between 0.0 and 1.0
    """
    try:
        logger.info("Scoring prompt improvement")
        result = score_prompt(raw_prompt, improved_prompt)
        logger.info(f"Score: {result}")
        return result
    except Exception as e:
        logger.error(f"Error scoring prompt: {e}")
        raise

if __name__ == "__main__":
    try:
        logger.info("Starting Prompt Optimizer MCP Server...")
        # Configure for STDIO transport (default for local development)
        app.run()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Server failed to start: {e}")
        sys.exit(1) 