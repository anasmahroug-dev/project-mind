import threading

from app.engine.engine import Engine
from app.events.base_event import Event
from app.events.event_types import EventType


def start_console_input(engine: Engine) -> None:
    def listen() -> None:
        while True:
            try:
                text = input()
            except EOFError:
                return
            if text.strip():
                engine.submit(Event(type=EventType.USER_MESSAGE, content=text))

    threading.Thread(target=listen, daemon=True).start()