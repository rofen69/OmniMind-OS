"""
Base Agent Module

Defines the contract for all OmniMind agents.
"""
from typing import Any, Dict

from src.shared.types import Task


class BaseAgent:
    """Base class for all agents in the OmniMind OS."""

    def __init__(self, name: str) -> None:
        """
        Initialize the agent with a given name.

        Args:
            name (str): The name of the agent.
        """
        self.name = name

    def execute(self, task: str) -> Dict[str, Any]:
        """
        Execute the given task.

        Args:
            task (str): The task description.

        Returns:
            Dict[str, Any]: The execution result.
        """
        return {
            "agent": self.name,
            "task": task,
            "output": f"Processed: {task}"
        }