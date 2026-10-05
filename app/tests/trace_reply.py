import random

from app.brain.brain import Brain
from app.defaults.initial_state import create_initial_mind_state
from app.events.base_event import Event
from app.events.event_types import EventType
from app.events.tone import Tone
from app.personality.modulation import reply_urge, willingness

PRESET, AFFINITY, SEED = "erudit", 0.0, 0

random.seed(SEED)
brain = Brain()
state = create_initial_mind_state(PRESET)
for _ in range(300):
    state, *_ = brain.step(state, [])
state.relationship.affinity = AFFINITY
print("avant le message : action en cours =",
      state.current_action.type.value if state.current_action else None,
      "| besoin =", round(state.relationship.contact_need, 2))

message = Event(type=EventType.USER_MESSAGE, content="hello",
                tone=Tone(valence=0.2, directed=True))
for tick in range(10):
    state, percepts, thoughts, focus, goal, action = brain.step(
        state, [message] if tick == 0 else [])
    r = state.relationship
    wants = [round(p.intensity, 2) for p in percepts if p.type.value == "wants_contact"]
    print(tick,
          "pression", round(r.reply_pressure, 2),
          "volonté", round(willingness(state.personality, r), 2),
          "envie", round(reply_urge(state.personality, r), 2),
          "| percept wants_contact", wants,
          "| pensées", [(t.type.value, round(t.priority, 2)) for t in thoughts],
          "| goal", goal.type.value if goal else None,
          "| action", action.type.value if action else None)