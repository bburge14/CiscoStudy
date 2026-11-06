"""Open-Book Practice: a true open-book test with adjustable help.

The book is there while you answer. Leave it shut and a miss is free; open it and
a wrong answer costs XP — more the more the book helped — while a correct answer
earns less the more help you took. Either way answers count toward your progress
like Endless Drill. You choose how much the book helps you find the answer:

* Full book    — every lesson is browsable; nothing tells you where the answer
                 is. You search it like real documentation.
* General area — the book is narrowed to this question's domain; find the right
                 lesson within it.
* Pinpoint     — the book opens straight to the lesson for this sub-topic.
"""
from __future__ import annotations

import streamlit as st

from studyengine import get_blueprint, lesson_markdown
from ui_common import (
    answer_widget,
    get_bank,
    get_curriculum,
    get_profile,
    get_scheduler,
    grade_and_record,
    last_xp_event,
    page_header,
    page_setup,
    render_feedback,
    render_xp_event,
)

exam = page_setup("Open-Book Practice", icon="📖")
bank = get_bank()
bp = get_blueprint(exam)
prof = get_profile(exam)
sched = get_scheduler(exam)
SKEY = f"openbook_{exam}"

ob = st.session_state.setdefault(
    SKEY, {"qid": None, "phase": "answering", "fb": None,
           "recent": [], "answered": 0, "correct": 0},
)

page_header("book_search", "Open-Book Practice")

st.markdown(
    "An open-book test: the book is there while you answer. Leave it shut and a miss is "
    "free — **open it and a wrong answer costs you**, more the more the book helped. "
    "Choose how much help it gives you finding the answer."
)
st.markdown("**How much help do you want?** (this scales your XP — pick before you answer)")
mode = st.radio(
    "Help level", ["Full book", "General area", "Pinpoint"], horizontal=True,
    key=f"{SKEY}_mode", label_visibility="collapsed",
    help="Full book = search everything (hardest, full XP). General area = narrowed to "
         "this question's domain. Pinpoint = the exact lesson (easiest, least XP).",
)
XP_SCALE = {"Full book": 1.0, "General area": 0.7, "Pinpoint": 0.4}
# A miss costs XP only if you opened the book, scaled UP by how much it helped:
# with Pinpoint the answer was in front of you, so missing stings most.
MISS_SCALE = {"Full book": 0.4, "General area": 0.7, "Pinpoint": 1.0}
st.caption("Answer **without opening the book** for full XP and no risk. Open it and a "
           "correct answer earns less the more help the mode gives — **Full book 100% · "
           "General area 70% · Pinpoint 40%** — while a **miss now costs you**, and more "
           "the more help you had (**Pinpoint** stings most). Leave the book shut and a "
           "miss is still free.")

# --- scoreboard -------------------------------------------------------------
acc = f"{round(ob['correct'] / ob['answered'] * 100)}%" if ob["answered"] else "—"
m1, m2 = st.columns(2)
m1.metric("Answered", ob["answered"])
m2.metric("Accuracy", acc)
st.divider()

# --- pick a question --------------------------------------------------------
if ob["qid"] is None:
    nxt = sched.next(prof, recent_ids=ob["recent"])
    ob["qid"] = nxt.id if nxt else None
    ob["phase"] = "answering"
    ob["fb"] = None

if ob["qid"] is None:
    st.warning("No questions available for this exam track.")
    st.stop()

q = bank.get(ob["qid"])
st.caption(f"Domain: {bp.domain(q.domain).name}  ·  Sub-topic: {q.subtopic.replace('_', ' ')}  "
           f"·  Difficulty: {'●' * q.difficulty}{'○' * (3 - q.difficulty)}")


def _pinpoint_lessons():
    out = []
    for u in get_curriculum().units_for(exam):
        for lesson in u.lessons:
            if q.subtopic in lesson.subtopics:
                out.append((u, lesson))
    return out


def _render_book() -> None:
    """Render the open book for the current question, scoped by the chosen mode."""
    if mode == "Pinpoint":
        pairs = _pinpoint_lessons()
        if pairs:
            st.caption("Pinpoint: the lesson(s) that cover this question's sub-topic.")
            i = st.selectbox("Lesson", range(len(pairs)), key=f"{SKEY}_pp",
                             format_func=lambda i: f"{pairs[i][1].title} (Unit {pairs[i][0].order})")
            with st.container(border=True):
                st.markdown(lesson_markdown(pairs[i][1]))
            return
        st.info("No single lesson maps to this sub-topic — browse the unit below.")

    units = get_curriculum().units_for(exam)
    if mode == "General area":
        scoped = [u for u in units if q.domain in getattr(u, "domains", [])]
        if scoped:
            units = scoped
            st.caption(f"General area: narrowed to **{bp.domain(q.domain).name}** — "
                       "find the right lesson within it.")
    elif mode == "Full book":
        st.caption("Full book: the whole library. Nothing tells you which lesson holds the answer.")

    if not units:
        st.info("No lessons are available for this track yet.")
        return
    bu = st.selectbox("Unit", units, key=f"{SKEY}_bu",
                      format_func=lambda u: f"Unit {u.order}: {u.title}")
    bl = st.selectbox("Lesson", bu.lessons, key=f"{SKEY}_bl", format_func=lambda l: l.title)
    with st.container(border=True):
        st.markdown(lesson_markdown(bl))


# --- answering phase --------------------------------------------------------
if ob["phase"] == "answering":
    sel = answer_widget(q, key=f"{SKEY}_ans_{q.id}")

    csub, cskip = st.columns(2)
    with csub:
        submit = st.button("Submit", type="primary", key=f"{SKEY}_submit")
    with cskip:
        if st.button("Skip ▶", key=f"{SKEY}_skip",
                     help="Move on without answering — no effect on your score."):
            ob["recent"] = ([q.id] + ob["recent"])[:8]
            ob["qid"] = None
            st.session_state.pop(f"{SKEY}_book", None)   # reset the book per question
            st.rerun()
    if submit:
        # The book is scored only if it was open for THIS question. A correct
        # answer's reward shrinks with how much the mode helped; a miss costs
        # nothing with the book shut, and more the more it helped when open.
        used_book = bool(st.session_state.get(f"{SKEY}_book", False))
        scale = XP_SCALE.get(mode, 1.0) if used_book else 1.0
        miss = MISS_SCALE.get(mode, 0.0) if used_book else 0.0
        fb = grade_and_record(exam, q, sel, xp_scale=scale, miss_scale=miss)
        ob["fb"] = fb
        ob["answered"] += 1
        if fb.correct:
            ob["correct"] += 1
        ob["recent"] = ([q.id] + ob["recent"])[:8]
        ob["phase"] = "feedback"
        st.rerun()

    st.divider()
    if st.toggle("📖 Open the book", key=f"{SKEY}_book",
                 help="Browse the lessons (scoped by the mode above) to find the answer."):
        _render_book()

# --- feedback phase ---------------------------------------------------------
else:
    fb = ob["fb"]
    if fb.correct:
        st.success("✅ **Correct.**")
    else:
        st.error("❌ **Incorrect** — this one will resurface so you can nail it next time.")
    render_xp_event(last_xp_event())
    render_feedback(q, fb)
    if st.button("Next question ▶", type="primary", key=f"{SKEY}_next"):
        ob["qid"] = None
        st.session_state.pop(f"{SKEY}_book", None)   # reset the book per question
        st.rerun()
