from app.state.mind_state import MindState
from app.events.base_event import Event
from app.actions.base_action import Action
from app.brain.perception import Perception
from app.brain.state_updater import StateUpdater
from app.brain.thinking import Thinking
from app.brain.decision import Decision


class Brain:
    def __init__(self):

        self.perception = Perception()

        self.state_updater = StateUpdater()

        self.thinking = Thinking()

        self.decision = Decision()
        
    def step(
        self,
        state: MindState,
        events: list[Event]
    ) -> tuple[MindState, list[Action]]:
        new_state = state.model_copy(deep=True)
        
        self.perception.process(new_state, events)
        
        self.state_updater.process(new_state)
        
        thoughts = self.thinking.process(new_state)
        
        actions = self.decision.process(new_state, thoughts)
        
        
        return new_state, actions