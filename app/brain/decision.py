from app.state.mind_state import MindState
from app.actions.base_action import Action
from app.thinking.thought import Thought


class Decision:

    def process(
        self,
        mind_state: MindState,
        thoughts: list[Thought]
    ) -> list[Action]:
        """
        Chooses actions based on thoughts and state.
        """
        return []