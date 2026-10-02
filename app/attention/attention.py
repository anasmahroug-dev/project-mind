from app.state.mind_state import MindState
from app.thinking.thought import Thought

DOMINANT_BONUS = 0.05

class Attention:
    def focus(
        self,
        thoughts: list[Thought],
        state: MindState,
    ) -> Thought | None:
        if not thoughts:
            return None
        
        dominant = state.mood.dominant.value
        
        def score(thought: Thought) -> float:
            score = thought.priority
            if any(trigger.type.value == dominant for trigger in thought.triggers):
                score += DOMINANT_BONUS
            return score
        
        return max(thoughts,
                   key=score
                   )