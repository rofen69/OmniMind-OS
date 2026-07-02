from dataclasses import dataclass, field
from typing import Any


@dataclass
class Task:
    """Represents one executable task."""

    id: str
    description: str
    assigned_agent: str
    status: str = "pending"


@dataclass
class ExecutionPlan:
    """Planner execution plan."""

    goal: str
    tasks: list[Task] = field(default_factory=list)


@dataclass
class AgentResult:
    """Standard result returned by every agent."""

    success: bool
    output: Any
    message: str = ""