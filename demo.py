#!/usr/bin/env python3
"""
Demo script for the Prompt Optimizer tools.

This script demonstrates the functionality of the prompt optimization tools
without requiring the MCP server to be running.
"""

from tools.optimize import optimize_prompt, score_prompt


def demo_optimize_prompt():
    """Demonstrate the optimize_prompt function with different styles."""
    print("🎯 PROMPT OPTIMIZATION DEMO")
    print("=" * 50)
    
    # Test prompt
    test_prompt = "Please write a very detailed explanation about machine learning and artificial intelligence"
    
    print(f"Original prompt: {test_prompt}")
    print()
    
    # Test each style
    for style in ['creative', 'precise', 'fast']:
        print(f"📝 {style.upper()} STYLE:")
        variants = optimize_prompt(test_prompt, style)
        
        for i, variant in enumerate(variants, 1):
            print(f"  Variant {i}: {variant}")
        
        print()


def demo_score_prompt():
    """Demonstrate the score_prompt function."""
    print("📊 PROMPT SCORING DEMO")
    print("=" * 50)
    
    # Test cases
    test_cases = [
        {
            "raw": "Please write a very detailed explanation about machine learning",
            "improved": "Write an explanation about machine learning",
            "description": "Improved (shorter, removes redundant words)"
        },
        {
            "raw": "Write about AI",
            "improved": "Please write a very detailed and comprehensive explanation about artificial intelligence",
            "description": "Worse (longer, adds redundant words)"
        },
        {
            "raw": "Write about artificial intelligence and machine learning",
            "improved": "Write about AI and ML",
            "description": "Similar (shorter but maintains keywords)"
        }
    ]
    
    for case in test_cases:
        score = score_prompt(case["raw"], case["improved"])
        print(f"Original: {case['raw']}")
        print(f"Improved: {case['improved']}")
        print(f"Score: {score:.3f} - {case['description']}")
        print()


def demo_integration():
    """Demonstrate the integration of optimize and score functions."""
    print("🔄 INTEGRATION DEMO")
    print("=" * 50)
    
    test_prompt = "Please write a very detailed explanation about machine learning"
    print(f"Original: {test_prompt}")
    print()
    
    for style in ['creative', 'precise', 'fast']:
        print(f"Style: {style}")
        variants = optimize_prompt(test_prompt, style)
        
        for i, variant in enumerate(variants, 1):
            score = score_prompt(test_prompt, variant)
            print(f"  Variant {i} (Score: {score:.3f}): {variant}")
        
        print()


def main():
    """Run all demos."""
    print("🚀 PROMPT OPTIMIZER MCP DEMO")
    print("=" * 60)
    print()
    
    try:
        demo_optimize_prompt()
        demo_score_prompt()
        demo_integration()
        
        print("✅ All demos completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during demo: {e}")
        print("Make sure you have installed the required dependencies:")
        print("pip install mcp-server-fastmcp")


if __name__ == "__main__":
    main() 