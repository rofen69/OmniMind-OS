from abc import ABC, abstractmethod

from src.shared.types import AgentResult, Task


class BaseAgent(ABC):
    """
    Base class for every OmniMind OS agent.

    Every built-in or third-party agent must inherit this class.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique agent name."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Short description of agent capability."""
        pass

    @abstractmethod
    def can_handle(self, task: Task) -> bool:
        """
        Returns True if this agent can execute the task.
        """
        pass

    @abstractmethod
    def execute(self, task: Task) -> AgentResult:
        """
        Execute one task.
        """
        pass