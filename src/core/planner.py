from src.shared.models import Plan, Step


class Planner:
    """Creates an execution plan for a user request."""

    def create_plan(self, user_input: str) -> Plan:
        """
        Current MVP:
        Single-step planning.
        Multi-step planning will be added after submission.
        """

        return Plan(
            steps=[
                Step(
                    agent="research",
                    task=user_input,
                )
            ]
        )