from pydantic import BaseModel, Field

from app.actions.types import ActionType
from app.state.mood import Mood


class ActionSpec(BaseModel):
    duration: tuple[int, int]
    energy_per_tick: float = 0.0
    mood_per_tick: dict[Mood, float] = Field(default_factory=dict)
    interruptible: bool = True


ACTION_SPECS = {
    ActionType.READ: ActionSpec(
        duration=(2, 6),
        energy_per_tick=-0.5,
        mood_per_tick={Mood.CURIOUS: -0.005},
    ),
    ActionType.TALK_TO_USER: ActionSpec(
        duration=(1, 1),
        energy_per_tick=-0.5,
        mood_per_tick={Mood.CURIOUS: -0.03},
        interruptible=False,
    ),
    ActionType.DANCE: ActionSpec(
        duration=(2, 5),
        energy_per_tick=-1.5,
        mood_per_tick={Mood.HAPPY: 0.003,
                       Mood.BORED: -0.004},
    ),
    ActionType.PLAY_GAME: ActionSpec(
        duration=(3, 6),
        energy_per_tick=-0.7,
        mood_per_tick={Mood.HAPPY: 0.002,
                       Mood.BORED: -0.004},
    ),
    ActionType.EAT: ActionSpec(
        duration=(2, 4),
        energy_per_tick=3.0,
    ),
    ActionType.SLEEP: ActionSpec(
        duration=(6, 14),
        energy_per_tick=5.0,
    ),
}

assert set(ACTION_SPECS) == set(ActionType), "il manque une fiche d'action"