import re

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from app.events.tone import Tone

SECOND_PERSON = re.compile(
    r"\b(you|your|yours|yourself|you're|youre|u|ur)\b", re.IGNORECASE
)

# Mots à ajouter ou à corriger, sur l'échelle de VADER (-4 à +4). Exemples à ajuster.
EXTRA_WORDS = {
    "stfu": -3.0,
    "gtfo": -2.5,
    "cringe": -2.0,
    "toxic": -2.5,
    "slay": 2.0,

}

# Expressions : (valence ajoutée, adressée au PNJ ?). Exemples à compléter.
EXPRESSIONS = {
    "shut up": (-0.5, True),
    "go away": (-0.5, True),
    "leave me alone": (-0.5, True),
    "hello": (0.2, True),
    "hi": (0.2, True),
    "good morning": (0.2, True),
    "good night": (0.2, True),
    "kys": (-0.9, True),
}
_EXPRESSION_PATTERNS = {
    phrase: re.compile(rf"\b{re.escape(phrase)}\b", re.IGNORECASE)
    for phrase in EXPRESSIONS
}


def _emphasis(text: str) -> float:
    """Multiplicateur : chaque '!' (jusqu'à 3) et les majuscules renforcent."""
    boost = 1.0 + 0.15 * min(text.count("!"), 3)
    letters = [c for c in text if c.isalpha()]
    if len(letters) >= 3 and all(c.isupper() for c in letters):
        boost += 0.25
    return boost


class ToneAnalyzer:
    def analyze(self, text: str) -> Tone:
        raise NotImplementedError


class VaderToneAnalyzer(ToneAnalyzer):
    def __init__(self) -> None:
        self._vader = SentimentIntensityAnalyzer()
        self._vader.lexicon.update(EXTRA_WORDS)

    def analyze(self, text: str) -> Tone:
        valence = self._vader.polarity_scores(text)["compound"]
        directed = bool(SECOND_PERSON.search(text))

        extra = 0.0
        for phrase, (phrase_valence, phrase_directed) in EXPRESSIONS.items():
            if _EXPRESSION_PATTERNS[phrase].search(text):
                extra += phrase_valence
                directed = directed or phrase_directed

        valence = max(-1.0, min(1.0, valence + extra * _emphasis(text)))
        return Tone(valence=valence, directed=directed)