"""A real drag-and-drop arrangement widget for the CompTIA performance tasks.

This is a self-contained Streamlit custom component (no build step / no npm — the
frontend is a single hand-written HTML file that speaks the Streamlit component
postMessage protocol). It renders HTML5 drag-and-drop for the three task kinds and
returns the learner's arrangement as a ``{row_key: choice}`` dict that
``PerfTask.grade`` understands. Callers keep a dropdown fallback for touch screens.
"""
from __future__ import annotations

import os
import random

import streamlit as st
import streamlit.components.v1 as components

_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend")
_impl = components.declare_component("certlab_dragdrop", path=_DIR)


def drag_arrange(task, *, accent: str = "#4D8DFF", key: str) -> dict | None:
    """Render the drag canvas for a PerfTask and return {row_key: choice} or None.

    Restores the board across reruns from session_state so a drop (which triggers a
    rerun) doesn't reset the learner's work.
    """
    rows = task.rows()
    payload = {"task_id": task.id, "kind": task.kind, "accent": accent}
    if task.kind == "categorize":
        payload["items"] = [label for _k, label, _ch, _c in rows]
        payload["zones"] = list(rows[0][2]) if rows else []
    elif task.kind == "match":
        payload["lefts"] = [label for _k, label, _ch, _c in rows]
        payload["rights"] = list(rows[0][2]) if rows else []
    elif task.kind == "order":
        steps = [correct for _k, _label, _ch, correct in rows]
        order = list(steps)
        random.Random(task.id).shuffle(order)          # stable initial shuffle
        payload["steps"] = order

    state_key = f"__dd_state_{key}"
    payload["initial"] = st.session_state.get(state_key)

    val = _impl(key=key, default=None, **payload)
    resp = val.get("response") if isinstance(val, dict) else None
    if resp is not None:
        st.session_state[state_key] = resp
    return resp
