"""
Documentation Agent Module

Responsible for generating and maintaining project documentation.
"""
from typing import Any, Dict
import logging

from src.core.base_agent import BaseAgent
from src.memory.session import global_session
from .skills import format_as_markdown

logger = logging.getLogger(__name__)


class DocumentationAgent(BaseAgent):
    """Agent responsible for documentation tasks."""

    def __init__(self) -> None:
        """Initialize the documentation agent."""
        super().__init__("DocumentationAgent")

    def execute(self, task: str) -> Dict[str, Any]:
        """
        Execute a documentation task.

        Args:
            task (str): The documentation task description.

        Returns:
            Dict[str, Any]: The result containing the formatted doc.
        """
        logger.info(f"Documentation agent executing task: {task}")
        
        # Read from global session memory
        raw_data = global_session.get("latest_research")
        if not raw_data:
            raw_data = f"Task: {task}\n(No prior research data found in memory.)"
            
        formatted_doc = format_as_markdown(raw_data)
        
        # Save the formatted doc back to memory
        global_session.set("formatted_doc", formatted_doc)
        
        return {
            "agent": self.name,
            "task": task,
            "output": f"Successfully formatted document and saved to memory. Excerpt: {formatted_doc[:50].replace(chr(10), ' ')}..."
        }
