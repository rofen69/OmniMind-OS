"""
Tool Manager Module

Central registry for tools and the MCP bridge layer.
"""
import logging
from typing import Any, Dict

from src.tools.git_tool import GitTool
from src.tools.api_tool import APITool
from src.mcp.client import MCPClient

logger = logging.getLogger(__name__)


class ToolManager:
    """
    Central registry for tools + MCP bridge layer.
    """

    def __init__(self) -> None:
        """Initialize the tool manager and the MCP client fallback stub."""
        self.tools: Dict[str, Any] = {}

        # MCP client (safe stub for V2 extensibility)
        self.mcp = MCPClient()

    def register(self, name: str, tool: Any) -> None:
        """
        Register a tool by name.

        Args:
            name (str): The name of the tool.
            tool (Any): The tool instance.
        """
        self.tools[name] = tool
        logger.debug(f"Tool registered: {name}")

    def get(self, name: str) -> Any:
        """
        Retrieve a registered tool by name.

        Args:
            name (str): The name of the tool.

        Returns:
            Any: The tool instance, or None if not found.
        """
        return self.tools.get(name)

    def run(self, name: str, *args: Any, **kwargs: Any) -> Any:
        """
        Execute a tool by name, with a fallback to the MCP client if not found locally.

        Args:
            name (str): The name of the tool to execute.
            *args: Positional arguments to pass to the tool.
            **kwargs: Keyword arguments to pass to the tool.

        Returns:
            Any: The execution result.
        """
        # 1. Normal tool execution if registered locally
        if name in self.tools:
            logger.info(f"Executing local tool: {name}")
            return self.tools[name].execute(*args, **kwargs)

        # 2. MCP fallback (safe simulation layer) if not found locally
        logger.info(f"Tool {name} not found locally, falling back to MCP.")
        return self.mcp.send(
            {
                "tool": name,
                "args": args,
                "kwargs": kwargs,
            }
        )