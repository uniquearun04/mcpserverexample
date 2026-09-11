# server.py
from mcp.server.mcpserver import MCPServer

# Create an MCP server
mcp = MCPServer("Demo")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
