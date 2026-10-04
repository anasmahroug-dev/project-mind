from app.engine.engine import Engine
from app.interface.console import start_console_input
from app.perception.ear import VaderToneAnalyzer

def main():
    engine = Engine()
    ear = VaderToneAnalyzer()
    start_console_input(engine, ear)
    try:
        engine.run()
    except KeyboardInterrupt:
        print("\nArrêt du moteur.")

if __name__ == "__main__":
    main()