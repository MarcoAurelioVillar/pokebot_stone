from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Callable

from core.state_machine import StateMachine
from core.types import BotState, Context

DetectFn = Callable[[int], Context]
ActFn = Callable[[BotState, Context], None]


@dataclass(slots=True)
class BotEngine:
    detect: DetectFn
    act: ActFn
    logger: logging.Logger
    fsm: StateMachine

    def run(self, ticks: int) -> None:
        for tick in range(1, ticks + 1):
            context = self.detect(tick)
            next_state = self.fsm.transition(context)
            self.logger.info(
                "tick=%s state=%s hp=%.2f enemy=%s inv_full=%s",
                tick,
                next_state.value,
                context.hp_percent,
                context.has_enemy,
                context.inventory_full,
            )
            self.act(next_state, context)
