from studyengine.cli_sim import SCENARIOS, topology_dot


def test_dot_valid_for_every_scenario():
    for sid, scen in SCENARIOS.items():
        topo = scen.build()
        dot = topology_dot(topo, scen.device)
        assert dot.startswith("graph G {")
        assert dot.rstrip().endswith("}")
        for name in topo.devices:
            assert f'"{name}"' in dot, f"{sid}: {name} missing from diagram"
        assert "#1BA0D7" in dot  # the console device is highlighted


def test_dot_annotates_interfaces_and_ips():
    topo = SCENARIOS["pbq-ccna-ospf-area"].build()
    dot = topology_dot(topo)
    assert "Gi0/0" in dot              # abbreviated interface name on the link
    assert "10.1.12.1/30" in dot       # router IP annotation on the node


def test_dot_marks_down_links():
    topo = SCENARIOS["pbq-ccna-ospf-area"].build()
    topo.devices["R2"].get_if("Gi0/0", create=False).shutdown = True
    dot = topology_dot(topo)
    assert "dashed" in dot or "#e06c6c" in dot
