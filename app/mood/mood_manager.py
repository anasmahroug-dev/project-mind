
from app.state.mind_state import MindState
from app.state.mood import Mood
from random import choice

MOOD_DECAY = {
    Mood.HAPPY: 0.05,
}

class MoodManager:

    def process(self, mind_state: MindState) -> None:
        
        mood = mind_state.mood
        
        decay = MOOD_DECAY.get(mood.current, 0.0)
        
        mood.intensity = max(0.0,
                             mood.intensity - decay)
        
        if mood.intensity == 0.0:
            self._transition(mind_state)
            
            
        
    def _transition(self, mind_state: MindState) -> None:
        mood = mind_state.mood
        
        if mood.current == Mood.HAPPY:
            mood.current = choice([Mood.CURIOUS,])
            
            mood.intensity = 0.5