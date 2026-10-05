from app.state.personality import PersonalityState

PERSONALITY_PRESETS = {
    "neutre": PersonalityState(),
    "original": PersonalityState(
        curiosity=0.9, empathy=0.7, humor=0.6, patience=0.8, confidence=0.5,
        dominance=0.5, sociability=0.6,
    ),
    "erudit": PersonalityState(
        curiosity=0.95, empathy=0.4, humor=0.3, patience=0.8, confidence=0.6,
        dominance=0.6, sociability=0.3,
    ),
    "joueur": PersonalityState(
        curiosity=0.3, empathy=0.6, humor=0.9, patience=0.3, confidence=0.7,
        dominance=0.6, sociability=0.8,
    ),
    "impatient": PersonalityState(
        curiosity=0.6, empathy=0.4, humor=0.5, patience=0.1, confidence=0.5,
        dominance=0.8, sociability=0.5,
    ),
    "doux": PersonalityState(
        curiosity=0.5, empathy=0.9, humor=0.6, patience=0.9, confidence=0.3,
        dominance=0.2, sociability=0.7,
    ),
    "dominant": PersonalityState(
        curiosity=0.5, empathy=0.3, humor=0.5, patience=0.4, confidence=0.9,
        dominance=0.9, sociability=0.6,
    ),
    "timide": PersonalityState(
        curiosity=0.6, empathy=0.7, humor=0.4, patience=0.7, confidence=0.2,
        dominance=0.1, sociability=0.2,
    ),
}