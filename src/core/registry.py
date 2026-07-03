from src.core.base_agent import BaseAgent


class AgentRegistry:
    def __init__(self):
        self._agents = {
            "research": BaseAgent("research")
        }

    def get_agent(self, name: str):
        return self._agents[name]