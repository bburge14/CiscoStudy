"""A console that interprets a useful subset of Cisco IOS and renders realistic
`show` output and IOS-style error messages.

Scope is deliberately bounded to what the drills and PBQ scenarios exercise:
VLAN/trunk, STP priority, EtherChannel, basic routed interfaces and OSPF. Any
unrecognised input returns an authentic IOS error (caret + message) rather than
silently passing, so the terminal behaves like the real thing.
"""
from __future__ import annotations

import re

from .device import (
    Topology,
    etherchannel_bundles,
    interface_ospf,
    mac_to_int,
    normalize_ifname,
    ospf_router_id,
    resolve_ifname,
)
from .netutils import is_valid_ipv4, mask_to_prefix, prefix_to_mask

CONF_MODES = {"CONF", "CONF_IF", "CONF_ROUTER", "CONF_VLAN", "CONF_LINE"}


def _kw(tok: str, canonical: str, min_len: int = 1) -> bool:
    tok = tok.lower()
    return len(tok) >= min_len and canonical.startswith(tok)


def _token_spans(line: str) -> list[int]:
    return [m.start() for m in re.finditer(r"\S+", line)]


class Console:
    def __init__(self, topology: Topology, device_name: str, start_mode: str = "USER"):
        self.topo = topology
        self.dev = topology.devices[device_name]
        self.mode = start_mode
        self.ctx_ifs = []        # interfaces targeted by config-if (range aware)
        self.ctx_router = None
        self.ctx_vlan = None
        self.range = False
        self.history: list[str] = []

    # -- prompt ------------------------------------------------------------
    @property
    def prompt(self) -> str:
        h = self.dev.hostname
        suffix = {
            "USER": ">",
            "PRIV": "#",
            "CONF": "(config)#",
            "CONF_IF": "(config-if-range)#" if self.range else "(config-if)#",
            "CONF_ROUTER": "(config-router)#",
            "CONF_VLAN": "(config-vlan)#",
            "CONF_LINE": "(config-line)#",
        }[self.mode]
        return f"{h}{suffix}"

    # -- error helpers -----------------------------------------------------
    def _invalid(self, orig: str, token_index: int = 0) -> str:
        spans = _token_spans(orig)
        pos = spans[token_index] if token_index < len(spans) else len(orig)
        return f"{orig}\n{' ' * pos}^\n% Invalid input detected at '^' marker."

    @staticmethod
    def _incomplete() -> str:
        return "% Incomplete command."

    # -- seeding -----------------------------------------------------------
    def apply_config(self, lines: list[str]) -> None:
        """Seed device state by running config lines from global-config context."""
        saved = (self.mode, self.ctx_ifs, self.ctx_router, self.ctx_vlan, self.range)
        self.mode, self.ctx_ifs, self.ctx_router, self.ctx_vlan, self.range = "CONF", [], None, None, False
        for ln in lines:
            self.execute(ln)
        self.mode, self.ctx_ifs, self.ctx_router, self.ctx_vlan, self.range = saved

    # -- main dispatch -----------------------------------------------------
    def execute(self, line: str) -> str:
        orig = line.rstrip("\n").rstrip()
        s = orig.strip()
        if s == "" or s.startswith("!"):
            return ""
        # Context-sensitive help: `?` lists what's valid at this point, in this
        # mode — the real IOS discovery feature (and it only offers commands the
        # simulator actually supports).
        if "?" in s:
            from .clihelp import help_query
            return help_query(self.mode, orig[:orig.index("?")].lstrip())
        self.history.append(s)
        toks = s.split()
        t0 = toks[0].lower()
        if t0 == "help":
            from .clihelp import HELP_BLURB
            return HELP_BLURB

        # `end` from any config mode
        if _kw(t0, "end", 3) and self.mode in CONF_MODES:
            self._to_priv()
            return ""
        # `do <cmd>` runs an exec command from config
        if self.mode in CONF_MODES and t0 == "do":
            return self._exec(toks[1:], " ".join(orig.split()[1:]))
        # `show` works from any mode in this study sim
        if _kw(t0, "show", 2):
            return self._show(toks[1:], orig)
        # exit transitions
        if _kw(t0, "exit", 3) or _kw(t0, "quit", 4):
            return self._exit()

        if self.mode == "USER":
            return self._user(toks, orig)
        if self.mode == "PRIV":
            return self._priv(toks, orig)
        if self.mode == "CONF":
            return self._conf(toks, orig)
        if self.mode == "CONF_IF":
            return self._conf_if(toks, orig)
        if self.mode == "CONF_ROUTER":
            return self._conf_router(toks, orig)
        if self.mode == "CONF_VLAN":
            return self._conf_vlan(toks, orig)
        if self.mode == "CONF_LINE":
            return self._conf_line(toks, orig)
        return self._invalid(orig)

    # -- mode transitions --------------------------------------------------
    def _to_priv(self):
        self.mode = "PRIV"
        self.ctx_ifs, self.ctx_router, self.ctx_vlan, self.range = [], None, None, False

    def _exit(self) -> str:
        if self.mode == "USER":
            return ""
        if self.mode == "PRIV":
            self.mode = "USER"
        elif self.mode == "CONF":
            self.mode = "PRIV"
        else:
            self.mode = "CONF"
            self.ctx_ifs, self.ctx_router, self.ctx_vlan, self.range = [], None, None, False
        return ""

    # -- USER / PRIV -------------------------------------------------------
    def _user(self, toks, orig):
        t0 = toks[0].lower()
        if _kw(t0, "enable", 2):
            self.mode = "PRIV"
            return ""
        if _kw(t0, "ping", 2) or _kw(t0, "traceroute", 5):
            return self._ping(toks)
        return self._invalid(orig)

    def _priv(self, toks, orig):
        t0 = toks[0].lower()
        if _kw(t0, "disable", 3):
            self.mode = "USER"
            return ""
        if _kw(t0, "configure", 4):
            self.mode = "CONF"
            return "Enter configuration commands, one per line.  End with CNTL/Z."
        if _kw(t0, "write", 2):
            return "Building configuration...\n[OK]"
        if _kw(t0, "copy", 2):
            return "Destination filename [startup-config]?\nBuilding configuration...\n[OK]"
        if _kw(t0, "ping", 2) or _kw(t0, "traceroute", 5):
            return self._ping(toks)
        if _kw(t0, "reload", 3):
            return "Proceed with reload? [confirm]  (reload is disabled in the simulator)"
        return self._invalid(orig)

    def _ping(self, toks):
        target = toks[1] if len(toks) > 1 else None
        if not target:
            return self._incomplete()
        # Reachable if some local up interface shares a subnet with target, or an
        # OSPF neighbor exists (1-hop best effort).
        reachable = False
        for iface in self.dev.interfaces.values():
            if iface.ip and iface.mask and not iface.shutdown and is_valid_ipv4(target):
                from .netutils import same_subnet
                if same_subnet(iface.ip, target, iface.mask):
                    reachable = True
                    break
        if not reachable:
            for ifn in list(self.dev.interfaces):
                if self.topo.ospf_adjacency(self.dev.hostname, ifn):
                    reachable = True
                    break
        dots = "!!!!!" if reachable else "....."
        rate = "100 percent (5/5)" if reachable else "0 percent (0/5)"
        return (f"Type escape sequence to abort.\nSending 5, 100-byte ICMP Echos to {target}, "
                f"timeout is 2 seconds:\n{dots}\nSuccess rate is {rate}")

    # -- global config -----------------------------------------------------
    def _conf(self, toks, orig):
        t0 = toks[0].lower()
        neg = t0 == "no"
        body = toks[1:] if neg else toks
        if not body:
            return self._incomplete()
        b0 = body[0].lower()

        if _kw(b0, "hostname", 4):
            if len(body) < 2:
                return self._incomplete()
            self.dev.hostname = body[1]
            return ""
        if _kw(b0, "interface", 3):
            return self._enter_interface(body[1:], orig)
        if _kw(b0, "vlan", 2):
            if len(body) < 2 or not body[1].isdigit():
                return self._incomplete()
            vid = int(body[1])
            if neg:
                self.dev.vlans.pop(vid, None)
                return ""
            self.dev.vlans.setdefault(vid, f"VLAN{vid:04d}")
            self.ctx_vlan = vid
            self.mode = "CONF_VLAN"
            return ""
        if _kw(b0, "router", 4):
            if len(body) < 3 or not _kw(body[1].lower(), "ospf", 2):
                return self._invalid(orig, 1)
            if not body[2].isdigit():
                return self._invalid(orig, 2)
            pid = int(body[2])
            if neg:
                self.dev.ospf.pop(pid, None)
                return ""
            self.ctx_router = self.dev.ospf_process(pid)
            self.mode = "CONF_ROUTER"
            return ""
        if _kw(b0, "ip", 2) and len(body) > 1 and _kw(body[1].lower(), "routing", 4):
            self.dev.ip_routing = not neg
            return ""
        if _kw(b0, "spanning-tree", 4):
            return self._conf_stp(body[1:], orig, neg)
        if _kw(b0, "line", 4):
            self.mode = "CONF_LINE"
            return ""
        if _kw(b0, "enable", 3) or _kw(b0, "username", 4) or _kw(b0, "banner", 3) or _kw(b0, "service", 4):
            return ""  # accepted, not modelled
        return self._invalid(orig, 1 if neg else 0)

    def _conf_stp(self, rest, orig, neg):
        if not rest:
            return self._incomplete()
        r0 = rest[0].lower()
        if _kw(r0, "mode", 3):
            if len(rest) > 1:
                self.dev.stp_mode = rest[1].lower()
            return ""
        if _kw(r0, "vlan", 2):
            if len(rest) < 3 or not rest[1].isdigit():
                return self._incomplete()
            vid = int(rest[1])
            kw2 = rest[2].lower()
            if _kw(kw2, "priority", 4):
                if len(rest) < 4 or not rest[3].isdigit():
                    return self._incomplete()
                pr = int(rest[3])
                if pr % 4096 != 0 or pr > 61440:
                    return ("% Bridge Priority must be in increments of 4096.\n"
                            "% Allowed values are:\n  0     4096  8192  12288 16384 20480 "
                            "24576 28672\n  32768 36864 40960 45056 49152 53248 57344 61440")
                self.dev.stp_priority[vid] = pr
                return ""
            if _kw(kw2, "root", 4):
                sub = rest[3].lower() if len(rest) > 3 else ""
                cur = self.topo.stp_lowest_base_priority(vid)
                if _kw(sub, "primary", 4):
                    self.dev.stp_priority[vid] = 24576 if cur > 24576 else max(0, cur - 4096)
                    return ""
                if _kw(sub, "secondary", 3):
                    self.dev.stp_priority[vid] = 28672
                    return ""
                return self._incomplete()
        return self._invalid(orig)

    # -- interface config --------------------------------------------------
    def _enter_interface(self, rest, orig):
        if not rest:
            return self._incomplete()
        if _kw(rest[0].lower(), "range", 3) and len(rest) > 1:
            ifaces = self._expand_range(rest[1:])
            if not ifaces:
                return self._invalid(orig)
            self.ctx_ifs = ifaces
            self.range = True
        else:
            if resolve_ifname("".join(rest)) is None:    # e.g. "ge0/1" isn't a real type
                return self._invalid(orig, 1)
            iface = self.dev.get_if("".join(rest))
            self.ctx_ifs = [iface]
            self.range = False
        self.mode = "CONF_IF"
        return ""

    def _expand_range(self, parts):
        spec = " ".join(parts).replace(" - ", "-").replace("- ", "-").replace(" -", "-")
        out = []
        for chunk in spec.split(","):
            chunk = chunk.strip()
            if "-" in chunk:
                a, b = chunk.split("-", 1)
                a = normalize_ifname(a.strip())
                m = re.match(r"^(.*?)(\d+)$", a)
                if not m:
                    return []
                prefix, start = m.group(1), int(m.group(2))
                end = int(re.sub(r"\D", "", b)) if re.sub(r"\D", "", b) else start
                for n in range(start, end + 1):
                    if resolve_ifname(f"{prefix}{n}") is None:
                        return []
                    out.append(self.dev.get_if(f"{prefix}{n}"))
            elif chunk:
                if resolve_ifname(chunk) is None:
                    return []
                out.append(self.dev.get_if(chunk))
        return out

    def _conf_if(self, toks, orig):
        t0 = toks[0].lower()
        neg = t0 == "no"
        body = toks[1:] if neg else toks
        if not body:
            return self._incomplete()
        b0 = body[0].lower()

        # shutdown
        if _kw(b0, "shutdown", 4):
            for i in self.ctx_ifs:
                i.shutdown = not neg
            return ""
        # description
        if _kw(b0, "description", 4):
            text = orig.split(None, 1)[1] if len(orig.split(None, 1)) > 1 else ""
            for i in self.ctx_ifs:
                i.description = "" if neg else text
            return ""
        # ip address / ip mtu / ip ospf
        if _kw(b0, "ip", 2):
            return self._conf_if_ip(body[1:], orig, neg)
        if _kw(b0, "mtu", 3):
            if neg:
                for i in self.ctx_ifs:
                    i.mtu = 1500
                return ""
            if len(body) < 2 or not body[1].isdigit():
                return self._incomplete()
            for i in self.ctx_ifs:
                i.mtu = int(body[1])
            return ""
        # switchport family
        if _kw(b0, "switchport", 2):
            return self._conf_if_switchport(body[1:], orig, neg)
        # channel-group
        if _kw(b0, "channel-group", 4):
            return self._conf_if_channel(body[1:], orig, neg)
        if _kw(b0, "speed", 3):
            for i in self.ctx_ifs:
                i.speed = body[1] if len(body) > 1 else "auto"
            return ""
        if _kw(b0, "duplex", 3):
            for i in self.ctx_ifs:
                i.duplex = body[1] if len(body) > 1 else "auto"
            return ""
        return self._invalid(orig, 1 if neg else 0)

    def _conf_if_ip(self, rest, orig, neg):
        if not rest:
            return self._incomplete()
        r0 = rest[0].lower()
        if _kw(r0, "address", 3):
            if neg:
                for i in self.ctx_ifs:
                    i.ip = i.mask = None
                return ""
            if len(rest) < 3:
                return self._incomplete()
            ip, mask = rest[1], rest[2]
            if not is_valid_ipv4(ip):
                return self._invalid(orig)
            if mask.isdigit():  # /nn form not accepted on IOS interface; require dotted
                return self._invalid(orig)
            if not is_valid_ipv4(mask) or mask_to_prefix(mask) is None:
                return "% Invalid input detected at '^' marker."
            for i in self.ctx_ifs:
                if i.is_switchport:
                    return ("% IP addresses may not be configured on L2 links.\n"
                            "  Enter 'no switchport' first to make this a routed port.")
                i.ip, i.mask = ip, mask
            return ""
        if _kw(r0, "mtu", 3):
            if len(rest) < 2 or not rest[1].isdigit():
                return self._incomplete()
            for i in self.ctx_ifs:
                i.mtu = int(rest[1])
            return ""
        if _kw(r0, "ospf", 2):
            # ip ospf <pid> area <area>
            if len(rest) < 4 or not rest[1].isdigit() or not _kw(rest[2].lower(), "area", 3):
                return self._invalid(orig)
            for i in self.ctx_ifs:
                i.ospf_pid = int(rest[1])
                i.ospf_area = rest[3]
            return ""
        return self._invalid(orig)

    def _conf_if_switchport(self, rest, orig, neg):
        for i in self.ctx_ifs:
            if self.dev.kind == "router":
                return self._invalid(orig)
        if not rest:  # 'switchport' / 'no switchport'
            for i in self.ctx_ifs:
                i.is_switchport = not neg
            return ""
        r0 = rest[0].lower()
        if _kw(r0, "mode", 3):
            if len(rest) < 2:
                return self._incomplete()
            m = rest[1].lower()
            val = None
            if _kw(m, "access", 3):
                val = "access"
            elif _kw(m, "trunk", 2):
                val = "trunk"
            elif _kw(m, "dynamic", 3):
                sub = rest[2].lower() if len(rest) > 2 else ""
                val = "dynamic_desirable" if _kw(sub, "desirable", 4) else "dynamic_auto"
            if val is None:
                return self._invalid(orig)
            for i in self.ctx_ifs:
                i.sw_mode = val
            return ""
        if _kw(r0, "access", 3):
            if len(rest) < 3 or not _kw(rest[1].lower(), "vlan", 2) or not rest[2].isdigit():
                return self._invalid(orig)
            for i in self.ctx_ifs:
                i.access_vlan = int(rest[2])
            return ""
        if _kw(r0, "trunk", 2):
            return self._conf_if_trunk(rest[1:], orig, neg)
        if _kw(r0, "voice", 3):
            return ""  # accepted, not modelled
        if _kw(r0, "nonegotiate", 4):
            return ""
        return self._invalid(orig)

    def _conf_if_trunk(self, rest, orig, neg):
        if not rest:
            return self._incomplete()
        r0 = rest[0].lower()
        if _kw(r0, "native", 3):
            if len(rest) < 3 or not _kw(rest[1].lower(), "vlan", 2) or not rest[2].isdigit():
                return self._invalid(orig)
            for i in self.ctx_ifs:
                i.trunk_native = int(rest[2])
            return ""
        if _kw(r0, "encapsulation", 3):
            if len(rest) > 1:
                for i in self.ctx_ifs:
                    i.trunk_encap = rest[1].lower()
            return ""
        if _kw(r0, "allowed", 3):
            if len(rest) < 3 or not _kw(rest[1].lower(), "vlan", 2):
                return self._invalid(orig)
            spec = rest[2].lower()
            arg = rest[3] if len(rest) > 3 else ""
            for i in self.ctx_ifs:
                if spec in ("all", "none"):
                    i.trunk_allowed = spec
                elif spec == "add" and arg:
                    cur = set() if i.trunk_allowed in ("all", "none", "") else set(i.trunk_allowed.split(","))
                    cur.update(arg.split(","))
                    i.trunk_allowed = ",".join(sorted(cur, key=lambda x: int(x) if x.isdigit() else 0))
                elif spec == "remove" and arg:
                    cur = set() if i.trunk_allowed in ("all", "none", "") else set(i.trunk_allowed.split(","))
                    cur.discard(arg)
                    i.trunk_allowed = ",".join(sorted(cur, key=lambda x: int(x) if x.isdigit() else 0))
                else:
                    i.trunk_allowed = spec
            return ""
        return self._invalid(orig)

    def _conf_if_channel(self, rest, orig, neg):
        if neg:
            for i in self.ctx_ifs:
                i.channel_group = None
                i.channel_mode = None
            return ""
        if len(rest) < 3 or not rest[0].isdigit() or not _kw(rest[1].lower(), "mode", 3):
            return self._invalid(orig)
        grp = int(rest[0])
        mode = rest[2].lower()
        valid = {"on", "active", "passive", "desirable", "auto"}
        matched = next((m for m in valid if m.startswith(mode)), None)
        if matched is None:
            return self._invalid(orig)
        for i in self.ctx_ifs:
            i.channel_group = grp
            i.channel_mode = matched
        # ensure a Port-channel interface exists
        self.dev.get_if(f"Port-channel{grp}")
        return ""

    # -- router ospf config ------------------------------------------------
    def _conf_router(self, toks, orig):
        t0 = toks[0].lower()
        neg = t0 == "no"
        body = toks[1:] if neg else toks
        if not body:
            return self._incomplete()
        b0 = body[0].lower()
        proc = self.ctx_router

        if _kw(b0, "router-id", 7):
            if len(body) < 2 or not is_valid_ipv4(body[1]):
                return self._invalid(orig)
            proc.router_id = None if neg else body[1]
            return ""
        if _kw(b0, "network", 3):
            if len(body) < 5 or not _kw(body[3].lower(), "area", 3):
                return self._invalid(orig)
            net, wild, area = body[1], body[2], body[4]
            if not is_valid_ipv4(net) or not is_valid_ipv4(wild):
                return self._invalid(orig)
            tup = (net, wild, area)
            if neg:
                proc.networks = [t for t in proc.networks if t != tup]
            elif tup not in proc.networks:
                proc.networks.append(tup)
            return ""
        if _kw(b0, "passive-interface", 4):
            if len(body) < 2:
                return self._incomplete()
            arg = body[1].lower()
            if _kw(arg, "default", 3):
                proc.passive_default = not neg
                return ""
            ifn = normalize_ifname("".join(body[1:]))
            if neg:
                proc.passive_interfaces.discard(ifn)
                proc.no_passive_interfaces.add(ifn)
            else:
                proc.passive_interfaces.add(ifn)
                proc.no_passive_interfaces.discard(ifn)
            return ""
        if _kw(b0, "default-information", 7) or _kw(b0, "auto-cost", 4) or _kw(b0, "log-adjacency-changes", 3):
            return ""
        return self._invalid(orig, 1 if neg else 0)

    def _conf_vlan(self, toks, orig):
        t0 = toks[0].lower()
        if _kw(t0, "name", 3):
            if len(toks) < 2:
                return self._incomplete()
            self.dev.vlans[self.ctx_vlan] = toks[1]
            return ""
        return self._invalid(orig)

    def _conf_line(self, toks, orig):
        return ""  # line-mode commands accepted, not modelled

    # -- exec entry for `do show ...` --------------------------------------
    def _exec(self, toks, orig_after):
        if not toks:
            return self._incomplete()
        if _kw(toks[0].lower(), "show", 2):
            return self._show(toks[1:], "show " + orig_after.split(None, 1)[1] if len(orig_after.split(None, 1)) > 1 else "show")
        if _kw(toks[0].lower(), "ping", 2):
            return self._ping(toks)
        if _kw(toks[0].lower(), "write", 2):
            return "Building configuration...\n[OK]"
        return self._invalid(orig_after)

    # -- show renderers ----------------------------------------------------
    def _show(self, toks, orig):
        if not toks:
            return self._incomplete()
        t0 = toks[0].lower()
        if _kw(t0, "running-config", 2) or _kw(t0, "startup-config", 5):
            if len(toks) >= 3 and _kw(toks[1].lower(), "interface", 3):
                return self._run_config(only_if="".join(toks[2:]))
            return self._run_config()
        if _kw(t0, "ip", 2):
            return self._show_ip(toks[1:], orig)
        if _kw(t0, "interfaces", 3):
            rest = toks[1:]
            if rest and _kw(rest[0].lower(), "trunk", 2):
                return self._show_trunk()
            if rest and _kw(rest[0].lower(), "status", 3):
                return self._show_if_status()
            if rest:                                  # a specific interface
                want_status = len(rest) > 1 and _kw(rest[-1].lower(), "status", 3)
                name_toks = rest[:-1] if want_status else rest
                canon = resolve_ifname("".join(name_toks))   # joins "Gig 0/1" -> Gi0/1
                iface = self.dev.get_if(canon, create=False) if canon else None
                if iface is None:
                    return self._invalid(orig, 2)     # bad type or no such port
                return self._show_if_status(only=iface) if want_status else self._show_if_detail(iface)
            return self._show_if_all_detail()         # bare `show interfaces` is detailed on IOS
        if _kw(t0, "vlan", 2):
            if len(toks) == 1:
                return self._show_vlan_brief()
            sub = toks[1].lower()
            if _kw(sub, "brief", 2):
                return self._show_vlan_brief()
            if _kw(sub, "id", 2):
                if len(toks) < 3:
                    return self._incomplete()
                if not toks[2].isdigit():
                    return self._invalid(orig, 3)
                return self._show_vlan_brief(only=int(toks[2]))
            # bare "show vlan 1" / "show vlan summary" etc. are not valid IOS here
            return self._invalid(orig, 2)
        if _kw(t0, "spanning-tree", 4):
            vid = None
            if len(toks) >= 3 and _kw(toks[1].lower(), "vlan", 2) and toks[2].isdigit():
                vid = int(toks[2])
            return self._show_stp(vid)
        if _kw(t0, "etherchannel", 5):
            return self._show_etherchannel()
        if _kw(t0, "cdp", 3):
            return self._show_cdp()
        if _kw(t0, "version", 3):
            return self._show_version()
        return self._invalid(orig, 1)

    def _show_ip(self, rest, orig):
        if not rest:
            return self._incomplete()
        r0 = rest[0].lower()
        if _kw(r0, "interface", 3) and len(rest) > 1 and _kw(rest[1].lower(), "brief", 2):
            return self._show_if_brief()
        if _kw(r0, "route", 3):
            return self._show_ip_route()
        if _kw(r0, "ospf", 2):
            if len(rest) > 1 and _kw(rest[1].lower(), "neighbor", 3):
                return self._show_ospf_neighbor()
            if len(rest) > 2 and _kw(rest[1].lower(), "interface", 3) and _kw(rest[2].lower(), "brief", 2):
                return self._show_ospf_if_brief()
            return self._show_ospf_neighbor()
        return self._invalid(orig, 2)

    def _run_config(self, only_if=None):
        lines = ["Building configuration...", "", "Current configuration:", "!",
                 f"hostname {self.dev.hostname}", "!"]
        if only_if is None:
            if self.dev.vlans:
                for vid in sorted(self.dev.vlans):
                    lines += [f"vlan {vid}", f" name {self.dev.vlans[vid]}", "!"]
            lines.append(f"spanning-tree mode {self.dev.stp_mode}")
            for vid in sorted(self.dev.stp_priority):
                lines.append(f"spanning-tree vlan {vid} priority {self.dev.stp_priority[vid]}")
            lines.append("!")
        names = [normalize_ifname(only_if)] if only_if else sorted(self.dev.interfaces)
        for name in names:
            iface = self.dev.interfaces.get(name)
            if iface is None:
                continue
            lines.append(f"interface {iface.name}")
            if iface.description:
                lines.append(f" description {iface.description}")
            if not iface.is_switchport:
                if self.dev.kind != "router":
                    lines.append(" no switchport")
                if iface.ip:
                    lines.append(f" ip address {iface.ip} {iface.mask}")
            else:
                if iface.sw_mode == "access":
                    lines.append(" switchport mode access")
                    if iface.access_vlan != 1:
                        lines.append(f" switchport access vlan {iface.access_vlan}")
                elif iface.sw_mode == "trunk":
                    lines.append(" switchport trunk encapsulation dot1q")
                    lines.append(" switchport mode trunk")
                    if iface.trunk_native != 1:
                        lines.append(f" switchport trunk native vlan {iface.trunk_native}")
                    if iface.trunk_allowed not in ("all", ""):
                        lines.append(f" switchport trunk allowed vlan {iface.trunk_allowed}")
            if iface.mtu != 1500:
                lines.append(f" mtu {iface.mtu}")
            if iface.channel_group is not None:
                lines.append(f" channel-group {iface.channel_group} mode {iface.channel_mode}")
            if iface.ospf_pid is not None and iface.ospf_area is not None:
                lines.append(f" ip ospf {iface.ospf_pid} area {iface.ospf_area}")
            if iface.shutdown:
                lines.append(" shutdown")
            lines.append("!")
        for pid in sorted(self.dev.ospf):
            proc = self.dev.ospf[pid]
            lines.append(f"router ospf {pid}")
            if proc.router_id:
                lines.append(f" router-id {proc.router_id}")
            if proc.passive_default:
                lines.append(" passive-interface default")
            for ifn in sorted(proc.passive_interfaces):
                lines.append(f" passive-interface {ifn}")
            for net, wild, area in proc.networks:
                lines.append(f" network {net} {wild} area {area}")
            lines.append("!")
        lines.append("end")
        return "\n".join(lines)

    def _show_if_brief(self):
        rows = ["Interface                  IP-Address      OK? Method Status                Protocol"]
        for name in sorted(self.dev.interfaces):
            i = self.dev.interfaces[name]
            ip = i.ip or "unassigned"
            method = "manual" if i.ip else "unset"
            if i.shutdown:
                status, proto = "administratively down", "down"
            else:
                peer = self.topo.neighbor_of(self.dev.hostname, name)
                if peer:
                    pdev = self.topo.devices.get(peer[0])
                    pif = pdev.get_if(peer[1], create=False) if pdev else None
                    up = bool(pif and not pif.shutdown)
                    status, proto = ("up", "up") if up else ("down", "down")
                else:
                    status, proto = ("up", "up") if i.is_switchport else ("up", "down")
            rows.append(f"{i.name:<26} {ip:<15} YES {method:<6} {status:<21} {proto}")
        return "\n".join(rows)

    def _show_if_status(self, only=None):
        rows = ["Port      Name               Status       Vlan       Duplex  Speed Type"]
        items = [only] if only is not None else \
            [self.dev.interfaces[n] for n in sorted(self.dev.interfaces)]
        for i in items:
            st = "disabled" if i.shutdown else "connected"
            vlan = "trunk" if i.sw_mode == "trunk" else (str(i.access_vlan) if i.is_switchport else "routed")
            rows.append(f"{_short(i.name):<9} {i.description[:18]:<18} {st:<12} {vlan:<10} {i.duplex:<7} {i.speed:<5} 10/100/1000")
        return "\n".join(rows)

    def _show_if_detail(self, i):
        """Detailed single-interface view (show interfaces <name>)."""
        if i.shutdown:
            head = f"{i.name} is administratively down, line protocol is down"
        else:
            up = True
            peer = self.topo.neighbor_of(self.dev.hostname, i.name)
            if peer:
                pdev = self.topo.devices.get(peer[0])
                pif = pdev.get_if(peer[1], create=False) if pdev else None
                up = bool(pif and not pif.shutdown)
            head = (f"{i.name} is up, line protocol is up (connected)" if up
                    else f"{i.name} is down, line protocol is down (notconnect)")
        duplex = {"full": "Full-duplex", "half": "Half-duplex", "auto": "Auto-duplex"}.get(
            i.duplex, f"{i.duplex}-duplex")
        speed = "Auto-speed" if i.speed == "auto" else (
            f"{i.speed}Mb/s" if str(i.speed).isdigit() else str(i.speed))
        bw = 1000000 if i.name.startswith(
            ("GigabitEthernet", "TenGigabitEthernet", "Port-channel")) else 100000
        addr = (f"  Internet address is {i.ip}/{mask_to_prefix(i.mask)}"
                if i.ip and i.mask else "  Internet address is not set")
        return "\n".join([
            head,
            f"  Hardware is iGbE, address is {self.dev.base_mac} (bia {self.dev.base_mac})",
            addr,
            f"  MTU {i.mtu} bytes, BW {bw} Kbit/sec, DLY 10 usec,",
            "     reliability 255/255, txload 1/255, rxload 1/255",
            "  Encapsulation ARPA, loopback not set",
            "  Keepalive set (10 sec)",
            f"  {duplex}, {speed}, media type is 10/100/1000BaseTX",
            "  input flow-control is off, output flow-control is unsupported",
            "  5 minute input rate 0 bits/sec, 0 packets/sec",
            "  5 minute output rate 0 bits/sec, 0 packets/sec",
            "     0 packets input, 0 bytes, 0 no buffer",
            "     0 packets output, 0 bytes, 0 underruns",
        ])

    def _show_if_all_detail(self):
        """Bare `show interfaces` — detailed block for every interface (IOS)."""
        return "\n".join(self._show_if_detail(self.dev.interfaces[n])
                         for n in sorted(self.dev.interfaces))

    def _show_vlan_brief(self, only=None):
        base = {1: "default"}
        base.update(self.dev.vlans)
        base.update({1002: "fddi-default", 1003: "token-ring-default",
                     1004: "fddinet-default", 1005: "trnet-default"})
        if only is not None and only not in base:
            return f"VLAN id {only} not found in current VLAN database"
        ports: dict[int, list[str]] = {}
        for name in sorted(self.dev.interfaces):
            i = self.dev.interfaces[name]
            if i.is_switchport and i.sw_mode == "access":
                ports.setdefault(i.access_vlan, []).append(_short(i.name))
        rows = ["VLAN Name                             Status    Ports",
                "---- -------------------------------- --------- -------------------------------"]
        for vid in sorted(base):
            if only is not None and vid != only:
                continue
            status = "act/unsup" if vid >= 1002 else "active"
            plist = ", ".join(ports.get(vid, []))
            rows.append(f"{vid:<4} {base[vid]:<32} {status:<9} {plist}")
        return "\n".join(rows)

    def _show_trunk(self):
        trunks = [i for i in self.dev.interfaces.values() if i.sw_mode == "trunk" and not i.shutdown]
        if not trunks:
            return ""
        out = ["Port        Mode         Encapsulation  Status        Native vlan"]
        for i in trunks:
            out.append(f"{_short(i.name):<11} on           802.1q         trunking      {i.trunk_native}")
        out += ["", "Port        Vlans allowed on trunk"]
        for i in trunks:
            allowed = "1-4094" if i.trunk_allowed == "all" else ("none" if i.trunk_allowed == "none" else i.trunk_allowed)
            out.append(f"{_short(i.name):<11} {allowed}")
        return "\n".join(out)

    def _show_stp(self, vid):
        vids = [vid] if vid is not None else sorted(set(self.dev.vlans) | {1})
        blocks = []
        for v in vids:
            root = self.topo.stp_root(v)
            self_eff = self.topo.stp_effective_priority(self.dev, v)
            base = self.dev.stp_base_priority(v)
            proto = "rstp" if "rapid" in self.dev.stp_mode else "ieee"
            b = [f"VLAN{v:04d}", f"  Spanning tree enabled protocol {proto}"]
            if root is self.dev:
                b += ["  Root ID    Priority    " + str(self.topo.stp_effective_priority(self.dev, v)),
                      f"             Address     {self.dev.base_mac}",
                      "             This bridge is the root", ""]
            else:
                b += ["  Root ID    Priority    " + str(self.topo.stp_effective_priority(root, v) if root else 0),
                      f"             Address     {root.base_mac if root else '----.----.----'}",
                      "             Cost        4", "             Port        1 (GigabitEthernet0/1)", ""]
            b += [f"  Bridge ID  Priority    {self_eff}  (priority {base} sys-id-ext {v})",
                  f"             Address     {self.dev.base_mac}"]
            blocks.append("\n".join(b))
        return "\n\n".join(blocks)

    def _show_etherchannel(self):
        groups: dict[int, list] = {}
        for i in self.dev.interfaces.values():
            if i.channel_group is not None and not i.name.startswith("Port-channel"):
                groups.setdefault(i.channel_group, []).append(i)
        header = ("Flags:  D - down        P - bundled in port-channel\n"
                  "        I - stand-alone s - suspended\n"
                  "        U - in use      f - failed to allocate aggregator\n"
                  f"\nNumber of channel-groups in use: {len(groups)}\n"
                  f"Number of aggregators:           {len(groups)}\n\n"
                  "Group  Port-channel  Protocol    Ports\n"
                  "------+-------------+-----------+-----------------------------------------------")
        rows = [header]
        for grp in sorted(groups):
            members = groups[grp]
            proto = members[0].channel_protocol()
            port_flags = []
            bundled_any = False
            for m in members:
                peer = self.topo.neighbor_of(self.dev.hostname, m.name)
                flag = "D" if m.shutdown else "I"
                if peer and not m.shutdown:
                    pdev = self.topo.devices.get(peer[0])
                    pif = pdev.get_if(peer[1], create=False) if pdev else None
                    if pif is not None:
                        bundles, _, _ = etherchannel_bundles(m.channel_mode, pif.channel_mode)
                        if bundles and not pif.shutdown:
                            flag = "P"
                            bundled_any = True
                        else:
                            flag = "s"
                port_flags.append(f"{_short(m.name)}({flag})")
            po_state = "SU" if bundled_any else "SD"
            rows.append(f"{grp:<6} Po{grp}({po_state}){'':<{max(0, 7 - len(str(grp)))}}  {proto:<11} " + "  ".join(port_flags))
        return "\n".join(rows)

    def _show_ospf_neighbor(self):
        rows = []
        for name in sorted(self.dev.interfaces):
            adj = self.topo.ospf_adjacency(self.dev.hostname, name)
            if adj is None:
                continue
            peer = self.topo.neighbor_of(self.dev.hostname, name)
            pif = self.topo.devices[peer[0]].get_if(peer[1], create=False)
            addr = pif.ip if pif else "0.0.0.0"
            if not adj.mtu_match:
                state = "EXSTART/DROTHER"
            else:
                state = "FULL/DR" if adj.neighbor_dr else "FULL/BDR"
            rows.append(f"{adj.neighbor_rid:<15} 1   {state:<15} 00:00:38    {addr:<15} {name}")
        if not rows:
            return ""
        header = "Neighbor ID     Pri   State           Dead Time   Address         Interface"
        return header + "\n" + "\n".join(rows)

    def _show_ospf_if_brief(self):
        rows = ["Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C"]
        for name in sorted(self.dev.interfaces):
            i = self.dev.interfaces[name]
            oi = interface_ospf(self.dev, i)
            if not oi:
                continue
            pid, area, passive = oi
            pfx = mask_to_prefix(i.mask) if i.mask else 0
            adj = self.topo.ospf_adjacency(self.dev.hostname, name)
            nbr = "1/1" if adj and adj.mtu_match else "0/0"
            rows.append(f"{_short(name):<12} {pid:<5} {area:<15} {i.ip}/{pfx:<8}   1     {'DR' if not passive else 'DROTH':<5} {nbr}")
        return "\n".join(rows)

    def _show_ip_route(self):
        rows = ["Codes: L - local, C - connected, O - OSPF", ""]
        seen = set()
        from .netutils import network_of, mask_to_prefix as _m2p
        for i in self.dev.interfaces.values():
            if i.ip and i.mask and not i.shutdown:
                net = network_of(i.ip, i.mask)
                pfx = _m2p(i.mask)
                rows.append(f"C        {net}/{pfx} is directly connected, {_short(i.name)}")
                rows.append(f"L        {i.ip}/32 is directly connected, {_short(i.name)}")
                seen.add(f"{net}/{pfx}")
        # 1-hop OSPF routes from FULL neighbors
        for name in list(self.dev.interfaces):
            adj = self.topo.ospf_adjacency(self.dev.hostname, name)
            if not adj or not adj.mtu_match:
                continue
            peer = self.topo.neighbor_of(self.dev.hostname, name)
            pdev = self.topo.devices[peer[0]]
            for pi in pdev.interfaces.values():
                if pi.ip and pi.mask and not pi.shutdown:
                    net = network_of(pi.ip, pi.mask)
                    pfx = _m2p(pi.mask)
                    key = f"{net}/{pfx}"
                    if key not in seen:
                        rows.append(f"O        {net}/{pfx} [110/2] via {pi.ip}, {_short(name)}")
                        seen.add(key)
        return "\n".join(rows)

    def _show_cdp(self):
        rows = ["Capability Codes: R - Router, S - Switch, H - Host, I - IGMP",
                "",
                "Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID"]
        for name in sorted(self.dev.interfaces):
            peer = self.topo.neighbor_of(self.dev.hostname, name)
            if not peer:
                continue
            pdev = self.topo.devices.get(peer[0])
            cap = "R" if pdev and pdev.kind == "router" else "S I"
            rows.append(f"{peer[0]:<16} {_short(name):<17} 150        {cap:<11} IOSv      {_short(peer[1])}")
        return "\n".join(rows) if len(rows) > 3 else "\n".join(rows[:2])

    def _show_version(self):
        return (f"Cisco IOS Software, {self.dev.hostname} study simulator\n"
                f"System image: iosv-study\n"
                f"{self.dev.hostname} uptime is 1 hour, 0 minutes\n"
                "Configuration register is 0x2102")


def _short(name: str) -> str:
    """Abbreviate an interface name the way IOS does in tabular output."""
    repl = [
        ("TenGigabitEthernet", "Te"), ("GigabitEthernet", "Gi"),
        ("FastEthernet", "Fa"), ("Ethernet", "Et"), ("Port-channel", "Po"),
        ("Loopback", "Lo"), ("Vlan", "Vl"), ("Tunnel", "Tu"), ("Serial", "Se"),
    ]
    for long, short in repl:
        if name.startswith(long):
            return short + name[len(long):]
    return name
