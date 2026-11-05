"""CiscoStudy — a custom CCNA 200-301 & CCNP ENCOR 350-401 study platform.

This is the app entry point / router. It renders the login gate, the account
menu and the sidebar chrome once, then hands off to the selected page via
Streamlit's native multipage navigation.

Run locally with:  streamlit run Home.py
"""
from __future__ import annotations

import streamlit as st

from ui_common import (
    current_user,
    ensure_login,
    is_instructor,
    render_account_bar,
    render_sidebar_chrome,
)

st.set_page_config(page_title="CiscoStudy", page_icon="🛜", layout="wide")

# Login gate: renders the sign-in screen and stops if not authenticated.
if not ensure_login():
    st.stop()

pages = [
    st.Page("views/home.py", title="Home", icon=":material/home:", default=True),
    st.Page("views/diagnostic.py", title="Diagnostic Baseline", icon=":material/fact_check:"),
    st.Page("views/study_plan.py", title="My Study Plan", icon=":material/route:"),
    st.Page("views/drill.py", title="Endless Drill", icon=":material/all_inclusive:"),
    st.Page("views/exam_sim.py", title="Exam Simulation", icon=":material/timer:"),
    st.Page("views/milestones.py", title="Lessons & Milestones", icon=":material/menu_book:"),
    st.Page("views/pbq_lab.py", title="PBQ Lab", icon=":material/terminal:"),
    st.Page("views/progress.py", title="Progress", icon=":material/bar_chart:"),
]
if is_instructor(current_user()):
    pages.append(
        st.Page("views/instructor.py", title="Instructor", icon=":material/supervisor_account:")
    )

# Register the pages first: st.page_link (used by the account bar) can only
# target pages already passed to st.navigation.
nav = st.navigation(pages)
render_account_bar()
render_sidebar_chrome()
nav.run()
