from dataclasses import dataclass


@dataclass
class Task:
    description: str


@dataclass
class AgentResult:
    agent: str
    output: str