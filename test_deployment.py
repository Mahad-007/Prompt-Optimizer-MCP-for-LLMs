#!/usr/bin/env python3
"""
Test script for Prompt Optimizer MCP Server

This script tests both the optimization and scoring functionality.
"""

import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_optimization():
    """Test the optimization functionality."""
    try:
        from tools.optimize import optimize_prompt
        
        # Test cases
        test_cases = [
            ("Write a story about a cat", "creative"),
            ("Please write a very detailed explanation about machine learning", "precise"),
            ("Could you help me understand artificial intelligence", "fast")
        ]
        
        for prompt, style in test_cases:
            logger.info(f"Testing optimization: '{prompt}' with style '{style}'")
            variants = optimize_prompt(prompt, style)
            
            if not isinstance(variants, list) or len(variants) != 3:
                raise ValueError(f"Expected 3 variants, got {len(variants)}")
            
            logger.info(f"✓ Generated {len(variants)} variants for style '{style}'")
            for i, variant in enumerate(variants, 1):
                logger.info(f"  Variant {i}: {variant[:50]}...")
        
        return True
    except Exception as e:
        logger.error(f"❌ Optimization test failed: {e}")
        return False

def test_scoring():
    """Test the scoring functionality."""
    try:
        from tools.optimize import score_prompt
        
        # Test cases
        test_cases = [
            ("Please write a very detailed explanation about machine learning", 
             "Write an explanation about machine learning"),
            ("Could you help me understand artificial intelligence",
             "Explain artificial intelligence"),
            ("Write a story about a cat",
             "Craft a compelling story about a cat")
        ]
        
        for raw, improved in test_cases:
            logger.info(f"Testing scoring: '{raw[:30]}...' vs '{improved[:30]}...'")
            score = score_prompt(raw, improved)
            
            if not isinstance(score, float) or score < 0 or score > 1:
                raise ValueError(f"Expected score between 0 and 1, got {score}")
            
            logger.info(f"✓ Score: {score}")
        
        return True
    except Exception as e:
        logger.error(f"❌ Scoring test failed: {e}")
        return False

def test_imports():
    """Test that all required modules can be imported."""
    try:
        logger.info("Testing imports...")
        
        # Test core modules
        import tools.optimize
        logger.info("✓ tools.optimize imported successfully")
        
        # Test server modules
        import server
        logger.info("✓ server imported successfully")
        
        # Test HTTP server modules
        import http_server
        logger.info("✓ http_server imported successfully")
        
        # Test FastAPI dependencies
        import fastapi
        import uvicorn
        import pydantic
        logger.info("✓ FastAPI dependencies imported successfully")
        
        return True
    except Exception as e:
        logger.error(f"❌ Import test failed: {e}")
        return False

def main():
    """Run all tests."""
    logger.info("Starting deployment tests...")
    
    tests = [
        ("Import Test", test_imports),
        ("Optimization Test", test_optimization),
        ("Scoring Test", test_scoring)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        logger.info(f"\n--- Running {test_name} ---")
        if test_func():
            passed += 1
            logger.info(f"✓ {test_name} PASSED")
        else:
            logger.error(f"❌ {test_name} FAILED")
    
    logger.info(f"\n--- Test Results ---")
    logger.info(f"Passed: {passed}/{total}")
    
    if passed == total:
        logger.info("🎉 All tests passed! Ready for deployment.")
        return 0
    else:
        logger.error("❌ Some tests failed. Please fix issues before deployment.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 