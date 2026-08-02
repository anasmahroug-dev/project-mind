from pydantic import BaseModel
from app.perception.types import PerceptType


class BasePercept(BaseModel):
    type: PerceptType