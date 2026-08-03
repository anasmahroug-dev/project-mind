from app.state.mind_state import MindState
from app.events.base_event import Event
from app.actions.base_action import Action
from app.perception.perception import Perception
from app.brain.state_updater import StateUpdater
from app.thinking.thinking import Thinking
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
        
        
        self.state_updater.process(new_state)
        
        percepts = self.perception.process(new_state, events)
        
        thoughts = self.thinking.process(new_state, percepts)
        
        actions = self.decision.process(new_state, thoughts)
        

        return new_state, actions, percepts, thoughts