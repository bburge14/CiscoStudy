from studyengine import grade, load_bank, score_session
from studyengine.models import Question

BANK = load_bank()


def _mcq():
    return Question.from_dict({
        "id": "t-mcq", "exam": "ccna", "domain": "d", "subtopic": "s", "type": "mcq",
        "stem": "x", "options": [{"id": "A", "text": "a"}, {"id": "B", "text": "b"}],
        "correct": ["B"], "explanation": {"correct": "b is right",
                                          "distractors": {"A": "nope"}, "exam_pattern": "cue"},
    })


def _multi():
    return Question.from_dict({
        "id": "t-multi", "exam": "ccna", "domain": "d", "subtopic": "s", "type": "multi",
        "stem": "x", "options": [{"id": "A", "text": "a"}, {"id": "B", "text": "b"},
                                 {"id": "C", "text": "c"}],
        "correct": ["A", "C"], "explanation": {"correct": "a and c"},
    })


def _fill():
    return Question.from_dict({
        "id": "t-fill", "exam": "ccna", "domain": "d", "subtopic": "s", "type": "fill",
        "stem": "x", "correct": ["0.0.3.255", "/26"], "explanation": {"correct": "inverse mask"},
    })


def test_mcq_grading():
    q = _mcq()
    assert q.check("B")
    assert not q.check("A")
    assert not q.check(None)


def test_multi_requires_exact_set():
    q = _multi()
    assert q.check(["A", "C"])
    assert q.check(["C", "A"])       # order independent
    assert not q.check(["A"])        # partial is wrong
    assert not q.check(["A", "B", "C"])


def test_fill_normalizes():
    q = _fill()
    assert q.check("0.0.3.255")
    assert q.check("  0.0.3.255 ")   # whitespace tolerant
    assert q.check("/26")
    assert not q.check("0.0.255.255")


def test_feedback_payload():
    q = _mcq()
    fb = grade(q, "A")
    assert fb.correct is False
    assert fb.why_correct == "b is right"
    assert fb.distractor_notes["A"] == "nope"
    assert fb.exam_pattern == "cue"


def test_format_selection_for_review():
    # The after-quiz review shows what the learner actually chose.
    from ui_common import _format_selection
    assert _format_selection(_mcq(), "B") == "B. b"
    assert _format_selection(_multi(), ["C", "A"]) == "C. c; A. a"   # preserves chosen order
    assert _format_selection(_fill(), "0.0.3.255") == "“0.0.3.255”"
    # a skipped / blank answer reads as skipped, in every shape
    for blank in (None, "", [], ()):
        assert "skipped" in _format_selection(_mcq(), blank)
    # an option id that isn't on the question falls back to the raw value
    assert _format_selection(_mcq(), "Z") == "Z"


def test_score_session_aggregates_by_domain():
    ids = [q.id for q in BANK.query(exam="ccna", domain="ip_connectivity")[:4]]
    attempts = [(ids[0], True), (ids[1], True), (ids[2], False), (ids[3], True)]
    score = score_session(attempts, BANK)
    assert score.total == 4
    assert score.correct == 3
    assert score.by_domain["ip_connectivity"].seen == 4
    assert score.by_domain["ip_connectivity"].correct == 3
    assert score.pct == 75
