from app.state.goal import Goal, GoalType
from app.thinking.thought import Thought
from app.thinking.types import ThoughtType

from app.goal_manager.mappers.base_mapper import BaseGoalMapper


class HappinessGoalMapper(BaseGoalMapper):

    def can_handle(
        self,
        thought: Thought,
    ) -> bool:

        return thought.type == ThoughtType.ENJOY

    def map(
        self,
        thought: Thought,
    ) -> Goal:

        return Goal(
            type=GoalType.SEEK_ENJOYMENT,
            priority=thought.priority,
        )