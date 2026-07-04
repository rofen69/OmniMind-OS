from src.core.base_agent import BaseAgent
from src.core.tool_manager import ToolManager

from src.tools.git_tool import GitTool
from src.tools.api_tool import APITool

from src.memory.memory import Memory
from src.discovery.catalog import AgentCatalog


class AgentRegistry:
    """
    Central registry for agents, tools, memory,
    and capability discovery.
    """

    def __init__(self):
        self._agents: dict[str, BaseAgent] = {}

        # Shared services
        self.memory = Memory()
        self.agent_catalog = AgentCatalog()

        # Tool manager
        self.tool_manager = ToolManager()
        self.tool_manager.register("git", GitTool())
        self.tool_manager.register("api", APITool())

        # Register built-in agents
        self._register_builtin_agents()

    def _register_builtin_agents(self):
        """Register built-in agents."""
        self._agents["research"] = BaseAgent("research")

    def register_agent(self, agent: BaseAgent):
        """Register a new agent."""
        self._agents[agent.name] = agent

    def get_agent(self, name: str) -> BaseAgent:
        """Return an agent instance."""

        agent = self._agents[name]

        # Inject shared memory if supported
        if hasattr(agent, "memory"):
            agent.memory = self.memory

        return agent

    def has_agent(self, name: str) -> bool:
        """Check whether an agent exists."""
        return name in self._agents

    def get_tool(self, name: str):
        """Return a registered tool."""
        return self.tool_manager.get(name)

    def discover_capability(self, capability: str):
        """
        Return all available agents capable of
        satisfying the requested capability.
        """
        return self.agent_catalog.installed(capability)