"""
Google ADK Adapter (Safe Integration Layer)

This module is isolated from core execution to avoid breaking MVP runtime.
"""

try:
    from google.adk import Agent
except ImportError:
    Agent = None


class ADKAdapter:
    """
    Safe wrapper for Google ADK.

    If ADK is unavailable or incompatible, system still runs.
    """

    def create_agent(self, name: str, description: str):
        if Agent is None:
            # fallback stub for MVP safety
            return {
                "name": name,
                "description": description,
                "runtime": "stub-agent"
            }

        return Agent(
            name=name,
            description=description
        )