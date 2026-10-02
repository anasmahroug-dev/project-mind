from app.state.mind_state import MindState
from app.state.mood import Mood, MoodState
from app.state.energy import EnergyState
from app.state.personality import PersonalityState
from app.state.working_memory import WorkingMemory

def create_initial_mind_state() -> MindState:
    return MindState(
        age=0,
        mood=MoodState(
            levels={
                Mood.HAPPY: 0.0,
                Mood.CURIOUS: 0.5,
                Mood.SAD: 0.0,
                Mood.STRESSED: 0.0,
                Mood.BORED: 0.0,
            }
            
        ),
        energy=EnergyState(
            level=100.0,
        ),
        personality=PersonalityState(
            curiosity=0.9,
            empathy=0.7,
            humor=0.6,
            patience=0.8,
            confidence=0.5,
        ),
        working_memory=WorkingMemory(
            items=[],
        ),
        current_goal=None,
    )
    