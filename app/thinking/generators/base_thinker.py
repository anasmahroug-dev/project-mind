from abc import ABC, abstractmethod

from app.state.mind_state import MindState
from app.perception.percept import Percept
from app.thinking.thought import Thought



class BaseThinker(ABC):

    @abstractmethod
    def generate(
        self,
        mind_state: MindState,
        percepts: list[Percept],
    ) -> list[Thought]:
        ...