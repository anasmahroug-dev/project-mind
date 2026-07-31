from pydantic import BaseModel, Field

class EnergyState(BaseModel):
    level: float = Field(ge=0.0, le=100.0)