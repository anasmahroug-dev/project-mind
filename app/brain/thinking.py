from app.state.mind_state import MindState
from app.thoughts.thought import Thought


class Thinking:

    def process(
        self,
        mind_state: MindState
    ) -> list[Thought]:
        """
        Generates thoughts from the current state.
        """
        return []