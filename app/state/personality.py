from pydantic import BaseModel, Field

class PersonalityState(BaseModel):
    curiosity: float = Field(default=0.5, ge=0.0, le=1.0)
    empathy: float = Field(default=0.5, ge=0.0, le=1.0)
    humor: float = Field(default=0.5, ge=0.0, le=1.0)
    patience: float = Field(default=0.5, ge=0.0, le=1.0)
    confidence: float = Field(default=0.5, ge=0.0, le=1.0)
    dominance: float = Field(default=0.5, ge=0.0, le=1.0)
    sociability: float = Field(default=0.5, ge=0.0, le=1.0)