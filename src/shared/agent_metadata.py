"""
Agent Metadata Module

Defines the core data model for describing agents.
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class AgentMetadata:
    """
    Rich metadata describing an available agent.
    """

    name: str
    source: str
    capability: str
    version: str
    license: str
    cost: str
    score: float
    latency: str
    installation: str
    limitations: List[str] = field(default_factory=list)
    requirements: List[str] = field(default_factory=list)