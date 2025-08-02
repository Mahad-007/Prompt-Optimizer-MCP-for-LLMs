#!/usr/bin/env python3
"""
Simple test script to verify the server functionality.
"""

import sys
import os

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(__file__))

def test_optimize_tools():
    """Test the optimize tools directly."""
    try:
        from tools.optimize import optimize_prompt, score_prompt
        
        print("Testing optimize_prompt function...")
        raw_prompt = "Write a story about a cat"
        
        # Test all styles
        for style in ['creative', 'precise', 'fast']:
            result = optimize_prompt(raw_prompt, style)
            print(f"  {style} style: {len(result)} variants generated")
            assert len(result) == 3, f"Expected 3 variants, got {len(result)}"
            assert all(isinstance(prompt, str) for prompt in result), "All variants should be strings"
        
        print("Testing score_prompt function...")
        improved_prompt = "Write a story about a cat"
        score = score_prompt(raw_prompt, improved_prompt)
        print(f"  Score: {score}")
        assert 0.0 <= score <= 1.0, f"Score should be between 0.0 and 1.0, got {score}"
        
        print("All tests passed!")
        return True
        
    except Exception as e:
        print(f"Test failed: {e}")
        return False

def test_http_server():
    """Test the HTTP server functionality."""
    try:
        import requests
        import time
        import subprocess
        import threading
        
        print("Testing HTTP server...")
        
        # Start the server in a separate process
        process = subprocess.Popen([
            sys.executable, "http_server.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait for server to start
        time.sleep(3)
        
        try:
            # Test health endpoint
            response = requests.get("http://localhost:8000/health", timeout=5)
            assert response.status_code == 200, f"Health check failed: {response.status_code}"
            print("  Health check passed")
            
            # Test optimize endpoint
            data = {
                "raw_prompt": "Write a story about a cat",
                "style": "creative"
            }
            response = requests.post("http://localhost:8000/optimize", json=data, timeout=5)
            assert response.status_code == 200, f"Optimize endpoint failed: {response.status_code}"
            result = response.json()
            assert "variants" in result, "Response should contain variants"
            assert len(result["variants"]) == 3, "Should return 3 variants"
            print("  Optimize endpoint passed")
            
            # Test score endpoint
            data = {
                "raw_prompt": "Write a story about a cat",
                "improved_prompt": "Write a story about a cat"
            }
            response = requests.post("http://localhost:8000/score", json=data, timeout=5)
            assert response.status_code == 200, f"Score endpoint failed: {response.status_code}"
            result = response.json()
            assert "score" in result, "Response should contain score"
            assert 0.0 <= result["score"] <= 1.0, "Score should be between 0.0 and 1.0"
            print("  Score endpoint passed")
            
            print("HTTP server tests passed!")
            return True
            
        finally:
            # Clean up
            process.terminate()
            process.wait()
            
    except Exception as e:
        print(f"HTTP server test failed: {e}")
        return False

if __name__ == "__main__":
    print("Running server tests...")
    
    # Test the optimize tools
    tools_ok = test_optimize_tools()
    
    # Test the HTTP server (if requests is available)
    try:
        import requests
        http_ok = test_http_server()
    except ImportError:
        print("requests not available, skipping HTTP server test")
        http_ok = True
    
    if tools_ok and http_ok:
        print("All tests passed!")
        sys.exit(0)
    else:
        print("Some tests failed!")
        sys.exit(1) 