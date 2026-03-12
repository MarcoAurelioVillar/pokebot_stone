from __future__ import annotations

import logging


class InputController:
    """Adaptador de entrada.

    Troque por implementacao real com pyautogui/pydirectinput/etc.
    """

    def __init__(self, logger: logging.Logger) -> None:
        self._logger = logger

    def press(self, key: str) -> None:
        self._logger.debug("input.press key=%s", key)

    def click(self, x: int, y: int) -> None:
        self._logger.debug("input.click x=%s y=%s", x, y)
