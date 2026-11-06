"""CertWize home: a branded landing — current-track progress, quick-start cards,
and the multi-certification catalog (live tracks + coming-soon placeholders)."""
from __future__ import annotations

import html

import streamlit as st

from ui_common import (
    CERT_CATALOG,
    EXAMS,
    current_user,
    get_bank,
    get_profile,
    is_instructor,
    list_users,
    page_setup,
    render_level_card,
)

exam = page_setup("Home", icon="🛜")   # gates on login
bank = get_bank()
prof = get_profile(exam)
name = html.escape(list_users().get(current_user(), {}).get("name", "there"))

# --- hero -------------------------------------------------------------------
st.markdown(
    f"<div style='margin:0.2rem 0 0.1rem;font-size:1.9rem;font-weight:800;"
    f"letter-spacing:-0.02em'>Welcome back, {name}</div>"
    f"<div style='color:#9AA4B2;margin-bottom:0.4rem'>You're training for "
    f"<b style='color:#E8ECF4'>{EXAMS[exam]}</b> — everything you do saves automatically.</div>",
    unsafe_allow_html=True,
)

# --- rank + headline metrics ------------------------------------------------
render_level_card(prof)
seen, correct = prof.study_overall()
c1, c2, c3 = st.columns(3)
c1.metric("Questions answered", seen)
c2.metric("Lifetime accuracy", f"{round(correct / seen * 100)}%" if seen else "—")
c3.metric("Diagnostic", f"{prof.baseline['overall']}%" if prof.baseline else "not taken")

# --- smart next step --------------------------------------------------------
st.markdown("### Your next step")
if not prof.baseline:
    with st.container(border=True):
        st.markdown("**🎯 Start with the Diagnostic Baseline**")
        st.caption("30 questions (5 per domain) map your weak spots and build a personalized plan.")
        st.page_link("views/diagnostic.py", label="Take the diagnostic", icon=":material/fact_check:")
else:
    with st.container(border=True):
        weak = prof.weak_subtopics()
        if weak:
            names = ", ".join(s.replace("_", " ") for s, _, _ in weak[:3])
            st.markdown(f"**🧭 Continue your Study Plan** — next up: *{names}*")
        else:
            st.markdown("**🧭 Continue your Study Plan**")
        st.caption("Guided, weakest-first: read the lesson, drill it, unlock the next topic.")
        st.page_link("views/study_plan.py", label="Continue my plan", icon=":material/route:")

# --- practice-mode grid -----------------------------------------------------
st.markdown(f"### Jump into {EXAMS[exam].split()[0]} practice")
MODES = [
    ("views/study_plan.py", "🧭", "Study Plan", "Guided, weakest-first path"),
    ("views/drill.py", "♾️", "Endless Drill", "Adaptive practice that resurfaces misses"),
    ("views/milestones.py", "📚", "Lessons & Milestones", "Read, quiz, then a hands-on gate"),
    ("views/open_book.py", "📖", "Open-Book Practice", "Find answers in the book — scaled XP"),
    ("views/pbq_lab.py", "🖥️", "PBQ Lab", "Fix broken networks in a real IOS CLI"),
    ("views/exam_sim.py", "⏱️", "Exam Simulation", "Timed, domain-weighted mock exam"),
    ("views/progress.py", "📊", "Progress", "Mastery by domain + exam readiness"),
    ("views/diagnostic.py", "🎯", "Diagnostic", "Re-baseline your weak spots"),
]
for r in range(0, len(MODES), 2):
    cols = st.columns(2)
    for col, (link, icon, title, desc) in zip(cols, MODES[r:r + 2]):
        with col, st.container(border=True):
            st.markdown(
                f"<div style='font-weight:700'>{icon}&nbsp; {title}</div>"
                f"<div style='color:#9AA4B2;font-size:0.86rem;min-height:2.3em'>{desc}</div>",
                unsafe_allow_html=True)
            st.page_link(link, label="Open", icon=":material/arrow_forward:")

if is_instructor(current_user()):
    st.page_link("views/instructor.py", label="Instructor view — your learners' progress",
                 icon=":material/supervisor_account:")

# --- certification catalog --------------------------------------------------
st.divider()
st.markdown("### Explore certifications")
st.caption("CertWize is growing into a full IT-cert trainer. Live tracks are ready now; "
           "more are on the way.")


def _switch(key: str) -> None:
    st.session_state["exam"] = key
    st.session_state["exam_selector"] = key   # keep the sidebar picker in sync


for prov in CERT_CATALOG:
    st.markdown(f"<div style='margin-top:0.5rem;font-weight:700'>{prov['provider']}"
                f"<span style='color:#8A94A6;font-weight:400'> · {prov['blurb']}</span></div>",
                unsafe_allow_html=True)
    cols = st.columns(3)
    for i, cert in enumerate(prov["certs"]):
        with cols[i % 3], st.container(border=True):
            active = cert["status"] == "active"
            current = active and cert["key"] == exam
            badge = "✓ Current" if current else ("● Live" if active else "Coming soon")
            color = "#4D8DFF" if current else ("#3DD68C" if active else "#6B7280")
            st.markdown(
                f"<div style='font-weight:700'>{cert['name']}</div>"
                f"<div style='color:{color};font-size:0.74rem;font-weight:700;"
                f"text-transform:uppercase;letter-spacing:0.05em;margin:0.15rem 0 0.1rem'>{badge}</div>",
                unsafe_allow_html=True)
            if current:
                st.caption("You're training this now.")
            elif active:
                st.button("Switch to this track", key=f"sw_{cert['key']}",
                          on_click=_switch, args=(cert["key"],), width="stretch")
            else:
                st.button("Coming soon", key=f"soon_{cert['key']}", disabled=True, width="stretch")

with st.expander("New here? How CertWize works"):
    st.markdown(
        "- **🎯 Diagnostic** finds your weak spots (5 questions per official domain).\n"
        "- **🧭 Study Plan** walks those weak topics one at a time — read, drill, unlock the next.\n"
        "- **📚 Lessons & Milestones** teach each unit, then gate the next behind a hands-on task.\n"
        "- **♾️ Endless Drill** resurfaces what you miss; **🖥️ PBQ Lab** drops you into a real CLI.\n"
        "- Every answer explains **why the right answer is right and why the wrong ones are traps.**"
    )

st.caption(f"{EXAMS[exam]} · {len(bank.query(exam=exam))} questions in this track · "
           "switch tracks or log out from the sidebar.")
