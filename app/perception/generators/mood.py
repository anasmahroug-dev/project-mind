from app.perception.percept import Percept
from app.perception.types import PerceptSource, PerceptType
from app.perception.generators.base_perceptor import BasePerceptor

class MoodPerceptor(BasePerceptor):

    def generate(
        self,
        mind_state,
        events,
    ) -> list[Percept]:

        return [
            Percept(
                type=PerceptType(mind_state.mood.current.value),
                intensity=mind_state.mood.intensity,
                source=PerceptSource.MOOD,
            )
        ]