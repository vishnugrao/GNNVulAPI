# GNNVulAPI

A MCP Server for analyzing C code vulnerabilities using Graph Attention Networks (GAT).

## Description

GNNVulAPI provides a simple interface to analyze C code snippets for potential security vulnerabilities. It uses a GAT-based model to predict Common Weakness Enumeration (CWE) identifiers and confidence scores.

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/gnnvulapi.git
cd gnnvulapi

```

## MCP Integration

### Configuration

Add the following to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "gnnvulapi": {
            "command": "/Users/vishnurao/.local/bin/uv",
            "args": [
                "--directory",
                "/Users/vishnurao/Desktop/Dev/ImplPractice/gnnvulapi",
                "run",
                "gnnvulapi.py"
            ]
        }
    }
}
```

Note: Replace the directory path with your actual workspace path where you cloned the repository.

### Starting the Server

```bash
uv run gnnvulapi.py
```

## Usage

Use through Claude desktop by pasting c code as a prompt with or without some instructions.

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
- uv (for running the server)

## Note

The code input must be a valid, compilable C program. All whitespace and newlines will be preserved in the analysis.

## Troubleshooting

If you encounter any issues:

1. Ensure `uv` is installed:
```bash
pip install uv
```

2. Verify the configuration path in `claude_desktop_config.json` matches your workspace location

3. Check that all dependencies are properly installed:
```bash
pip install -r requirements.txt
```
