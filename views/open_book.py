"""Open-Book Review: the lessons are here if you need them — but on your honor.

Looking something up is allowed and sometimes smart, but it's a signal that you
haven't mastered the topic yet. So a peek costs you: a correct-but-looked-up
answer scores as a peek AND is recorded as still-to-study (it resurfaces), while
a correct unaided answer counts toward mastery. Your "honest score" only counts
answers you got without the book.
"""
from __future__ import annotations

import streamlit as st

from studyengine import get_blueprint, grade, lesson_markdown
from ui_common import (
    answer_widget,
    get_bank,
    get_curriculum,
    get_profile,
    get_scheduler,
    page_header,
    page_setup,
    render_feedback,
    save_profile,
)

exam = page_setup("Open-Book Review", icon="📖")
bank = get_bank()
bp = get_blueprint(exam)
prof = get_profile(exam)
sched = get_scheduler(exam)
SKEY = f"openbook_{exam}"

ob = st.session_state.setdefault(
    SKEY, {"qid": None, "phase": "answering", "fb": None, "book_used": False,
           "recent": [], "answered": 0, "unaided": 0, "peeked": 0},
)

page_header("book_search", "Open-Book Review")


# Map each sub-topic to the lesson(s) that teach it (built once per exam/run).
def _subtopic_lessons(exam: str) -> dict[str, list]:
    out: dict[str, list] = {}
    for u in get_curriculum().units_for(exam):
        for lesson in u.lessons:
            for stp in lesson.subtopics:
                out.setdefault(stp, []).append(lesson)
    return out


st.markdown(
    "The book is open — but it's on your honor. **Looking a question up is allowed**, yet it "
    "means you don't know it *yet*, so a peek costs points and marks that topic for more "
    "study. Answer without the book whenever you can."
)

# --- scoreboard -------------------------------------------------------------
honest = f"{round(ob['unaided'] / ob['answered'] * 100)}%" if ob["answered"] else "—"
m1, m2, m3, m4 = st.columns(4)
m1.metric("Answered", ob["answered"])
m2.metric("Unaided correct", ob["unaided"])
m3.metric("Peeks", ob["peeked"])
m4.metric("Honest score", honest, help="Share of questions you got right WITHOUT the book.")
st.divider()

# --- pick a question --------------------------------------------------------
if ob["qid"] is None:
    nxt = sched.next(prof, recent_ids=ob["recent"])
    ob["qid"] = nxt.id if nxt else None
    ob["phase"] = "answering"
    ob["fb"] = None
    ob["book_used"] = False

if ob["qid"] is None:
    st.warning("No questions available for this exam track.")
    st.stop()

q = bank.get(ob["qid"])
st.caption(f"Domain: {bp.domain(q.domain).name}  ·  Sub-topic: {q.subtopic.replace('_', ' ')}  "
           f"·  Difficulty: {'●' * q.difficulty}{'○' * (3 - q.difficulty)}")

# --- answering phase --------------------------------------------------------
if ob["phase"] == "answering":
    sel = answer_widget(q, key=f"{SKEY}_ans_{q.id}")

    # The book: a deliberate, recorded peek (Streamlit can't detect an expander
    # opening, so looking it up is an explicit click).
    if not ob["book_used"]:
        if st.button("📖 Look it up in the lessons  (counts as a peek)", key=f"{SKEY}_peek"):
            ob["book_used"] = True
            st.rerun()
    else:
        st.warning("📖 Book open — this answer will count as a **peek** and the topic will be "
                   "marked for more study, even if you get it right.")
        lessons = _subtopic_lessons(exam).get(q.subtopic, [])
        if lessons:
            lesson = lessons[0]
            with st.container(border=True):
                st.markdown(f"#### 📘 {lesson.title}")
                st.markdown(lesson_markdown(lesson))
        else:
            st.info(f"No dedicated lesson page for **{q.subtopic.replace('_', ' ')}** yet. "
                    "Use the References below after you answer, and mark this topic to review.")

    if st.button("Submit", type="primary", key=f"{SKEY}_submit"):
        fb = grade(q, sel)
        mastered = fb.correct and not ob["book_used"]
        # A peeked-correct answer is recorded as NOT mastered, so it resurfaces
        # and counts toward "needs study" — the whole point of the honor system.
        prof.record(q, mastered)
        save_profile(exam)
        ob["fb"] = fb
        ob["answered"] += 1
        if mastered:
            ob["unaided"] += 1
        if ob["book_used"]:
            ob["peeked"] += 1
        ob["recent"] = ([q.id] + ob["recent"])[:8]
        ob["phase"] = "feedback"
        st.rerun()

# --- feedback phase ---------------------------------------------------------
else:
    fb = ob["fb"]
    if fb.correct and not ob["book_used"]:
        st.success("✅ **Correct, unaided** — that counts toward mastery.")
    elif fb.correct and ob["book_used"]:
        st.warning("📖 **Correct, but with the book.** Scored as a peek and marked for more "
                   "study — you'll see this topic again. Next time, try it closed-book first.")
    else:
        st.error("❌ **Incorrect** — marked for study."
                 + ("  (You had the book open — focus here.)" if ob["book_used"] else ""))

    render_feedback(q, fb)
    if st.button("Next question ▶", type="primary", key=f"{SKEY}_next"):
        ob["qid"] = None
        st.rerun()
