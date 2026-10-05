from pydantic import BaseModel, Field
from enum import Enum

class GoalType(Enum):
    ACQUIRE_KNOWLEDGE = "acquire_knowledge"
    SEEK_ENJOYMENT = "seek_enjoyment"
    RESTORE_ENERGY = "restore_energy"
    GET_ENTERTAINED = "get_entertained"
    SEEK_CONTACT = "seek_contact"

class Goal(BaseModel):
    type: GoalType
    priority: float 
    
