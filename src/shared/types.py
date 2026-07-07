"""
Types Module

Defines generic shared types used across the system.
"""
from dataclasses import dataclass


@dataclass
class Task:
    """
    Represents a generic task description.
    """
    description: str


@dataclass
class AgentResult:
    """
    Represents the raw result of an agent execution.
    """
    agent: str
    output: str