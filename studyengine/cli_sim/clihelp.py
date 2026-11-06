"""Context-sensitive IOS help (``?`` and ``help``) for the CLI simulator.

The tree below mirrors exactly what ``parser.py`` understands, so ``?`` only ever
offers commands that actually work. A node is a dict of ``keyword -> (desc, child)``
where ``child`` is another node, or ``None`` when the command can end there.
Special keys:
  * ``"__cr__": True``      — this point is a complete command (shows ``<cr>``)
  * ``"__arg__": (ph, desc, child)`` — a value argument (number / word / IP)
  * ``"__ifarg__": (desc, child)``   — an interface-name argument (Gi0/1, ...)
"""
from __future__ import annotations

from .device import resolve_ifname


def _arg(ph, desc, child=None):
    return {"__arg__": (ph, desc, child or {"__cr__": True})}


# -- shared sub-trees --------------------------------------------------------
_SHOW = {
    "running-config": ("Current operating configuration",
                       {"__cr__": True,
                        "interface": ("Show interface configuration", {"__ifarg__": ("Interface name", {"__cr__": True})})}),
    "startup-config": ("Contents of startup configuration", None),
    "interfaces": ("Interface status and configuration", {
        "__cr__": True,
        "__ifarg__": ("Interface name (e.g. GigabitEthernet0/1)",
                      {"__cr__": True, "status": ("Line status", None)}),
        "status": ("Interface line status", None),
        "trunk": ("Interface trunk information", None),
    }),
    "ip": ("IP information", {
        "interface": ("IP interface status", {"brief": ("Brief summary of IP status", None)}),
        "route": ("IP routing table", None),
        "ospf": ("OSPF information", {
            "__cr__": True,
            "neighbor": ("Neighbor list", None),
            "interface": ("Interface information", {"brief": ("Brief summary", None)}),
        }),
    }),
    "vlan": ("VTP VLAN status", {
        "__cr__": True,
        "brief": ("VTP all VLAN status in brief", None),
        "id": ("VTP VLAN status by VLAN id", _arg("<1-4094>", "VLAN id")),
    }),
    "spanning-tree": ("Spanning tree topology", {
        "__cr__": True,
        "vlan": ("VLAN information", _arg("<1-4094>", "VLAN id")),
    }),
    "etherchannel": ("EtherChannel information", {"__cr__": True, "summary": ("One line per channel-group", None)}),
    "cdp": ("CDP information", {"neighbors": ("CDP neighbor entries", None)}),
    "version": ("System hardware and software status", None),
}

_SWITCHPORT = {
    "__cr__": True,
    "mode": ("Set trunking mode of the interface", {
        "access": ("Set to access mode", None),
        "trunk": ("Set to trunking mode", None),
        "dynamic": ("Set to dynamic negotiation", {
            "auto": ("Become a trunk if the neighbor initiates", None),
            "desirable": ("Actively try to become a trunk", None)}),
    }),
    "access": ("Set access-mode characteristics", {
        "vlan": ("Set the access VLAN", _arg("<1-4094>", "VLAN id"))}),
    "trunk": ("Set trunking characteristics", {
        "native": ("Native VLAN for untragged traffic",
                   {"vlan": ("Set native VLAN", _arg("<1-4094>", "VLAN id"))}),
        "allowed": ("VLANs allowed on the trunk",
                    {"vlan": ("Set allowed VLANs", _arg("WORD", "all | none | add | remove | <list>"))}),
        "encapsulation": ("Trunking encapsulation",
                          {"dot1q": ("IEEE 802.1Q", None), "isl": ("ISL", None)}),
    }),
    "voice": ("Voice appliance attributes", {"vlan": ("Voice VLAN", _arg("<1-4094>", "VLAN id"))}),
    "nonegotiate": ("Device will not engage in negotiation (DTP)", None),
}

_IF = {
    "shutdown": ("Shutdown the selected interface", None),
    "description": ("Interface specific description", _arg("LINE", "Up to 240 characters")),
    "ip": ("Interface IP configuration commands", {
        "address": ("Set the IP address of an interface",
                    _arg("A.B.C.D", "IP address", _arg("A.B.C.D", "Subnet mask"))),
        "ospf": ("OSPF interface commands", _arg("<1-65535>", "Process ID",
                 {"area": ("Set the OSPF area", _arg("<0-4294967295>", "Area id"))})),
        "mtu": ("Set IP MTU", _arg("<68-1500>", "MTU (bytes)")),
    }),
    "mtu": ("Set the interface Maximum Transmission Unit", _arg("<64-9216>", "MTU (bytes)")),
    "switchport": ("Set switching mode characteristics", _SWITCHPORT),
    "channel-group": ("Etherchannel/port bundling configuration",
                      _arg("<1-48>", "Channel group number",
                           {"mode": ("Set the channel mode", {
                               "on": ("Unconditionally bundle (no protocol)", None),
                               "active": ("LACP, actively negotiate", None),
                               "passive": ("LACP, only respond", None),
                               "desirable": ("PAgP, actively negotiate", None),
                               "auto": ("PAgP, only respond", None)})})),
    "speed": ("Configure speed operation", None),
    "duplex": ("Configure duplex operation", None),
}

_ROUTER = {
    "router-id": ("router-id for this OSPF process", _arg("A.B.C.D", "OSPF router-id")),
    "network": ("Enable routing on an IP network",
                _arg("A.B.C.D", "Network", _arg("A.B.C.D", "Wildcard mask",
                     {"area": ("Set the OSPF area", _arg("<0-4294967295>", "Area id"))}))),
    "passive-interface": ("Suppress routing updates on an interface",
                          {"default": ("Suppress on all interfaces", None),
                           "__ifarg__": ("Interface name", {"__cr__": True})}),
}

_VLANCFG = {"name": ("Ascii name of the VLAN", _arg("WORD", "VLAN name"))}

_STP = {
    "mode": ("Spanning-tree mode", {"pvst": ("", None), "rapid-pvst": ("", None), "mst": ("", None)}),
    "vlan": ("VLAN Switch Spanning Tree",
             _arg("<1-4094>", "VLAN id", {
                 "priority": ("Set the bridge priority", _arg("<0-61440>", "In increments of 4096")),
                 "root": ("Configure this switch as root", {
                     "primary": ("Primary root", None), "secondary": ("Secondary root", None)})})),
}

# -- mode roots --------------------------------------------------------------
ROOTS: dict[str, dict] = {
    "USER": {
        "enable": ("Turn on privileged commands", None),
        "ping": ("Send echo messages", _arg("A.B.C.D", "Target address")),
        "traceroute": ("Trace route to destination", _arg("A.B.C.D", "Target address")),
        "show": ("Show running system information", _SHOW),
        "exit": ("Exit from the EXEC", None),
    },
    "PRIV": {
        "configure": ("Enter configuration mode", {"terminal": ("Configure from the terminal", None)}),
        "show": ("Show running system information", _SHOW),
        "ping": ("Send echo messages", _arg("A.B.C.D", "Target address")),
        "traceroute": ("Trace route to destination", _arg("A.B.C.D", "Target address")),
        "copy": ("Copy from one file to another", None),
        "write": ("Write running configuration to memory", None),
        "reload": ("Halt and perform a cold restart", None),
        "disable": ("Turn off privileged commands", None),
        "exit": ("Exit from the EXEC", None),
    },
    "CONF": {
        "hostname": ("Set system's network name", _arg("WORD", "This system's network name")),
        "interface": ("Select an interface to configure",
                      {"__ifarg__": ("Interface name (e.g. GigabitEthernet0/1)", _IF),
                       "range": ("Configure a range of interfaces", {"__ifarg__": ("First interface", {"__cr__": True})})}),
        "vlan": ("VLAN commands", _arg("<1-4094>", "ISL VLAN IDs 1-4094")),
        "router": ("Enable a routing process", {"ospf": ("Open Shortest Path First (OSPF)", _arg("<1-65535>", "Process ID"))}),
        "ip": ("Global IP configuration subcommands", {"routing": ("Enable IP routing", None)}),
        "spanning-tree": ("Spanning Tree Subsystem", _STP),
        "line": ("Configure a terminal line", None),
        "end": ("Exit to privileged EXEC mode", None),
        "exit": ("Exit from configure mode", None),
    },
    "CONF_IF": dict(_IF, **{"end": ("Exit to privileged EXEC mode", None), "exit": ("Exit interface configuration", None)}),
    "CONF_ROUTER": dict(_ROUTER, **{"end": ("Exit to privileged EXEC mode", None), "exit": ("Exit router configuration", None)}),
    "CONF_VLAN": dict(_VLANCFG, **{"end": ("Exit to privileged EXEC mode", None), "exit": ("Exit VLAN configuration", None)}),
    "CONF_LINE": {"end": ("Exit to privileged EXEC mode", None), "exit": ("Exit line configuration", None)},
}

# `no ...` negates whatever the mode can set.
for _m in ("CONF", "CONF_IF", "CONF_ROUTER", "CONF_VLAN"):
    _neg = {k: v for k, v in ROOTS[_m].items() if k not in ("no", "end", "exit")}
    ROOTS[_m]["no"] = ("Negate a command or set its defaults", _neg)


# -- query engine ------------------------------------------------------------
def _walk(node, toks):
    cur = node
    for t in toks:
        if not isinstance(cur, dict):
            return None
        tl = t.lower()
        kws = [k for k in cur if not k.startswith("__")]
        matches = [tl] if tl in cur else [k for k in kws if k.startswith(tl)]
        if matches:
            _desc, child = cur[matches[0]]
            cur = child if child is not None else {"__cr__": True}
        elif "__arg__" in cur:
            cur = cur["__arg__"][2]
        elif "__ifarg__" in cur and resolve_ifname(t) is not None:
            cur = cur["__ifarg__"][1]
        else:
            return None
    return cur


def _options(node, partial):
    if not isinstance(node, dict):
        return []
    opts = []
    for k in sorted(k for k in node if not k.startswith("__")):
        if k.startswith(partial):
            opts.append((k, node[k][0]))
    if not partial:
        if "__ifarg__" in node:
            opts.append(("<interface>", node["__ifarg__"][0]))
        if "__arg__" in node:
            ph, desc, _ = node["__arg__"]
            opts.append((ph, desc))
        if node.get("__cr__"):
            opts.append(("<cr>", ""))
    return opts


def help_query(mode: str, text_before_qmark: str) -> str:
    """Return the IOS ``?`` listing for the text typed before the '?'."""
    space_before = text_before_qmark == "" or text_before_qmark.endswith(" ")
    toks = text_before_qmark.split()
    walk_toks = toks if space_before else toks[:-1]
    partial = "" if space_before else toks[-1].lower()
    node = _walk(ROOTS.get(mode, {}), walk_toks)
    if node is None:
        return "% Unrecognized command"
    opts = _options(node, partial)
    if not opts:
        return "% Unrecognized command"
    return "\n".join(f"  {kw:<16}{desc}".rstrip() for kw, desc in opts)


def complete(mode: str, text: str) -> str:
    """Tab-style auto-finish: expand the last (partial) word to its full IOS
    keyword when it's unambiguous. Unknown or ambiguous input is left as typed."""
    if not text or text.endswith(" "):
        return text
    toks = text.split()
    node = _walk(ROOTS.get(mode, {}), toks[:-1])
    if not isinstance(node, dict):
        return text
    partial = toks[-1].lower()
    kws = [k for k in node if not k.startswith("__") and k.startswith(partial)]
    if len(kws) == 1:
        toks[-1] = kws[0]
        return " ".join(toks) + " "
    return text


HELP_BLURB = (
    "Help may be requested at any point in a command by entering\n"
    "a question mark '?'.  If nothing matches, the help list will\n"
    "be empty and you must backup until entering a '?' shows the\n"
    "available options.\n"
    "Two styles of help are provided:\n"
    "1. Full help is available when you are ready to enter a\n"
    "   command argument (e.g. 'show ?') and describes each possible\n"
    "   argument.\n"
    "2. Partial help is provided when an abbreviated argument is\n"
    "   entered and you want to know what arguments match the input\n"
    "   (e.g. 'show pr?'.)"
)
