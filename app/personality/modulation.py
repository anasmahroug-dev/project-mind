from app.actions.types import ActionType
from app.state.goal import GoalType
from app.state.mood import Mood
from app.state.personality import PersonalityState

WEIGHT_SPREAD = 1.0  # un trait de 0 à 1 fait varier le poids de 0.5 à 1.5
BOREDOM_DRIFT_DEFAULT = 0.003
BOREDOM_DRIFT_SPREAD = 0.003
REPETITION_DEFAULT = 0.05
REPETITION_SPREAD = 0.04
EFFECT_SPREAD = 0.3  # gain de 0.85 à 1.15


def trait_weight(trait: float, spread: float = WEIGHT_SPREAD) -> float:
    """1.0 pour un trait à 0.5 ; jamais proche de 0 : aucune action n'est exclue."""
    return max(0.05, 1.0 + spread * (trait - 0.5))


def action_weights(
    personality: PersonalityState,
    goal_type: GoalType,
) -> dict[ActionType, float]:
    if goal_type == GoalType.ACQUIRE_KNOWLEDGE:
        return {
            ActionType.READ: trait_weight(personality.curiosity),
            ActionType.TALK_TO_USER: trait_weight(personality.empathy),
        }
    if goal_type == GoalType.SEEK_ENJOYMENT:
        return {
            ActionType.TALK_TO_USER: trait_weight(personality.empathy),
            ActionType.DANCE: trait_weight(personality.humor),
            ActionType.PLAY_GAME: trait_weight(personality.humor),
        }
        
    if goal_type == GoalType.GET_ENTERTAINED:
        return {
        ActionType.READ: trait_weight(personality.curiosity),
        ActionType.DANCE: trait_weight(personality.humor),
        ActionType.PLAY_GAME: trait_weight(personality.humor),
        }
    raise ValueError(f"pas de poids d'action pour le goal {goal_type}")

def mood_drift(personality: PersonalityState) -> dict[Mood, float]:
    impatience = 1.0 - personality.patience
    return {
        Mood.BORED: BOREDOM_DRIFT_DEFAULT + BOREDOM_DRIFT_SPREAD * (impatience - 0.5),
    }


def repetition_boredom(personality: PersonalityState) -> float:
    impatience = 1.0 - personality.patience
    return REPETITION_DEFAULT + REPETITION_SPREAD * (impatience - 0.5)

def mood_effect_gain(personality: PersonalityState, mood: Mood) -> float:
    """Multiplicateur appliqué aux effets d'une action sur une humeur."""
    if mood == Mood.CURIOUS:
        # un PNJ très curieux se rassasie moins vite
        return max(0.05, 1.0 - EFFECT_SPREAD * (personality.curiosity - 0.5))
    if mood == Mood.HAPPY:
        # un PNJ plein d'humour tire plus de joie de ce qui l'amuse
        return max(0.05, 1.0 + EFFECT_SPREAD * (personality.humor - 0.5))
    return 1.0