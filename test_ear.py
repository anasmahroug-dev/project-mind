from app.perception.ear import VaderToneAnalyzer

ear = VaderToneAnalyzer()
for text in [
    "You are amazing!",
    "thank you :)",
    "you're so stupid",
    "SHUT UP!!!",
    "this movie is awful",
    "not good",
    "hello",
]:
    print(text, "->", ear.analyze(text))