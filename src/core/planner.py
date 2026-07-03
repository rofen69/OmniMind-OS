from src.shared.models import Plan, Step
from src.core.registry import AgentRegistry


class Planner:
    def __init__(self):
        self.registry = AgentRegistry()

    def create_plan(self, user_input: str) -> Plan:
        # For now: single-step plan (we will expand later)
        steps = [
            Step(
                agent="research",
                task=user_input
            )
        ]

        return Plan(steps=steps)