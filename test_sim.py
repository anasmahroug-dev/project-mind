import collections
import random

from app.brain.brain import Brain
from app.defaults.initial_state import create_initial_mind_state
from app.personality.presets import PERSONALITY_PRESETS
from app.state.mood import Mood


def simulate(preset: str = "neutre", ticks: int = 3000, seed: int = 42) -> dict:
    random.seed(seed)
    brain = Brain()
    state = create_initial_mind_state(preset)

    dominant = collections.Counter()
    actions = collections.Counter()
    goals = []
    energies = []
    sequence = []

    for _ in range(ticks):
        state, percepts, thoughts, focus, goal, action = brain.step(state, [])

        dominant[state.mood.dominant.value] += 1
        energies.append(state.energy.level)
        sequence.append(state.mood.dominant.value[0])

        is_new_action = action is not None and action.remaining_ticks == action.duration
        if is_new_action:
            actions[action.type.value] += 1
            if goal is not None and action.type.value not in ("sleep", "eat"):
                goals.append(goal.type.value)

    goal_changes = sum(1 for a, b in zip(goals, goals[1:]) if a != b)
    return {
        "dominant": dict(dominant),
        "actions": dict(actions),
        "goal_actions": len(goals),
        "goal_changes": goal_changes,
        "energy_min": round(min(energies)),
        "energy_mean": round(sum(energies) / len(energies)),
        "sequence": "".join(sequence),
    }


def print_report(name: str, result: dict, show_sequence: int = 0) -> None:
    print(f"== {name} ==")
    if show_sequence:
        print(result["sequence"][:show_sequence])
    print("humeur dominante :", result["dominant"])
    print("actions          :", result["actions"])
    print(f"{result['goal_actions']} actions de goal, {result['goal_changes']} changements de goal")
    print("énergie min", result["energy_min"], "moyenne", result["energy_mean"])


def trace_boredom(preset: str = "neutre", start: int = 40, end: int = 80, seed: int = 42) -> None:
    random.seed(seed)
    brain = Brain()
    state = create_initial_mind_state(preset)
    for tick in range(end):
        state, percepts, thoughts, focus, goal, action = brain.step(state, [])
        if tick >= start and state.mood.dominant == Mood.BORED:
            print(tick,
                  "pensée :", focus.type.value if focus else None,
                  "| goal :", goal.type.value if goal else None,
                  "| action :", action.type.value if action else None)

def compare(seeds=range(5)):
    for name in PERSONALITY_PRESETS:
        totals = collections.Counter()
        for seed in seeds:
            totals.update(simulate(name, seed=seed)["dominant"])
        means = {mood: round(count / len(seeds)) for mood, count in totals.items()}
        print(f"{name:10s}", means)

for name in PERSONALITY_PRESETS:
        print_report(name, simulate(name))
        
compare()
