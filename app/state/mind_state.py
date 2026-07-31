from pydantic import BaseModel
from state.mood import MoodState
from state.energy import EnergyState
from state.personality import PersonalityState
from state.working_memory import WorkingMemory
from state.goal import Goal

class MindState(BaseModel):
    age: int = 0
    mood: MoodState
    energy: EnergyState
    personality: PersonalityState
    working_memory: WorkingMemory
    current_goal: Goal | None = None