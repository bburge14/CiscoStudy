"""Timed exam simulation: domain-weighted, with real testing-engine navigation
(move back and forth, flag questions, review everything before you submit), a
live countdown that auto-submits at zero, and a scored pass/fail report."""
from __future__ import annotations

import random
import time

import pandas as pd
import streamlit as st

from studyengine import (
    PASS_SCORE,
    build_exam,
    exam_time_limit,
    get_blueprint,
    score_session,
)
from ui_common import (
    get_bank,
    get_profile,
    init_exam_state,
    page_header,
    page_setup,
    render_quiz_review,
    run_exam,
    save_profile,
)

exam = page_setup("Exam Simulation")
bank = get_bank()
bp = get_blueprint(exam)
prof = get_profile(exam)
SKEY = f"exam_{exam}"
IDS = f"examids_{exam}"
PASS_PCT = int(PASS_SCORE * 100)


def _fmt(sec: int) -> str:
    sec = max(0, sec)
    return f"{sec // 60}:{sec % 60:02d}"


page_header("stopwatch", "Exam Simulation")

state = st.session_state.get(SKEY)


def _start(size: int) -> None:
    qs = build_exam(bank, bp, size=size, rng=random.Random())
    st.session_state[IDS] = [q.id for q in qs]
    init_exam_state(SKEY, deadline=time.time() + exam_time_limit(len(qs)))


# --- setup ------------------------------------------------------------------
if state is None:
    avail = len(bank.query(exam=exam))
    st.markdown(
        f"A timed, domain-weighted mock of **{bp.name}**. You can move back and forth, "
        f"**flag** questions, and **review everything before you submit** — like the real "
        f"testing engine. The clock keeps running and **auto-submits at zero**. Pass line "
        f"here is **{PASS_PCT}%** — a study proxy; the real cut score is scaled and unpublished.")
    choice = st.radio(
        "Length", ["Quick (20)", "Standard (40)", f"Full ({avail})"], index=1,
        help="Time is ~1.25 minutes per question, like the real pace.")
    size = {"Quick (20)": 20, "Standard (40)": 40, f"Full ({avail})": avail}[choice]
    size = min(size, avail)
    st.caption(f"{size} questions · {_fmt(exam_time_limit(size))} time limit · pass at {PASS_PCT}%")
    if st.button("Start exam", type="primary"):
        _start(size)
        st.rerun()
    st.stop()

ids = st.session_state.get(IDS, [])
phase, exam_state = run_exam(exam, SKEY, ids)

# --- in progress: run_exam rendered the question / review UI ----------------
if phase != "done":
    st.stop()

# --- submitted (or time expired): record once, then the report --------------
answers = exam_state["answers"]
if not exam_state.get("recorded"):
    for qid in ids:
        prof.record_study(bank.get(qid), bank.get(qid).check(answers.get(qid)))
    exam_state["recorded"] = True
    save_profile(exam)

attempts = [(qid, bank.get(qid).check(answers.get(qid))) for qid in ids]
score = score_session(attempts, bank)
elapsed = int(time.time() - exam_state.get("started_at", time.time()))
answered = sum(1 for qid in ids if answers.get(qid) not in (None, [], ""))

if score.accuracy >= PASS_SCORE:
    st.success(f"## PASS — {score.pct}%")
else:
    st.error(f"## Below the line — {score.pct}%  (need {PASS_PCT}%)")

m = st.columns(4)
m[0].metric("Score", f"{score.correct}/{score.total}")
m[1].metric("Percent", f"{score.pct}%")
m[2].metric("Answered", f"{answered}/{score.total}")
m[3].metric("Time used", _fmt(elapsed))

st.subheader("By domain")
rows = []
for d in bp.domains:
    ds = score.by_domain.get(d.key)
    corr, sn = (ds.correct, ds.seen) if ds else (0, 0)
    rows.append({"Domain": d.name, "Score": f"{corr}/{sn}" if sn else "—",
                 "Accuracy": f"{round(corr/sn*100)}%" if sn else "—",
                 "Exam weight": f"{round(d.weight*100)}%"})
st.dataframe(pd.DataFrame(rows), width="stretch", hide_index=True)

# Full question-by-question review, opt-in (a Full exam is 200+ questions, so
# don't render it all unless asked). Mirrors the milestone-exam review.
st.divider()
wrong = score.total - score.correct
st.markdown(f"**Review** — you missed **{wrong}** of {score.total}. See each one with the "
            "correct answer and why.")
if st.toggle("Show the question-by-question review", key=f"{SKEY}_review"):
    render_quiz_review(exam, ids, answers)

st.info("These answers were recorded, so your **Study Plan** and **Progress** readiness now "
        "reflect this attempt. A mock like this is a study gauge — it doesn't predict the exact "
        "exam.")
if st.button("Take another exam"):
    st.session_state.pop(SKEY, None)
    st.session_state.pop(IDS, None)
    st.rerun()
