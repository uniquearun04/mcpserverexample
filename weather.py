from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Weather")

@mcp.tool()
def get_weather(location: str) -> str:
    """
    """
    return "The weather is hot and dry"


if __name__ == "__main__":
    mcp.run()
