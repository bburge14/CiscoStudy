"""Each PBQ must be broken on build and pass ONLY after the correct remediation,
proving validation checks real resulting protocol state, not keystrokes.
"""
import pytest

from studyengine.cli_sim import SCENARIOS

FIXES = {
    "pbq-ccna-native-vlan": [
        "enable", "conf t", "interface gi0/1",
        "switchport trunk native vlan 99", "end",
    ],
    "pbq-ccna-etherchannel": [
        "enable", "conf t", "interface range gi0/1 - 2",
        "channel-group 1 mode active", "end",
    ],
    "pbq-ccna-ospf-area": [
        "enable", "conf t", "router ospf 1",
        "no network 10.1.12.0 0.0.0.3 area 1",
        "network 10.1.12.0 0.0.0.3 area 0", "end",
    ],
    "pbq-ccna-stp-root": [
        "enable", "conf t", "spanning-tree vlan 10 root primary", "end",
    ],
    "pbq-encor-ospf-mtu": [
        "enable", "conf t", "interface gi0/0", "mtu 1500", "end",
    ],
    "pbq-ccna-access-vlan": [
        "enable", "conf t", "vlan 20", "name USERS", "exit",
        "interface gi0/5", "switchport mode access",
        "switchport access vlan 20", "end",
    ],
}


def test_all_scenarios_have_fixes():
    assert set(FIXES) == set(SCENARIOS)


@pytest.mark.parametrize("sid", sorted(SCENARIOS))
def test_scenario_broken_then_fixed(sid):
    scenario = SCENARIOS[sid]
    topo = scenario.build()
    assert not scenario.passed(topo), f"{sid}: should start broken"
    con = scenario.console(topo)
    for line in FIXES[sid]:
        con.execute(line)
    checks = scenario.validate(topo)
    assert all(c.passed for c in checks), (
        f"{sid}: still failing after fix: "
        + "; ".join(c.description for c in checks if not c.passed)
    )


@pytest.mark.parametrize("sid", sorted(SCENARIOS))
def test_scenario_has_ticket_and_hints(sid):
    s = SCENARIOS[sid]
    assert s.ticket.strip()
    assert s.hints and all(h.strip() for h in s.hints)
    assert s.device in s.build().devices


def test_wrong_fix_does_not_pass_ospf_area():
    """A plausible-but-wrong change (right area, wrong link) must NOT pass."""
    scenario = SCENARIOS["pbq-ccna-ospf-area"]
    topo = scenario.build()
    con = scenario.console(topo)
    for line in ["enable", "conf t", "router ospf 1",
                 "network 10.9.9.0 0.0.0.3 area 0", "end"]:
        con.execute(line)
    assert not scenario.passed(topo)
