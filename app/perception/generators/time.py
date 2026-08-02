from app.perception.percept import Percept
from app.perception.types import PerceptSource, PerceptType
from app.perception.generators.base_perceptor import BasePerceptor

class TimePerceptor(BasePerceptor):

    def generate(
        self,
        mind_state,
        events,
    ) -> list[Percept]:

        return [
            Percept(
                type=PerceptType.TIME_PASSED,
                source=PerceptSource.TIME,
            )
        ]