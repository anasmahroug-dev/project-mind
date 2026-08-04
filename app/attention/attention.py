from app.state.mind_state import MindState
from app.thinking.thought import Thought

class Attention:
    def focus(
        self,
        thoughts: list[Thought],
        state: MindState,
    ) -> Thought | None:
        if not thoughts:
            return None
        
        return max(thoughts,
                   key=lambda thought: thought.priority,
                   )