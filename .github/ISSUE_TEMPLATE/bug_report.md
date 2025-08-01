---
name: Bug report
about: Create a report to help us improve
title: '[BUG] '
labels: ['bug']
assignees: ''
---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment:**
 - OS: [e.g. Windows 10, macOS 12.0, Ubuntu 20.04]
 - Python Version: [e.g. 3.11.0]
 - Package Version: [e.g. 1.0.0]
 - MCP Client: [e.g. Cursor, Claude Desktop]

**Additional context**
Add any other context about the problem here.

**Error Logs**
If applicable, paste any error logs or stack traces here.

```python
# Example of the error
from tools.optimize import optimize_prompt
result = optimize_prompt("test", "invalid_style")
# Error: TypeError: style must be one of: 'creative', 'precise', 'fast'
``` 