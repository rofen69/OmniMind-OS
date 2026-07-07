"""
Capability Module

Defines capability requests and candidate models.
Note: AgentCandidate is intentionally kept separate from AgentMetadata for MVP, 
as requested by architecture constraints.
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class AgentCandidate:
    """
    Represents a potential candidate agent for a capability.
    """
    name: str
    source: str
    capability: str
    cost: str
    license: str
    score: float
    limitations: List[str] = field(default_factory=list)
    requirements: List[str] = field(default_factory=list)


@dataclass
class CapabilityRequest:
    """
    Represents a request for a specific capability and the resulting candidates.
    """
    capability: str
    candidates: List[AgentCandidate] = field(default_factory=list)