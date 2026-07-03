"""
Research Agent

Handles research-related tasks.
"""

from src.core.base_agent import BaseAgent
from .skills import summarize


class ResearchAgent(BaseAgent):
    """Agent responsible for research tasks."""

    @property
    def name(self) -> str:
        return "research"

    def run(self, task: str) -> str:
        """
        Execute a research task.
        """

        return summarize(task)