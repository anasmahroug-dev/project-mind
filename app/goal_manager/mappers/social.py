from app.goal_manager.mappers.base_mapper import BaseGoalMapper
from app.state.goal import Goal, GoalType
from app.thinking.thought import Thought
from app.thinking.types import ThoughtType


class SocialGoalMapper(BaseGoalMapper):

    def can_handle(self, thought: Thought) -> bool:
        return thought.type == ThoughtType.SPEAK

    def map(self, thought: Thought) -> Goal:
        return Goal(type=GoalType.SEEK_CONTACT, priority=thought.priority)