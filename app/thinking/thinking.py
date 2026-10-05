from app.perception.percept import Percept
from app.state.mind_state import MindState
from app.thinking.generators.boredom import BoredomThinker
from app.thinking.generators.curiosity import CuriosityThinker
from app.thinking.generators.happiness import HappinessThinker
from app.thinking.generators.energy import EnergyThinker
from app.thinking.generators.social import SocialThinker
from app.thinking.thought import Thought


class Thinking:
    def __init__(self):
        self.thinkers = [
            CuriosityThinker(),
            HappinessThinker(),
            EnergyThinker(),
            BoredomThinker(),
            SocialThinker(),
        ]
        
    def process(
        self,
        mind_state: MindState,
        percepts: list[Percept],
    ) -> list[Thought]:
        thoughts = []
        
        for thinker in self.thinkers:
            thoughts.extend(
                thinker.generate(
                    mind_state,
                    percepts,
                )
            )

        return thoughts