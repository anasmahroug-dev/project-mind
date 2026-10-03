
from app.state.mind_state import MindState
from app.state.mood import Mood

DOMINANCE_MARGIN = 0.02

MOOD_BASE = {
    Mood.HAPPY: 0.5,
    Mood.CURIOUS: 0.6,
    Mood.SAD: 0.2,
    Mood.STRESSED: 0.3,
    Mood.BORED: 0.4,
}

MOOD_DRIFT = {
    Mood.BORED: 0.003
}

RETURN_TO_BASE_SPEED = 0.05

class MoodManager:

    def process(self, mind_state: MindState) -> None:
        for mood, drift in MOOD_DRIFT.items():
            mind_state.mood.shift(mood, drift)
            
        for mood, level in mind_state.mood.levels.items():
            base_level = MOOD_BASE[mood]
            new_level = level + (base_level - level) * RETURN_TO_BASE_SPEED  
            mind_state.mood.levels[mood] = new_level
        
        mind_state.mood.update_dominant(DOMINANCE_MARGIN)