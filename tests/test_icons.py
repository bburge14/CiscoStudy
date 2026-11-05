"""Custom nav/header glyph set: mapping completeness + safe rendering."""
import base64

import ui_icons


def test_every_nav_glyph_exists():
    for suffix, key in ui_icons.NAV_GLYPHS.items():
        assert key in ui_icons._GLYPHS, f"{suffix} -> missing glyph {key!r}"


def test_data_uri_decodes_to_valid_svg_with_color_substituted():
    for key in ui_icons._GLYPHS:
        uri = ui_icons.data_uri(key, "#123456")
        assert uri.startswith("data:image/svg+xml;base64,")
        raw = base64.b64decode(uri.split(",", 1)[1]).decode("utf-8")
        assert raw.startswith("<svg") and raw.rstrip().endswith("</svg>")
        assert "#123456" in raw              # color token substituted
        assert '="CC"' not in raw            # no leftover placeholder


def test_nav_css_is_a_style_block_covering_every_section():
    css = ui_icons.nav_css()
    s = css.strip()
    assert s.startswith("<style>") and s.endswith("</style>")
    for suffix in ui_icons.NAV_GLYPHS:
        assert f'href$="{suffix}"' in css, f"nav css missing {suffix}"
    # masks both the sidebar nav and in-page page-links
    assert "stSidebarNav" in css and "stPageLink" in css


def test_header_html_escapes_title_and_embeds_icon():
    html = ui_icons.header_html("home", "A & B <x>")
    assert "A &amp; B &lt;x&gt;" in html
    assert "<img" in html and "data:image/svg+xml;base64," in html
