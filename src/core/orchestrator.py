from src.core.guardrails import Guardrails
from src.memory.memory import Memory


class Orchestrator:
    """
    Coordinates planning, agent execution, and tool execution.
    """

    def __init__(self, planner, registry):
        self.planner = planner
        self.registry = registry
        self.guardrails = Guardrails()
        self.memory = Memory()

    def run(self, user_input: str):
        if not self.guardrails.validate_input(user_input):
            return {"error": "Blocked by guardrails."}

        self.memory.store("last_user_input", user_input)

        plan = self.planner.create_plan(user_input)

        results = []

        for step in plan.steps:

            if step.agent.startswith("tool:"):
                tool_name = step.agent.split(":", 1)[1]
                tool = self.registry.get_tool(tool_name)

                if tool is None:
                    results.append(
                        {
                            "error": f"Tool '{tool_name}' is not registered."
                        }
                    )
                    continue

                result = tool.execute(step.task)

            else:
                if not self.registry.has_agent(step.agent):
                    results.append(
                        {
                            "error": f"Agent '{step.agent}' is not registered."
                        }
                    )
                    continue

                agent = self.registry.get_agent(step.agent)
                result = agent.execute(step.task)

            results.append(result)

        return {
            "input": user_input,
            "plan": [
                {
                    "agent": step.agent,
                    "task": step.task,
                }
                for step in plan.steps
            ],
            "results": results,
        }