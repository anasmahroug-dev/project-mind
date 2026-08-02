from abc import ABC, abstractmethod

from app.state.mind_state import MindState
from app.events.base_event import Event
from app.perception.percept import Percept


class BasePerceptor(ABC):

    @abstractmethod
    def generate(
        self,
        mind_state: MindState,
        events: list[Event],
    ) -> list[Percept]:
        ...