from app.state.personality import PersonalityState

PERSONALITY_PRESETS = {
    "neutre": PersonalityState(),
    "original": PersonalityState(
        curiosity=0.9, empathy=0.7, humor=0.6, patience=0.8, confidence=0.5
    ),
    "erudit": PersonalityState(
        curiosity=0.95, empathy=0.4, humor=0.3, patience=0.8, confidence=0.6
    ),
    "joueur": PersonalityState(
        curiosity=0.3, empathy=0.6, humor=0.9, patience=0.3, confidence=0.7
    ),
    "impatient": PersonalityState(
        curiosity=0.6, empathy=0.4, humor=0.5, patience=0.1, confidence=0.5
    ),
    "doux": PersonalityState(
        curiosity=0.5, empathy=0.9, humor=0.6, patience=0.9, confidence=0.3
    ),
}