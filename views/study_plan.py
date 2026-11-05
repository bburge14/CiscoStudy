"""My Study Plan: a personalized, ordered path that marches the learner through
their weakest sub-topics one at a time — read the lesson, then drill the topic
until it's mastered, then the next topic unlocks.
"""
from __future__ import annotations

import streamlit as st

from studyengine import (
    build_plan,
    current_step,
    get_blueprint,
    lesson_markdown,
    next_question_for_subtopic,
    plan_progress,
)
from studyengine.studyplan import MASTERY_TARGET, MIN_ATTEMPTS, is_mastered
from ui_common import (
    answer_widget,
    get_bank,
    get_curriculum,
    get_profile,
    grade_and_record,
    page_header,
    page_setup,
    render_feedback,
)

exam = page_setup("My Study Plan", icon="🧭")
bank = get_bank()
cur = get_curriculum()
bp = get_blueprint(exam)
prof = get_profile(exam)

TARGET_PCT = int(MASTERY_TARGET * 100)


def _need(subtopic: str) -> int:
    return max(1, min(MIN_ATTEMPTS, len(bank.query(exam=exam, subtopic=subtopic))))


def _mastered_now(subtopic: str) -> tuple[bool, int, int, int]:
    seen, correct, _ = prof.subtopic_stats().get(subtopic, (0, 0, 0.0))
    need = _need(subtopic)
    return is_mastered(seen, correct, need), seen, correct, need


def _render_drill(cur_step) -> None:
    """One-question-at-a-time drill locked to the current step's sub-topic."""
    K = f"plandrill_{exam}"
    ds = st.session_state.setdefault(
        K, {"sub": None, "qid": None, "phase": "answering", "fb": None, "last": None}
    )

    # Feedback phase: show the result of the question just answered (its own
    # sub-topic), and only advance when the learner clicks Next.
    if ds["phase"] == "feedback" and ds["qid"]:
        q = bank.get(ds["qid"])
        render_feedback(q, ds["fb"])
        mastered, seen, correct, need = _mastered_now(q.subtopic)
        if mastered:
            st.success(f"✅ **{q.subtopic.replace('_', ' ').title()} mastered** "
                       f"({correct}/{seen}) — unlocking your next topic.")
        else:
            st.caption(f"This topic: {correct}/{seen} right · need {need}+ answered at {TARGET_PCT}%+.")
        if st.button("Next question ▶", key=f"{K}_next", type="primary"):
            if mastered:
                ds.update({"sub": None, "qid": None, "phase": "answering", "fb": None})
            else:
                ds.update({"qid": None, "phase": "answering", "fb": None})
            st.rerun()
        return

    # Answering phase: serve a question from the current step's sub-topic.
    if cur_step is None:
        return
    if ds["sub"] != cur_step.subtopic:
        ds.update({"sub": cur_step.subtopic, "qid": None, "last": None})
    if ds["qid"] is None:
        q = next_question_for_subtopic(bank, prof, exam, cur_step.subtopic, exclude_id=ds["last"])
        ds["qid"] = q.id if q else None
    if not ds["qid"]:
        st.caption("No questions available for this topic yet.")
        return
    q = bank.get(ds["qid"])
    sel = answer_widget(q, key=f"{K}_ans_{q.id}")
    if st.button("Submit answer", key=f"{K}_submit", type="primary"):
        ds.update({"fb": grade_and_record(exam, q, sel), "phase": "feedback", "last": q.id})
        st.rerun()


# --- page body --------------------------------------------------------------
page_header("route", "My Study Plan")

steps = build_plan(prof, bank, cur, bp)
done, total = plan_progress(steps)
cur_step = current_step(steps)

if not prof.baseline:
    st.info("📋 Take the **Diagnostic Baseline** first and this plan rebuilds around the exact "
            "topics you're weakest on. You can start now, but it won't be personalized yet.")
elif prof.baseline:
    st.caption(f"Built from your diagnostic ({prof.baseline['overall']}%), weakest topics first.")

st.progress((done / total) if total else 0.0,
            text=f"{done} of {total} topics mastered")
st.caption(f"Work the steps in order. A topic is **mastered** once you answer it to {TARGET_PCT}%+ "
           "over a few questions — then the next one unlocks.")
st.divider()

# During feedback, keep the header on the topic just answered (not the advanced one).
ds = st.session_state.get(f"plandrill_{exam}")
display_sub = None
if ds and ds.get("phase") == "feedback" and ds.get("qid"):
    display_sub = bank.get(ds["qid"]).subtopic
display_step = next((s for s in steps if s.subtopic == display_sub), None) or cur_step

if cur_step is None and not display_sub:
    st.success("🎉 **Every topic is mastered.** Your coverage is exam-ready — keep it sharp with "
               "**Endless Drill**, and prove it under pressure in the **Structured Milestones** and **PBQ Lab**.")
else:
    s = display_step
    st.subheader(f"👉 Now studying: {s.label.title()}")
    st.caption(f"**{s.domain_name}** · {s.reason()}")

    with st.expander("📖 Read the lesson first", expanded=False):
        if s.lesson_ids:
            for lid in s.lesson_ids:
                les = cur.lesson(lid)
                st.markdown(lesson_markdown(les))
        else:
            st.caption("No dedicated lesson for this topic — you'll learn it by drilling below.")

    st.markdown(f"**🎯 Drill it until mastered** (need {s.need}+ answered at {TARGET_PCT}%+)")
    _render_drill(cur_step)

# --- the whole ordered plan -------------------------------------------------
st.divider()
with st.expander(f"📋 Full plan — {done}/{total} topics mastered", expanded=(total and done == 0)):
    for i, step in enumerate(steps, 1):
        icon = {"done": "✅", "current": "👉", "upcoming": "🔒"}[step.status]
        extra = f" · {step.pct}%" if step.pct is not None else " · not tested"
        weight = f" · {round(step.weight * 100)}% of exam"
        st.markdown(f"{icon} **{i}. {step.label.title()}** — {step.domain_name}{extra}{weight}")
    st.caption("🔒 locked topics unlock as you master the ones above them.")
