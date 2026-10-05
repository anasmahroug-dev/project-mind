from app.perception.percept import Percept
from app.perception.types import PerceptType
from app.perception.utils import find_percept
from app.state.mind_state import MindState
from app.thinking.generators.base_thinker import BaseThinker
from app.thinking.thought import Thought
from app.thinking.types import ThoughtType


class SocialThinker(BaseThinker):

    def generate(self, mind_state: MindState, percepts: list[Percept]) -> list[Thought]:
        wants_contact = find_percept(percepts, PerceptType.WANTS_CONTACT)

        if wants_contact is None:
            return []

        return [
            Thought(
                type=ThoughtType.SPEAK,
                priority=wants_contact.intensity,
                triggers=[wants_contact],
            )
        ]