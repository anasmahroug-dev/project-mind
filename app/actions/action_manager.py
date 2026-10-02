import random

from app.actions.action import Action
from app.actions.types import ActionType
from app.events.base_event import Event
from app.events.event_types import EventType
from app.state.goal import Goal, GoalType
from app.state.mind_state import MindState

from app.actions.specs import ACTION_SPECS

WEAK_LOW_ENERGY_THRESHOLD = 40.0
LOW_ENERGY_THRESHOLD = 30.0
MODERATE_ENERGY_THRESHOLD = 20.0
CRITICAL_ENERGY_THRESHOLD = 10.0

class ActionManager:

    def process(
        self,
        goal: Goal | None,
        mind_state: MindState,
    ) -> Action | None:

        if self._should_override_for_energy(mind_state):
            return self._create_energy_action(mind_state)
        
        if goal is None:
            return None

        if goal.type == GoalType.ACQUIRE_KNOWLEDGE:

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
        
        return None
    
    
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
        
    
    def _should_override_for_energy(
        self,
        mind_state: MindState,
    ) -> bool:
        energy = mind_state.energy.level
        
        if energy <= CRITICAL_ENERGY_THRESHOLD:
            return True
        
        if energy <= MODERATE_ENERGY_THRESHOLD:
            return random.random() < 0.8
        
        if energy <= LOW_ENERGY_THRESHOLD:
            return random.random() < 0.5
        if energy <= WEAK_LOW_ENERGY_THRESHOLD:
            return random.random() < 0.2
        
        return False
    
    def _create_energy_action(
        self,
        mind_state: MindState,
    ) -> Action:
        energy = mind_state.energy.level
        
        if energy <= CRITICAL_ENERGY_THRESHOLD:
            action_type = ActionType.SLEEP
            
        elif energy <= MODERATE_ENERGY_THRESHOLD:
            action_type = random.choice([
             ActionType.SLEEP,
             ActionType.SLEEP,
             ActionType.EAT,
             ActionType.TALK_TO_USER,   
            ])
            
        else:
            action_type = random.choice([
                ActionType.SLEEP,
                ActionType.EAT,
                ActionType.TALK_TO_USER,
            ])
        
        return self._create_action(action_type)
    
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
    
