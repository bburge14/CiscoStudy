"""Device + topology state model with real STP / OSPF / EtherChannel logic.

This is deliberately a *behavioural* model, not just config storage: it elects
STP roots, forms (or fails to form) OSPF adjacencies, and decides whether an
EtherChannel bundles, so `show` output and PBQ validation reflect genuine Cisco
behaviour rather than canned strings.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from .netutils import ip_to_int, same_subnet, wildcard_match, wildcard_specificity

# --- interface name normalisation ------------------------------------------
_CANON = {
    "tengigabitethernet": "TenGigabitEthernet",
    "gigabitethernet": "GigabitEthernet",
    "fastethernet": "FastEthernet",
    "ethernet": "Ethernet",
    "port-channel": "Port-channel",
    "loopback": "Loopback",
    "vlan": "Vlan",
    "tunnel": "Tunnel",
    "serial": "Serial",
}
_ALIAS: dict[str, str] = {}
for _canon, _names in [
    ("tengigabitethernet", ["te", "ten", "teng", "tengig", "tengigabit", "tengigabitethernet"]),
    ("gigabitethernet", ["g", "gi", "gig", "giga", "gigabit", "gigabitethernet"]),
    ("fastethernet", ["f", "fa", "fas", "fast", "fastethernet"]),
    ("ethernet", ["et", "eth", "ethernet"]),
    ("port-channel", ["po", "port", "portchannel", "port-channel"]),
    ("loopback", ["lo", "loop", "loopback"]),
    ("vlan", ["vl", "vla", "vlan"]),
    ("tunnel", ["tu", "tun", "tunnel"]),
    ("serial", ["s", "se", "ser", "serial"]),
]:
    for _n in _names:
        _ALIAS[_n] = _canon


def normalize_ifname(raw: str) -> str:
    raw = str(raw).strip().replace(" ", "")
    m = re.match(r"^([a-zA-Z\-]+)([0-9/.]*)$", raw)
    if not m:
        return raw
    alpha, num = m.group(1).lower(), m.group(2)
    canon = _ALIAS.get(alpha)
    if canon is None:
        # try prefix of a canonical key
        for key in _CANON:
            if key.startswith(alpha):
                canon = key
                break
    if canon is None:
        return raw
    return f"{_CANON[canon]}{num}"


def resolve_ifname(raw: str) -> str | None:
    """Canonical interface name, or None when the type is not a real IOS
    interface type (so ``ge0/1`` or ``bogus5`` are rejected with an IOS error
    instead of silently inventing a phantom interface). A recognised type must
    also be followed by a port number (``Gi0/1``, ``Po1``, ``Gi0/1.10``)."""
    norm = normalize_ifname(raw)
    for canon in _CANON.values():
        if norm.startswith(canon):
            rest = norm[len(canon):]
            return norm if re.fullmatch(r"\d+(/\d+)*(\.\d+)?", rest) else None
    return None


def mac_to_int(mac: str) -> int:
    return int(mac.replace(".", "").replace(":", "").replace("-", ""), 16)


# --- models -----------------------------------------------------------------
@dataclass
class Interface:
    name: str
    description: str = ""
    shutdown: bool = False
    ip: str | None = None
    mask: str | None = None
    mtu: int = 1500
    is_switchport: bool = True
    sw_mode: str = "dynamic_auto"      # access | trunk | dynamic_auto | dynamic_desirable
    access_vlan: int = 1
    trunk_native: int = 1
    trunk_allowed: str = "all"          # "all" | "none" | comma list
    trunk_encap: str = "dot1q"
    channel_group: int | None = None
    channel_mode: str | None = None     # on | active | passive | desirable | auto
    ospf_pid: int | None = None
    ospf_area: str | None = None
    ospf_passive: bool = False
    speed: str = "auto"
    duplex: str = "auto"

    @property
    def oper_up(self) -> bool:
        return not self.shutdown

    def channel_protocol(self) -> str:
        if self.channel_mode in ("active", "passive"):
            return "LACP"
        if self.channel_mode in ("desirable", "auto"):
            return "PAgP"
        if self.channel_mode == "on":
            return "-"
        return "-"


@dataclass
class OspfProcess:
    pid: int
    router_id: str | None = None
    networks: list[tuple[str, str, str]] = field(default_factory=list)  # (net, wildcard, area)
    passive_default: bool = False
    passive_interfaces: set[str] = field(default_factory=set)
    no_passive_interfaces: set[str] = field(default_factory=set)


@dataclass
class Device:
    hostname: str
    kind: str = "switch"               # switch | router | l3switch
    base_mac: str = "0012.3f00.0001"
    stp_mode: str = "rapid-pvst"
    ip_routing: bool = False
    interfaces: dict[str, Interface] = field(default_factory=dict)
    vlans: dict[int, str] = field(default_factory=dict)
    ospf: dict[int, OspfProcess] = field(default_factory=dict)
    stp_priority: dict[int, int] = field(default_factory=dict)  # vlan -> base priority

    def __post_init__(self):
        if self.kind == "router":
            self.ip_routing = True

    def get_if(self, name: str, create: bool = True) -> Interface | None:
        norm = normalize_ifname(name)
        iface = self.interfaces.get(norm)
        if iface is None and create:
            iface = Interface(name=norm, is_switchport=(self.kind != "router"))
            if self.kind == "router":
                iface.shutdown = True  # routers default physical ports admin-down
            self.interfaces[norm] = iface
        return iface

    def ospf_process(self, pid: int, create: bool = True) -> OspfProcess | None:
        proc = self.ospf.get(pid)
        if proc is None and create:
            proc = OspfProcess(pid=pid)
            self.ospf[pid] = proc
        return proc

    def stp_base_priority(self, vlan: int) -> int:
        return self.stp_priority.get(vlan, 32768)


@dataclass
class AdjInfo:
    up: bool
    neighbor_rid: str
    local_rid: str
    area: str
    mtu_match: bool
    neighbor_dr: bool  # is the neighbor the DR (from local perspective)


# --- protocol behaviour -----------------------------------------------------
def interface_ospf(device: Device, iface: Interface) -> tuple[int, str, bool] | None:
    """Return (pid, area, passive) if OSPF is active on the interface, else None."""
    if iface.shutdown or not iface.ip:
        return None
    if iface.ospf_pid is not None and iface.ospf_area is not None:
        return (iface.ospf_pid, iface.ospf_area, iface.ospf_passive)
    best: tuple[int, str] | None = None
    best_spec = -1
    best_proc: OspfProcess | None = None
    for proc in device.ospf.values():
        for net, wild, area in proc.networks:
            if wildcard_match(iface.ip, net, wild):
                spec = wildcard_specificity(wild)
                if spec > best_spec:
                    best_spec = spec
                    best = (proc.pid, area)
                    best_proc = proc
    if best is None or best_proc is None:
        return None
    pid, area = best
    passive = (
        iface.ospf_passive
        or iface.name in best_proc.passive_interfaces
        or (best_proc.passive_default and iface.name not in best_proc.no_passive_interfaces)
    )
    return (pid, area, passive)


def ospf_router_id(device: Device, proc: OspfProcess) -> str:
    if proc.router_id:
        return proc.router_id
    loops = [i.ip for i in device.interfaces.values()
             if i.name.startswith("Loopback") and i.ip and not i.shutdown]
    if loops:
        return max(loops, key=ip_to_int)
    ups = [i.ip for i in device.interfaces.values() if i.ip and not i.shutdown]
    if ups:
        return max(ups, key=ip_to_int)
    return "0.0.0.0"


def etherchannel_bundles(mode_a: str | None, mode_b: str | None) -> tuple[bool, str, str]:
    """(bundles, protocol, reason). Encodes the classic mode-compatibility matrix."""
    lacp = {"active", "passive"}
    pagp = {"desirable", "auto"}
    a, b = mode_a, mode_b
    if a is None or b is None:
        return (False, "-", "A channel-group mode is missing on one side")
    if a == "on" and b == "on":
        return (True, "-", "Static on/on bundles with no negotiation")
    if a in lacp and b in lacp:
        if a == "passive" and b == "passive":
            return (False, "LACP", "passive/passive: neither side initiates LACP")
        return (True, "LACP", "")
    if a in pagp and b in pagp:
        if a == "auto" and b == "auto":
            return (False, "PAgP", "auto/auto: neither side initiates PAgP")
        return (True, "PAgP", "")
    return (False, "-", f"Incompatible modes ({a}/{b}) mix static/LACP/PAgP")


class Topology:
    def __init__(self):
        self.devices: dict[str, Device] = {}
        self.links: list[tuple[tuple[str, str], tuple[str, str]]] = []

    def add_device(self, device: Device) -> Device:
        self.devices[device.hostname] = device
        return device

    def link(self, dev_a: str, if_a: str, dev_b: str, if_b: str) -> None:
        self.links.append(((dev_a, normalize_ifname(if_a)), (dev_b, normalize_ifname(if_b))))

    def neighbor_of(self, dev: str, ifn: str) -> tuple[str, str] | None:
        ifn = normalize_ifname(ifn)
        for (da, ia), (db, ib) in self.links:
            if da == dev and ia == ifn:
                return (db, ib)
            if db == dev and ib == ifn:
                return (da, ia)
        return None

    # -- OSPF --
    def ospf_adjacency(self, dev_name: str, ifn: str) -> AdjInfo | None:
        dev_a = self.devices[dev_name]
        ia = dev_a.get_if(ifn, create=False)
        if ia is None:
            return None
        peer = self.neighbor_of(dev_name, ifn)
        if peer is None:
            return None
        dev_b = self.devices[peer[0]]
        ib = dev_b.get_if(peer[1], create=False)
        if ib is None or ia.shutdown or ib.shutdown or not ia.ip or not ib.ip:
            return None
        if not (ia.mask and ib.mask and ia.mask == ib.mask and same_subnet(ia.ip, ib.ip, ia.mask)):
            return None
        oa = interface_ospf(dev_a, ia)
        ob = interface_ospf(dev_b, ib)
        if not oa or not ob:
            return None
        _, area_a, pass_a = oa
        _, area_b, pass_b = ob
        if pass_a or pass_b or area_a != area_b:
            return None
        rid_a = ospf_router_id(dev_a, dev_a.ospf[oa[0]])
        rid_b = ospf_router_id(dev_b, dev_b.ospf[ob[0]])
        mtu_match = ia.mtu == ib.mtu
        neighbor_dr = ip_to_int(rid_b) > ip_to_int(rid_a)
        return AdjInfo(
            up=mtu_match, neighbor_rid=rid_b, local_rid=rid_a,
            area=area_a, mtu_match=mtu_match, neighbor_dr=neighbor_dr,
        )

    # -- STP --
    def stp_switches(self) -> list[Device]:
        return [d for d in self.devices.values() if d.kind in ("switch", "l3switch")]

    def stp_effective_priority(self, device: Device, vlan: int) -> int:
        return device.stp_base_priority(vlan) + vlan

    def stp_root(self, vlan: int) -> Device | None:
        cands = self.stp_switches()
        if not cands:
            return None
        return min(cands, key=lambda d: (self.stp_effective_priority(d, vlan), mac_to_int(d.base_mac)))

    def stp_lowest_base_priority(self, vlan: int) -> int:
        cands = self.stp_switches()
        if not cands:
            return 32768
        return min(d.stp_base_priority(vlan) for d in cands)
