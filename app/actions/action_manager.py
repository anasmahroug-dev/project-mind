import random

from app.actions.action import Action
from app.actions.types import ActionType
from app.state.goal import Goal, GoalType
from app.state.mind_state import MindState


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

            return Action(
                type=action_type,
            )

        return None