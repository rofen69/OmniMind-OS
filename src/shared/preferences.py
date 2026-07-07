"""
Preferences Module

Defines user preferences for agent selection.
"""
from dataclasses import dataclass


@dataclass
class UserPreferences:
    """
    Controls how OmniMind selects agents during discovery.
    """

    prefer_free: bool = True
    allow_paid: bool = False
    prefer_local: bool = True
    minimum_score: float = 0.80