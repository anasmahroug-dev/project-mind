import argparse

from app.engine.engine import Engine
from app.interface.console import start_console_input
from app.perception.ear import VaderToneAnalyzer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preset", default="neutre")
    parser.add_argument("--affinity", type=float, default=0.0)
    parser.add_argument("--quiet", action="store_true", help="affichage compact pour discuter")

    args = parser.parse_args()

    engine = Engine(preset=args.preset, verbose=not args.quiet)
    engine.state.relationship.affinity = args.affinity

    start_console_input(engine, VaderToneAnalyzer())
    try:
        engine.run()
    except KeyboardInterrupt:
        print("\nArrêt.")


if __name__ == "__main__":
    main()