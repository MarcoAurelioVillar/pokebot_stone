from __future__ import annotations

from core.types import Context


def detect_context(tick: int) -> Context:
    """Detector mock: simula leitura de estado de jogo."""
    hp = 1.0 if tick % 7 else 0.2
    has_enemy = tick % 2 == 0
    inventory_full = tick % 11 == 0
    return Context(
        tick=tick,
        hp_percent=hp,
        has_enemy=has_enemy,
        inventory_full=inventory_full,
    )
