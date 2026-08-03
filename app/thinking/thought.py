from typing import Any


from pydantic import BaseModel, Field
from app.perception.percept import Percept

from app.thinking.types import ThoughtType


class Thought(BaseModel):
    type: ThoughtType
    priority: float = Field(default=0.5, ge=0.0, le=1.0)
    triggers: list[Percept]
    data: dict[str, Any] = Field(default_factory=dict)
    
    