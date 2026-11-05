"""Instructor view: see every account's progress on this instance.

Only the instructor account (the first account created on the instance) can see
the roster. Learner accounts get a polite notice instead.
"""
from __future__ import annotations

import time

import pandas as pd
import streamlit as st

from studyengine import get_blueprint
from ui_common import (
    EXAMS,
    current_user,
    is_instructor,
    load_user_profile,
    page_setup,
    roster_summary,
)

exam = page_setup("Instructor", icon="🧑‍🏫")
bp = get_blueprint(exam)

st.title("🧑‍🏫 Instructor View")

if not is_instructor(current_user()):
    st.warning("This page is for the **instructor** account on this instance.")
    st.info("The first account created on an instance becomes its instructor. If you set this "
            "up, sign in with that first account; otherwise this is your personal study view.")
    st.stop()

st.caption(f"Progress for every account on this instance · **{EXAMS[exam]}** track. "
           "Switch tracks in the sidebar.")

rows = roster_summary(exam)
learners = [r for r in rows if r["role"] != "instructor"]

# --- headline metrics -------------------------------------------------------
took_baseline = sum(1 for r in learners if r["baseline"] is not None)
active = [r for r in learners if r["answered"] > 0]
avg_acc = round(sum(r["accuracy"] for r in active) / len(active)) if active else None
c1, c2, c3, c4 = st.columns(4)
c1.metric("Learner accounts", len(learners))
c2.metric("Took the diagnostic", took_baseline)
c3.metric("Active (answered ≥1)", len(active))
c4.metric("Avg accuracy (active)", f"{avg_acc}%" if avg_acc is not None else "—")

st.divider()
st.subheader("Roster")

if not learners:
    st.info("No learner accounts yet. Have your airmen open the app and create an account — "
            "they'll appear here. (On a shared instance, run `run-shared.bat` and give them "
            "your PC's `http://<ip>:8501` address.)")
    st.stop()


def _last(ts: float) -> str:
    return "—" if not ts else time.strftime("%Y-%m-%d", time.localtime(ts))


table = [{
    "Learner": r["name"],
    "Baseline": f"{r['baseline']}%" if r["baseline"] is not None else "—",
    "Answered": r["answered"],
    "Accuracy": f"{r['accuracy']}%" if r["accuracy"] is not None else "—",
    "Milestones": r["milestones"],
    "Weak areas": ", ".join(s.replace("_", " ") for s in r["weak"]) or "—",
    "Last active": _last(r["last_seen"]),
} for r in learners]
st.dataframe(pd.DataFrame(table), width="stretch", hide_index=True)

# --- per-learner drill-down -------------------------------------------------
st.divider()
st.subheader("Inspect a learner")
by_slug = {r["slug"]: r for r in learners}
pick = st.selectbox("Learner", list(by_slug), format_func=lambda s: by_slug[s]["name"])
prof = load_user_profile(pick, exam)

seen, correct = prof.overall()
d1, d2, d3 = st.columns(3)
d1.metric("Answered", seen)
d2.metric("Accuracy", f"{round(correct/seen*100)}%" if seen else "—")
d3.metric("Baseline", f"{prof.baseline['overall']}%" if prof.baseline else "not taken")

dstats = prof.domain_stats()
dom_rows = []
for d in bp.domains:
    s, c, acc = dstats.get(d.key, (0, 0, 0.0))
    dom_rows.append({
        "Domain": d.name,
        "Answered": s,
        "Accuracy": f"{round(acc*100)}%" if s else "—",
        "Exam weight": f"{round(d.weight*100)}%",
    })
st.markdown("**By domain**")
st.dataframe(pd.DataFrame(dom_rows), width="stretch", hide_index=True)

weak = prof.weak_subtopics()
if weak:
    st.markdown("**Weak sub-topics (below 80%)**")
    st.dataframe(
        pd.DataFrame([{"Sub-topic": s.replace("_", " "), "Accuracy": f"{round(a*100)}%", "Attempts": n}
                      for s, a, n in weak]),
        width="stretch", hide_index=True,
    )
else:
    st.success("No sub-topics below 80% for this learner.")

st.caption("Read-only view. Progress is stored per account on this machine; learners can't see "
           "each other's. (Hiding this page from learners' sidebars would need a nav refactor — "
           "say the word if you want it.)")
