from app.state.mind_state import MindState
from app.personality.modulation import contact_need_rate
ENERGY_DECAY_RATE = 0.1 
REPLY_PRESSURE_DECAY = 0.95

class StateUpdater:

    def process(
        self,
        mind_state: MindState
    ) -> None:
        self._update_age(mind_state)
        self._apply_metabolism(mind_state)
        self._update_contact_need(mind_state)
        self._update_reply_pressure(mind_state)
    
    def _update_age(
        self,
        mind_state: MindState
    ) -> None:
        mind_state.age += 1
        
    def _apply_metabolism(
        self,
        mind_state: MindState
    ) -> None:
        
        mind_state.energy.level = max(
            0.0,
            mind_state.energy.level - ENERGY_DECAY_RATE)
        
    def _update_contact_need(
        self,
        mind_state: MindState
    ) -> None:
        
        mind_state.relationship.contact_need = min(mind_state.relationship.contact_need + contact_need_rate(mind_state.personality), 1.0)
        
    def _update_reply_pressure(
        self,
        mind_state: MindState
    ) -> None:
        mind_state.relationship.reply_pressure *= REPLY_PRESSURE_DECAY