from abc import ABC, abstractmethod

from app.state.goal import Goal
from app.thinking.thought import Thought


class BaseGoalMapper(ABC):

    @abstractmethod
    def can_handle(
        self,
        thought: Thought,
    ) -> bool:
        ...

    @abstractmethod
    def map(
        self,
        thought: Thought,
    ) -> Goal:
        ...