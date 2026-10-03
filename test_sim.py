import collections
from app.brain.brain import Brain
from app.defaults.initial_state import create_initial_mind_state
import random
from app.state.mood import Mood

random.seed(42)

brain = Brain()
state = create_initial_mind_state()
dominant = collections.Counter()
actions = collections.Counter()
sequence = ""
for tick in range(300):
    state, *_ = brain.step(state, [])
    sequence += state.mood.dominant.value[0]   # "h" ou "c"
print(sequence)
for tick in range(3000):
    state, percepts, thoughts, focus, goal, action = brain.step(state, [])
    dominant[state.mood.dominant.value] += 1
    if action is not None and action.remaining_ticks == action.duration:
        actions[action.type.value] += 1

print(dominant)
print(actions)

goals = []
for tick in range(3000):
    state, percepts, thoughts, focus, goal, action = brain.step(state, [])
    if (action is not None
            and action.remaining_ticks == action.duration
            and action.type.value not in ("sleep", "eat")
            and goal is not None):
        goals.append(goal.type.value)

changes = sum(1 for a, b in zip(goals, goals[1:]) if a != b)
print(len(goals), "actions,", changes, "changements de goal")
energies = []
for tick in range(3000):
    state, percepts, thoughts, focus, goal, action = brain.step(state, [])
    energies.append(state.energy.level)
    
    
print("énergie min", round(min(energies)), "moyenne", round(sum(energies) / len(energies)))

for tick in range(200):
    state, percepts, thoughts, focus, goal, action = brain.step(state, [])
    if 40 <= tick < 80 and state.mood.dominant == Mood.BORED:
        print(tick,
              "pensée :", focus.type.value if focus else None,
              "| goal :", goal.type.value if goal else None,
              "| action :", action.type.value if action else None)