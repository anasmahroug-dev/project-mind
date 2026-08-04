from app.state.goal import Goal, GoalType
from app.thinking.thought import Thought
from app.thinking.types import ThoughtType

from app.goal_manager.mappers.base_mapper import BaseGoalMapper


class CuriosityGoalMapper(BaseGoalMapper):

    def can_handle(
        self,
        thought: Thought,
    ) -> bool:

        return thought.type == ThoughtType.WONDER

    def map(
        self,
        thought: Thought,
    ) -> Goal:

        return Goal(
            type=GoalType.ACQUIRE_KNOWLEDGE,
            priority=thought.priority,
        )