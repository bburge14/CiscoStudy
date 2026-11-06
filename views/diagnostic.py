"""Diagnostic baseline: 30 questions (5 per official domain) → starting scorecard."""
from __future__ import annotations

import random
import time

import streamlit as st

from studyengine import build_baseline, get_blueprint, recommend_focus, score_session
from ui_common import (
    answer_widget,
    get_bank,
    get_profile,
    page_header,
    page_setup,
    pct_bar,
    save_profile,
)

exam = page_setup("Diagnostic Baseline")
bank = get_bank()
bp = get_blueprint(exam)
prof = get_profile(exam)
SKEY = f"dx_{exam}"

page_header("gauge", "Diagnostic Baseline")
st.caption(f"{bp.name} — 30 questions, 5 from each of the 6 official domains.")

state = st.session_state.get(SKEY)


def _start():
    qs = build_baseline(bank, bp, per_domain=5, rng=random.Random())
    st.session_state[SKEY] = {"ids": [q.id for q in qs], "idx": 0, "answers": {}, "done": False}


# --- intro / not started ----------------------------------------------------
if state is None:
    if prof.baseline:
        st.info(f"Last baseline score: **{prof.baseline['overall']}%** "
                f"({time.strftime('%Y-%m-%d', time.localtime(prof.baseline.get('ts') or time.time()))}).")
    st.markdown(
        "This untimed snapshot maps your starting level across every domain and "
        "**auto-builds a remediation queue** for any domain/sub-topic under 80%. "
        "Answer honestly — results feed the adaptive drill engine."
    )
    if st.button("Start 30-question baseline", type="primary"):
        _start()
        st.rerun()
    st.stop()

# --- results ----------------------------------------------------------------
if state["done"]:
    attempts = []
    for qid in state["ids"]:
        q = bank.get(qid)
        sel = state["answers"].get(qid)
        attempts.append((qid, q.check(sel)))
    score = score_session(attempts, bank)

    st.subheader(f"Result: {score.correct}/{score.total}  ·  {score.pct}%")
    verdict = "on track" if score.passed(0.8) else "needs focused study"
    st.progress(score.accuracy, text=f"Overall {score.pct}% — {verdict}")

    rows, chart = [], {}
    for d in bp.domains:
        ds = score.by_domain.get(d.key)
        pct = ds.pct if ds else 0
        chart[d.name] = pct
        rows.append({"Domain": d.name, "Score": f"{ds.correct}/{ds.seen}" if ds else "0/0",
                     "Accuracy": f"{pct}%", "Exam weight": f"{round(d.weight*100)}%"})
    pct_bar(chart)
    st.dataframe(rows, width="stretch", hide_index=True)

    recs = recommend_focus(score, bp, threshold=0.8)
    if recs:
        st.warning("**Focus here first** (weakest, weighted by exam impact): "
                   + ", ".join(f"{r.name} ({r.pct}%)" for r in recs))
    else:
        st.success("Every domain ≥ 80% — strong baseline! Keep drilling to retain it.")

    weak = prof.weak_subtopics()
    if weak:
        st.markdown("**Remediation queue (sub-topics < 80%)** — target these in Endless Drill:")
        st.dataframe(
            [{"Sub-topic": s.replace("_", " "), "Accuracy": f"{round(a*100)}%", "Seen": n}
             for s, a, n in weak],
            width="stretch", hide_index=True,
        )

    if st.button("Retake baseline"):
        _start()
        st.rerun()
    st.stop()

# --- in progress ------------------------------------------------------------
idx = state["idx"]
total = len(state["ids"])
q = bank.get(state["ids"][idx])
st.progress((idx) / total, text=f"Question {idx + 1} of {total}")
st.caption(f"Domain: {bp.domain(q.domain).name}")

sel = answer_widget(q, key=f"{SKEY}_ans_{idx}")

col1, col2 = st.columns([1, 5])
with col1:
    last = idx == total - 1
    if st.button("Finish" if last else "Next", type="primary"):
        state["answers"][q.id] = sel
        # Record into the adaptive profile to seed the scheduler/plan, but mark
        # it as a benchmark answer so it is EXCLUDED from study metrics + XP.
        _correct = q.check(sel)
        prof.record(q, _correct)
        prof.note_baseline_answer(q, _correct)
        save_profile(exam)
        if last:
            state["done"] = True
            prof.baseline = {
                "overall": round(
                    sum(1 for i in state["ids"] if bank.get(i).check(state["answers"].get(i)))
                    / total * 100),
                "total": total,
                "ts": time.time(),
            }
            save_profile(exam)
        else:
            state["idx"] += 1
        st.rerun()
with col2:
    if sel in (None, [], ""):
        st.caption("No selection yet — you may skip (counts as incorrect).")
