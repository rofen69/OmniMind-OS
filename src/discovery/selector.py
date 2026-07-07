"""
Selector Module

Handles intelligent selection of candidates based on preferences.
"""
from typing import List, Optional
import logging

from src.shared.preferences import UserPreferences
from src.shared.agent_metadata import AgentMetadata

logger = logging.getLogger(__name__)


class AgentSelector:
    """
    Chooses the best candidate according to user preferences.
    """

    def select(self, candidates: List[AgentMetadata], preferences: UserPreferences) -> Optional[AgentMetadata]:
        """
        Select the best candidate based on user preferences.

        Args:
            candidates (List[AgentMetadata]): A list of candidate agents.
            preferences (UserPreferences): The user's preferences.

        Returns:
            Optional[AgentMetadata]: The selected agent, or None if no candidate fits.
        """
        if not candidates:
            return None

        filtered = []

        for agent in candidates:
            # Filter by minimum score
            if agent.score < preferences.minimum_score:
                logger.debug(f"Agent {agent.name} rejected: score {agent.score} < {preferences.minimum_score}")
                continue

            # Filter by cost preference
            if preferences.prefer_free and agent.cost != "Free":
                logger.debug(f"Agent {agent.name} rejected: not free")
                continue

            # Priority ordering for local agents
            if preferences.prefer_local and agent.source == "Local":
                filtered.insert(0, agent)
            else:
                filtered.append(agent)

        # Fallback to unfiltered if constraints are too strict
        if not filtered:
            logger.warning("No candidates matched preferences. Falling back to highest score.")
            filtered = candidates

        # Sort by score descending as final tiebreaker
        filtered.sort(key=lambda a: a.score, reverse=True)

        return filtered[0]