import random

from studyengine import (
    lesson_markdown,
    lesson_quiz,
    load_bank,
    load_curriculum,
    milestone_exam,
)
from studyengine.cli_sim import SCENARIOS
from studyengine.perf import is_perf_task

BANK = load_bank()
CUR = load_curriculum()


def test_units_exist_for_each_track():
    expected = {"ccna": 6, "encor": 6, "secplus": 5, "netplus": 5, "aplus1": 5, "aplus2": 4,
                "isc2cc": 5, "sc900": 4, "az900": 3, "clf": 4, "ms900": 4,
                "cysa": 4, "cbrops": 5, "sscp": 7, "cisa": 5, "cism": 4,
                "cissp": 8, "ceh": 6, "pentest": 5, "securityx": 4}
    for exam, n in expected.items():
        assert len(CUR.units_for(exam)) == n, exam


def test_every_lesson_markdown_resolves():
    for u in CUR.all():
        for les in u.lessons:
            md = lesson_markdown(les)
            assert not md.startswith("> Lesson content not found"), les.markdown_path
            assert len(md) > 200, f"{les.markdown_path} looks too short to be a real lesson"


def test_unit_pbq_ids_reference_real_scenarios():
    for u in CUR.all():
        if u.pbq_id is not None:
            assert u.pbq_id in SCENARIOS or is_perf_task(u.pbq_id), \
                f"{u.id} references unknown PBQ {u.pbq_id}"


def test_lesson_quiz_within_subtopics_and_size():
    les = CUR.lesson("ccna-l-ospf")
    quiz = lesson_quiz(BANK, les, rng=random.Random(1))
    assert quiz
    assert len(quiz) <= les.quiz_size
    assert {q.subtopic for q in quiz} <= set(les.subtopics)


def test_milestone_is_cumulative():
    units = CUR.units_for("ccna")
    first = milestone_exam(BANK, CUR, units[0], rng=random.Random(2))
    last = milestone_exam(BANK, CUR, units[-1], rng=random.Random(2))
    # cumulative pool grows, so the final unit draws from strictly more material
    assert len(last) >= len(first)
    assert len(last) <= units[-1].milestone_size


def test_milestone_pool_respects_size_cap():
    u = CUR.unit("ccna-u6")
    exam = milestone_exam(BANK, CUR, u, size=10, rng=random.Random(3))
    assert len(exam) == 10
