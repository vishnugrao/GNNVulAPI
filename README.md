# GNNVulAPI

A MCP Server for analyzing C code vulnerabilities using Graph Attention Networks (GAT).

## Description

GNNVulAPI provides a simple interface to analyze C code snippets for potential security vulnerabilities. It uses a GAT-based model to predict Common Weakness Enumeration (CWE) identifiers and confidence scores.

## Installation

```bash
pip install gnnvulapi
```

## Usage

```python
from gnnvulapi import check_vulnerability

# Example C code
c_code = """
#include <stdio.h>
#include <string.h>

int main() {
    char buffer[10];
    strcpy(buffer, "This is too long");
    return 0;
}
"""

# Check for vulnerabilities
result = await check_vulnerability(c_code)
print(result)
```

## API Reference

### `check_vulnerability(c_code: str) -> str`

Analyzes a C code snippet for potential vulnerabilities.

**Parameters:**
- `c_code` (str): A multiline string containing the C code to analyze. The code should be a complete, compilable C program.

**Returns:**
- A formatted string containing:
  - Predicted CWE identifier
  - Confidence score

## Dependencies

- httpx
- mcp

## Note

The code input must be a valid, compilable C program. All whitespace and newlines will be preserved in the analysis.
