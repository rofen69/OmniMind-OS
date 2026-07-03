"""
MCP Client (Minimal Capstone Version)

Acts as a placeholder interface for future Model Context Protocol integration.
Currently non-networked and safe for offline execution.
"""


class MCPClient:
    """
    Lightweight MCP client stub.

    In V2, this will connect to external model/tool servers.
    """

    def __init__(self):
        self.connected = False

    def connect(self):
        """
        Simulate MCP connection.
        """
        self.connected = True
        return {"status": "connected", "mode": "stub"}

    def send(self, payload: dict):
        """
        Simulate sending data to MCP server.
        """
        return {
            "status": "ok",
            "echo": payload,
            "note": "MCP stub mode (no external call)"
        }

    def disconnect(self):
        self.connected = False
        return {"status": "disconnected"}