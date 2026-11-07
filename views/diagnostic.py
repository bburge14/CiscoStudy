"""Diagnostic baseline: 5 questions per official domain → starting scorecard.

The size follows the blueprint — 6-domain tracks (CCNA/ENCOR) get 30, Security+/
Network+/A+ Core 1 (5 domains) get 25, A+ Core 2 (4 domains) gets 20.

Real-exam navigation: move back and forth freely, flag questions, and review the
whole set before you submit (see ``run_exam`` in ui_common)."""
from __future__ import annotations

import random
import time

import streamlit as st

from studyengine import build_baseline, get_blueprint, recommend_focus, score_session
from ui_common import (
    get_bank,
    get_profile,
    init_exam_state,
    page_header,
    page_setup,
    pct_bar,
    render_quiz_review,
    run_exam,
    save_profile,
)

exam = page_setup("Diagnostic Baseline")
bank = get_bank()
bp = get_blueprint(exam)
prof = get_profile(exam)
SKEY = f"dx_{exam}"
IDS = f"dxids_{exam}"
PER_DOMAIN = 5
N_DOMAINS = len(bp.domains)
BASE_N = N_DOMAINS * PER_DOMAIN

page_header("gauge", "Diagnostic Baseline")
st.caption(f"{bp.name} — {BASE_N} questions, {PER_DOMAIN} from each of the "
           f"{N_DOMAINS} official domains.")

state = st.session_state.get(SKEY)


def _start() -> None:
    qs = build_baseline(bank, bp, per_domain=PER_DOMAIN, rng=random.Random())
    st.session_state[IDS] = [q.id for q in qs]
    init_exam_state(SKEY)


# --- intro / not started ----------------------------------------------------
if state is None:
    if prof.baseline:
        st.info(f"Last baseline score: **{prof.baseline['overall']}%** "
                f"({time.strftime('%Y-%m-%d', time.localtime(prof.baseline.get('ts') or time.time()))}).")
    st.markdown(
        "This untimed snapshot maps your starting level across every domain and "
        "**auto-builds a remediation queue** for any domain/sub-topic under 80%. "
        "You can move back and forth, **flag** questions, and **review everything "
        "before submitting** — just like a real testing engine. Answer honestly: "
        "results feed the adaptive drill engine."
    )
    if st.button(f"Start {BASE_N}-question baseline", type="primary"):
        _start()
        st.rerun()
    st.stop()

ids = st.session_state.get(IDS, [])
phase, exam_state = run_exam(exam, SKEY, ids)

# --- in progress: run_exam rendered the question / review UI ----------------
if phase != "done":
    st.stop()

# --- submitted: record once, then show the scorecard ------------------------
answers = exam_state["answers"]
if not exam_state.get("recorded"):
    for qid in ids:
        q = bank.get(qid)
        ok = q.check(answers.get(qid))
        # Seed the adaptive scheduler/plan, but mark it a benchmark answer so it
        # is EXCLUDED from study metrics + XP.
        prof.record(q, ok)
        prof.note_baseline_answer(q, ok)
    total = len(ids)
    prof.baseline = {
        "overall": round(sum(1 for i in ids if bank.get(i).check(answers.get(i))) / total * 100),
        "total": total,
        "ts": time.time(),
    }
    exam_state["recorded"] = True
    save_profile(exam)

attempts = [(qid, bank.get(qid).check(answers.get(qid))) for qid in ids]
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

# Full question-by-question review (the baseline gives no feedback as you go).
st.divider()
if st.toggle("Review every question (your answer vs. the correct one)", key=f"{SKEY}_review"):
    render_quiz_review(exam, ids, answers)

if st.button("Retake baseline"):
    _start()
    st.rerun()
