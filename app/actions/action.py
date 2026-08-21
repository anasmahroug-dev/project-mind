from pydantic import BaseModel

from app.actions.types import ActionType


class Action(BaseModel):
    type: ActionType
    
    duration: int = 1
    remaining_ticks: int = 1
    
    @property
    def is_finished(self) -> bool:
        return self.remaining_ticks <= 0
    