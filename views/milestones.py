"""Structured Milestone mode: Read → Lesson Quiz → cumulative Milestone + PBQ."""
from __future__ import annotations

import streamlit as st

from studyengine import lesson_markdown, lesson_quiz, milestone_exam
from studyengine.cli_sim import get_scenario
from ui_common import (
    EXAMS,
    PASS_THRESHOLD,
    get_bank,
    get_curriculum,
    get_profile,
    page_header,
    page_setup,
    render_pbq,
    render_quiz_review,
    reset_quiz,
    run_quiz,
    save_profile,
)

exam = page_setup("Structured Milestones", icon="📚")
bank = get_bank()
cur = get_curriculum()
prof = get_profile(exam)
units = cur.units_for(exam)

page_header("book", "Structured Milestones")
st.caption("Work each unit in order: read the lesson, pass the lesson quiz, then "
           "clear the cumulative milestone exam and PBQ to unlock the next unit.")

if not units:
    st.info(f"📚 Structured lessons for **{EXAMS[exam]}** are on the way. In the "
            "meantime, use **Diagnostic**, **Endless Drill**, and **Exam Simulation** "
            "(all fully stocked for this track) to study.")
    st.stop()


def unlocked(i: int) -> bool:
    return i == 0 or units[i - 1].id in prof.passed_milestones


labels = [f"{'🔓' if unlocked(i) else '🔒'}  Unit {u.order}: {u.title}"
          + ("  ✅" if u.id in prof.passed_milestones else "")
          for i, u in enumerate(units)]
choice = st.selectbox("Select a unit", range(len(units)), format_func=lambda i: labels[i])
u = units[choice]

if not unlocked(choice):
    st.warning(f"🔒 This unit is locked. Pass the **Unit {units[choice-1].order}** "
               "milestone (exam + PBQ) to unlock it.")
    st.stop()

st.markdown(f"## Unit {u.order}: {u.title}")
st.caption(u.summary)

tab_read, tab_quiz, tab_ms = st.tabs(["① Read", "② Lesson Quiz", "③ Milestone + PBQ"])

# --- Step 1: Read -----------------------------------------------------------
with tab_read:
    lesson = st.selectbox("Lesson", u.lessons, format_func=lambda l: l.title, key=f"read_{u.id}")
    if lesson.id in prof.completed_lessons:
        st.success("✓ Lesson quiz already passed.")
    st.markdown(lesson_markdown(lesson))

# --- Step 2: Lesson Quiz ----------------------------------------------------
with tab_quiz:
    lesson = st.selectbox(
        "Lesson quiz", u.lessons,
        format_func=lambda l: ("✓ " if l.id in prof.completed_lessons else "") + l.title,
        key=f"quizpick_{u.id}")
    ids_key = f"lqids_{exam}_{lesson.id}"
    skey = f"lq_{exam}_{lesson.id}"
    if ids_key not in st.session_state:
        st.session_state[ids_key] = [q.id for q in lesson_quiz(bank, lesson)]
    st.caption(f"{len(st.session_state[ids_key])} authentic questions · instant feedback.")
    status, score = run_quiz(exam, skey, st.session_state[ids_key], instant=True)
    if status == "done":
        st.subheader(f"Lesson quiz score: {score.correct}/{score.total} · {score.pct}%")
        if score.passed(PASS_THRESHOLD):
            st.success(f"Passed (≥{int(PASS_THRESHOLD*100)}%) — lesson marked complete.")
            if lesson.id not in prof.completed_lessons:
                prof.completed_lessons.add(lesson.id)
                save_profile(exam)
        else:
            st.warning(f"Below {int(PASS_THRESHOLD*100)}% — revisit the lesson and retry.")
        if st.button("Retake lesson quiz", key=f"rq_{lesson.id}"):
            reset_quiz(skey)
            st.session_state.pop(ids_key, None)
            st.rerun()

# --- Step 3: Milestone Exam + PBQ ------------------------------------------
with tab_ms:
    done_lessons = sum(1 for l in u.lessons if l.id in prof.completed_lessons)
    st.caption(f"Lessons passed: {done_lessons}/{len(u.lessons)} (recommended before the milestone).")

    ids_key = f"msids_{exam}_{u.id}"
    skey = f"ms_{exam}_{u.id}"
    if ids_key not in st.session_state:
        st.session_state[ids_key] = [q.id for q in milestone_exam(bank, cur, u)]
    st.markdown(f"**Cumulative milestone exam — {len(st.session_state[ids_key])} questions** "
                "(drawn from this unit and all prior units; graded at the end).")

    status, score = run_quiz(exam, skey, st.session_state[ids_key], instant=False)
    exam_passed = False
    if status == "done":
        st.subheader(f"Milestone exam: {score.correct}/{score.total} · {score.pct}%")
        exam_passed = score.passed(PASS_THRESHOLD)
        (st.success if exam_passed else st.error)(
            ("Exam passed." if exam_passed else "Exam not passed.")
            + f" (need ≥{int(PASS_THRESHOLD*100)}%)")
        # The milestone exam is graded at the end with no feedback as you go, so
        # offer a full review afterward (the lesson quiz already gives it inline).
        render_quiz_review(exam, st.session_state[ids_key], st.session_state[skey]["answers"])
        if st.button("Retake milestone exam", key=f"rm_{u.id}"):
            reset_quiz(skey)
            st.session_state.pop(ids_key, None)
            st.rerun()

    pbq_ok = True
    if u.pbq_id:
        st.divider()
        st.markdown("### 🖥️ Performance-Based Question (required to unlock)")
        scen = get_scenario(u.pbq_id)
        pbq_ok = render_pbq(scen, skey_prefix=f"mspbq_{exam}_{u.id}")

    if exam_passed and pbq_ok:
        if u.id not in prof.passed_milestones:
            prof.passed_milestones.add(u.id)
            save_profile(exam)
        nxt = f" — Unit {units[choice+1].order} unlocked!" if choice + 1 < len(units) else " — track complete!"
        st.success(f"✅ Unit {u.order} milestone complete{nxt}")
    elif exam_passed and not pbq_ok:
        st.info("Exam passed — now resolve the PBQ above to finish the milestone.")
