from app.perception.percept import Percept
from app.perception.types import PerceptSource, PerceptType
from app.perception.generators.base_perceptor import BasePerceptor

class MoodPerceptor(BasePerceptor):

    def generate(
        self,
        mind_state,
        events,
    ) -> list[Percept]:
        percepts = []
        
        for mood, level in mind_state.mood.levels.items():
            percepts.append(
                Percept(type=PerceptType(mood.value),
                        intensity=level,
                        source=PerceptSource.MOOD)
            )
        return percepts