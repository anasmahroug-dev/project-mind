import random
from app.personality.modulation import action_weights, mood_effect_gain, repetition_boredom, reply_urge
from app.actions.action import Action
from app.actions.types import ActionType
from app.events.base_event import Event
from app.events.event_types import EventType
from app.state import mind_state
from app.state import goal
from app.state.goal import Goal, GoalType
from app.state.mind_state import MindState
from app.state.mood import Mood



from app.actions.specs import ACTION_SPECS

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

        elif goal.type in (
            GoalType.ACQUIRE_KNOWLEDGE,
            GoalType.SEEK_ENJOYMENT,
            GoalType.GET_ENTERTAINED,
        ):
            weights = action_weights(mind_state.personality, goal.type)
            if goal.type == GoalType.GET_ENTERTAINED:
                weights.pop(mind_state.last_action_type, None)
            action_type = random.choices(list(weights), weights=list(weights.values()))[0]
            return self._create_action(action_type)
        
        elif goal.type == GoalType.SEEK_CONTACT:
            return self._create_action(ActionType.TALK_TO_USER)
        
        return None
    def _register_action(self, action: Action, mind_state: MindState) -> None:
        if action.type == ActionType.TALK_TO_USER:  
            return      
        if mind_state.last_action_type is not None:
            if action.type == mind_state.last_action_type:
                mind_state.mood.shift(Mood.BORED, repetition_boredom(mind_state.personality))
            
            else:
                mind_state.mood.shift(Mood.BORED, -NOVELTY_RELIEF)
        
        mind_state.last_action_type = action.type
        
    def interrupt_current_action(self, mind_state: MindState) -> None:
        mind_state.current_action = None
        
    def should_interrupt(self, 
                         action: Action,
                         events: list[Event],
                         mind_state: MindState,) -> bool:
        if not any(event.type == EventType.USER_MESSAGE for event in events):
            return False

        urge = reply_urge(mind_state.personality, mind_state.relationship)
        return urge > ACTION_SPECS[action.type].resistance
        
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
        mind_state.relationship.contact_need = max(0.0, min(1.0, mind_state.relationship.contact_need + ACTION_SPECS[action.type].contact_per_tick)) 
        
        relationship = mind_state.relationship      
        relationship.reply_pressure = max(
            0.0, min(1.0, relationship.reply_pressure + ACTION_SPECS[action.type].reply_per_tick)
            )
                
        for mood, delta in ACTION_SPECS[action.type].mood_per_tick.items():
                    mind_state.mood.shift(mood, delta * mood_effect_gain(mind_state.personality, mood))
                    
        action.remaining_ticks -= 1
        if action.is_finished:
            mind_state.current_action = None

        return action
    
