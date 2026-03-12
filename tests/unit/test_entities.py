from core.entities import Creature, Monster, Player, Summon


def test_creature_hp_percent_and_alive() -> None:
    creature = Creature(entity_id="c1", name="Base", hp_current=50, hp_max=100)
    assert creature.hp_percent == 0.5
    assert creature.is_alive is True


def test_creature_hp_percent_clamps_values() -> None:
    low = Creature(entity_id="c2", name="Low", hp_current=-10, hp_max=100)
    high = Creature(entity_id="c3", name="High", hp_current=300, hp_max=100)
    assert low.hp_percent == 0.0
    assert high.hp_percent == 1.0


def test_monster_and_summon_inheritance() -> None:
    monster = Monster(entity_id="m1", name="Rat", threat_level=2)
    summon = Summon(entity_id="s1", name="Wolf", owner_id="p1", can_tank=True)
    assert monster.is_aggressive is True
    assert monster.threat_level == 2
    assert summon.owner_id == "p1"
    assert summon.can_tank is True


def test_player_mana_percent_and_summons() -> None:
    summon = Summon(entity_id="s1", name="Dragon", owner_id="p1")
    player = Player(
        entity_id="p1",
        name="Hero",
        mana_current=30,
        mana_max=60,
        summons=[summon],
    )
    assert player.mana_percent == 0.5
    assert len(player.summons) == 1
    assert player.summons[0].name == "Dragon"
