from app.state.mind_state import MindState
from app.events.base_event import Event
from app.actions.base_action import Action


class Brain:
    
    def step(
        self,
        state: MindState,
        events: list[Event]
    ) -> tuple[MindState, list[Action]]:
        ...