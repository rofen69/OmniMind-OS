"""
File Agent Module

Responsible for file system operations.
"""
from typing import Any, Dict
import logging
import re

from src.core.base_agent import BaseAgent
from src.memory.session import global_session
from .skills import save_to_disk

logger = logging.getLogger(__name__)


class FileAgent(BaseAgent):
    """Agent responsible for reading and writing files."""

    def __init__(self) -> None:
        """Initialize the file agent."""
        super().__init__("FileAgent")

    def execute(self, task: str) -> Dict[str, Any]:
        """
        Execute a file operation task.

        Args:
            task (str): The file task description.

        Returns:
            Dict[str, Any]: The execution result.
        """
        logger.info(f"File agent executing task: {task}")
        
        # Read the formatted doc from memory
        content = global_session.get("formatted_doc")
        if not content:
            content = "No content provided."
            
        # Create a highly predictable filename
        ext = "md"
        if "txt" in task.lower() or "text" in task.lower():
            ext = "txt"
        elif "pdf" in task.lower():
            ext = "txt"
            content = "[PDF generation not installed. Defaulting to TXT]\n\n" + content
            
        filename = f"task_output.{ext}"
        
        status = save_to_disk(filename, content)
        
        return {
            "agent": self.name,
            "task": task,
            "output": status
        }
