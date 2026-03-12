from __future__ import annotations

from core.types import BotState, Context


class StateMachine:
    """Finite-state machine com regras explicitas para transicoes."""

    def __init__(self, initial_state: BotState = BotState.IDLE) -> None:
        self._state = initial_state

    @property
    def state(self) -> BotState:
        return self._state

    def transition(self, context: Context) -> BotState:
        if context.hp_percent < 0.30:
            self._state = BotState.RECOVERY
            return self._state

        if context.has_enemy:
            self._state = BotState.COMBAT
            return self._state

        if context.inventory_full:
            self._state = BotState.IDLE
            return self._state

        self._state = BotState.FARM
        return self._state
