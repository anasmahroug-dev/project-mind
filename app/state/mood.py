from enum import Enum
from pydantic import BaseModel, Field

class Mood(Enum):
    HAPPY = "happy"
    CURIOUS = "curious"
    SAD = "sad"
    STRESSED = "stressed"
    BORED = "bored"


class MoodState:
    current: Mood
    intensity: float = Field(ge=0.0, le=1.0)