from app.perception.percept import Percept
from app.state.mind_state import MindState
from app.thinking.thought import Thought


class Thinking:

    def process(
        self,
        mind_state: MindState,
        percepts: list[Percept],
    ) -> list[Thought]:
        """
        Generates thoughts from the current state.
        """
        return []