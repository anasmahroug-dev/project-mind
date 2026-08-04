from pydantic import BaseModel, Field
from enum import Enum

class Goal(BaseModel):
    title : str
    priority: int = Field(ge=1, le=10)
    
class GoalType(Enum):
    ACQUIRE_KNOWLEDGE = "acquire_knowledge"
    RESTORE_ENERGY = "restore_energy"
    GET_ENTERTAINED = "get_entertained"