import random

from studyengine import build_exam, exam_readiness, exam_time_limit, get_blueprint, load_bank
from studyengine.progress import Profile

BANK = load_bank()
BP = get_blueprint("ccna")


def test_build_exam_size_and_no_dups():
    qs = build_exam(BANK, BP, size=30, rng=random.Random(1))
    assert 0 < len(qs) <= 30
    ids = [q.id for q in qs]
    assert len(ids) == len(set(ids))
    assert all(q.exam == "ccna" for q in qs)


def test_build_exam_covers_weighted_domains():
    qs = build_exam(BANK, BP, size=40, rng=random.Random(2))
    doms = {q.domain for q in qs}
    assert "ip_connectivity" in doms and "network_access" in doms


def test_time_limit():
    assert exam_time_limit(40) == 40 * 75


def test_readiness_none_when_empty():
    r = exam_readiness(Profile("ccna"), BP)
    assert r["estimate"] is None
    assert r["coverage"] == 0
    assert r["ready"] is False


def test_readiness_partial_coverage_not_ready():
    prof = Profile("ccna")
    for q in BANK.query(exam="ccna", domain="ip_connectivity"):
        prof.record(q, True)
    r = exam_readiness(prof, BP)
    assert r["estimate"] == 100          # the one practiced domain is perfect
    assert 0 < r["coverage"] < 100       # but only part of the exam is covered
    assert r["ready"] is False


def test_readiness_ready_when_strong_and_fully_covered():
    prof = Profile("ccna")
    for q in BANK.query(exam="ccna"):
        prof.record(q, True)
    r = exam_readiness(prof, BP)
    assert r["estimate"] == 100
    assert r["coverage"] == 100
    assert r["ready"] is True
