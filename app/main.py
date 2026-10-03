from app.engine.engine import Engine
from app.interface.console import start_console_input

def main():
    engine = Engine()
    start_console_input(engine)
    try:
        engine.run()
    except KeyboardInterrupt:
        print("\nArrêt du moteur.")

if __name__ == "__main__":
    main()