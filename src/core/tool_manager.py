from src.tools.git_tool import GitTool
from src.tools.api_tool import APITool
from src.mcp.client import MCPClient


class ToolManager:
    """
    Central registry for tools + MCP bridge layer.
    """

    def __init__(self):
        self.tools = {}

        # MCP client (safe stub)
        self.mcp = MCPClient()

    def register(self, name, tool):
        self.tools[name] = tool

    def get(self, name):
        return self.tools.get(name)

    def run(self, name, *args, **kwargs):
        """
        Executes tool or MCP fallback.
        """

        # 1. normal tool execution
        if name in self.tools:
            return self.tools[name].execute(*args, **kwargs)

        # 2. MCP fallback (safe simulation layer)
        return self.mcp.send(
            {
                "tool": name,
                "args": args,
                "kwargs": kwargs,
            }
        )