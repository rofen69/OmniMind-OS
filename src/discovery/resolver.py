"""
Resolver Module

Simulates capability resolution across multiple sources.
"""
from typing import List

from src.shared.agent_metadata import AgentMetadata


class CapabilityResolver:
    """
    Resolves which agents can satisfy a capability.

    Current implementation uses a local catalog.
    Future versions will query:
    - GitHub
    - MCP
    - Hugging Face
    - ADK
    """

    def __init__(self) -> None:
        """Initialize the resolver with a static catalog of capabilities."""
        self.catalog = {
            "research": [
                AgentMetadata(
                    name="LocalResearchAgent",
                    version="1.0",
                    source="Local",
                    capability="research",
                    cost="Free",
                    latency="Fast",
                    license="Internal",
                    score=1.0,
                    limitations=["Local only"],
                    requirements=[],
                    installation="Built-in",
                ),
                AgentMetadata(
                    name="GitHubResearchAgent",
                    version="1.0",
                    source="GitHub",
                    capability="research",
                    cost="Free",
                    latency="Medium",
                    license="MIT",
                    score=0.93,
                    limitations=["Requires installation"],
                    requirements=["Internet"],
                    installation="Git Clone",
                ),
                AgentMetadata(
                    name="HFResearchAgent",
                    version="1.0",
                    source="HuggingFace",
                    capability="research",
                    cost="Paid",
                    latency="Medium",
                    license="Commercial",
                    score=0.97,
                    limitations=["API cost"],
                    requirements=["API Token"],
                    installation="Remote",
                )
            ],
            "file": [
                AgentMetadata(
                    name="FileAgent",
                    version="1.0",
                    source="Local",
                    capability="file",
                    cost="Free",
                    latency="Fast",
                    license="Internal",
                    score=1.0,
                    limitations=["Local file system only"],
                    requirements=[],
                    installation="Built-in",
                )
            ],
            "documentation": [
                AgentMetadata(
                    name="DocumentationAgent",
                    version="1.0",
                    source="Local",
                    capability="documentation",
                    cost="Free",
                    latency="Fast",
                    license="Internal",
                    score=1.0,
                    limitations=["Markdown only"],
                    requirements=[],
                    installation="Built-in",
                )
            ],
            "evaluation": [
                AgentMetadata(
                    name="evaluation",
                    version="1.0",
                    source="Local",
                    capability="evaluation",
                    cost="Free",
                    latency="Fast",
                    license="Internal",
                    score=1.0,
                    limitations=["Basic scoring only"],
                    requirements=[],
                    installation="Built-in",
                )
            ]
        }

    def discover(self, capability: str) -> List[AgentMetadata]:
        """
        Discover agents capable of satisfying the request.

        Args:
            capability (str): The requested capability.

        Returns:
            List[AgentMetadata]: List of metadata for available agents.
        """
        return self.catalog.get(capability, [])