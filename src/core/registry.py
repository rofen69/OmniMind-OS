"""
Registry Module

Provides the central registry for managing agents, tools, memory, and capability discovery.
"""
import logging
from typing import Any, Dict, List

from src.core.base_agent import BaseAgent
from src.core.tool_manager import ToolManager
from src.tools.git_tool import GitTool
from src.tools.api_tool import APITool
from src.memory.memory import Memory
from src.discovery.catalog import AgentCatalog
from src.shared.agent_metadata import AgentMetadata
from src.agents.research.agent import ResearchAgent
from src.agents.file.agent import FileAgent
from src.agents.documentation.agent import DocumentationAgent
from src.agents.evaluation.agent import EvaluationAgent

logger = logging.getLogger(__name__)


class AgentRegistry:
    """
    Central registry for agents, tools, memory,
    and capability discovery.
    """

    def __init__(self) -> None:
        """Initialize the agent registry with shared services and built-in agents."""
        self._agents: Dict[str, BaseAgent] = {}

        # Shared services
        self.memory = Memory()
        self.agent_catalog = AgentCatalog()

        # Tool manager
        self.tool_manager = ToolManager()
        self.tool_manager.register("git", GitTool())
        self.tool_manager.register("api", APITool())

        # Register built-in agents
        self._register_builtin_agents()

    def _register_builtin_agents(self) -> None:
        """Register built-in agents for the MVP."""
        self.register_agent(ResearchAgent())
        self.register_agent(FileAgent())
        self.register_agent(DocumentationAgent())
        self.register_agent(EvaluationAgent())
        logger.debug("Registered built-in agents: LocalResearchAgent, FileAgent, DocumentationAgent, EvaluationAgent")

    def register_agent(self, agent: BaseAgent) -> None:
        """
        Register a new agent instance.

        Args:
            agent (BaseAgent): The agent to register.
        """
        self._agents[agent.name] = agent
        logger.info(f"Registered agent: {agent.name}")

    def get_agent(self, name: str) -> BaseAgent:
        """
        Return a registered agent instance by name.
        Also injects shared memory if the agent supports it.

        Args:
            name (str): The name of the agent to retrieve.

        Returns:
            BaseAgent: The agent instance.
        """
        agent = self._agents[name]

        # Inject shared memory if supported by the agent
        if hasattr(agent, "memory"):
            agent.memory = self.memory

        return agent

    def has_agent(self, name: str) -> bool:
        """
        Check whether an agent exists in the registry.

        Args:
            name (str): The name of the agent to check.

        Returns:
            bool: True if the agent is registered, False otherwise.
        """
        return name in self._agents

    def get_tool(self, name: str) -> Any:
        """
        Return a registered tool instance by name.

        Args:
            name (str): The name of the tool to retrieve.

        Returns:
            Any: The tool instance (e.g., GitTool, APITool).
        """
        return self.tool_manager.get(name)

    def discover_capability(self, capability: str) -> List[AgentMetadata]:
        """
        Return all available agents capable of satisfying the requested capability.

        Args:
            capability (str): The capability to search for (e.g., "research").

        Returns:
            List[AgentMetadata]: A list of agent metadata objects.
        """
        logger.debug(f"Discovering capability: {capability}")
        return self.agent_catalog.installed(capability)