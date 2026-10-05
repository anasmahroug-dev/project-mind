import random
import statistics

from app.actions.types import ActionType
from app.brain.brain import Brain
from app.defaults.initial_state import create_initial_mind_state
from app.events.base_event import Event
from app.events.event_types import EventType
from app.events.tone import Tone

PRESETS_TO_TEST = ["neutre", "doux", "timide", "erudit", "dominant"]
AFFINITIES = [0.5, 0.0, -0.5, -1.0]
SEEDS = range(40)
WARMUP = 300
HORIZON = 60


def reply_test(preset: str, affinity: float, seed: int) -> tuple[int | None, int]:
    """(délai avant la première réponse ou None, nombre de messages envoyés)."""
    random.seed(seed)
    brain = Brain()
    state = create_initial_mind_state(preset)
    for _ in range(WARMUP):
        state, *_ = brain.step(state, [])

    state.relationship.affinity = affinity
    message = Event(
        type=EventType.USER_MESSAGE,
        content="hello",
        tone=Tone(valence=0.2, directed=True),
    )

    first_delay = None
    sent = 0
    for tick in range(HORIZON):
        events = [message] if tick == 0 else []
        state, percepts, thoughts, focus, goal, action = brain.step(state, events)
        if (action is not None
                and action.type == ActionType.TALK_TO_USER
                and action.remaining_ticks == action.duration):
            sent += 1
            if first_delay is None:
                first_delay = tick
    return first_delay, sent


def main() -> None:
    print("affinité " + "".join(f"{name:>24s}" for name in PRESETS_TO_TEST))
    for affinity in AFFINITIES:
        cells = []
        for preset in PRESETS_TO_TEST:
            results = [reply_test(preset, affinity, seed) for seed in SEEDS]
            replied = [(d, n) for d, n in results if d is not None]
            median = statistics.median(d for d, _ in replied) if replied else "-"
            mean_sent = statistics.mean(n for _, n in replied) if replied else 0
            cells.append(f"{len(replied)}/{len(results)} d={median} n={mean_sent:.1f}")
        print(f"{affinity:>+8.1f} " + "".join(f"{cell:>24s}" for cell in cells))


if __name__ == "__main__":
    main()