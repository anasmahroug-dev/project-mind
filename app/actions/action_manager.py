import random

from app.actions.action import Action
from app.actions.types import ActionType
from app.events.base_event import Event
from app.events.event_types import EventType
from app.state.goal import Goal, GoalType
from app.state.mind_state import MindState
from app.state.mood import Mood


from app.actions.specs import ACTION_SPECS

REPETITION_BOREDOM = 0.05
NOVELTY_RELIEF = 0.02

class ActionManager:
    def process(self, goal, mind_state):
        action = self._choose_action(goal, mind_state)
        if action is not None:
            self._register_action(action, mind_state)
        return action
    
    
    def _choose_action(
        self,
        goal: Goal | None,
        mind_state: MindState,
    ) -> Action | None:
     
        if goal is None:
            return None
        
        if goal.type == GoalType.RESTORE_ENERGY:
            action_type = random.choice([
                ActionType.SLEEP,
                ActionType.EAT,])
            return self._create_action(action_type)

        elif goal.type == GoalType.ACQUIRE_KNOWLEDGE:

            action_type = random.choice([
                ActionType.READ,
                ActionType.TALK_TO_USER,
            ])

            return self._create_action(action_type)
            
        elif goal.type == GoalType.SEEK_ENJOYMENT:
            
            action_type = random.choice([ActionType.TALK_TO_USER, 
                                         ActionType.DANCE, 
                                         ActionType.PLAY_GAME])
            
            return self._create_action(action_type)
        
        elif goal.type == GoalType.GET_ENTERTAINED:
            actions = [ActionType.DANCE, ActionType.PLAY_GAME, ActionType.READ,]
            actions.remove(mind_state.last_action_type) if mind_state.last_action_type in actions else None
            action_type = random.choice(actions)    
            return self._create_action(action_type)
        
        return None
    def _register_action(self, action: Action, mind_state: MindState) -> None:
                
        if mind_state.last_action_type is not None:
            if action.type == mind_state.last_action_type:
                mind_state.mood.shift(Mood.BORED, REPETITION_BOREDOM)
            
            else:
                mind_state.mood.shift(Mood.BORED, -NOVELTY_RELIEF)
        
        mind_state.last_action_type = action.type
        
    
    def is_interruptible(self, action: Action) -> bool:
        return ACTION_SPECS[action.type].interruptible
    
    def interrupt_current_action(self, mind_state: MindState) -> None:
        mind_state.current_action = None
        
    def should_interrupt(self, 
                         action: Action,
                         events: list[Event],) -> bool:
        if not self.is_interruptible(action):
            return False
        
        if not events:
            return False
        
        return any(
            event.type == EventType.USER_MESSAGE
            for event in events
        )
        
    def _change_energy(self,mind_state: MindState, delta: float) -> None:
        mind_state.energy.level = max(0.0, min(100.0, mind_state.energy.level + delta))
    

    def _create_action(self, action_type: ActionType) -> Action:
        low, high = ACTION_SPECS[action_type].duration
        duration = random.randint(low, high)
        return Action(type=action_type, duration=duration, remaining_ticks=duration)
        
    def process_current_action(self,
                               mind_state: MindState,
                               ) -> Action:
        action = mind_state.current_action
        
        self._change_energy(mind_state, ACTION_SPECS[action.type].energy_per_tick)    
                
        for mood, delta in ACTION_SPECS[action.type].mood_per_tick.items():
                    mind_state.mood.shift(mood, delta)
        
        action.remaining_ticks -= 1
        if action.is_finished:
            mind_state.current_action = None

        return action
    
