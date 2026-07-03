from src.shared.types import AgentResult, Task


class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    def execute(self, task: str):
        return {
            "agent": self.name,
            "task": task,
            "output": f"Processed: {task}"
        }