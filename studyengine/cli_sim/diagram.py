"""Render a live topology as a Graphviz DOT string for the PBQ lab.

The diagram is generated from the actual scenario topology (devices, links,
interface config), so it is always accurate and updates as the learner changes
the configuration — no copyrighted exam images involved.
"""
from __future__ import annotations

from .device import Topology
from .netutils import mask_to_prefix
from .parser import _short

# Dark-theme-friendly fills per device kind.
_FILL = {"router": "#1f5c82", "l3switch": "#5a4b8a", "switch": "#1f7a4d"}


def _iface_line(iface) -> str | None:
    """A compact one-line annotation for a configured interface, or None."""
    name = _short(iface.name)
    if iface.ip and iface.mask:
        pfx = mask_to_prefix(iface.mask)
        tag = f"{name} {iface.ip}/{pfx}"
        return tag + ("  (shut)" if iface.shutdown else "")
    if iface.is_switchport and iface.sw_mode == "trunk":
        extra = f" nat{iface.trunk_native}" if iface.trunk_native != 1 else ""
        return f"{name} trunk{extra}"
    if iface.is_switchport and iface.sw_mode == "access" and iface.access_vlan != 1:
        return f"{name} access v{iface.access_vlan}"
    if iface.channel_group is not None:
        return f"{name} po{iface.channel_group}/{iface.channel_mode}"
    return None


def _node_label(dev) -> str:
    lines = [dev.hostname]
    shown = 0
    for name in sorted(dev.interfaces):
        if shown >= 4:
            break
        ln = _iface_line(dev.interfaces[name])
        if ln:
            lines.append(ln)
            shown += 1
    return "\\n".join(lines)


def topology_dot(topo: Topology, highlight_device: str | None = None) -> str:
    """Build a Graphviz DOT string for `st.graphviz_chart`."""
    out = [
        "graph G {",
        '  bgcolor="transparent";',
        "  rankdir=LR;",
        '  node [shape=box, style="filled,rounded", fontname="Helvetica", '
        'fontsize=11, fontcolor="#E9EDF5", color="#39414f", penwidth=1.2];',
        '  edge [color="#9aa3b5", fontname="Helvetica", fontsize=9, fontcolor="#b7c0d0"];',
    ]
    for name, dev in topo.devices.items():
        fill = _FILL.get(dev.kind, "#333a47")
        shape = "ellipse" if dev.kind == "router" else "box"
        hl = ', color="#1BA0D7", penwidth=3' if name == highlight_device else ""
        out.append(f'  "{name}" [label="{_node_label(dev)}", fillcolor="{fill}", shape={shape}{hl}];')
    for (a, ia), (b, ib) in topo.links:
        da = topo.devices[a].get_if(ia, create=False)
        db = topo.devices[b].get_if(ib, create=False)
        down = bool((da and da.shutdown) or (db and db.shutdown))
        style = ', color="#e06c6c", style=dashed' if down else ""
        out.append(f'  "{a}" -- "{b}" [taillabel="{_short(ia)}", headlabel="{_short(ib)}"{style}];')
    out.append("}")
    return "\n".join(out)
