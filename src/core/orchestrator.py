class Orchestrator:
    def __init__(self, planner, registry):
        self.planner = planner
        self.registry = registry

    def run(self, user_input: str):
        plan = self.planner.create_plan(user_input)

        results = []

        for step in plan.steps:
            agent = self.registry.get_agent(step.agent)
            result = agent.execute(step.task)
            results.append(result)

        return {
            "input": user_input,
            "plan": [s.task for s in plan.steps],
            "results": results
        }