class ToolManager:
    """
    Central registry for external tools (API, Git, MCP, etc.)
    """

    def __init__(self):
        self.tools = {}

    def register(self, name, tool):
        self.tools[name] = tool

    def get(self, name):
        return self.tools.get(name)

    def run(self, name, *args, **kwargs):
        if name not in self.tools:
            return {"error": f"Tool {name} not found"}
        return self.tools[name].execute(*args, **kwargs)