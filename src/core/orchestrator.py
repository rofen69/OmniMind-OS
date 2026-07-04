from src.core.guardrails import Guardrails

from src.discovery.selector import AgentSelector
from src.shared.preferences import UserPreferences


class Orchestrator:
    """
    OmniMind Execution Engine

    Flow:
    User Input
        ↓
    Planner (Capability Plan)
        ↓
    Discovery (Agent Candidates)
        ↓
    Selection (Best Agent)
        ↓
    Execution (Agent Output)
    """

    def __init__(self, planner, registry):
        self.planner = planner
        self.registry = registry

        self.guardrails = Guardrails()
        self.selector = AgentSelector()
        self.preferences = UserPreferences()

    def run(self, user_input: str):

        if not self.guardrails.validate_input(user_input):
            return {"error": "Blocked by guardrails"}

        plan = self.planner.create_plan(user_input)

        discovered = {}
        selected = {}
        timeline = []
        results = []

        for step in plan.steps:

            capability = step.capability

            # 1. DISCOVER
            candidates = self.registry.discover_capability(capability)

            discovered[capability] = [
                {
                    "name": a.name,
                    "source": a.source,
                    "installed": getattr(a, "installed", False),
                    "cost": a.cost,
                    "license": a.license,
                    "score": a.score,
                    "limitations": a.limitations,
                    "requirements": a.requirements,
                }
                for a in candidates
            ]

            # 2. SELECT BEST AGENT
            chosen = self.selector.select(candidates, self.preferences)

            if chosen:
                selected[capability] = {
                    "name": chosen.name,
                    "source": chosen.source,
                    "score": chosen.score,
                }

                timeline.append({
                    "capability": capability,
                    "selected_agent": chosen.name,
                    "source": chosen.source,
                    "status": "executed"
                })

            # 3. EXECUTION
            if capability.startswith("tool:"):
                tool = self.registry.get_tool(capability.split(":")[1])
                result = tool.execute(step.task)
            else:
                agent = self.registry.get_agent("research")
                result = agent.execute(step.task)

            results.append(result)

        return {
            "input": user_input,
            "plan": [
                {
                    "capability": s.capability,
                    "task": s.task,
                }
                for s in plan.steps
            ],
            "candidate_agents": discovered,
            "selected_agents": selected,
            "timeline": timeline,
            "results": results,
        }