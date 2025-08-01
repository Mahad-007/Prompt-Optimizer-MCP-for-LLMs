#!/usr/bin/env python3
"""
Setup script for Prompt Optimizer MCP.
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="prompt-optimizer-mcp",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Model Context Protocol server for optimizing and scoring LLM prompts",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/prompt-optimizer-mcp",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/prompt-optimizer-mcp/issues",
        "Documentation": "https://github.com/yourusername/prompt-optimizer-mcp#readme",
        "Source Code": "https://github.com/yourusername/prompt-optimizer-mcp",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.11",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "flake8>=6.0.0",
            "black>=23.0.0",
            "bandit>=1.7.0",
            "safety>=2.0.0",
        ],
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "prompt-optimizer-mcp=server:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "mcp",
        "model-context-protocol",
        "prompt-engineering",
        "ai",
        "llm",
        "optimization",
        "scoring",
        "fastmcp",
    ],
    platforms=["any"],
    license="MIT",
    maintainer="Your Name",
    maintainer_email="your.email@example.com",
) 