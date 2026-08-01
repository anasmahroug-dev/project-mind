from app.state.mind_state import MindState

ENERGY_DECAY_RATE = 0.1 

class StateUpdater:

    def process(
        self,
        mind_state: MindState
    ) -> None:
        """
        Updates internal state over time.
        """
        pass
    
    def _update_age(
        self,
        mind_state: MindState
    ) -> None:
        mind_state.age += 1
        
    def _update_energy(
        self,
        mind_state: MindState
    ) -> None:
        
        mind_state.energy.level = max(
            0.0,
            mind_state.energy.level - ENERGY_DECAY_RATE)