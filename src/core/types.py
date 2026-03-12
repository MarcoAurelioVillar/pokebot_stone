from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class BotState(str, Enum):
    IDLE = "IDLE"
    FARM = "FARM"
    COMBAT = "COMBAT"
    RECOVERY = "RECOVERY"


@dataclass(slots=True)
class Context:
    tick: int = 0
    hp_percent: float = 1.0
    has_enemy: bool = False
    inventory_full: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)
