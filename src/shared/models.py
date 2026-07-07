"""
Shared Models Module

Defines planning and step structures.
"""
from dataclasses import dataclass
from typing import List


@dataclass
class Step:
    """
    Represents a single step in a capability-based plan.
    """
    capability: str
    task: str


@dataclass
class Plan:
    """
    Represents an execution plan composed of sequential steps.
    """
    steps: List[Step]