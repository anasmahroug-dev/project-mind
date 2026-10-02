import random

from app.actions.action import Action
from app.actions.types import ActionType
from app.events.base_event import Event
from app.events.event_types import EventType
from app.state.goal import Goal, GoalType
from app.state.mind_state import MindState
from app.state.mood import Mood


WEAK_LOW_ENERGY_THRESHOLD = 40.0
LOW_ENERGY_THRESHOLD = 30.0
MODERATE_ENERGY_THRESHOLD = 20.0
CRITICAL_ENERGY_THRESHOLD = 10.0

ACTION_ENERGY_COSTS = {
    ActionType.READ: 2.0,
    ActionType.TALK_TO_USER: 0.5,
    ActionType.DANCE: 5,
    ActionType.PLAY_GAME: 3,
}
MOOD_EFFECTS = {
    ActionType.READ: {Mood.CURIOUS: -0.01,},
    ActionType.TALK_TO_USER: {Mood.CURIOUS: -0.015},
    ActionType.DANCE: {Mood.HAPPY: 0.01},
    ActionType.PLAY_GAME: {Mood.HAPPY: 0.01},
    
}

INTERRUPTIBLE_ACTIONS = {
    ActionType.SLEEP: True,
    ActionType.READ: True,
    ActionType.DANCE: True,
    ActionType.PLAY_GAME: True,
    ActionType.TALK_TO_USER: False,
}

ACTION_DURATIONS = {
    ActionType.READ: (2, 6),
    ActionType.DANCE: (2, 5),
    ActionType.PLAY_GAME: (3, 6),
    ActionType.EAT: (2, 4),
    ActionType.SLEEP: (3, 8),
    ActionType.TALK_TO_USER: (1, 1),
}

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

            action = Action(
                type=action_type)
            
            self._apply_energy_cost(action, mind_state)
            
            self._apply_mood_effects(action, mind_state)
            
            return action
        
        elif goal.type == GoalType.SEEK_ENJOYMENT:
            
            action_type = random.choice([ActionType.TALK_TO_USER, 
                                         ActionType.DANCE, 
                                         ActionType.PLAY_GAME])
            action = Action(
                type=action_type)
            
            self._apply_energy_cost(action, mind_state)
            
            self._apply_mood_effects(action, mind_state)
            
            return action
        
        return None
    
    
    def is_interruptible(self, action: Action) -> bool:
        return INTERRUPTIBLE_ACTIONS.get(action.type, True)
    
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
        
        if action_type == ActionType.SLEEP:
            return self._create_sleep_action(mind_state)
        action = Action(type=action_type)
        self._apply_action_effect(action, mind_state)       

        return action
        
    def _apply_action_effect(
        self,
        action: Action,
        mind_state: MindState,
        ) -> None:

        self._apply_energy_cost(action, mind_state)

        self._apply_mood_effects(action, mind_state)
        
        if action.type == ActionType.SLEEP:
            self._apply_sleep_effect(mind_state)

        elif action.type == ActionType.EAT:
            self._apply_eat_effect(mind_state)
            
    def _apply_mood_effects(self, action: Action, mind_state: MindState) -> None:
        mood_effects = MOOD_EFFECTS.get(action.type, {})
        for mood, delta in mood_effects.items():
            mind_state.mood.shift(mood, delta)
            
                            
    def _apply_energy_cost(
    self,
    action: Action,
    mind_state: MindState,
    ) -> None:

        cost = ACTION_ENERGY_COSTS.get(action.type, 0.0)

        mind_state.energy.level = max(
            0.0,
            mind_state.energy.level - cost,
        )
    
    def _apply_sleep_effect(
        self,
        mind_state: MindState,
    ) -> None:
        
        recovery = 20.0
        
        mind_state.energy.level = min(
            100.0,
            mind_state.energy.level + recovery,
        )
        
    def _create_sleep_action(self, mind_state: MindState) -> Action:
        
        duration = random.randint(3, 8)
        
        return Action(type=ActionType.SLEEP, duration=duration, remaining_ticks=duration)
    
    def process_current_action(self,
                               mind_state: MindState,
                               ) -> Action:
        action = mind_state.current_action
        if action.type == ActionType.SLEEP:
            self._apply_sleep_tick(mind_state)
            
        action.remaining_ticks -= 1
        if action.is_finished:
            mind_state.current_action = None
        
        return action
    
    def _apply_sleep_tick(
        self, mind_state: MindState, 
    ) -> None:
        recovery = 5.0
        
        mind_state.energy.level = min(100.0,                                      
                                     mind_state.energy.level + recovery
                                     )
        
    def _apply_eat_effect(
        self,
        mind_state: MindState,
        ) -> None:

        recovery = 10.0

        mind_state.energy.level = min(
            100.0,
            mind_state.energy.level + recovery,
        )