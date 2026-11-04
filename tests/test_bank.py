import pytest

from studyengine import load_bank
from studyengine.bank import QuestionBank
from studyengine.models import Question

BANK = load_bank()


def _q(qid, exam="ccna", domain="d", subtopic="s"):
    return Question.from_dict({
        "id": qid, "exam": exam, "domain": domain, "subtopic": subtopic,
        "stem": "x", "options": [{"id": "A", "text": "a"}, {"id": "B", "text": "b"}],
        "correct": ["A"], "explanation": {"correct": "because"},
    })


def test_duplicate_ids_rejected():
    with pytest.raises(ValueError):
        QuestionBank([_q("dup"), _q("dup")])


def test_query_by_exam_and_domain():
    ccna = BANK.query(exam="ccna")
    assert all(q.exam == "ccna" for q in ccna)
    na = BANK.query(exam="ccna", domain="network_access")
    assert na and all(q.domain == "network_access" for q in na)


def test_query_by_subtopics_and_exclude():
    ospf = BANK.query(exam="ccna", subtopic="ospf")
    assert ospf and all(q.subtopic == "ospf" for q in ospf)
    some = {ospf[0].id}
    excl = BANK.query(exam="ccna", subtopic="ospf", exclude_ids=some)
    assert ospf[0].id not in {q.id for q in excl}


def test_query_multi_subtopics():
    res = BANK.query(exam="ccna", subtopics=["ospf", "wildcard_masks"])
    assert {q.subtopic for q in res} <= {"ospf", "wildcard_masks"}
    assert res


def test_get_and_contains():
    q = BANK.all()[0]
    assert q.id in BANK
    assert BANK.get(q.id) is q
