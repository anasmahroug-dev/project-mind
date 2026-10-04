import threading

from app.engine.engine import Engine
from app.events.base_event import Event
from app.events.event_types import EventType
from app.perception.ear import ToneAnalyzer


def start_console_input(engine: Engine, ear: ToneAnalyzer) -> None:
    def listen() -> None:
        while True:
            try:
                text = input()
                tone = ear.analyze(text)
                
            except EOFError:
                return
            if text.strip():
                engine.submit(Event(type=EventType.USER_MESSAGE, content=text, tone=tone))

    threading.Thread(target=listen, daemon=True).start()