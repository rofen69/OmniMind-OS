from src.core.base_agent import BaseAgent
from src.core.tool_manager import ToolManager

from src.tools.git_tool import GitTool
from src.tools.api_tool import APITool


class AgentRegistry:
    """
    Registry for OmniMind agents and tools.
    """

    def __init__(self):
        self._agents: dict[str, BaseAgent] = {}

        self.tool_manager = ToolManager()
        self.tool_manager.register("git", GitTool())
        self.tool_manager.register("api", APITool())

        self._register_builtin_agents()

    def _register_builtin_agents(self):
        self._agents["research"] = BaseAgent("research")

    def register_agent(self, agent: BaseAgent):
        self._agents[agent.name] = agent

    def get_agent(self, name: str) -> BaseAgent:
        return self._agents[name]

    def has_agent(self, name: str) -> bool:
        return name in self._agents

    def get_tool(self, name: str):
        return self.tool_manager.get(name)