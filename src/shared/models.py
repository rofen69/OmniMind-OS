from dataclasses import dataclass
from typing import List


@dataclass
class Step:
    agent: str
    task: str


@dataclass
class Plan:
    steps: List[Step]