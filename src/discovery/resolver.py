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

    def __init__(self):

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
            ]
        }

    def discover(self, capability: str):

        return self.catalog.get(capability, [])