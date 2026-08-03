from app.perception.percept import Percept
from app.perception.types import PerceptType


def find_percept(
    percepts: list[Percept],
    percept_type: PerceptType,
) -> Percept | None:

    for percept in percepts:

        if percept.type == percept_type:
            return percept

    return None

def find_percepts(
    percepts: list[Percept],
    *types: PerceptType,
) -> list[Percept]:

    return [
        percept
        for percept in percepts
        if percept.type in types
    ]