from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("gnnvulapi")

GNNAPIBASE = "https://vishnugrao--c-code-analyzer-orchestrator.modal.run"

async def make_gnn_request(url: str, c_code: str) -> dict[str, Any] | None:
    """Make a request to the GNN API with proper error handling
    
    Args:
        url: The API endpoint URL
        c_code: A multiline string containing the C code to analyze
    """
    headers={
        "Content-Type": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            # Ensure the code is properly formatted as a string
            if not isinstance(c_code, str):
                return None
                
            # Format the code as a proper multiline string, preserving indentation
            formatted_code = c_code.strip()
            
            data = {
                "c_code": f"""{formatted_code}"""
            }
            response = await client.post(url, headers=headers, json=data, timeout=60.0)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return None
    
def format_prediction(prediction: dict) -> str:
    """Format a vulnerability prediction into a readable string."""
    return f"""
Analysis Results:
    Predicted Common Weakness Enumeration (CWE): {prediction['predicted_cwe']}
    Confidence: {prediction['confidence']:.2f}
"""

@mcp.tool()
async def check_vulnerability(c_code: str) -> str:
    """Check which vulnerability is most likely present in snippet of C code.
    
    Args:
        c_code: A multiline string containing the C code to analyze.
               The code should be a complete, compilable C program.
               Example:
               ```
               #include <stdio.h>
               #include <string.h>
               
               int main() {
                   char buffer[10];
                   strcpy(buffer, "This is too long");
                   return 0;
               }
               ```
               
               The code can be provided as a multiline string with proper indentation.
               All whitespace and newlines will be preserved.
    """
    # Validate input
    if not c_code or not isinstance(c_code, str):
        return "Invalid input: Code must be provided as a multiline string"

    # Clean up the code string while preserving newlines and indentation
    formatted_code = c_code.strip()
    
    url = f"{GNNAPIBASE}"
    data = await make_gnn_request(url, c_code=formatted_code)

    if not data or "predicted_cwe" not in data or "confidence" not in data:
        return "Unable to fetch the vulnerability that's most likely present in this code"
    
    return format_prediction(data)

if __name__ == "__main__":
    mcp.run(transport="stdio")

