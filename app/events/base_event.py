from pydantic import BaseModel

from app.events.event_types import EventType
from app.events.tone import Tone


class Event(BaseModel):
    type: EventType
    content: str = ""
    tone: Tone | None = None