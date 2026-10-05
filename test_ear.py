from app.perception.ear import VaderToneAnalyzer

ear = VaderToneAnalyzer()
CASES = [
    # (texte, signe attendu : +1 / -1 / 0, adressé au PNJ ?)
    ("You are amazing!", +1, True),
    ("thank you :)", +1, True),
    ("you're so stupid", -1, True),
    ("SHUT UP!!!", -1, True),
    ("this movie is awful", -1, False),
    ("not good", -1, False),
    ("hello", +1, True),
]

for text, sign, directed in CASES:
    tone = ear.analyze(text)
    got = 0 if abs(tone.valence) < 0.05 else (1 if tone.valence > 0 else -1)
    status = "OK  " if got == sign and tone.directed == directed else "FAIL"
    print(status, text, "->", tone)