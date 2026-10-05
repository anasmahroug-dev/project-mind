from pydantic import BaseModel, Field

class RelationshipState(BaseModel):
    affinity: float = Field(default=0.0, ge = -1.0, le=1.0)
    last_contact_age: int | None = None
    contact_need: float = Field(default=0.0, ge=0.0, le=1.0)
    reply_pressure: float = Field(default=0.0, ge=0.0, le=1.0)
    