"""Endless Drill: infinite adaptive stream with instant grading + deep breakdowns."""
from __future__ import annotations

import streamlit as st

from studyengine import get_blueprint
from ui_common import (
    answer_widget,
    get_bank,
    get_profile,
    get_scheduler,
    grade_and_record,
    page_setup,
    render_feedback,
)

exam = page_setup("Endless Drill", icon="♾️")
bank = get_bank()
bp = get_blueprint(exam)
prof = get_profile(exam)
sched = get_scheduler(exam)
SKEY = f"drill_{exam}"

drill = st.session_state.setdefault(
    SKEY, {"qid": None, "phase": "answering", "fb": None,
           "recent": [], "seen": 0, "correct": 0, "streak": 0, "missed": []}
)

st.title("♾️ Endless Drill")

# --- controls ---------------------------------------------------------------
dom_keys = sched.domains_available()
cf, cr = st.columns([3, 1])
with cf:
    picked = st.multiselect(
        "Focus domains", options=dom_keys, format_func=lambda k: bp.domain(k).name,
        default=[], key=f"{SKEY}_domains",
        help="Leave empty to drill all domains (weighted like the real exam). "
             "Pick one or more to focus the stream on just those domains.",
    )
with cr:
    remediation = st.toggle("Remediation mode", value=False,
                            help="Draw only from sub-topics you score below 80% on.")

c1, c2, c3 = st.columns(3)
c1.metric("Answered (session)", drill["seen"])
acc = f"{round(drill['correct']/drill['seen']*100)}%" if drill["seen"] else "—"
c2.metric("Session accuracy", acc)
c3.metric("Streak", drill["streak"])

if remediation and not sched.remediation_available(prof):
    st.info("No weak sub-topics yet (need at least 3 attempts in a sub-topic scoring "
            "<80%). Showing the full adaptive stream instead.")
    remediation = False

# Changing the domain focus re-picks within the new scope immediately.
if drill.get("domains") != picked:
    drill["domains"] = picked
    drill["qid"] = None

if picked:
    names = ", ".join(bp.domain(k).name for k in picked)
    st.caption(f"Focused on **{names}**. Missed questions resurface more often until you master them.")
else:
    st.caption("All domains, weighted like the real exam. "
               "Missed questions automatically resurface more often until you master them.")
st.divider()

# --- pick a question if needed ---------------------------------------------
if drill["qid"] is None:
    nxt = sched.next(prof, recent_ids=drill["recent"], remediation=remediation,
                     domains=picked or None)
    drill["qid"] = nxt.id if nxt else None
    drill["phase"] = "answering"
    drill["fb"] = None

if drill["qid"] is None:
    st.warning("No questions available for this selection.")
    st.stop()

q = bank.get(drill["qid"])
st.caption(f"Domain: {bp.domain(q.domain).name}  ·  Sub-topic: {q.subtopic.replace('_', ' ')}  "
           f"·  Difficulty: {'●' * q.difficulty}{'○' * (3 - q.difficulty)}  ·  Box {prof.box_of(q.id)}/5")

# --- answering phase --------------------------------------------------------
if drill["phase"] == "answering":
    sel = answer_widget(q, key=f"{SKEY}_ans_{q.id}")
    if st.button("Submit", type="primary"):
        fb = grade_and_record(exam, q, sel)
        drill["fb"] = fb
        drill["phase"] = "feedback"
        drill["seen"] += 1
        if fb.correct:
            drill["correct"] += 1
            drill["streak"] = drill["streak"] + 1 if drill["streak"] >= 0 else 1
        else:
            drill["streak"] = drill["streak"] - 1 if drill["streak"] <= 0 else -1
            drill["missed"] = ([q.id] + [m for m in drill["missed"] if m != q.id])[:8]
        drill["recent"] = ([q.id] + drill["recent"])[:8]
        st.rerun()

# --- feedback phase ---------------------------------------------------------
else:
    render_feedback(q, drill["fb"])
    if st.button("Next question ▶", type="primary"):
        drill["qid"] = None
        st.rerun()

# --- recently missed --------------------------------------------------------
if drill["missed"]:
    st.divider()
    with st.expander("Recently missed (these are now weighted to reappear)"):
        for mid in drill["missed"]:
            mq = bank.get(mid)
            st.markdown(f"- `{mid}` — {mq.subtopic.replace('_', ' ')}: {mq.stem[:90]}…")
