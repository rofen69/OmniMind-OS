"""
Catalog Module

Coordinates capability discovery using the CapabilityResolver.
"""
from typing import List

from src.discovery.resolver import CapabilityResolver
from src.shared.agent_metadata import AgentMetadata


class AgentCatalog:
    """
    Central catalog of discoverable agents.

    Future versions will merge results from:
    - Local
    - GitHub
    - MCP
    - Hugging Face
    - ADK
    """

    def __init__(self) -> None:
        """Initialize the catalog with a capability resolver."""
        self.resolver = CapabilityResolver()

    def search(self, capability: str) -> List[AgentMetadata]:
        """
        Search for agents that provide the given capability.

        Args:
            capability (str): The capability to search for.

        Returns:
            List[AgentMetadata]: A list of matching agent metadata.
        """
        return self.resolver.discover(capability)

    def installed(self, capability: str) -> List[AgentMetadata]:
        """
        Search for agents and annotate them with their installation status.

        Args:
            capability (str): The capability to search for.

        Returns:
            List[AgentMetadata]: Annotated list of agent metadata.
        """
        agents = self.search(capability)

        for agent in agents:
            # Annotate if the agent is already available locally
            if agent.source == "Local":
                setattr(agent, "installed", True)
            else:
                setattr(agent, "installed", False)

        return agents