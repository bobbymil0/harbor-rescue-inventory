from src.challenges import (
    mission_snapshot,
    cargo_window,
    first_supply_index,
    supply_report,
    priority_load,
)


def test_mission_snapshot():
    assert mission_snapshot(["rope", "radio", "water"]) == ("rope", "water")
    assert mission_snapshot(["flare"]) == ("flare", "flare")
    assert mission_snapshot([]) == (None, None)


def test_cargo_window():
    assert cargo_window(["rope", "radio", "water", "medkit"], 1, 2) == ["radio", "water"]
    assert cargo_window(["rope", "radio"], 0, 5) == ["rope", "radio"]
    assert cargo_window(["rope", "radio"], 5, 2) == []
    assert cargo_window(["rope", "radio"], 1, 0) == []


def test_first_supply_index():
    assert first_supply_index(["rope", "radio", "water"], "radio") == 1
    assert first_supply_index(["rope", "rope", "water"], "rope") == 0
    assert first_supply_index([], "radio") == -1
    assert first_supply_index(["rope", "radio"], "medkit") == -1


def test_supply_report():
    assert supply_report(["medkit", "rope", "medkit"], "medkit") == (2, 0)
    assert supply_report(["rope", "radio", "water"], "medkit") == (0, -1)
    assert supply_report([], "medkit") == (0, -1)


def test_priority_load():
    assert priority_load(["rope", "radio"], "medkit") == ["medkit", "rope", "radio"]
    assert priority_load([], "flare") == ["flare"]