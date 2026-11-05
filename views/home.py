"""CiscoStudy — a custom CCNA 200-301 & CCNP ENCOR 350-401 study platform.

Run locally with:  streamlit run Home.py
"""
from __future__ import annotations

import streamlit as st

from studyengine import get_blueprint
from ui_common import (
    EXAMS,
    current_user,
    get_bank,
    get_profile,
    is_instructor,
    list_users,
    page_header,
    page_setup,
)

exam = page_setup("Home", icon="🛜")   # gates on login
bank = get_bank()
bp = get_blueprint(exam)
prof = get_profile(exam)
name = list_users().get(current_user(), {}).get("name", "there")

page_header("home", f"Welcome, {name}")
st.markdown(f"Your study tool for **{EXAMS[exam]}**. Pick where to start — everything you do "
            "saves to your account automatically.")

seen, correct = prof.overall()
c1, c2, c3 = st.columns(3)
c1.metric("Questions answered", seen)
c2.metric("Lifetime accuracy", f"{round(correct / seen * 100)}%" if seen else "—")
c3.metric("Diagnostic", f"{prof.baseline['overall']}%" if prof.baseline else "not taken")

st.divider()
st.subheader("Where do you want to start?")

if not prof.baseline:
    st.markdown("**New here? Start with the diagnostic** — 30 questions (5 per domain) that map "
                "your weak spots and build your personalized study plan.")
    st.page_link("views/diagnostic.py",
                 label="Take the Diagnostic Baseline  (recommended first)", icon=":material/fact_check:")
else:
    weak = prof.weak_subtopics()
    if weak:
        names = ", ".join(s.replace("_", " ") for s, _, _ in weak[:3])
        st.markdown(f"Pick up your **personalized plan** — next up: *{names}*.")
    st.page_link("views/study_plan.py", label="Continue my Study Plan", icon=":material/route:")

st.markdown("#### …or jump straight into anything:")
colA, colB = st.columns(2)
with colA:
    st.page_link("views/study_plan.py", label="My Study Plan — guided, weakest-first", icon=":material/route:")
    st.page_link("views/drill.py", label="Endless Drill — adaptive practice", icon=":material/all_inclusive:")
    st.page_link("views/progress.py", label="Progress Dashboard", icon=":material/bar_chart:")
with colB:
    st.page_link("views/milestones.py", label="Lessons & Milestones — read then test", icon=":material/menu_book:")
    st.page_link("views/pbq_lab.py", label="PBQ Lab — hands-on Cisco CLI", icon=":material/terminal:")
    st.page_link("views/exam_sim.py", label="Exam Simulation — timed mock test", icon=":material/timer:")
    st.page_link("views/diagnostic.py", label="Diagnostic Baseline", icon=":material/fact_check:")

if is_instructor(current_user()):
    st.info("🧑‍🏫 You're the **instructor** on this instance.")
    st.page_link("views/instructor.py", label="Instructor view — see your learners' progress", icon=":material/supervisor_account:")

st.divider()
st.subheader("How it works")
st.markdown(
    "- **🎯 Diagnostic Baseline** finds your weak spots (5 questions per official domain).\n"
    "- **🧭 My Study Plan** then walks you through those weak topics one at a time — read the "
    "lesson, drill it until you've got it, and the next topic unlocks.\n"
    "- **📚 Lessons & Milestones** teach each unit in plain language, then test you and gate the "
    "next unit behind a hands-on task.\n"
    "- **♾️ Endless Drill** is open practice that resurfaces what you miss; **🖥️ PBQ Lab** drops "
    "you into a real Cisco IOS command line to fix broken networks.\n"
    "- Every answer explains **why the right answer is right and why the wrong ones are traps.**"
)
st.caption(f"{EXAMS[exam]} · {len(bank.query(exam=exam))} questions in this track. "
           "Switch tracks or log out from the sidebar.")
