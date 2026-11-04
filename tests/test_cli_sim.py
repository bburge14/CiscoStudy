from studyengine.cli_sim import Console, Device, Topology, etherchannel_bundles, normalize_ifname


def _switch_topo():
    t = Topology()
    t.add_device(Device("SW1", kind="switch"))
    return t


def _router_topo():
    t = Topology()
    t.add_device(Device("R1", kind="router"))
    return t


def test_normalize_ifname():
    assert normalize_ifname("gi0/1") == "GigabitEthernet0/1"
    assert normalize_ifname("g0/1") == "GigabitEthernet0/1"
    assert normalize_ifname("Gig 0/1") == "GigabitEthernet0/1"
    assert normalize_ifname("fa0/24") == "FastEthernet0/24"
    assert normalize_ifname("te1/1/1") == "TenGigabitEthernet1/1/1"
    assert normalize_ifname("po1") == "Port-channel1"
    assert normalize_ifname("lo0") == "Loopback0"


def test_mode_transitions_and_prompt():
    con = Console(_switch_topo(), "SW1")
    assert con.prompt == "SW1>"
    con.execute("enable")
    assert con.prompt == "SW1#"
    con.execute("configure terminal")
    assert con.prompt == "SW1(config)#"
    con.execute("interface gi0/1")
    assert con.prompt == "SW1(config-if)#"
    con.execute("exit")
    assert con.prompt == "SW1(config)#"
    con.execute("end")
    assert con.prompt == "SW1#"


def test_invalid_command_gives_ios_error():
    con = Console(_switch_topo(), "SW1")
    con.execute("enable")
    out = con.execute("show ip bananas")
    assert "% Invalid input detected at '^' marker." in out
    assert "^" in out


def test_vlan_and_access_port():
    con = Console(_switch_topo(), "SW1")
    con.apply_config(["vlan 20", "name USERS", "exit",
                      "interface gi0/5", "switchport mode access",
                      "switchport access vlan 20"])
    dev = con.dev
    assert dev.vlans.get(20) == "USERS"
    gi5 = dev.get_if("Gi0/5", create=False)
    assert gi5.sw_mode == "access" and gi5.access_vlan == 20
    out = con.execute("show vlan brief")
    assert "USERS" in out and "Gi0/5" in out


def test_ip_address_rejected_on_switchport_but_ok_on_router():
    sw = Console(_switch_topo(), "SW1")
    # interactive flow keeps config-if context across calls (apply_config resets it)
    for line in ["enable", "configure terminal", "interface gi0/1"]:
        sw.execute(line)
    msg = sw.execute("ip address 10.0.0.1 255.255.255.0")
    assert "no switchport" in msg.lower()

    r = Console(_router_topo(), "R1")
    r.apply_config(["interface gi0/0", "ip address 10.0.0.1 255.255.255.0", "no shutdown"])
    gi0 = r.dev.get_if("Gi0/0", create=False)
    assert gi0.ip == "10.0.0.1" and gi0.mask == "255.255.255.0"
    assert not gi0.shutdown


def test_show_ip_interface_brief():
    r = Console(_router_topo(), "R1")
    r.apply_config(["interface gi0/0", "ip address 10.0.0.1 255.255.255.0", "no shutdown"])
    out = r.execute("show ip interface brief")
    assert "GigabitEthernet0/0" in out and "10.0.0.1" in out


def test_show_running_config_contains_key_lines():
    con = Console(_switch_topo(), "SW1")
    con.apply_config(["hostname ACCESS1", "vlan 10", "name DATA", "exit",
                      "interface gi0/1", "switchport mode trunk",
                      "switchport trunk native vlan 99"])
    out = con.execute("show running-config")
    assert "hostname ACCESS1" in out
    assert "switchport mode trunk" in out
    assert "switchport trunk native vlan 99" in out


def test_interface_range_applies_to_all():
    con = Console(_switch_topo(), "SW1")
    con.apply_config(["interface range gi0/1 - 3", "switchport mode trunk"])
    for n in (1, 2, 3):
        assert con.dev.get_if(f"Gi0/{n}", create=False).sw_mode == "trunk"


def test_etherchannel_matrix():
    assert etherchannel_bundles("active", "passive")[0] is True
    assert etherchannel_bundles("active", "active")[0] is True
    assert etherchannel_bundles("passive", "passive")[0] is False
    assert etherchannel_bundles("desirable", "auto")[0] is True
    assert etherchannel_bundles("auto", "auto")[0] is False
    assert etherchannel_bundles("on", "on")[0] is True
    assert etherchannel_bundles("on", "active")[0] is False


def test_stp_priority_validation():
    con = Console(_switch_topo(), "SW1")
    con.execute("enable")
    con.execute("configure terminal")
    bad = con.execute("spanning-tree vlan 10 priority 1000")  # not multiple of 4096
    assert "increments of 4096" in bad
    con.execute("spanning-tree vlan 10 priority 24576")
    assert con.dev.stp_base_priority(10) == 24576


def test_ping_reachable_same_subnet():
    r = Console(_router_topo(), "R1")
    r.apply_config(["interface gi0/0", "ip address 10.0.0.1 255.255.255.0", "no shutdown"])
    out = r.execute("ping 10.0.0.9")
    assert "Success rate is 100 percent" in out
