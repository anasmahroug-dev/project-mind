from pydantic import BaseModel, Field
from app.actions.action import Action
from app.state.mood import MoodState
from app.state.energy import EnergyState
from app.state.personality import PersonalityState
from app.state.working_memory import WorkingMemory
from app.state.goal import Goal
from app.actions.types import ActionType
from app.state.relationship import RelationshipState

class MindState(BaseModel):
    age: int = 0
    mood: MoodState
    energy: EnergyState
    personality: PersonalityState
    working_memory: WorkingMemory
    current_goal: Goal | None = None
    current_action: Action | None = None
    last_action_type: ActionType | None = None
    relationship: RelationshipState = Field(default_factory=RelationshipState)