from dataclasses import dataclass


@dataclass
class UserPreferences:
    """
    Controls how OmniMind selects agents.
    """

    prefer_free: bool = True
    allow_paid: bool = False
    prefer_local: bool = True

    minimum_score: float = 0.80