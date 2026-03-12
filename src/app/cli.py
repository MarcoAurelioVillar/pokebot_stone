from __future__ import annotations

import argparse
import sys

from games.game_a.bot import build_bot


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="robo-game")
    sub = parser.add_subparsers(dest="command", required=True)

    run_parser = sub.add_parser("run", help="Executa um bot")
    run_parser.add_argument("--game", default="game_a", choices=["game_a"])
    run_parser.add_argument("--ticks", type=int, default=10)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "run":
        if args.game == "game_a":
            bot = build_bot()
            bot.run(ticks=args.ticks)
            return 0
        parser.error(f"Jogo nao suportado: {args.game}")
        return 2

    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
