from pydantic import BaseModel

from app.actions.types import ActionType


class Action(BaseModel):
    type: ActionType