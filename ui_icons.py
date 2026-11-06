"""Original, network/enterprise-themed glyph set for CertWize.

Streamlit's native sidebar nav only accepts Material symbols or emoji, which is
why the default build looks generic. These are hand-authored monochrome SVG
glyphs (24x24) drawn in a consistent technical style. Each works two ways:

* as a CSS **mask** on the sidebar nav links (alpha only — paints in the theme
  text color so active/hover states keep working), and
* as a colored **<img>** in page headers.

They are original artwork using generic industry conventions (a router puck, a
switch, a shield, a terminal), not any vendor's trademarked logo art.
"""
from __future__ import annotations

import base64

# Each glyph is the inner markup of a 24x24 viewBox. The literal token ``CC`` is
# the stroke/fill color, substituted per use. Shapes are opaque so the glyph
# doubles as a CSS mask.
_GLYPHS: dict[str, str] = {
    # app sections ----------------------------------------------------------
    "home": (
        '<path d="M3.5 11.5 12 4l8.5 7.5" stroke="CC" stroke-width="2" fill="none" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M5.5 10.5V20h13v-9.5" stroke="CC" stroke-width="2" fill="none" '
        'stroke-linejoin="round"/>'
        '<path d="M10 20v-4.5h4V20" stroke="CC" stroke-width="2" fill="none" '
        'stroke-linejoin="round"/>'
    ),
    "gauge": (  # diagnostic baseline = a measurement dial
        '<path d="M4 16.5a8 8 0 0 1 16 0" stroke="CC" stroke-width="2" fill="none" '
        'stroke-linecap="round"/>'
        '<path d="M12 16.5 16 11" stroke="CC" stroke-width="2" fill="none" stroke-linecap="round"/>'
        '<circle cx="12" cy="16.5" r="1.7" fill="CC"/>'
        '<path d="M4 16.5h1.6M18.4 16.5H20M12 8.6v1.4" stroke="CC" stroke-width="2" '
        'stroke-linecap="round"/>'
    ),
    "route": (  # study plan = a mapped route with endpoints
        '<path d="M6.5 5h5.5a3.5 3.5 0 0 1 0 7H9a3.5 3.5 0 0 0 0 7h8.5" stroke="CC" '
        'stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
        '<circle cx="6.5" cy="5" r="2.3" fill="CC"/>'
        '<circle cx="17.5" cy="19" r="2.3" fill="CC"/>'
    ),
    "cycle": (  # endless drill = an adaptive repeat loop
        '<path d="M20 12a8 8 0 1 1-2.4-5.7" stroke="CC" stroke-width="2" fill="none" '
        'stroke-linecap="round"/>'
        '<path d="M20.5 4.5V9h-4.5" stroke="CC" stroke-width="2" fill="none" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
    ),
    "stopwatch": (  # timed exam
        '<circle cx="12" cy="14" r="7" stroke="CC" stroke-width="2" fill="none"/>'
        '<path d="M12 14V9.8" stroke="CC" stroke-width="2" stroke-linecap="round"/>'
        '<path d="M10 3.2h4M12 3.2v3.6" stroke="CC" stroke-width="2" stroke-linecap="round"/>'
        '<path d="M18.6 7.6 20 6.2" stroke="CC" stroke-width="2" stroke-linecap="round"/>'
    ),
    "book": (  # lessons & milestones
        '<path d="M12 6.2C10 4.9 7.5 4.2 4 4.2v13c3.5 0 6 .7 8 2 2-1.3 4.5-2 8-2v-13'
        'c-3.5 0-6 .7-8 2Z" stroke="CC" stroke-width="2" fill="none" stroke-linejoin="round"/>'
        '<path d="M12 6.2v13" stroke="CC" stroke-width="2"/>'
    ),
    "book_search": (  # open-book review = a book + magnifier
        '<path d="M11 6.4C9.3 5.2 7.1 4.6 4 4.6v11.8c3.1 0 5.3.6 7 1.8" stroke="CC" '
        'stroke-width="2" fill="none" stroke-linejoin="round"/>'
        '<path d="M11 6.4v11.8" stroke="CC" stroke-width="2"/>'
        '<path d="M11 6.4C11.9 5.8 12.9 5.4 14 5.1" stroke="CC" stroke-width="2" '
        'fill="none" stroke-linecap="round"/>'
        '<circle cx="17" cy="14.2" r="3.3" stroke="CC" stroke-width="2" fill="none"/>'
        '<path d="M19.5 16.7 21.6 18.8" stroke="CC" stroke-width="2" stroke-linecap="round"/>'
    ),
    "terminal": (  # PBQ lab = IOS CLI
        '<rect x="3" y="5" width="18" height="14" rx="2.2" stroke="CC" stroke-width="2" fill="none"/>'
        '<path d="M7 10l3.2 2.6L7 15.2M12.6 15.4H16.5" stroke="CC" stroke-width="2" '
        'fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    ),
    "bars": (  # progress
        '<rect x="4" y="12" width="3.4" height="8" rx="1" fill="CC"/>'
        '<rect x="10.3" y="5" width="3.4" height="15" rx="1" fill="CC"/>'
        '<rect x="16.6" y="14.5" width="3.4" height="5.5" rx="1" fill="CC"/>'
    ),
    "user_gear": (  # my account
        '<circle cx="10" cy="8" r="3.4" stroke="CC" stroke-width="2" fill="none"/>'
        '<path d="M3.8 20c0-3.4 2.8-6 6.2-6 1 0 2 .25 2.9.7" stroke="CC" stroke-width="2" '
        'fill="none" stroke-linecap="round"/>'
        '<circle cx="17.6" cy="17.6" r="2.2" fill="CC"/>'
        '<path d="M17.6 14.1v1.1M17.6 21.1v-1.1M21.1 17.6h-1.1M14.1 17.6h1.1" '
        'stroke="CC" stroke-width="1.5" stroke-linecap="round"/>'
    ),
    "people": (  # instructor = oversees a group
        '<circle cx="9" cy="8" r="3.2" stroke="CC" stroke-width="2" fill="none"/>'
        '<path d="M3.6 20c0-3 2.4-5.4 5.4-5.4s5.4 2.4 5.4 5.4" stroke="CC" stroke-width="2" '
        'fill="none" stroke-linecap="round"/>'
        '<path d="M16.2 5.3a3.1 3.1 0 0 1 0 5.9M17.8 14.9c2 .7 3.5 2.6 3.5 4.9" '
        'stroke="CC" stroke-width="2" fill="none" stroke-linecap="round"/>'
    ),
    # device glyphs (available for headers / future use) --------------------
    "router": (
        '<ellipse cx="12" cy="15.5" rx="9" ry="4" stroke="CC" stroke-width="2" fill="none"/>'
        '<path d="M12 11.5V4M12 4 9.6 6.4M12 4l2.4 2.4M6 13.8 3.6 15.6 6 17.4'
        'M18 13.8l2.4 1.8-2.4 1.8" stroke="CC" stroke-width="2" fill="none" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
    ),
    "switch": (
        '<rect x="3" y="8.5" width="18" height="7.5" rx="1.6" stroke="CC" stroke-width="2" fill="none"/>'
        '<path d="M7 8.5V5.5M12 8.5V5.5M17 8.5V5.5" stroke="CC" stroke-width="2" stroke-linecap="round"/>'
        '<path d="M8.5 12.3h7M12.6 12.3l1.6-1.4M12.6 12.3l1.6 1.4" stroke="CC" stroke-width="1.8" '
        'fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    ),
    "shield": (
        '<path d="M12 3.2 19 6v5c0 4.4-3 7.7-7 8.9-4-1.2-7-4.5-7-8.9V6l7-2.8Z" stroke="CC" '
        'stroke-width="2" fill="none" stroke-linejoin="round"/>'
        '<path d="M9 11.8 11 14l4-4.2" stroke="CC" stroke-width="2" fill="none" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
    ),
}

# Sidebar-nav + page-link href suffix -> glyph key.
NAV_GLYPHS: dict[str, str] = {
    "/": "home",
    "diagnostic": "gauge",
    "study_plan": "route",
    "drill": "cycle",
    "exam_sim": "stopwatch",
    "milestones": "book",
    "open_book": "book_search",
    "pbq_lab": "terminal",
    "progress": "bars",
    "account": "user_gear",
    "instructor": "people",
}

BRAND = "#4D8DFF"  # CertWize blue — header icons + highlights (matches theme primaryColor)


def svg(key: str, color: str = "#000000") -> str:
    inner = _GLYPHS[key].replace("CC", color)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
            f'fill="none">{inner}</svg>')


def data_uri(key: str, color: str = "#000000") -> str:
    b64 = base64.b64encode(svg(key, color).encode("utf-8")).decode("ascii")
    return f"data:image/svg+xml;base64,{b64}"


def nav_css() -> str:
    """A <style> block that swaps every Material nav glyph for a custom mask.

    Targets both the sidebar nav links and in-page st.page_link icons by their
    href suffix, so the same custom icon shows everywhere a section is linked."""
    rules = [
        # Give masked icons a consistent box.
        '[data-testid="stSidebarNav"] a span[data-testid="stIconMaterial"],'
        '[data-testid="stPageLink"] a span[data-testid="stIconMaterial"]{'
        'width:1.5rem;height:1.5rem;}'
    ]
    for suffix, key in NAV_GLYPHS.items():
        uri = data_uri(key)  # color irrelevant: used as a mask (alpha only)
        sel = (f'[data-testid="stSidebarNav"] a[href$="{suffix}"] span[data-testid="stIconMaterial"],'
               f'[data-testid="stPageLink"] a[href$="{suffix}"] span[data-testid="stIconMaterial"]')
        rules.append(
            f'{sel}{{font-size:0 !important;display:inline-block;'
            f'background-color:currentColor;'
            f'-webkit-mask:url("{uri}") no-repeat center / contain;'
            f'mask:url("{uri}") no-repeat center / contain;}}'
        )
    return "<style>\n" + "\n".join(rules) + "\n</style>"


def header_html(key: str, title: str, color: str = BRAND) -> str:
    """A page-title row: a colored custom glyph beside a large heading."""
    uri = data_uri(key, color)
    safe = (title.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    return (
        '<div style="display:flex;align-items:center;gap:0.6rem;margin:0.1rem 0 0.7rem">'
        f'<img src="{uri}" width="38" height="38" alt="" style="flex:none"/>'
        f'<span style="font-size:2.1rem;font-weight:700;line-height:1.15">{safe}</span>'
        '</div>'
    )
