from studyengine.cli_sim import SCENARIOS, topology_dot, topology_svg


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


def test_svg_valid_for_every_scenario():
    for sid, scen in SCENARIOS.items():
        topo = scen.build()
        svg = topology_svg(topo, scen.device)
        assert svg.startswith("<svg") and svg.rstrip().endswith("</svg>")
        for name in topo.devices:
            assert name in svg, f"{sid}: {name} missing from SVG"
        assert "#1BA0D7" in svg  # console device highlight ring


def test_svg_marks_down_links():
    topo = SCENARIOS["pbq-ccna-ospf-area"].build()
    topo.devices["R2"].get_if("Gi0/0", create=False).shutdown = True
    svg = topology_svg(topo)
    assert "stroke-dasharray" in svg or "#e06c6c" in svg
