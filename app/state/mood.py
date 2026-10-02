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
    
    @property
    def dominant(self) -> Mood:
        return max(self.levels, key=self.levels.get)
    
    def shift(self, mood:Mood, delta: float) -> None:
        self.levels[mood] = max(0.0, min(1.0, self.levels[mood] + delta))