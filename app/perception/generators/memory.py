from app.perception.percept import Percept
from app.perception.generators.base_perceptor import BasePerceptor


class MemoryPerceptor(BasePerceptor):

    def generate(
        self,
        mind_state,
        events,
    ) -> list[Percept]:

        return []