# 🤝 Contributing to Prompt Optimizer MCP

Thank you for your interest in contributing to Prompt Optimizer MCP! This document provides guidelines and information for contributors.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Release Process](#release-process)

## 📜 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## 🎯 How Can I Contribute?

### Reporting Bugs

- Use the GitHub issue tracker
- Include a clear and descriptive title
- Provide detailed steps to reproduce the bug
- Include your operating system and Python version
- Add any relevant error messages or logs

### Suggesting Enhancements

- Use the GitHub issue tracker with the "enhancement" label
- Describe the feature and why it would be useful
- Include any mockups or examples if applicable

### Code Contributions

- Fork the repository
- Create a feature branch
- Make your changes
- Add tests for new functionality
- Ensure all tests pass
- Submit a pull request

## 🛠️ Development Setup

### Prerequisites

- Python 3.11 or higher
- Git
- pip

### Local Development

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/yourusername/prompt-optimizer-mcp.git
   cd prompt-optimizer-mcp
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

4. **Install development dependencies:**
   ```bash
   pip install pytest pytest-cov flake8 black bandit safety
   ```

5. **Run tests to ensure everything works:**
   ```bash
   python -m pytest tests/ -v
   ```

## 📝 Coding Standards

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications:

- **Line length**: 88 characters (Black default)
- **Docstrings**: Google style
- **Type hints**: Required for all public functions

### Code Formatting

We use [Black](https://black.readthedocs.io/) for code formatting:

```bash
# Format all Python files
black .

# Check formatting without making changes
black --check --diff .
```

### Linting

We use [flake8](https://flake8.pycqa.org/) for linting:

```bash
# Run flake8
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics
```

### Security

We use [bandit](https://bandit.readthedocs.io/) for security checks:

```bash
# Run security checks
bandit -r . -f json -o bandit-report.json
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ -v --cov=tools --cov-report=html

# Run specific test file
python -m pytest tests/test_optimize.py -v

# Run specific test class
python -m pytest tests/test_optimize.py::TestOptimizePrompt -v
```

### Writing Tests

- Write tests for all new functionality
- Use descriptive test names
- Follow the AAA pattern (Arrange, Act, Assert)
- Use fixtures for common setup
- Aim for high test coverage

### Test Structure

```python
def test_function_name():
    """Test description."""
    # Arrange
    input_data = "test input"
    
    # Act
    result = function_to_test(input_data)
    
    # Assert
    assert result == expected_output
```

## 🔄 Pull Request Process

### Before Submitting

1. **Ensure tests pass:**
   ```bash
   python -m pytest tests/ -v
   ```

2. **Check code formatting:**
   ```bash
   black --check --diff .
   ```

3. **Run linting:**
   ```bash
   flake8 . --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics
   ```

4. **Run security checks:**
   ```bash
   bandit -r . -f json -o bandit-report.json
   ```

### Pull Request Guidelines

1. **Title**: Use a clear, descriptive title
2. **Description**: Explain what the PR does and why
3. **Fixes**: Link to any related issues
4. **Tests**: Ensure all tests pass
5. **Documentation**: Update docs if needed

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] Added tests for new functionality
- [ ] Updated existing tests

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes
```

## 🚀 Release Process

### Versioning

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Steps

1. **Update version in relevant files**
2. **Update CHANGELOG.md**
3. **Create release branch**
4. **Run full test suite**
5. **Create GitHub release**
6. **Deploy to Smithery**

## 📚 Documentation

### Code Documentation

- Use Google-style docstrings
- Include type hints
- Document all public functions and classes
- Provide usage examples

### Example Docstring

```python
def optimize_prompt(raw_prompt: str, style: Literal['creative', 'precise', 'fast']) -> List[str]:
    """Generate 3 optimized variants of the raw LLM prompt in the specified style.
    
    Args:
        raw_prompt: The original prompt to optimize
        style: The optimization style - 'creative', 'precise', or 'fast'
    
    Returns:
        List[str]: 3 optimized prompt variants
    
    Raises:
        TypeError: If inputs are not strings or style is invalid
    
    Example:
        >>> optimize_prompt("Write about AI", "creative")
        ['Craft a compelling story about AI', ...]
    """
```

## 🐛 Issue Templates

### Bug Report Template

```markdown
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Environment:**
- OS: [e.g. Windows 10]
- Python Version: [e.g. 3.11.0]
- Package Version: [e.g. 1.0.0]

**Additional context**
Add any other context about the problem here.
```

### Feature Request Template

```markdown
**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is.

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions.

**Additional context**
Add any other context or screenshots about the feature request here.
```

## 📞 Getting Help

- **Issues**: [GitHub Issues](https://github.com/yourusername/prompt-optimizer-mcp/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/prompt-optimizer-mcp/discussions)
- **Documentation**: [README.md](README.md)

## 🙏 Acknowledgments

Thank you to all contributors who have helped make this project better!

---

**Happy coding! 🚀** 