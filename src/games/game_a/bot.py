from __future__ import annotations

from pathlib import Path

from core.bot import BotEngine
from core.state_machine import StateMachine
from games.game_a.actions import Actions
from games.game_a.detectors import detect_context
from infra.config import load_yaml
from infra.input_controller import InputController
from infra.logger import setup_logger


def build_bot() -> BotEngine:
    logger = setup_logger("game_a")
    config_path = Path(__file__).with_name("config.yaml")
    config = load_yaml(config_path)
    logger.info("config carregada: profile=%s", config.get("profile", "default"))

    input_controller = InputController(logger=logger)
    actions = Actions(input_controller=input_controller, logger=logger)
    fsm = StateMachine()

    return BotEngine(
        detect=detect_context,
        act=actions.run,
        logger=logger,
        fsm=fsm,
    )
