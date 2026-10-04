import re

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from app.events.tone import Tone

SECOND_PERSON = re.compile(
    r"\b(you|your|yours|yourself|you're|youre|u|ur|your)\b", re.IGNORECASE
)               


class ToneAnalyzer:
    def analyze(self, text: str) -> Tone:
        raise NotImplementedError
    
class VaderToneAnalyzer(ToneAnalyzer):
    def __init__(self):
        self._vader = SentimentIntensityAnalyzer()
        
    def analyze(self, text: str) -> Tone:
        compound = self._vader.polarity_scores(text)["compound"]
        return Tone(valence=compound, directed=bool(SECOND_PERSON.search(text)))
    
    
        