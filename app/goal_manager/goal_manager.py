from app.state.goal import Goal
from app.thinking.thought import Thought

from app.goal_manager.mappers.curiosity import CuriosityGoalMapper


class GoalManager:

    def __init__(self):

        self.mappers = [
            CuriosityGoalMapper(),
        ]

    def process(
        self,
        focused_thought: Thought | None,
    ) -> Goal | None:

        if focused_thought is None:
            return None

        for mapper in self.mappers:

            if mapper.can_handle(focused_thought):
                return mapper.map(focused_thought)

        return None