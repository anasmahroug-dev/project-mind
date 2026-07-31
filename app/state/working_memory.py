from pydantic import BaseModel

class WorkingMemory(BaseModel):
    items: list[str]