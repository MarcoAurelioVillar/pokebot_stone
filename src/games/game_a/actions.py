from __future__ import annotations

import logging

from core.types import BotState, Context
from infra.input_controller import InputController


class Actions:
    def __init__(self, input_controller: InputController, logger: logging.Logger) -> None:
        self._input = input_controller
        self._logger = logger

    def run(self, state: BotState, context: Context) -> None:
        if state == BotState.RECOVERY:
            self._logger.info("acao=recovery usar_pocao")
            self._input.press("F1")
            return

        if state == BotState.COMBAT:
            self._logger.info("acao=combat atacar")
            self._input.press("SPACE")
            return

        if state == BotState.FARM:
            self._logger.info("acao=farm coletar")
            self._input.press("E")
            return

        self._logger.info("acao=idle aguardar")
