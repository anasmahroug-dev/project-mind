from app.perception.percept import Percept
from app.perception.types import PerceptSource, PerceptType
from app.perception.generators.base_perceptor import BasePerceptor



class GoalPerceptor(BasePerceptor):

    def generate(
        self,
        mind_state,
        events,
    ) -> list[Percept]:

        if mind_state.current_goal is None:

            return [
                Percept(
                    type=PerceptType.NO_GOAL,
                    source=PerceptSource.GOAL,
                )
            ]

        return [
            Percept(
                type=PerceptType.HAS_GOAL,
                source=PerceptSource.GOAL,
            )
        ]