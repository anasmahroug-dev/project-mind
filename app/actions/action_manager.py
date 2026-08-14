import random

from app.actions.action import Action
from app.actions.types import ActionType
from app.state.goal import Goal, GoalType
from app.state.mind_state import MindState
from app.state.mood import Mood

ACTION_ENERGY_COSTS = {
    ActionType.READ: 2.0,
    ActionType.TALK_TO_USER: 0.5,
    ActionType.DANCE: 5,
    ActionType.PLAY_GAME: 3,
}

class ActionManager:

    def process(
        self,
        goal: Goal | None,
        mind_state: MindState,
    ) -> Action | None:

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
            
            if action_type == ActionType.READ:
                self._apply_read_effect(mind_state)
            
            elif action_type == ActionType.TALK_TO_USER:
                self._apply_talk_to_user_effect(mind_state)
            
            return action
        
        elif goal.type == GoalType.SEEK_ENJOYMENT:
            
            action_type = random.choice([ActionType.TALK_TO_USER, 
                                         ActionType.DANCE, 
                                         ActionType.PLAY_GAME])
            action = Action(
                type=action_type)
            
            self._apply_energy_cost(action, mind_state)
            
            if action_type == ActionType.TALK_TO_USER:
                self._apply_talk_to_user_effect(mind_state)
            
            elif action_type == ActionType.DANCE:
                self._apply_dance_effect(mind_state)
            
            elif action_type == ActionType.PLAY_GAME:
                self._apply_play_game_effect(mind_state)
            
            return action
        
        return None
    
    def _apply_read_effect(self, mind_state: MindState) -> None:

        mood = mind_state.mood

        if mood.current != Mood.CURIOUS:
            return

        base_decay = 1

        personality_factor = 1.0 - mind_state.personality.curiosity

        decay = base_decay * personality_factor

        mood.intensity = max(
            0.0,
            mood.intensity - decay,
        )

        if mood.intensity == 0.0:
            mood.current = Mood.HAPPY
            mood.intensity = 0.5
    
    def _apply_talk_to_user_effect(
    self,
    mind_state: MindState,
    ) -> None:

        if mind_state.mood.current == Mood.CURIOUS:

            decay = 0.1

            mind_state.mood.intensity = max(
                0.0,
                mind_state.mood.intensity - decay,
            )
            
    def _apply_dance_effect(
        self,
        mind_state: MindState,
    ) -> None:
        
        if mind_state.mood.current == Mood.HAPPY:
            increase = 0.2

            mind_state.mood.intensity = min(
                1.0,
                mind_state.mood.intensity + increase,
            )
            
    def _apply_play_game_effect(
        self,
        mind_state: MindState,
    ) -> None:
        
        if mind_state.mood.current == Mood.HAPPY:
            increase = 0.3

            mind_state.mood.intensity = min(
                1.0,
                mind_state.mood.intensity + increase,
            )

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