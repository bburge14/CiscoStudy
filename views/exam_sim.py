"""Timed exam simulation: domain-weighted, one question at a time (no going
back, like the real CCNA), a countdown, and a scored pass/fail report."""
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
from ui_common import answer_widget, get_bank, get_profile, page_header, page_setup, save_profile

exam = page_setup("Exam Simulation", icon="📝")
bank = get_bank()
bp = get_blueprint(exam)
prof = get_profile(exam)
SKEY = f"exam_{exam}"
PASS_PCT = int(PASS_SCORE * 100)

page_header("stopwatch", "Exam Simulation")

state = st.session_state.get(SKEY)


def _start(size: int) -> None:
    qs = build_exam(bank, bp, size=size, rng=random.Random())
    limit = exam_time_limit(len(qs))
    st.session_state[SKEY] = {
        "ids": [q.id for q in qs], "idx": 0, "answers": {}, "phase": "running",
        "start": time.time(), "deadline": time.time() + limit, "limit": limit,
        "summary": None,
    }


def _finalize(state: dict) -> None:
    attempts = []
    for qid in state["ids"]:
        q = bank.get(qid)
        ok = q.check(state["answers"].get(qid))
        attempts.append((qid, ok))
        prof.record(q, ok)
    save_profile(exam)
    score = score_session(attempts, bank)
    state["summary"] = {
        "pct": score.pct, "correct": score.correct, "total": score.total,
        "passed": score.accuracy >= PASS_SCORE,
        "by_domain": {k: (v.correct, v.seen) for k, v in score.by_domain.items()},
        "elapsed": int(time.time() - state["start"]),
        "answered": sum(1 for i in state["ids"] if state["answers"].get(i) not in (None, [], "")),
    }
    state["phase"] = "done"


def _fmt(sec: int) -> str:
    sec = max(0, sec)
    return f"{sec // 60}:{sec % 60:02d}"


@st.fragment(run_every=1)
def _timer(state: dict) -> None:
    """Native, self-refreshing countdown (ticks every second, auto-ends at 0)."""
    remaining = int(state["deadline"] - time.time())
    color = "#e06c6c" if remaining < 120 else "#E6EAF1"
    st.markdown(
        f"<div style='text-align:right;font-size:20px;font-weight:700;color:{color}'>"
        f"⏱ {_fmt(remaining)}</div>", unsafe_allow_html=True)
    if remaining <= 0 and state.get("phase") == "running":
        _finalize(state)
        st.rerun()


# --- setup ------------------------------------------------------------------
if state is None:
    avail = len(bank.query(exam=exam))
    st.markdown(
        f"A timed, domain-weighted mock of **{bp.name}**. Questions come one at a time and you "
        f"**can't go back** (like the real exam). Pass line here is **{PASS_PCT}%** — a study "
        "proxy; Cisco's real cut score is scaled and unpublished.")
    choice = st.radio(
        "Length", ["Quick (20)", f"Standard (40)", f"Full ({avail})"], index=1,
        help="Time is ~1.25 minutes per question, like the real pace.")
    size = {"Quick (20)": 20, "Standard (40)": 40, f"Full ({avail})": avail}[choice]
    size = min(size, avail)
    st.caption(f"{size} questions · {_fmt(exam_time_limit(size))} time limit · pass at {PASS_PCT}%")
    if st.button("Start exam", type="primary"):
        _start(size)
        st.rerun()
    st.stop()

# --- running ----------------------------------------------------------------
if state["phase"] == "running":
    remaining = int(state["deadline"] - time.time())
    if remaining <= 0:
        _finalize(state)
        st.rerun()

    total = len(state["ids"])
    idx = state["idx"]
    top = st.columns([3, 1])
    top[0].progress(idx / total, text=f"Question {idx + 1} of {total}")
    with top[1]:
        _timer(state)   # live countdown; auto-ends at zero

    q = bank.get(state["ids"][idx])
    st.caption(f"{bp.domain(q.domain).name}")
    sel = answer_widget(q, key=f"{SKEY}_ans_{idx}")

    c = st.columns([1, 1, 4])
    last = idx == total - 1
    if c[0].button("Finish" if last else "Submit & next ▶", type="primary"):
        state["answers"][q.id] = sel
        if last or int(state["deadline"] - time.time()) <= 0:
            _finalize(state)
        else:
            state["idx"] += 1
        st.rerun()
    if c[1].button("End exam now"):
        state["answers"][q.id] = sel
        _finalize(state)
        st.rerun()
    st.caption("No going back once you move on — just like the real exam.")
    st.stop()

# --- done -------------------------------------------------------------------
s = state["summary"]
if s["passed"]:
    st.success(f"## ✅ PASS — {s['pct']}%")
else:
    st.error(f"## ❌ Below the line — {s['pct']}%  (need {PASS_PCT}%)")

m = st.columns(4)
m[0].metric("Score", f"{s['correct']}/{s['total']}")
m[1].metric("Percent", f"{s['pct']}%")
m[2].metric("Answered", f"{s['answered']}/{s['total']}")
m[3].metric("Time used", _fmt(s["elapsed"]))

st.subheader("By domain")
rows = []
for d in bp.domains:
    corr, sn = s["by_domain"].get(d.key, (0, 0))
    rows.append({"Domain": d.name, "Score": f"{corr}/{sn}" if sn else "—",
                 "Accuracy": f"{round(corr/sn*100)}%" if sn else "—",
                 "Exam weight": f"{round(d.weight*100)}%"})
st.dataframe(pd.DataFrame(rows), width="stretch", hide_index=True)

st.info("These answers were recorded, so your **Study Plan** and **Progress** readiness now "
        "reflect this attempt. A mock like this is a study gauge — it doesn't predict the exact "
        "exam.")
if st.button("Take another exam"):
    st.session_state.pop(SKEY, None)
    st.rerun()
