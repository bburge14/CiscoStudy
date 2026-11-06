from studyengine.cli_sim import (
    Console,
    Device,
    Topology,
    etherchannel_bundles,
    normalize_ifname,
    resolve_ifname,
)


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


def test_resolve_ifname_accepts_aliases_rejects_bogus():
    assert resolve_ifname("gi0/1") == "GigabitEthernet0/1"
    assert resolve_ifname("g0/1") == "GigabitEthernet0/1"
    assert resolve_ifname("ge0/1") == "GigabitEthernet0/1"   # common 'ge' alias
    assert resolve_ifname("fe0/1") == "FastEthernet0/1"
    assert resolve_ifname("po1") == "Port-channel1"
    assert resolve_ifname("GigabitEthernet0/1.10") == "GigabitEthernet0/1.10"
    # a genuinely unknown type, and a type without a port number, are rejected
    assert resolve_ifname("zz0/1") is None
    assert resolve_ifname("bogus5") is None
    assert resolve_ifname("gi") is None


def test_interface_bad_type_is_rejected_not_invented():
    con = Console(_switch_topo(), "SW1")
    con.execute("enable")
    con.execute("configure terminal")
    out = con.execute("interface zz0/1")          # 'zz' isn't a valid type
    assert "% Invalid input detected at '^' marker." in out
    assert con.prompt == "SW1(config)#"           # did NOT enter config-if
    assert "zz0/1" not in con.dev.interfaces       # and no phantom interface
    # 'ge' resolves to the real GigabitEthernet port (no phantom, no error)
    assert con.execute("interface ge 0/1") == ""
    assert con.prompt == "SW1(config-if)#"
    assert "GigabitEthernet0/1" in con.dev.interfaces and "ge0/1" not in con.dev.interfaces


def test_show_vlan_id_filters_and_bare_number_is_invalid():
    con = Console(_switch_topo(), "SW1")
    con.apply_config(["vlan 99", "name NATIVE", "exit",
                      "vlan 20", "name USERS", "exit"])
    con.execute("enable")
    # bare "show vlan 1" is not valid IOS -> caret error (the reported bug)
    bad = con.execute("show vlan 1")
    assert "% Invalid input detected at '^' marker." in bad
    # "show vlan id N" shows only that VLAN
    one = con.execute("show vlan id 99")
    assert "NATIVE" in one and "USERS" not in one and "default" not in one
    # a non-existent id reports the IOS not-found message
    assert "not found" in con.execute("show vlan id 5")
    # the full table still lists everything
    full = con.execute("show vlan")
    assert "NATIVE" in full and "USERS" in full and "default" in full


def test_show_interface_name_is_scoped_and_validates_type():
    con = Console(_switch_topo(), "SW1")
    con.apply_config(["interface gi0/1", "description UPLINK", "exit",
                      "interface gi0/2", "description SERVER"])
    con.execute("enable")
    # a specific interface shows only itself, in detail (not the whole brief table)
    detail = con.execute("show interfaces gi0/1")
    assert "GigabitEthernet0/1 is" in detail and "line protocol" in detail
    assert "GigabitEthernet0/2" not in detail
    # a bogus type is rejected rather than dumping every interface
    assert "% Invalid input" in con.execute("show interfaces zz0/1")


def test_show_interface_accepts_spaced_name_and_is_detailed():
    con = Console(_switch_topo(), "SW1")
    con.apply_config(["interface gi0/1", "description UPLINK"])
    con.execute("enable")
    # "GigabitEthernet 0/1" (space between type and number) is valid IOS
    out = con.execute("show interface GigabitEthernet 0/1")
    assert "GigabitEthernet0/1 is" in out and "line protocol" in out
    assert "MTU 1500 bytes" in out            # detailed, not the brief table
    # bare `show interfaces` is the DETAILED view on IOS, not the brief table
    allout = con.execute("show interfaces")
    assert "line protocol" in allout and "IP-Address" not in allout
    # the compact table is `show ip interface brief`
    brief = con.execute("show ip interface brief")
    assert "IP-Address" in brief and "line protocol" not in brief


def test_context_help_lists_valid_commands_per_mode():
    con = Console(_switch_topo(), "SW1")
    # user mode
    top = con.execute("?")
    assert "enable" in top and "show" in top and "configure" not in top
    # show subcommands
    assert "vlan" in con.execute("show ?") and "interfaces" in con.execute("show ?")
    # context-sensitive deeper help
    si = con.execute("show int ?")
    assert "status" in si and "trunk" in si and "<interface>" in si
    assert "<1-4094>" in con.execute("show vlan id ?")
    # partial-word completion
    assert "show" in con.execute("sh?")
    # priv vs config roots
    con.execute("enable")
    assert "configure" in con.execute("?")
    con.execute("configure terminal")
    cfg = con.execute("?")
    assert "interface" in cfg and "spanning-tree" in cfg and "vlan" in cfg
    # interface mode
    con.execute("interface gi0/1")
    sp = con.execute("switchport ?")
    assert "mode" in sp and "access" in sp and "trunk" in sp
    # a bogus token gets the IOS 'unrecognized' help response, not a traceback
    assert "Unrecognized" in con.execute("bogus?")


def test_help_keyword_and_help_does_not_break_execution():
    con = Console(_switch_topo(), "SW1")
    assert "question mark" in con.execute("help")
    # a real command still runs normally (the '?' hook doesn't swallow it)
    con.execute("enable")
    assert con.prompt == "SW1#"
    con.apply_config(["vlan 7", "name TEST"])
    assert con.dev.vlans.get(7) == "TEST"


def test_show_ip_protocols_lists_ospf_and_passive():
    con = Console(_router_topo(), "R1")
    con.apply_config([
        "interface gi0/0", "ip address 10.0.0.1 255.255.255.0", "no shutdown", "exit",
        "router ospf 1", "router-id 1.1.1.1",
        "network 10.0.0.0 0.0.0.255 area 0", "passive-interface gi0/0", "exit",
    ])
    out = con.execute("show ip protocols")
    assert 'Routing Protocol is "ospf 1"' in out and "Router ID 1.1.1.1" in out
    assert "Routing for Networks" in out and "10.0.0.0 0.0.0.255 area 0" in out
    assert "Passive Interface(s)" in out and "GigabitEthernet0/0" in out


def test_output_pipe_filters():
    con = Console(_switch_topo(), "SW1")
    con.apply_config(["hostname SW1", "vlan 10", "name DATA", "exit",
                      "interface gi0/1", "switchport mode trunk"])
    con.execute("enable")
    inc = con.execute("show run | include hostname")
    assert "hostname SW1" in inc and "interface" not in inc
    sec = con.execute("show run | section vlan 10")
    assert "vlan 10" in sec and "name DATA" in sec and "hostname" not in sec


def test_router_loopback_is_up_by_default():
    con = Console(_router_topo(), "R1")
    con.apply_config(["interface loopback0", "ip address 1.1.1.1 255.255.255.255"])
    lo = con.dev.get_if("Loopback0", create=False)
    assert lo is not None and not lo.shutdown          # loopbacks default up
    con.apply_config(["interface gi0/3"])              # physical port defaults admin-down
    assert con.dev.get_if("GigabitEthernet0/3", create=False).shutdown


def test_etherchannel_summary_zero_aggregators_when_unbundled():
    from studyengine.cli_sim import SCENARIOS
    s = SCENARIOS["pbq-ccna-etherchannel"]
    topo = s.build(); con = s.console(topo); con.execute("enable")
    out = con.execute("show etherchannel summary")
    assert "Number of aggregators:           0" in out    # nothing bundled yet
    assert "(I)" in out and "(P)" not in out              # stand-alone, not bundled


def test_short_abbreviations_and_interface_jump():
    con = Console(_switch_topo(), "SW1")
    con.apply_config(["interface gi0/1", "switchport mode trunk", "exit"])
    con.execute("enable")
    # any unique prefix resolves, like real IOS
    for cmd in ("sh ip o n", "sh int st", "sh vlan br", "sh ip r"):
        assert "Invalid input" not in con.execute(cmd), cmd
    con.execute("conf t")
    con.execute("interface gi0/1")
    assert con.execute("sw mo acc") == ""                        # switchport mode access
    assert con.dev.get_if("Gi0/1", create=False).sw_mode == "access"
    # jump straight to another interface from config-if (no `exit` needed)
    assert con.execute("int gi0/2") == "" and con.prompt == "SW1(config-if)#"
    con.execute("shutdown")
    assert con.dev.get_if("Gi0/2", create=False).shutdown


def test_ping_reachable_same_subnet():
    r = Console(_router_topo(), "R1")
    r.apply_config(["interface gi0/0", "ip address 10.0.0.1 255.255.255.0", "no shutdown"])
    out = r.execute("ping 10.0.0.9")
    assert "Success rate is 100 percent" in out
