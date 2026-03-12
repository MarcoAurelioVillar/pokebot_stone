from core.state_machine import StateMachine
from core.types import BotState, Context


def test_recovery_has_priority() -> None:
    fsm = StateMachine()
    context = Context(tick=1, hp_percent=0.2, has_enemy=True, inventory_full=False)
    assert fsm.transition(context) == BotState.RECOVERY


def test_combat_when_enemy_and_hp_ok() -> None:
    fsm = StateMachine()
    context = Context(tick=2, hp_percent=0.9, has_enemy=True, inventory_full=False)
    assert fsm.transition(context) == BotState.COMBAT


def test_idle_when_inventory_full_without_enemy() -> None:
    fsm = StateMachine()
    context = Context(tick=3, hp_percent=0.9, has_enemy=False, inventory_full=True)
    assert fsm.transition(context) == BotState.IDLE
