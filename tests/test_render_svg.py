"""Regression guard for PBQ topology rendering.

The topology SVG must reach the browser wrapped in a base64 data-URI <img>, not
as raw <svg> markup: Streamlit's HTML sanitizer strips raw <svg>, which made the
diagram silently vanish (no exception, just a blank gap). These tests lock in the
data-URI wrapper so that regression can't come back unnoticed.
"""
import base64

import ui_common
from studyengine.cli_sim import SCENARIOS, topology_svg


def test_svg_img_tag_is_sanitizer_safe_data_uri():
    svg = '<svg xmlns="http://www.w3.org/2000/svg"><circle cx="5" cy="5" r="4"/></svg>'
    tag = ui_common._svg_img_tag(svg)
    assert tag.startswith("<img ")
    assert "data:image/svg+xml;base64," in tag
    # The raw <svg> must NOT appear as live markup (only inside the base64 blob),
    # otherwise the sanitizer would strip it.
    assert "<svg" not in tag
    assert "<circle" not in tag


def test_svg_img_tag_round_trips_exact_svg():
    for sid, scen in SCENARIOS.items():
        svg = topology_svg(scen.build(), scen.device)
        tag = ui_common._svg_img_tag(svg)
        b64 = tag.split("base64,", 1)[1].split('"', 1)[0]
        assert base64.b64decode(b64).decode("utf-8") == svg, f"{sid}: data URI must preserve the SVG"


def test_svg_img_tag_respects_max_width():
    tag = ui_common._svg_img_tag("<svg/>", max_width=480)
    assert "max-width:480px" in tag
