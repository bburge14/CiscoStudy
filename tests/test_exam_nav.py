"""AppTest smoke/behaviour tests for the navigable, graded-at-the-end exam
engine (``run_exam``) and the per-track baseline size.

These guard two things that regressed/were requested:
  * the Diagnostic baseline is 5 questions per *official domain*, so its size
    follows the blueprint (6-domain CCNA/ENCOR = 30, 5-domain Security+/Network+/
    A+ Core 1 = 25, 4-domain A+ Core 2 = 20) — NOT a hard-coded 30; and
  * real-exam navigation works: a Previous button restores a prior answer, a
    question can be flagged, and the review screen submits for grading.
"""
from __future__ import annotations

import os
import pathlib
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

# Point persistence at a throwaway dir BEFORE ui_common computes USERDATA.
_TMP = tempfile.mkdtemp(prefix="certwize-nav-test-")
os.environ["CISCOSTUDY_DATA"] = _TMP

import ui_common  # noqa: E402

ui_common.USERDATA = pathlib.Path(_TMP)  # in case it imported earlier

from streamlit.testing.v1 import AppTest  # noqa: E402


def _run(page: str, exam: str) -> AppTest:
    at = AppTest.from_file(str(REPO / "views" / page), default_timeout=120)
    at.session_state["exam"] = exam
    at.session_state["auth_user"] = "default"
    at.run()
    return at


def _set_first_answer(at: AppTest):
    """Answer the current question whatever its type (the first question's type
    is random), returning (kind, value) so persistence can be re-checked."""
    if len(at.radio):
        at.radio[0].set_value(at.radio[0].options[0]).run()
        return "radio", at.radio[0].value
    if len(at.multiselect):
        at.multiselect[0].set_value([at.multiselect[0].options[0]]).run()
        return "multiselect", at.multiselect[0].value
    at.text_input[0].set_value("router").run()
    return "text", at.text_input[0].value


def _first_answer_value(at: AppTest, kind: str):
    return {"radio": at.radio, "multiselect": at.multiselect,
            "text": at.text_input}[kind][0].value


# --- the reported bug: "benchmark says 30 but gives 25" ---------------------
def test_baseline_size_follows_blueprint():
    expected = {"ccna": 30, "encor": 30, "secplus": 25,
                "netplus": 25, "aplus1": 25, "aplus2": 20}
    for exam, n in expected.items():
        at = _run("diagnostic.py", exam)
        assert not at.exception, (exam, at.exception)
        start = [b for b in at.button if "baseline" in b.label.lower()][0]
        assert f"{n}-question" in start.label, (exam, start.label)
        caption = " ".join(c.value for c in at.caption)
        assert f"{n} questions" in caption, (exam, caption)


def test_baseline_actually_builds_that_many():
    for exam, n in (("ccna", 30), ("secplus", 25), ("aplus2", 20)):
        at = _run("diagnostic.py", exam)
        [b for b in at.button if "baseline" in b.label.lower()][0].click()
        at.run()
        assert not at.exception, (exam, at.exception)
        assert len(at.session_state[f"dxids_{exam}"]) == n


# --- real-exam navigation ---------------------------------------------------
def test_previous_button_restores_answer():
    exam = "ccna"
    at = _run("diagnostic.py", exam)
    [b for b in at.button if "baseline" in b.label.lower()][0].click()
    at.run()

    kind, chosen = _set_first_answer(at)
    qid0 = at.session_state[f"dxids_{exam}"][0]
    assert at.session_state[f"dx_{exam}"]["answers"][qid0] == chosen

    at.button(key=f"dx_{exam}_next").click().run()
    assert at.session_state[f"dx_{exam}"]["idx"] == 1
    at.button(key=f"dx_{exam}_prev").click().run()
    assert not at.exception, at.exception
    assert at.session_state[f"dx_{exam}"]["idx"] == 0
    # the earlier selection survives the round trip (even though Streamlit GCs
    # the off-screen widget) because run_exam restores it from its own store.
    assert _first_answer_value(at, kind) == chosen


def test_flag_review_and_submit():
    exam = "ccna"
    at = _run("diagnostic.py", exam)
    [b for b in at.button if "baseline" in b.label.lower()][0].click()
    at.run()

    _set_first_answer(at)
    qid0 = at.session_state[f"dxids_{exam}"][0]
    at.button(key=f"dx_{exam}_flag_{qid0}").click().run()
    assert qid0 in at.session_state[f"dx_{exam}"]["flags"]

    at.button(key=f"dx_{exam}_toreview").click().run()
    assert at.session_state[f"dx_{exam}"]["view"] == "review"
    assert any("unanswered" in w.value.lower() for w in at.warning)

    at.button(key=f"dx_{exam}_submit").click().run()
    assert not at.exception, at.exception
    assert at.session_state[f"dx_{exam}"]["submitted"] is True
    assert at.session_state[f"dx_{exam}"]["recorded"] is True
    assert any("Result:" in s.value for s in at.subheader)
    # a baseline score was stored
    prof = at.session_state[ui_common._profile_key(exam)]
    assert prof.baseline and prof.baseline["total"] == 30


def test_flag_survives_navigation():
    # A flag must NOT be dropped when the question is also answered and the
    # learner moves away and back (the flag is button-driven, so only an
    # explicit click changes it — navigation never does).
    exam = "ccna"
    at = _run("diagnostic.py", exam)
    [b for b in at.button if "baseline" in b.label.lower()][0].click()
    at.run()
    _set_first_answer(at)
    qid0 = at.session_state[f"dxids_{exam}"][0]
    at.button(key=f"dx_{exam}_flag_{qid0}").click().run()
    assert qid0 in at.session_state[f"dx_{exam}"]["flags"]

    at.button(key=f"dx_{exam}_next").click().run()
    assert qid0 in at.session_state[f"dx_{exam}"]["flags"]   # untouched on Q2
    at.button(key=f"dx_{exam}_prev").click().run()
    at.button(key=f"dx_{exam}_toreview").click().run()
    assert not at.exception, at.exception
    assert qid0 in at.session_state[f"dx_{exam}"]["flags"]   # still flagged at review
    # answer also survived the round trip
    assert not ui_common._is_blank(at.session_state[f"dx_{exam}"]["answers"].get(qid0))


def test_exam_sim_is_timed_and_navigable():
    exam = "ccna"
    at = _run("exam_sim.py", exam)
    at.radio[0].set_value("Quick (20)").run()
    [b for b in at.button if b.label == "Start exam"][0].click()
    at.run()
    assert not at.exception, at.exception
    assert at.session_state[f"exam_{exam}"]["deadline"] is not None
    assert len(at.session_state[f"examids_{exam}"]) == 20

    kind, chosen = _set_first_answer(at)
    at.button(key=f"exam_{exam}_next").click().run()
    at.button(key=f"exam_{exam}_prev").click().run()
    assert _first_answer_value(at, kind) == chosen  # persists under the timed/fragment page

    at.button(key=f"exam_{exam}_toreview").click().run()
    at.button(key=f"exam_{exam}_submit").click().run()
    assert not at.exception, at.exception
    assert at.session_state[f"exam_{exam}"]["submitted"] is True


def test_milestone_exam_renders_through_engine():
    for exam in ("ccna", "secplus", "aplus2"):
        at = _run("milestones.py", exam)
        assert not at.exception, (exam, at.exception)
        assert any(k.startswith(f"ms_{exam}_") for k in at.session_state)
