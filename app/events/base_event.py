from pydantic import BaseModel

from app.events.event_types import EventType


class Event(BaseModel):
    type: EventType
    content: str = ""