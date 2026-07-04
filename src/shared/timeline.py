from dataclasses import dataclass
from typing import List


@dataclass
class TimelineStep:
    capability: str
    selected_agent: str
    source: str
    status: str


@dataclass
class ExecutionTimeline:
    steps: List[TimelineStep]