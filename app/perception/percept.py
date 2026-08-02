from pydantic import Field

from app.perception.base_percept import BasePercept
from app.perception.types import PerceptSource


class Percept(BasePercept):
    intensity: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
    )

    source: PerceptSource