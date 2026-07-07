"""
Timeline Module

Defines structures for execution tracing.
"""
from dataclasses import dataclass
from typing import List


@dataclass
class TimelineStep:
    """
    Represents a single entry in the execution timeline.
    """
    capability: str
    selected_agent: str
    source: str
    status: str


@dataclass
class ExecutionTimeline:
    """
    Represents the full timeline of an execution run.
    """
    steps: List[TimelineStep]