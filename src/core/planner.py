from src.shared.models import Plan, Step


class Planner:
    """
    Converts a user request into capability-based steps.
    """

    def create_plan(self, user_input: str) -> Plan:

        return Plan(
            steps=[
                Step(
                    capability="research",
                    task=user_input,
                )
            ]
        )