from pydantic import BaseModel
from app.state.mood import MoodState
from app.state.energy import EnergyState
from app.state.personality import PersonalityState
from app.state.working_memory import WorkingMemory
from app.state.goal import Goal

class MindState(BaseModel):
    age: int = 0
    mood: MoodState
    energy: EnergyState
    personality: PersonalityState
    working_memory: WorkingMemory
    current_goal: Goal | None = None