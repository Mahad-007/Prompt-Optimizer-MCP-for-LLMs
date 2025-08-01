#!/usr/bin/env python3
"""
Prompt Optimizer MCP Server

A Model Context Protocol server that provides tools for optimizing and scoring LLM prompts.
"""

from typing import List, Literal
from mcp.server.fastmcp import FastMCP
from mcp.server.models import InitializationOptions
from tools.optimize import optimize_prompt, score_prompt

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
    return optimize_prompt(raw_prompt, style)

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
    return score_prompt(raw_prompt, improved_prompt)

if __name__ == "__main__":
    # Configure for STDIO transport (default for local development)
    app.run() 