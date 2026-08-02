from enum import Enum


class PerceptType(str, Enum):
    LOW_ENERGY = "low_energy"
    HIGH_ENERGY = "high_energy"

    HAPPY = "happy"
    CURIOUS = "curious"
    SAD = "sad"
    STRESSED = "stressed"
    BORED = "bored"

    USER_MESSAGE = "user_message"

    HAS_GOAL = "has_goal"
    NO_GOAL = "no_goal"

    MEMORY_RECALL = "memory_recall"

    TIME_PASSED = "time_passed"
    
    
class PerceptSource(str, Enum):
    ENERGY = "energy"
    MOOD = "mood"
    GOAL = "goal"
    MEMORY = "memory"
    USER = "user"
    TIME = "time"