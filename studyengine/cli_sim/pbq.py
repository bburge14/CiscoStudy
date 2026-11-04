"""Performance-Based Question scenarios: broken topologies the learner repairs
in the CLI simulator. Validation inspects *actual* resulting state (does the
EtherChannel bundle? is the OSPF neighbor FULL? is this switch the STP root?),
so there is no way to "pass" except by configuring the fix correctly.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from .device import Device, Topology, etherchannel_bundles, interface_ospf
from .parser import Console


@dataclass
class PBQCheck:
    description: str
    passed: bool


@dataclass
class PBQScenario:
    id: str
    exam: str
    domain: str
    subtopic: str
    title: str
    ticket: str
    device: str
    hints: list[str]
    success: str
    build_fn: Callable[[], Topology]
    validate_fn: Callable[[Topology], list[PBQCheck]]
    start_mode: str = "USER"

    def build(self) -> Topology:
        return self.build_fn()

    def console(self, topo: Topology) -> Console:
        return Console(topo, self.device, self.start_mode)

    def validate(self, topo: Topology) -> list[PBQCheck]:
        return self.validate_fn(topo)

    def passed(self, topo: Topology) -> bool:
        checks = self.validate(topo)
        return bool(checks) and all(c.passed for c in checks)


def _seed(topo: Topology, name: str, lines: list[str]) -> None:
    Console(topo, name).apply_config(lines)


# --- 1. Native VLAN mismatch -----------------------------------------------
def _build_native_vlan() -> Topology:
    t = Topology()
    t.add_device(Device("SW1", kind="switch", base_mac="0012.3f00.1101"))
    t.add_device(Device("SW2", kind="switch", base_mac="0012.3f00.1102"))
    t.link("SW1", "Gi0/1", "SW2", "Gi0/1")
    _seed(t, "SW1", [
        "vlan 99", "name NATIVE", "exit",
        "interface Gi0/1", "switchport trunk encapsulation dot1q",
        "switchport mode trunk", "switchport trunk native vlan 1", "exit",
    ])
    _seed(t, "SW2", [
        "vlan 99", "name NATIVE", "exit",
        "interface Gi0/1", "switchport trunk encapsulation dot1q",
        "switchport mode trunk", "switchport trunk native vlan 99", "exit",
    ])
    return t


def _validate_native_vlan(t: Topology) -> list[PBQCheck]:
    sw1 = t.devices["SW1"].get_if("Gi0/1", create=False)
    sw2 = t.devices["SW2"].get_if("Gi0/1", create=False)
    return [
        PBQCheck("SW1 Gi0/1 is operating as an 802.1Q trunk", sw1.sw_mode == "trunk"),
        PBQCheck("Native VLAN matches on both ends of the trunk (no mismatch)",
                 sw1.trunk_native == sw2.trunk_native),
        PBQCheck("Native VLAN standardized to 99", sw1.trunk_native == 99),
    ]


# --- 2. EtherChannel will not bundle ---------------------------------------
def _build_etherchannel() -> Topology:
    t = Topology()
    t.add_device(Device("ACC1", kind="switch", base_mac="0012.3f00.2201"))
    t.add_device(Device("DSW1", kind="switch", base_mac="0012.3f00.2202"))
    t.link("ACC1", "Gi0/1", "DSW1", "Gi0/1")
    t.link("ACC1", "Gi0/2", "DSW1", "Gi0/2")
    # DSW1 correctly uses LACP active; ACC1 was mis-set to static "on" -> no bundle
    _seed(t, "DSW1", [
        "interface range Gi0/1 - 2", "switchport mode trunk",
        "channel-group 1 mode active", "exit",
    ])
    _seed(t, "ACC1", [
        "interface range Gi0/1 - 2", "switchport mode trunk",
        "channel-group 1 mode on", "exit",
    ])
    return t


def _validate_etherchannel(t: Topology) -> list[PBQCheck]:
    acc = t.devices["ACC1"]
    dsw = t.devices["DSW1"]
    checks = []
    all_bundle = True
    for ifn in ("Gi0/1", "Gi0/2"):
        a = acc.get_if(ifn, create=False)
        d = dsw.get_if(ifn, create=False)
        bundles, proto, _ = etherchannel_bundles(a.channel_mode, d.channel_mode)
        all_bundle = all_bundle and bundles
        checks.append(PBQCheck(f"ACC1 {ifn} negotiates a channel with DSW1 ({proto})", bundles))
    checks.append(PBQCheck(
        "Both members use a compatible LACP mode (not static 'on' vs 'active')",
        all(acc.get_if(i, create=False).channel_mode in ("active", "passive") for i in ("Gi0/1", "Gi0/2"))
        and all_bundle,
    ))
    return checks


# --- 3. OSPF neighbor down (area mismatch) ---------------------------------
def _build_ospf_area() -> Topology:
    t = Topology()
    t.add_device(Device("R1", kind="router", base_mac="0012.3f00.3301"))
    t.add_device(Device("R2", kind="router", base_mac="0012.3f00.3302"))
    t.link("R1", "Gi0/0", "R2", "Gi0/0")
    _seed(t, "R1", [
        "interface Gi0/0", "ip address 10.1.12.1 255.255.255.252", "no shutdown", "exit",
        "interface Loopback0", "ip address 1.1.1.1 255.255.255.255", "exit",
        "router ospf 1", "router-id 1.1.1.1",
        "network 10.1.12.0 0.0.0.3 area 0", "exit",
    ])
    _seed(t, "R2", [
        "interface Gi0/0", "ip address 10.1.12.2 255.255.255.252", "no shutdown", "exit",
        "interface Loopback0", "ip address 2.2.2.2 255.255.255.255", "exit",
        # BUG: interface placed in area 1, so no adjacency with R1 (area 0)
        "router ospf 1", "router-id 2.2.2.2",
        "network 10.1.12.0 0.0.0.3 area 1", "exit",
    ])
    return t


def _validate_ospf_area(t: Topology) -> list[PBQCheck]:
    r2 = t.devices["R2"].get_if("Gi0/0", create=False)
    adj = t.ospf_adjacency("R2", "Gi0/0")
    return [
        PBQCheck("R2 Gi0/0 is administratively up", not r2.shutdown),
        PBQCheck("R2 and R1 agree on area 0 for the 10.1.12.0/30 link", adj is not None),
        PBQCheck("OSPF adjacency to R1 reaches FULL state", bool(adj and adj.up)),
    ]


# --- 4. STP root bridge placement ------------------------------------------
def _build_stp_root() -> Topology:
    t = Topology()
    # DSW1 is meant to be root but SW_ACCESS currently wins by lower MAC.
    t.add_device(Device("DSW1", kind="l3switch", base_mac="0012.3f00.4402"))
    t.add_device(Device("ACC1", kind="switch", base_mac="0012.3f00.4401"))
    t.add_device(Device("ACC2", kind="switch", base_mac="0012.3f00.4403"))
    t.link("DSW1", "Gi0/1", "ACC1", "Gi0/1")
    t.link("DSW1", "Gi0/2", "ACC2", "Gi0/1")
    for name in ("DSW1", "ACC1", "ACC2"):
        _seed(t, name, ["vlan 10", "name USERS", "exit"])
    return t


def _validate_stp_root(t: Topology) -> list[PBQCheck]:
    dsw = t.devices["DSW1"]
    root = t.stp_root(10)
    return [
        PBQCheck("VLAN 10 is defined on DSW1", 10 in dsw.vlans),
        PBQCheck("DSW1 is elected root bridge for VLAN 10 (lowest bridge ID)", root is dsw),
        PBQCheck("DSW1 bridge priority for VLAN 10 is below the 32768 default",
                 dsw.stp_base_priority(10) < 32768),
    ]


# --- 5. OSPF stuck in EXSTART (MTU mismatch) -------------------------------
def _build_ospf_mtu() -> Topology:
    t = Topology()
    t.add_device(Device("CORE1", kind="router", base_mac="0012.3f00.5501"))
    t.add_device(Device("CORE2", kind="router", base_mac="0012.3f00.5502"))
    t.link("CORE1", "Gi0/0", "CORE2", "Gi0/0")
    _seed(t, "CORE1", [
        "interface Gi0/0", "ip address 10.0.0.1 255.255.255.0", "no shutdown", "exit",
        "router ospf 10", "router-id 10.10.10.1",
        "network 10.0.0.0 0.0.0.255 area 0", "exit",
    ])
    _seed(t, "CORE2", [
        # BUG: ip mtu 1400 -> DBD exchange fails, neighbor stuck EXSTART/EXCHANGE
        "interface Gi0/0", "ip address 10.0.0.2 255.255.255.0", "mtu 1400", "no shutdown", "exit",
        "router ospf 10", "router-id 10.10.10.2",
        "network 10.0.0.0 0.0.0.255 area 0", "exit",
    ])
    return t


def _validate_ospf_mtu(t: Topology) -> list[PBQCheck]:
    c1 = t.devices["CORE1"].get_if("Gi0/0", create=False)
    c2 = t.devices["CORE2"].get_if("Gi0/0", create=False)
    adj = t.ospf_adjacency("CORE2", "Gi0/0")
    return [
        PBQCheck("IP MTU matches on both ends of the 10.0.0.0/24 link", c1.mtu == c2.mtu),
        PBQCheck("OSPF adjacency progresses past EXSTART to FULL", bool(adj and adj.up)),
    ]


# --- 6. Access port in wrong VLAN ------------------------------------------
def _build_access_vlan() -> Topology:
    t = Topology()
    t.add_device(Device("SW1", kind="switch", base_mac="0012.3f00.6601"))
    _seed(t, "SW1", [
        "interface Gi0/5", "switchport mode access", "exit",  # left in default VLAN 1
    ])
    return t


def _validate_access_vlan(t: Topology) -> list[PBQCheck]:
    sw1 = t.devices["SW1"]
    gi5 = sw1.get_if("Gi0/5", create=False)
    return [
        PBQCheck("VLAN 20 is created in the VLAN database", 20 in sw1.vlans),
        PBQCheck("Gi0/5 is configured as an access port", gi5.sw_mode == "access"),
        PBQCheck("Gi0/5 is assigned to access VLAN 20", gi5.access_vlan == 20),
    ]


def _vlan_allowed_on_trunk(iface, vid: int) -> bool:
    a = iface.trunk_allowed
    if a in ("all", ""):
        return True
    if a == "none":
        return False
    return str(vid) in set(a.split(","))


# --- 7. Trunk allowed-VLAN pruning -----------------------------------------
def _build_trunk_allowed() -> Topology:
    t = Topology()
    t.add_device(Device("SW1", kind="switch", base_mac="0012.3f00.7701"))
    t.add_device(Device("SW2", kind="switch", base_mac="0012.3f00.7702"))
    t.link("SW1", "Gi0/1", "SW2", "Gi0/1")
    for name in ("SW1", "SW2"):
        _seed(t, name, ["vlan 10", "name DATA", "exit", "vlan 20", "name VOICE", "exit",
                        "vlan 30", "name GUEST", "exit"])
    # BUG: SW1's trunk allows only 10,20 -> VLAN 30 is pruned and cannot cross.
    _seed(t, "SW1", ["interface Gi0/1", "switchport trunk encapsulation dot1q",
                     "switchport mode trunk", "switchport trunk allowed vlan 10,20", "exit"])
    _seed(t, "SW2", ["interface Gi0/1", "switchport trunk encapsulation dot1q",
                     "switchport mode trunk", "exit"])
    return t


def _validate_trunk_allowed(t: Topology) -> list[PBQCheck]:
    sw1 = t.devices["SW1"].get_if("Gi0/1", create=False)
    return [
        PBQCheck("SW1 Gi0/1 is an 802.1Q trunk", sw1.sw_mode == "trunk"),
        PBQCheck("VLAN 30 exists in SW1's VLAN database", 30 in t.devices["SW1"].vlans),
        PBQCheck("VLAN 30 is permitted across the SW1 trunk", _vlan_allowed_on_trunk(sw1, 30)),
        PBQCheck("VLANs 10 and 20 are still permitted (not clobbered)",
                 _vlan_allowed_on_trunk(sw1, 10) and _vlan_allowed_on_trunk(sw1, 20)),
    ]


# --- 8. OSPF neighbor blocked by passive-interface -------------------------
def _build_ospf_passive() -> Topology:
    t = Topology()
    t.add_device(Device("R3", kind="router", base_mac="0012.3f00.8803"))
    t.add_device(Device("R4", kind="router", base_mac="0012.3f00.8804"))
    t.link("R3", "Gi0/0", "R4", "Gi0/0")
    _seed(t, "R3", [
        "interface Gi0/0", "ip address 10.3.4.1 255.255.255.252", "no shutdown", "exit",
        "interface Loopback0", "ip address 3.3.3.3 255.255.255.255", "exit",
        # BUG: the transit link is passive, so R3 sends no hellos on it.
        "router ospf 1", "router-id 3.3.3.3",
        "network 10.3.4.0 0.0.0.3 area 0", "passive-interface Gi0/0", "exit",
    ])
    _seed(t, "R4", [
        "interface Gi0/0", "ip address 10.3.4.2 255.255.255.252", "no shutdown", "exit",
        "interface Loopback0", "ip address 4.4.4.4 255.255.255.255", "exit",
        "router ospf 1", "router-id 4.4.4.4", "network 10.3.4.0 0.0.0.3 area 0", "exit",
    ])
    return t


def _validate_ospf_passive(t: Topology) -> list[PBQCheck]:
    r3 = t.devices["R3"]
    gi0 = r3.get_if("Gi0/0", create=False)
    oi = interface_ospf(r3, gi0)
    adj = t.ospf_adjacency("R3", "Gi0/0")
    return [
        PBQCheck("R3 Gi0/0 runs OSPF and is NOT passive (sends hellos)",
                 oi is not None and not oi[2]),
        PBQCheck("OSPF adjacency with R4 reaches FULL", bool(adj and adj.up)),
    ]


# --- 9. OSPF interface missed by a too-specific wildcard -------------------
def _build_ospf_wildcard() -> Topology:
    t = Topology()
    t.add_device(Device("R6", kind="router", base_mac="0012.3f00.9906"))
    t.add_device(Device("R7", kind="router", base_mac="0012.3f00.9907"))
    t.link("R6", "Gi0/0", "R7", "Gi0/0")
    _seed(t, "R6", [
        "interface Gi0/0", "ip address 10.6.6.1 255.255.255.0", "no shutdown", "exit",
        # BUG: wildcard 0.0.0.0 matches only 10.6.6.0, never the interface IP 10.6.6.1,
        # so Gi0/0 is never activated in OSPF.
        "router ospf 1", "router-id 6.6.6.6",
        "network 10.6.6.0 0.0.0.0 area 0", "exit",
    ])
    _seed(t, "R7", [
        "interface Gi0/0", "ip address 10.6.6.2 255.255.255.0", "no shutdown", "exit",
        "router ospf 1", "router-id 7.7.7.7", "network 10.6.6.0 0.0.0.255 area 0", "exit",
    ])
    return t


def _validate_ospf_wildcard(t: Topology) -> list[PBQCheck]:
    r6 = t.devices["R6"]
    gi0 = r6.get_if("Gi0/0", create=False)
    adj = t.ospf_adjacency("R6", "Gi0/0")
    return [
        PBQCheck("R6 Gi0/0 is activated in OSPF (network/wildcard now matches 10.6.6.1)",
                 interface_ospf(r6, gi0) is not None),
        PBQCheck("OSPF adjacency with R7 reaches FULL", bool(adj and adj.up)),
    ]


# --- 10. EtherChannel LACP vs PAgP protocol mismatch -----------------------
def _build_ec_protocol() -> Topology:
    t = Topology()
    t.add_device(Device("DSWA", kind="l3switch", base_mac="0012.3f00.aa0a"))
    t.add_device(Device("DSWB", kind="l3switch", base_mac="0012.3f00.aa0b"))
    t.link("DSWA", "Gi0/1", "DSWB", "Gi0/1")
    t.link("DSWA", "Gi0/2", "DSWB", "Gi0/2")
    # DSWA uses LACP; DSWB was wrongly set to PAgP -> protocols don't interoperate.
    _seed(t, "DSWA", ["interface range Gi0/1 - 2", "switchport mode trunk",
                      "channel-group 1 mode active", "exit"])
    _seed(t, "DSWB", ["interface range Gi0/1 - 2", "switchport mode trunk",
                      "channel-group 1 mode desirable", "exit"])
    return t


def _validate_ec_protocol(t: Topology) -> list[PBQCheck]:
    dswa, dswb = t.devices["DSWA"], t.devices["DSWB"]
    checks = []
    ok_all = True
    for ifn in ("Gi0/1", "Gi0/2"):
        a = dswa.get_if(ifn, create=False)
        b = dswb.get_if(ifn, create=False)
        bundles, proto, _ = etherchannel_bundles(b.channel_mode, a.channel_mode)
        ok_all = ok_all and bundles
        checks.append(PBQCheck(f"DSWB {ifn} and DSWA negotiate one protocol ({proto})", bundles))
    checks.append(PBQCheck(
        "DSWB members use LACP to match DSWA (not PAgP)",
        all(dswb.get_if(i, create=False).channel_mode in ("active", "passive")
            for i in ("Gi0/1", "Gi0/2")) and ok_all))
    return checks


# --- 11. L3 switch uplink left as an L2 switchport -------------------------
def _build_l3_routed_port() -> Topology:
    t = Topology()
    t.add_device(Device("DSW1", kind="l3switch", base_mac="0012.3f00.bb01"))
    t.add_device(Device("R1", kind="router", base_mac="0012.3f00.bb02"))
    t.link("DSW1", "Gi0/1", "R1", "Gi0/0")
    # R1 side is a correctly-configured routed OSPF interface.
    _seed(t, "R1", [
        "interface Gi0/0", "ip address 10.0.1.2 255.255.255.252", "no shutdown", "exit",
        "router ospf 1", "router-id 1.1.1.1", "network 10.0.1.0 0.0.0.3 area 0", "exit",
    ])
    # BUG: DSW1's uplink is still a default L2 switchport with no IP and no OSPF.
    return t


def _validate_l3_routed_port(t: Topology) -> list[PBQCheck]:
    dsw1 = t.devices["DSW1"]
    gi1 = dsw1.get_if("Gi0/1", create=False)
    adj = t.ospf_adjacency("DSW1", "Gi0/1")
    same_subnet = bool(gi1 and gi1.ip and gi1.mask
                       and gi1.ip.startswith("10.0.1.") and gi1.mask == "255.255.255.252")
    return [
        PBQCheck("DSW1 Gi0/1 is a routed port (no switchport)", gi1 is not None and not gi1.is_switchport),
        PBQCheck("DSW1 Gi0/1 has an IP in the 10.0.1.0/30 uplink subnet", same_subnet),
        PBQCheck("OSPF adjacency with R1 reaches FULL", bool(adj and adj.up)),
    ]


SCENARIOS: dict[str, PBQScenario] = {}


def _register(s: PBQScenario) -> None:
    SCENARIOS[s.id] = s


_register(PBQScenario(
    id="pbq-ccna-native-vlan", exam="ccna", domain="network_access", subtopic="vlans_trunking",
    title="Trunk native VLAN mismatch", device="SW1", start_mode="USER",
    ticket=(
        "**Ticket #4471 — Console: SW1**\n\n"
        "Users report intermittent connectivity between the two access-layer "
        "switches. The console on SW1 is logging:\n\n"
        "```\n%CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on\n"
        "GigabitEthernet0/1 (1), with SW2 GigabitEthernet0/1 (99).\n```\n\n"
        "SW2's trunk already uses native VLAN **99** by design. Reconfigure **SW1** "
        "so the trunk native VLAN matches SW2 and the mismatch clears."
    ),
    hints=[
        "`show interfaces trunk` shows the Native vlan column for each trunk port.",
        "On the trunk interface: `switchport trunk native vlan 99`.",
    ],
    success="Native VLANs now match (99/99) — the CDP mismatch log clears and both VLANs tag consistently.",
    build_fn=_build_native_vlan, validate_fn=_validate_native_vlan,
))

_register(PBQScenario(
    id="pbq-ccna-etherchannel", exam="ccna", domain="network_access", subtopic="etherchannel",
    title="EtherChannel will not bundle", device="ACC1", start_mode="USER",
    ticket=(
        "**Ticket #4490 — Console: ACC1**\n\n"
        "The Gi0/1–Gi0/2 port-channel to DSW1 is not forming. `show etherchannel "
        "summary` on ACC1 reports the members as stand-alone `(I)` and:\n\n"
        "```\nNumber of channel-groups in use: 1\nNumber of aggregators:           0\n```\n\n"
        "DSW1 is correctly configured for **LACP** (`channel-group 1 mode active`). "
        "ACC1 was mistakenly set to static `on`. Reconfigure **ACC1's** members to "
        "the correct LACP mode so the bundle comes up."
    ),
    hints=[
        "Static `on` does not negotiate; it is incompatible with LACP `active`.",
        "Set both members: `interface range gi0/1 - 2` then `channel-group 1 mode active`.",
    ],
    success="Both members negotiate LACP and bundle into Po1 — members show `(P)` and Po1 is `(SU)`.",
    build_fn=_build_etherchannel, validate_fn=_validate_etherchannel,
))

_register(PBQScenario(
    id="pbq-ccna-ospf-area", exam="ccna", domain="ip_connectivity", subtopic="ospf",
    title="OSPF neighbor will not come up", device="R2", start_mode="USER",
    ticket=(
        "**Ticket #4512 — Console: R2**\n\n"
        "R1 and R2 are directly connected on 10.1.12.0/30 but never form an OSPF "
        "adjacency — `show ip ospf neighbor` on R2 is empty. R1's interface is in "
        "**area 0**. Inspect R2's OSPF configuration and correct it so the neighbor "
        "reaches **FULL**.\n\n"
        "```\nR2# show ip ospf neighbor\nR2#\n```"
    ),
    hints=[
        "Both ends of a link must be in the SAME area to become neighbors.",
        "Check `show running-config | section ospf` — the network statement area is wrong.",
        "Re-add the network in the right area: `network 10.1.12.0 0.0.0.3 area 0` (remove the area 1 line with `no network ...`).",
    ],
    success="R2's link is in area 0 — the adjacency with R1 reaches FULL and routes exchange.",
    build_fn=_build_ospf_area, validate_fn=_validate_ospf_area,
))

_register(PBQScenario(
    id="pbq-ccna-stp-root", exam="ccna", domain="network_access", subtopic="stp_root_election",
    title="Force the distribution switch to be STP root", device="DSW1", start_mode="USER",
    ticket=(
        "**Ticket #4533 — Console: DSW1**\n\n"
        "VLAN 10's spanning-tree root is currently an access switch because every "
        "switch uses the default priority 32768 and the access switch has the lowest "
        "MAC. The design requires **DSW1** to be the root bridge for VLAN 10 so traffic "
        "follows the intended path. Make DSW1 the root for VLAN 10."
    ),
    hints=[
        "Root = lowest bridge ID (priority + VLAN, then MAC). Lower the priority on DSW1.",
        "`spanning-tree vlan 10 root primary` or `spanning-tree vlan 10 priority 24576`.",
    ],
    success="DSW1 now owns the lowest bridge ID for VLAN 10 and is elected root bridge.",
    build_fn=_build_stp_root, validate_fn=_validate_stp_root,
))

_register(PBQScenario(
    id="pbq-encor-ospf-mtu", exam="encor", domain="infrastructure", subtopic="ospf_advanced",
    title="OSPF stuck in EXSTART (MTU mismatch)", device="CORE2", start_mode="USER",
    ticket=(
        "**Ticket #7120 — Console: CORE2**\n\n"
        "CORE1 and CORE2 are stuck and never reach FULL. `show ip ospf neighbor` on "
        "CORE2 shows:\n\n"
        "```\nNeighbor ID     Pri   State        Dead Time   Address      Interface\n"
        "10.10.10.1        1   EXSTART/DR   00:00:35    10.0.0.1     GigabitEthernet0/0\n```\n\n"
        "CORE1's interface uses the default MTU 1500. Someone set a non-default MTU on "
        "**CORE2's** Gi0/0. Correct CORE2 so the DBD exchange completes and the "
        "neighbor reaches FULL."
    ),
    hints=[
        "EXSTART/EXCHANGE that never advances is the classic MTU-mismatch symptom.",
        "`show running-config interface gi0/0` reveals the mtu line; restore it to 1500.",
        "On the interface: `mtu 1500` (or `no mtu`).",
    ],
    success="MTU matches (1500/1500) on both ends — the DBD exchange completes and the adjacency reaches FULL.",
    build_fn=_build_ospf_mtu, validate_fn=_validate_ospf_mtu,
))

_register(PBQScenario(
    id="pbq-ccna-access-vlan", exam="ccna", domain="network_access", subtopic="vlans_trunking",
    title="Place a host port in the correct VLAN", device="SW1", start_mode="USER",
    ticket=(
        "**Ticket #4402 — Console: SW1**\n\n"
        "A new workstation on **Gi0/5** cannot reach the VLAN 20 (USERS) subnet. The "
        "port is still in default VLAN 1, and VLAN 20 does not yet exist on this switch. "
        "Create VLAN 20 and move the access port into it."
    ),
    hints=[
        "Create the VLAN first: `vlan 20` / `name USERS`.",
        "Then on `interface gi0/5`: `switchport mode access` and `switchport access vlan 20`.",
    ],
    success="VLAN 20 exists and Gi0/5 is an access port in VLAN 20 — the host now reaches the USERS subnet.",
    build_fn=_build_access_vlan, validate_fn=_validate_access_vlan,
))


_register(PBQScenario(
    id="pbq-ccna-trunk-allowed", exam="ccna", domain="network_access", subtopic="vlans_trunking",
    title="VLAN pruned from the trunk allowed list", device="SW1", start_mode="USER",
    ticket=(
        "**Ticket #4478 — Console: SW1**\n\n"
        "VLAN 10 and 20 work across the SW1–SW2 trunk, but the new **VLAN 30 "
        "(GUEST)** cannot reach SW2. VLAN 30 exists on both switches. "
        "`show interfaces trunk` on SW1 shows:\n\n"
        "```\nPort        Vlans allowed on trunk\nGi0/1       10,20\n```\n\n"
        "Permit VLAN 30 on the **SW1** trunk **without** removing VLANs 10 or 20."
    ),
    hints=[
        "Use the `add` keyword or you will REPLACE the whole allowed list.",
        "`interface gi0/1` then `switchport trunk allowed vlan add 30`.",
    ],
    success="VLAN 30 is now permitted (10,20,30) and reaches SW2 — and VLANs 10/20 were preserved.",
    build_fn=_build_trunk_allowed, validate_fn=_validate_trunk_allowed,
))

_register(PBQScenario(
    id="pbq-ccna-ospf-passive", exam="ccna", domain="ip_connectivity", subtopic="ospf",
    title="OSPF neighbor blocked by passive-interface", device="R3", start_mode="USER",
    ticket=(
        "**Ticket #4520 — Console: R3**\n\n"
        "R3 and R4 share 10.3.4.0/30 and are both in area 0 with correct IPs, yet "
        "`show ip ospf neighbor` on R3 is empty. The link is up and pings. "
        "`show ip protocols` lists Gi0/0 under **Passive Interface(s)**. Correct R3 "
        "so the adjacency forms."
    ),
    hints=[
        "A passive interface still advertises its subnet but sends NO hellos, so no neighbor forms.",
        "Under `router ospf 1`: `no passive-interface GigabitEthernet0/0`.",
    ],
    success="Gi0/0 sends hellos again — the adjacency with R4 reaches FULL.",
    build_fn=_build_ospf_passive, validate_fn=_validate_ospf_passive,
))

_register(PBQScenario(
    id="pbq-ccna-ospf-wildcard", exam="ccna", domain="ip_connectivity", subtopic="wildcard_masks",
    title="OSPF network statement with the wrong wildcard", device="R6", start_mode="USER",
    ticket=(
        "**Ticket #4527 — Console: R6**\n\n"
        "R6 should peer with R7 over 10.6.6.0/24 (R6 = 10.6.6.1, R7 = 10.6.6.2) in "
        "area 0, but no adjacency forms and R6's Gi0/0 never appears in "
        "`show ip ospf interface brief`. R6's OSPF config contains:\n\n"
        "```\nrouter ospf 1\n network 10.6.6.0 0.0.0.0 area 0\n```\n\n"
        "Fix R6's network statement so Gi0/0 (10.6.6.1/24) is activated in OSPF."
    ),
    hints=[
        "Wildcard 0.0.0.0 matches ONLY 10.6.6.0 — not the interface IP 10.6.6.1.",
        "A /24 needs wildcard 0.0.0.255: `network 10.6.6.0 0.0.0.255 area 0` "
        "(remove the wrong line with `no network 10.6.6.0 0.0.0.0 area 0`).",
    ],
    success="The /24 wildcard now matches Gi0/0 — it joins OSPF and the R7 adjacency reaches FULL.",
    build_fn=_build_ospf_wildcard, validate_fn=_validate_ospf_wildcard,
))

_register(PBQScenario(
    id="pbq-encor-ec-protocol", exam="encor", domain="infrastructure", subtopic="etherchannel_advanced",
    title="EtherChannel protocol mismatch (LACP vs PAgP)", device="DSWB", start_mode="USER",
    ticket=(
        "**Ticket #7145 — Console: DSWB**\n\n"
        "The Gi0/1–Gi0/2 port-channel between DSWA and DSWB will not bundle. "
        "`show etherchannel summary` shows the members as independent `(I)`. DSWA is "
        "configured for **LACP** (`channel-group 1 mode active`), but DSWB was set "
        "to **PAgP** (`mode desirable`) — the two negotiation protocols cannot "
        "interoperate. Standardize **DSWB** on LACP so the channel forms."
    ),
    hints=[
        "LACP (active/passive) and PAgP (desirable/auto) never negotiate with each other.",
        "`interface range gi0/1 - 2` then `channel-group 1 mode active`.",
    ],
    success="Both members now speak LACP and bundle into Po1 — members show `(P)`.",
    build_fn=_build_ec_protocol, validate_fn=_validate_ec_protocol,
))

_register(PBQScenario(
    id="pbq-encor-l3-routed-port", exam="encor", domain="infrastructure", subtopic="ospf_advanced",
    title="L3 switch uplink still an L2 switchport", device="DSW1", start_mode="USER",
    ticket=(
        "**Ticket #7160 — Console: DSW1**\n\n"
        "The uplink from distribution switch **DSW1** (Gi0/1) to router **R1** "
        "(Gi0/0, 10.0.1.2/30, OSPF area 0) has no Layer 3 adjacency. DSW1's Gi0/1 is "
        "still a default **L2 switchport** with no IP address. Convert Gi0/1 to a "
        "routed port, address it as **10.0.1.1/30**, and bring it up in OSPF area 0."
    ),
    hints=[
        "Enable routing (`ip routing`), then make the port routed: `interface gi0/1` / `no switchport`.",
        "`ip address 10.0.1.1 255.255.255.252`, then under `router ospf 1` add "
        "`network 10.0.1.0 0.0.0.3 area 0`.",
    ],
    success="Gi0/1 is a routed port in 10.0.1.0/30 and the OSPF adjacency with R1 reaches FULL.",
    build_fn=_build_l3_routed_port, validate_fn=_validate_l3_routed_port,
))


def get_scenario(scenario_id: str) -> PBQScenario:
    return SCENARIOS[scenario_id]


def scenarios_for(exam: str) -> list[PBQScenario]:
    return [s for s in SCENARIOS.values() if s.exam == exam]
