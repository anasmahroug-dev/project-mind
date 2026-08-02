from app.perception.percept import Percept
from app.perception.types import PerceptSource, PerceptType
from app.perception.generators.base_perceptor import BasePerceptor


class EnergyPerceptor(BasePerceptor):

    def generate(
        self,
        mind_state,
        events,
    ) -> list[Percept]:

        percepts = []

        energy = mind_state.energy.level

        if energy <= 20:

            percepts.append(
                Percept(
                    type=PerceptType.LOW_ENERGY,
                    intensity=1 - energy / 20,
                    source=PerceptSource.ENERGY,
                )
            )

        elif energy >= 80:

            percepts.append(
                Percept(
                    type=PerceptType.HIGH_ENERGY,
                    intensity=(energy - 80) / 20,
                    source=PerceptSource.ENERGY,
                )
            )

        return percepts