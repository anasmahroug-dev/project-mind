from enum import Enum
from pydantic import BaseModel

class Mood(Enum):
    HAPPY = "happy"
    CURIOUS = "curious"
    SAD = "sad"
    STRESSED = "stressed"
    BORED = "bored"

class MoodState(BaseModel):
    levels: dict[Mood, float]
    dominant: Mood = Mood.CURIOUS
    @property
    def strongest(self) -> Mood:
        return max(self.levels, key=self.levels.get)
    
    def shift(self, mood:Mood, delta: float) -> None:
        self.levels[mood] = max(0.0, min(1.0, self.levels[mood] + delta))
        
    def update_dominant(self, margin:float) -> None:
        strongest_mood = self.strongest
        if self.levels[strongest_mood] - self.levels[self.dominant] > margin:
            self.dominant = strongest_mood