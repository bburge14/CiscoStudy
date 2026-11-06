"""The interactive CompTIA PBQ engine: every task is well-formed and grades
only a fully-correct arrangement as passing."""
import pytest

from studyengine.perf import (
    PERF_TASKS,
    get_perf_task,
    is_perf_task,
    perf_tasks_for,
)


def test_every_live_comptia_track_has_tasks():
    assert len(PERF_TASKS) >= 8
    for exam in ("secplus", "netplus", "aplus1", "aplus2"):
        assert perf_tasks_for(exam), f"{exam} has no performance tasks"


def test_ids_unique_and_resolvable():
    ids = [t.id for t in PERF_TASKS]
    assert len(ids) == len(set(ids))
    for i in ids:
        assert is_perf_task(i)
        assert get_perf_task(i).id == i


@pytest.mark.parametrize("t", PERF_TASKS, ids=lambda t: t.id)
def test_task_wellformed_and_grades(t):
    assert t.kind in ("categorize", "match", "order")
    rows = t.rows()
    assert rows, f"{t.id}: no rows"

    # the keyed-correct value is always an available choice
    for key, _label, choices, correct in rows:
        assert correct in choices, f"{t.id}:{key} correct not in choices"

    # a fully-correct arrangement passes
    right = {k: c for k, _l, _ch, c in rows}
    assert t.passed(right), f"{t.id}: correct arrangement should pass"

    # changing any row to a different valid choice fails the whole task
    wrong = {}
    for k, _l, ch, c in rows:
        wrong[k] = next((o for o in ch if o != c), c)
    assert not t.passed(wrong), f"{t.id}: wrong arrangement should fail"

    # an empty/partial arrangement fails
    assert not t.passed({}), f"{t.id}: empty answer should fail"
