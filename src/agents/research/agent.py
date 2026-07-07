"""
Research Agent Module

Handles research-related tasks.
"""
from typing import Any, Dict, Optional
import logging
import requests

from src.core.base_agent import BaseAgent
from src.memory.session import global_session
from .skills import summarize

logger = logging.getLogger(__name__)


class ResearchAgent(BaseAgent):
    """Agent responsible for research tasks."""

    def __init__(self) -> None:
        """Initialize the research agent."""
        super().__init__("LocalResearchAgent")

    def _query_ollama(self, prompt: str) -> Optional[str]:
        """Attempt to query a local Ollama instance (Option B)."""
        try:
            # Assumes standard local Ollama port 11434 and llama3 model
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": "llama3", "prompt": f"Research this topic and provide a comprehensive markdown summary:\n\n{prompt}", "stream": False},
                timeout=15
            )
            if response.status_code == 200:
                logger.info("Successfully received live LLM response from Ollama.")
                return response.json().get("response", "")
        except requests.exceptions.RequestException as e:
            logger.debug(f"Ollama local LLM not available or timed out: {e}")
        return None

    def execute(self, task: str) -> Dict[str, Any]:
        """
        Execute a research task.

        Args:
            task (str): The research task description.

        Returns:
            Dict[str, Any]: The research result containing the summary.
        """
        logger.info(f"Research agent executing task: {task}")
        
        # 1. Try Live Local LLM
        summary = self._query_ollama(task)
        
        # 2. Safe Fallback
        if not summary:
            logger.info("Falling back to simulated heuristic research.")
            summary = summarize(task)
        
        # Save to global session memory for other agents to consume
        global_session.set("latest_research", summary)
        
        return {
            "agent": self.name,
            "task": task,
            "output": summary
        }