from games.game_a.bot import build_bot


def test_game_a_runs_two_ticks() -> None:
    bot = build_bot()
    bot.run(ticks=2)
