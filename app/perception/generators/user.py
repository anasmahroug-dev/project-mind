from app.perception.percept import Percept
from app.perception.types import PerceptType
from app.perception.generators.base_perceptor import BasePerceptor

class UserPerceptor(BasePerceptor):

    def generate(
        self,
        mind_state,
        events,
    ) -> list[Percept]:

        return []