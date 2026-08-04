from pydantic import BaseModel, Field
from enum import Enum

class Goal(BaseModel):
    type: GoalType
    priority: float 
    
class GoalType(Enum):
    ACQUIRE_KNOWLEDGE = "acquire_knowledge"
    RESTORE_ENERGY = "restore_energy"
    GET_ENTERTAINED = "get_entertained"