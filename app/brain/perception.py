from app.state.mind_state import MindState
from app.events.base_event import Event

class Perception:

    def process(self,
                mind_state: MindState,
                events: list[Event]) -> None:
        """
        Updates the mind state based on incoming events.
        """
        pass