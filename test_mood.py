from app.defaults.initial_state import create_initial_mind_state
from app.mood.mood_manager import MoodManager
from app.perception.generators.mood import MoodPerceptor
from app.state.mood import Mood

state = create_initial_mind_state()
manager = MoodManager()

for tick in range(61):
    if tick % 10 == 0:
        levels = {m.value: round(v, 2) for m, v in state.mood.levels.items()}
        print(tick, levels, "->", state.mood.dominant.value)
    manager.process(state)
    
percepts = MoodPerceptor().generate(state, [])
print(len(percepts))
for p in percepts:
    print(p.type.value, round(p.intensity, 2))
    
state.mood.shift(Mood.HAPPY, 5.0)
print(state.mood.levels[Mood.HAPPY])   # attendu : 1.0
state.mood.shift(Mood.HAPPY, -5.0)
print(state.mood.levels[Mood.HAPPY])   # attendu : 0.0    