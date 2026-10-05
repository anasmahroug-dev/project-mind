from app.events.event_types import EventType
from app.events.base_event import Event
from app.personality.modulation import message_impact, UNDIRECTED_WEIGHT
from app.state.mind_state import MindState


AFFINITY_RATE = 0.05
CONTACT_RELIEF = 0.6

class Appraisal:
    def process(self, mind_state: MindState, events: list[Event]) -> None:
        for event in events:
            if event.type == EventType.USER_MESSAGE and event.tone is not None:
                impact = message_impact(mind_state.personality, event.tone)
                for mood, delta in impact.items():
                    mind_state.mood.shift(mood, delta)
                weight = 1.0 if event.tone.directed else UNDIRECTED_WEIGHT
                relationship = mind_state.relationship
                relationship.affinity = max(
                    -1.0,
                    min(1.0, relationship.affinity + AFFINITY_RATE * event.tone.valence * weight),
                )
                relationship.contact_need = max(0.0, relationship.contact_need - CONTACT_RELIEF * (1 + event.tone.valence) / 2)
                relationship.reply_pressure = max(relationship.reply_pressure, weight)
                
                relationship.last_contact_age = mind_state.age