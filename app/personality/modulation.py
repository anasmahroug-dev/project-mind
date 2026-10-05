from app.actions.types import ActionType
from app.state.goal import GoalType
from app.state.mood import Mood
from app.state.personality import PersonalityState
from app.events.tone import Tone
from app.state.relationship import RelationshipState


WEIGHT_SPREAD = 1.0  # un trait de 0 à 1 fait varier le poids de 0.5 à 1.5
BOREDOM_DRIFT_DEFAULT = 0.003
BOREDOM_DRIFT_SPREAD = 0.003
REPETITION_DEFAULT = 0.05
REPETITION_SPREAD = 0.04
EFFECT_SPREAD = 0.3  # gain de 0.85 à 1.15

UNDIRECTED_WEIGHT = 0.3   # un message qui ne s'adresse pas au PNJ compte 30 %
EMPATHY_SPREAD = 0.6      # sensibilité de 0.7 à 1.3
CONFIDENCE_SPREAD = 0.6   # vulnérabilité à l'hostilité de 1.3 à 0.7

CONTACT_RISE_DEFAULT = 0.002   # 0.0 désactive toute la chaîne
SOCIABILITY_SPREAD = 1.0       # facteur de 0.5 à 1.5

REPLY_BASE = 0.80


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
            ActionType.REFLECT: trait_weight(personality.empathy),
        }
    if goal_type == GoalType.SEEK_ENJOYMENT:
        return {
            ActionType.REFLECT: trait_weight(personality.empathy),
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


def message_impact(personality: PersonalityState, tone: Tone) -> dict[Mood, float]:
    weight = 1.0 if tone.directed else UNDIRECTED_WEIGHT
    sensitivity = 1.0 + EMPATHY_SPREAD * (personality.empathy - 0.5)
    vulnerability = 1.0 + CONFIDENCE_SPREAD * (0.5 - personality.confidence)

    v = tone.valence * weight * sensitivity
    if v < 0:
        v *= vulnerability

    return {
        Mood.HAPPY: 0.15 * v,
        Mood.SAD: -0.10 * v,
        Mood.STRESSED: 0.10 * max(0.0, -v),
        Mood.BORED: -0.08 * weight,   # tout contact est une stimulation
    }
    
def contact_need_rate(personality: PersonalityState) -> float:
    return CONTACT_RISE_DEFAULT * (1.0 + SOCIABILITY_SPREAD * (personality.sociability - 0.5))

def willingness(personality: PersonalityState, relationship: RelationshipState) -> float:
    w = (
        REPLY_BASE
        + 0.50 * relationship.affinity
        + 0.30 * (personality.sociability - 0.5)
        + 0.25 * (personality.empathy - 0.5)
        - 0.40 * (personality.dominance - 0.5)
        + 0.20 * (personality.humor - 0.5)
        + 0.30 * relationship.contact_need
    )
    return max(0.0, min(1.0, w))

def reply_urge(personality: PersonalityState, relationship: RelationshipState) -> float:
    x = max(0.0, min(1.0, (willingness(personality, relationship) - 0.25)/0.40))
    return relationship.reply_pressure * x * x * (3 - 2 * x) # transition douce entre 0.25 et 0.65