"""Shared Streamlit helpers: data loading, profile persistence, question rendering.

Kept UI-only; all study logic lives in the `studyengine` package so it stays
testable without Streamlit.
"""
from __future__ import annotations

import os
import random
import sys
from pathlib import Path

import streamlit as st

from studyengine import (
    DrillScheduler,
    Feedback,
    get_blueprint,
    grade,
    load_bank,
    load_curriculum,
    score_session,
)
from studyengine.cli_sim import Console
from studyengine.models import Question
from studyengine.progress import BOX_WEIGHT, Profile

ROOT = Path(__file__).resolve().parent
if getattr(sys, "frozen", False):
    # Packaged .exe: the bundle is extracted to a temp dir that is wiped on
    # exit, so keep learner progress in a stable, writable per-user folder.
    USERDATA = Path(os.environ.get("CISCOSTUDY_DATA") or (Path.home() / ".ciscostudy"))
else:
    USERDATA = ROOT / ".userdata"
EXAMS = {"ccna": "CCNA 200-301", "encor": "CCNP ENCOR 350-401"}
PASS_THRESHOLD = 0.8


# --- cached immutable resources --------------------------------------------
@st.cache_resource
def get_bank():
    return load_bank()


@st.cache_resource
def get_curriculum():
    return load_curriculum()


# --- profile persistence ----------------------------------------------------
def _profile_path(exam: str) -> Path:
    return USERDATA / f"profile_{exam}.json"


def get_profile(exam: str) -> Profile:
    key = f"profile_{exam}"
    if key not in st.session_state:
        st.session_state[key] = Profile.load(_profile_path(exam), exam)
    return st.session_state[key]


def save_profile(exam: str) -> None:
    prof = st.session_state.get(f"profile_{exam}")
    if prof is not None:
        prof.save(_profile_path(exam))


def reset_profile(exam: str) -> None:
    st.session_state[f"profile_{exam}"] = Profile(exam=exam)
    p = _profile_path(exam)
    if p.exists():
        p.unlink()


# --- shared page chrome -----------------------------------------------------
def page_setup(title: str, icon: str = "🛜") -> str:
    st.set_page_config(page_title=f"CiscoStudy · {title}", page_icon=icon, layout="wide")
    if "exam" not in st.session_state:
        st.session_state["exam"] = "ccna"
    with st.sidebar:
        st.markdown("### CiscoStudy")
        exam = st.radio(
            "Exam track",
            list(EXAMS),
            format_func=lambda e: EXAMS[e],
            index=list(EXAMS).index(st.session_state["exam"]),
            key="exam_selector",
        )
        if exam != st.session_state["exam"]:
            st.session_state["exam"] = exam
            st.rerun()
        prof = get_profile(exam)
        seen, correct = prof.overall()
        acc = f"{round(correct / seen * 100)}%" if seen else "—"
        st.metric("Questions answered", seen)
        st.metric("Lifetime accuracy", acc)
        st.caption("Progress auto-saves to .userdata/ after every answer.")
    return st.session_state["exam"]


def get_scheduler(exam: str) -> DrillScheduler:
    key = f"sched_{exam}"
    if key not in st.session_state:
        st.session_state[key] = DrillScheduler(get_bank(), exam, get_blueprint(exam),
                                               rng=random.Random())
    return st.session_state[key]


# --- question rendering -----------------------------------------------------
def render_exhibit(q: Question) -> None:
    if q.exhibit:
        st.code(q.exhibit, language="text")


def answer_widget(q: Question, key: str):
    """Render the input for a question and return the current selection."""
    render_exhibit(q)
    st.markdown(f"**{q.stem}**")
    if q.is_fill:
        return st.text_input("Your answer", key=key, placeholder="type your answer…")
    labels = {o.id: f"{o.id}.  {o.text}" for o in q.options}
    if q.type == "multi":
        st.caption(f"Select {q.select_count}.")
        return st.multiselect("Choose all that apply", options=[o.id for o in q.options],
                              format_func=lambda i: labels[i], key=key)
    return st.radio("Choose one", options=[o.id for o in q.options],
                    format_func=lambda i: labels[i], index=None, key=key)


def render_feedback(q: Question, fb: Feedback) -> None:
    key_txt = ", ".join(fb.correct_ids)
    if fb.correct:
        st.success("✅  Correct")
    else:
        st.error(f"❌  Incorrect — correct answer: **{key_txt}**")

    st.markdown("**Why the correct answer is right**")
    st.markdown(fb.why_correct)

    traps = {k: v for k, v in fb.distractor_notes.items() if v}
    if traps:
        with st.expander("Why the Cisco distractors are traps", expanded=not fb.correct):
            for oid, note in traps.items():
                st.markdown(f"- **{oid}** — {note}")

    if fb.exam_pattern:
        st.info(f"🎯  **Spot it on the exam:** {fb.exam_pattern}")

    if fb.verify_cli:
        st.markdown("**Verify on the device**")
        st.code("\n".join(fb.verify_cli), language="text")

    if fb.references:
        st.caption("Reference: " + " · ".join(fb.references))


def grade_and_record(exam: str, q: Question, selection) -> Feedback:
    fb = grade(q, selection)
    prof = get_profile(exam)
    prof.record(q, fb.correct)
    save_profile(exam)
    return fb


# --- small analytics widgets ------------------------------------------------
def domain_mastery_table(exam: str):
    prof = get_profile(exam)
    bp = get_blueprint(exam)
    stats = prof.domain_stats()
    rows = []
    for d in bp.domains:
        seen, corr, acc = stats.get(d.key, (0, 0, 0.0))
        rows.append({
            "Domain": d.name,
            "Exam weight": f"{round(d.weight * 100)}%",
            "Answered": seen,
            "Accuracy": f"{round(acc * 100)}%" if seen else "—",
        })
    return rows


def box_distribution(exam: str) -> dict[int, int]:
    prof = get_profile(exam)
    dist = {b: 0 for b in BOX_WEIGHT}
    for st_ in prof.q.values():
        dist[st_.box] = dist.get(st_.box, 0) + 1
    return dist


# --- reusable quiz runner ---------------------------------------------------
def reset_quiz(skey: str) -> None:
    st.session_state.pop(skey, None)


def run_quiz(exam: str, skey: str, question_ids: list[str], instant: bool = False):
    """Drive a quiz/exam stored in session_state[skey].

    Records each answered item into the profile exactly once. Returns
    ("empty"|"in_progress"|"done", SessionScore|None). With instant=True the
    learner gets per-question feedback (lesson quizzes); with instant=False
    answers are graded at the end (milestone exams).
    """
    bank = get_bank()
    prof = get_profile(exam)
    bp = get_blueprint(exam)
    state = st.session_state.setdefault(
        skey, {"idx": 0, "answers": {}, "phase": "answering", "done": False, "fb": None}
    )
    total = len(question_ids)
    if total == 0:
        st.info("No questions available for this selection yet.")
        return ("empty", None)

    if state["done"]:
        attempts = [(qid, bank.get(qid).check(state["answers"].get(qid))) for qid in question_ids]
        return ("done", score_session(attempts, bank))

    idx = state["idx"]
    q = bank.get(question_ids[idx])
    st.progress(idx / total, text=f"Question {idx + 1} of {total}")
    st.caption(f"Domain: {bp.domain(q.domain).name}  ·  {q.subtopic.replace('_', ' ')}")

    if instant and state["phase"] == "feedback":
        render_feedback(q, state["fb"])
        label = "See results ▶" if idx == total - 1 else "Next ▶"
        if st.button(label, key=f"{skey}_next", type="primary"):
            if idx + 1 >= total:
                state["done"] = True
            else:
                state["idx"] += 1
                state["phase"] = "answering"
            st.rerun()
        return ("in_progress", None)

    sel = answer_widget(q, key=f"{skey}_ans_{idx}")
    submit_label = "Submit" if instant else ("Finish" if idx == total - 1 else "Next ▶")
    if st.button(submit_label, key=f"{skey}_submit", type="primary"):
        state["answers"][q.id] = sel
        fb = grade(q, sel)
        prof.record(q, fb.correct)
        save_profile(exam)
        if instant:
            state["fb"] = fb
            state["phase"] = "feedback"
        elif idx + 1 >= total:
            state["done"] = True
        else:
            state["idx"] += 1
        st.rerun()
    return ("in_progress", None)


# --- reusable PBQ terminal --------------------------------------------------
def render_pbq(scenario, skey_prefix: str) -> bool:
    """Render a scenario's ticket, CLI terminal and validation. Returns True
    once all checks pass (also sets a cross-page flag pbq_passed_<id>)."""
    topo_key = f"{skey_prefix}_topo"
    tx_key = f"{skey_prefix}_tx"
    dev_key = f"{skey_prefix}_dev"
    cons_key = f"{skey_prefix}_cons"

    if topo_key not in st.session_state:
        st.session_state[topo_key] = scenario.build()
        st.session_state[tx_key] = []
        st.session_state[dev_key] = scenario.device
        st.session_state[cons_key] = {}

    topo = st.session_state[topo_key]
    consoles = st.session_state[cons_key]

    st.markdown(scenario.ticket)
    with st.expander("Hints"):
        for h in scenario.hints:
            st.markdown(f"- {h}")

    devices = list(topo.devices)
    dev = st.selectbox("Console device", devices,
                       index=devices.index(st.session_state[dev_key]),
                       key=f"{skey_prefix}_devsel",
                       help="You may inspect peer devices; fix the one named in the ticket.")
    st.session_state[dev_key] = dev
    if dev not in consoles:
        consoles[dev] = Console(topo, dev)
    con = consoles[dev]

    # transcript
    lines = []
    for p, c, o in st.session_state[tx_key]:
        lines.append(f"{p} {c}")
        if o:
            lines.append(o)
    lines.append(con.prompt)
    st.code("\n".join(lines) or con.prompt, language="text")

    with st.form(f"{skey_prefix}_form", clear_on_submit=True):
        cmd = st.text_input("Enter IOS command", placeholder="e.g. configure terminal",
                            label_visibility="collapsed")
        cols = st.columns([1, 1, 6])
        run = cols[0].form_submit_button("Run ▶", type="primary")
        clear = cols[1].form_submit_button("Reset lab")
    if run and cmd.strip():
        prompt_before = con.prompt
        out = con.execute(cmd)
        st.session_state[tx_key].append((prompt_before, cmd, out))
        st.rerun()
    if clear:
        for k in (topo_key, tx_key, dev_key, cons_key):
            st.session_state.pop(k, None)
        st.session_state.pop(f"pbq_passed_{scenario.id}", None)
        st.rerun()

    passed = False
    if st.button("Validate ticket ✔", key=f"{skey_prefix}_validate"):
        checks = scenario.validate(topo)
        for c in checks:
            (st.success if c.passed else st.error)(
                f"{'✅' if c.passed else '❌'}  {c.description}")
        if all(c.passed for c in checks):
            passed = True
            st.session_state[f"pbq_passed_{scenario.id}"] = True
            st.success(f"🎉  {scenario.success}")
            st.balloons()
        else:
            st.warning("Not resolved yet — review the failed checks above and the hints.")
    return passed or st.session_state.get(f"pbq_passed_{scenario.id}", False)
