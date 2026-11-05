"""Render a live topology as a Graphviz DOT string for the PBQ lab.

The diagram is generated from the actual scenario topology (devices, links,
interface config), so it is always accurate and updates as the learner changes
the configuration — no copyrighted exam images involved.
"""
from __future__ import annotations

import math

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


# --- hand-drawn SVG topology (router / switch / L3 glyphs) -------------------
def _esc(t: str) -> str:
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _arrow_h(cx: float, cy: float, half: float, color: str) -> str:
    x1, x2 = cx - half, cx + half
    return (f'<line x1="{x1:.0f}" y1="{cy:.0f}" x2="{x2:.0f}" y2="{cy:.0f}" stroke="{color}" stroke-width="2"/>'
            f'<polygon points="{x1:.0f},{cy:.0f} {x1+5:.0f},{cy-3:.0f} {x1+5:.0f},{cy+3:.0f}" fill="{color}"/>'
            f'<polygon points="{x2:.0f},{cy:.0f} {x2-5:.0f},{cy-3:.0f} {x2-5:.0f},{cy+3:.0f}" fill="{color}"/>')


def _arrow_v(cx: float, cy: float, half: float, color: str) -> str:
    y1, y2 = cy - half, cy + half
    return (f'<line x1="{cx:.0f}" y1="{y1:.0f}" x2="{cx:.0f}" y2="{y2:.0f}" stroke="{color}" stroke-width="2"/>'
            f'<polygon points="{cx:.0f},{y1:.0f} {cx-3:.0f},{y1+5:.0f} {cx+3:.0f},{y1+5:.0f}" fill="{color}"/>'
            f'<polygon points="{cx:.0f},{y2:.0f} {cx-3:.0f},{y2-5:.0f} {cx+3:.0f},{y2-5:.0f}" fill="{color}"/>')


def _icon_svg(dev, x: float, y: float) -> str:
    fill = _FILL.get(dev.kind, "#333a47")
    if dev.kind == "router":   # circle + routing arrows (the classic router glyph)
        return (f'<circle cx="{x:.0f}" cy="{y:.0f}" r="19" fill="{fill}" stroke="#cdd6e6" stroke-width="1.5"/>'
                + _arrow_h(x, y, 10, "#ffffff") + _arrow_v(x, y, 10, "#ffffff"))
    rect = f'<rect x="{x-24:.0f}" y="{y-16:.0f}" width="48" height="32" rx="5" fill="{fill}" stroke="#cdd6e6" stroke-width="1.5"/>'
    if dev.kind == "l3switch":  # switch body + routing arrows
        return rect + _arrow_h(x, y, 13, "#ffffff") + _arrow_v(x, y, 9, "#ffffff")
    ticks = "".join(f'<rect x="{x-16+i*12:.0f}" y="{y-16:.0f}" width="6" height="4" fill="#cdd6e6"/>' for i in range(3))
    return rect + ticks + _arrow_h(x, y + 3, 14, "#ffffff")


def _label_svg(dev, x: float, y: float) -> str:
    out = [f'<text x="{x:.0f}" y="{y+36:.0f}" fill="#E9EDF5" font-size="13" '
           f'font-weight="700" text-anchor="middle">{_esc(dev.hostname)}</text>']
    ln = y + 51
    shown = 0
    for name in sorted(dev.interfaces):
        if shown >= 2:
            break
        t = _iface_line(dev.interfaces[name])
        if t:
            out.append(f'<text x="{x:.0f}" y="{ln:.0f}" fill="#aeb6c6" font-size="10" '
                       f'text-anchor="middle">{_esc(t)}</text>')
            ln += 13
            shown += 1
    return "".join(out)


def _positions(n: int, cw: float, ch: float):
    cx, cy = cw / 2, ch / 2
    if n == 1:
        return [(cx, cy - 8)]
    if n == 2:
        return [(cx - 150, cy - 8), (cx + 150, cy - 8)]
    r = 120 + (n - 3) * 22
    return [(cx + r * math.cos(2 * math.pi * i / n - math.pi / 2),
             cy + r * math.sin(2 * math.pi * i / n - math.pi / 2)) for i in range(n)]


def topology_svg(topo: Topology, highlight_device: str | None = None) -> str:
    """A self-contained SVG topology with router/switch/L3 icons (render via st.html)."""
    devs = list(topo.devices.items())
    n = len(devs)
    if n <= 2:
        cw, ch = 620, 200
    else:
        r = 120 + (n - 3) * 22
        cw, ch = int(2 * r + 340), int(2 * r + 200)

    pos = {name: xy for (name, _), xy in zip(devs, _positions(n, cw, ch))}
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {cw} {ch}" '
             f'width="100%" style="max-width:{cw}px;height:auto">']

    for (a, ia), (b, ib) in topo.links:
        if a not in pos or b not in pos:
            continue
        (x1, y1), (x2, y2) = pos[a], pos[b]
        da = topo.devices[a].get_if(ia, create=False)
        db = topo.devices[b].get_if(ib, create=False)
        down = bool((da and da.shutdown) or (db and db.shutdown))
        col = "#e06c6c" if down else "#8b93a7"
        dash = ' stroke-dasharray="6 4"' if down else ""
        parts.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
                     f'stroke="{col}" stroke-width="2"{dash}/>')
        for frac, lab in ((0.27, _short(ia)), (0.73, _short(ib))):
            lx = x1 + (x2 - x1) * frac
            ly = y1 + (y2 - y1) * frac
            parts.append(f'<text x="{lx:.0f}" y="{ly-4:.0f}" fill="#b7c0d0" font-size="10" '
                         f'text-anchor="middle">{_esc(lab)}</text>')

    for name, dev in devs:
        x, y = pos[name]
        if name == highlight_device:
            parts.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="none" '
                         f'stroke="#1BA0D7" stroke-width="2.5"/>')
        parts.append(_icon_svg(dev, x, y))
        parts.append(_label_svg(dev, x, y))

    parts.append("</svg>")
    return "".join(parts)
