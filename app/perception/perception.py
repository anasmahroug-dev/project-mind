from app.perception.generators.energy import EnergyPerceptor
from app.perception.generators.goal import GoalPerceptor
from app.perception.generators.memory import MemoryPerceptor
from app.perception.generators.mood import MoodPerceptor
from app.perception.generators.time import TimePerceptor
from app.perception.generators.user import UserPerceptor    

from app.state.mind_state import MindState
from app.events.base_event import Event  

from app.perception.percept import Percept

class Perception:

    def __init__(self):

        self.generators = [
            EnergyPerceptor(),
            MoodPerceptor(),
            GoalPerceptor(),
            MemoryPerceptor(),
            TimePerceptor(),
            UserPerceptor(),
        ]

    def process(
        self,
        mind_state: MindState,
        events: list[Event],
    ) -> list[Percept]:

        percepts = []

        for generator in self.generators:
            percepts.extend(
                generator.generate(
                    mind_state,
                    events,
                )
            )

        return percepts