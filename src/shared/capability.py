from dataclasses import dataclass, field
from typing import List


@dataclass
class AgentCandidate:
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
    capability: str
    candidates: List[AgentCandidate] = field(default_factory=list)