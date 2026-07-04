from src.discovery.resolver import CapabilityResolver


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

    def __init__(self):
        self.resolver = CapabilityResolver()

    def search(self, capability: str):
        return self.resolver.discover(capability)

    def installed(self, capability: str):

        agents = self.search(capability)

        for agent in agents:

            if agent.source == "Local":
                setattr(agent, "installed", True)
            else:
                setattr(agent, "installed", False)

        return agents