from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Creature:
    entity_id: str
    name: str
    level: int = 1
    hp_current: int = 100
    hp_max: int = 100

    @property
    def hp_percent(self) -> float:
        if self.hp_max <= 0:
            return 0.0
        return max(0.0, min(1.0, self.hp_current / self.hp_max))

    @property
    def is_alive(self) -> bool:
        return self.hp_current > 0


@dataclass(slots=True)
class Monster(Creature):
    is_boss: bool = False
    is_aggressive: bool = True
    threat_level: int = 1


@dataclass(slots=True)
class Summon(Creature):
    owner_id: str = ""
    duration_ticks: int | None = None
    can_tank: bool = False


@dataclass(slots=True)
class Player(Creature):
    mana_current: int = 100
    mana_max: int = 100
    summons: list[Summon] = field(default_factory=list)

    @property
    def mana_percent(self) -> float:
        if self.mana_max <= 0:
            return 0.0
        return max(0.0, min(1.0, self.mana_current / self.mana_max))
