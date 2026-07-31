from pydantic import BaseModel, Field

class Goal(BaseModel):
    title : str
    priority: int = Field(ge=1, le=10)