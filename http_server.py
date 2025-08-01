#!/usr/bin/env python3
"""
HTTP Server wrapper for Prompt Optimizer MCP Server

This provides HTTP transport for the MCP server when deployed.
"""

import os
import logging
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Literal
import uvicorn

from tools.optimize import optimize_prompt, score_prompt

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Prompt Optimizer MCP Server",
    description="A Model Context Protocol server for optimizing and scoring LLM prompts",
    version="1.0.0"
)

# Pydantic models for request/response
class OptimizeRequest(BaseModel):
    raw_prompt: str
    style: Literal['creative', 'precise', 'fast']

class OptimizeResponse(BaseModel):
    variants: List[str]

class ScoreRequest(BaseModel):
    raw_prompt: str
    improved_prompt: str

class ScoreResponse(BaseModel):
    score: float

class HealthResponse(BaseModel):
    status: str
    message: str

@app.get("/", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        message="Prompt Optimizer MCP Server is running"
    )

@app.post("/optimize", response_model=OptimizeResponse)
async def optimize_prompt_endpoint(request: OptimizeRequest):
    """Optimize a prompt using the specified style."""
    try:
        logger.info(f"Optimizing prompt with style: {request.style}")
        variants = optimize_prompt(request.raw_prompt, request.style)
        logger.info(f"Successfully generated {len(variants)} variants")
        return OptimizeResponse(variants=variants)
    except Exception as e:
        logger.error(f"Error optimizing prompt: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/score", response_model=ScoreResponse)
async def score_prompt_endpoint(request: ScoreRequest):
    """Score an improved prompt relative to the original."""
    try:
        logger.info("Scoring prompt improvement")
        score = score_prompt(request.raw_prompt, request.improved_prompt)
        logger.info(f"Score: {score}")
        return ScoreResponse(score=score)
    except Exception as e:
        logger.error(f"Error scoring prompt: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/tools")
async def list_tools():
    """List available tools."""
    return {
        "tools": [
            {
                "name": "optimize_prompt",
                "description": "Generate 3 optimized variants of a raw LLM prompt",
                "parameters": {
                    "raw_prompt": "string",
                    "style": "creative|precise|fast"
                }
            },
            {
                "name": "score_prompt", 
                "description": "Evaluate the effectiveness of an improved prompt",
                "parameters": {
                    "raw_prompt": "string",
                    "improved_prompt": "string"
                }
            }
        ]
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    
    logger.info(f"Starting HTTP server on {host}:{port}")
    uvicorn.run(app, host=host, port=port) 