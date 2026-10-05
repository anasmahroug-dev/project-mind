from app.events.event_types import EventType
from app.perception.generators.base_perceptor import BasePerceptor
from app.perception.percept import Percept
from app.perception.types import PerceptSource, PerceptType
from app.personality.modulation import reply_urge

CONTACT_PERCEPT_THRESHOLD = 0.05


class UserPerceptor(BasePerceptor):

    def generate(self, mind_state, events) -> list[Percept]:
        percepts = [
            Percept(type=PerceptType.USER_MESSAGE, intensity=1.0, source=PerceptSource.USER)
            for event in events
            if event.type == EventType.USER_MESSAGE
        ]

        need = mind_state.relationship.contact_need
        urge = max(need, reply_urge(mind_state.personality, mind_state.relationship))
        if urge > CONTACT_PERCEPT_THRESHOLD:
            percepts.append(
                Percept(type=PerceptType.WANTS_CONTACT, intensity=urge, source=PerceptSource.USER)
                )

        return percepts