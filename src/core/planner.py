"""
Planner Module

Converts a user request into a step-by-step capability-based plan.
"""
import re
from src.shared.models import Plan, Step


class Planner:
    """
    Converts a user request into capability-based steps.
    """

    def create_plan(self, user_input: str) -> Plan:
        """
        Create a plan based on the user input.

        Args:
            user_input (str): The raw input provided by the user.

        Returns:
            Plan: A plan containing capability-based steps.
        """
        steps = []
        user_input_lower = user_input.lower()

        # Rule 1: Research
        if re.search(r'\b(?:research|find|search|what|who)\b', user_input_lower):
            steps.append(Step(capability="research", task=user_input))
            
        # Rule 2: Evaluation
        if re.search(r'\b(?:evaluate|score|judge|assess)\b', user_input_lower):
            steps.append(Step(capability="evaluation", task=user_input))
            
        # Rule 3: Documentation
        if re.search(r'\b(?:document|documentation|format|markdown|summarize|summary)\b', user_input_lower):
            steps.append(Step(capability="documentation", task=user_input))
            
        # Rule 4: File IO
        if re.search(r'\b(?:write|save|file|files|disk|output)\b', user_input_lower):
            steps.append(Step(capability="file", task=user_input))

        # Fallback: If no keywords matched, default to research
        if not steps:
            steps.append(Step(capability="research", task=user_input))

        return Plan(steps=steps)