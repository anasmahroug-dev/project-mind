from pydantic import BaseModel, Field

class Tone(BaseModel):
    valence: float = Field(ge=-1.0, le=1.0)
    directed: bool