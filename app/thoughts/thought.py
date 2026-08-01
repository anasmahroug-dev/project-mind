from pydantic import BaseModel, Field


class Thought(BaseModel):
    content: str
    priority: float = Field(default=0.5, ge=0.0, le=1.0)