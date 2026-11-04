import random

from studyengine import DrillScheduler, get_blueprint, load_bank
from studyengine.progress import Profile

BANK = load_bank()
BP = get_blueprint("ccna")


def _sched():
    return DrillScheduler(BANK, "ccna", BP, rng=random.Random(42))


def test_missed_question_gets_higher_weight():
    prof = Profile("ccna")
    sch = _sched()
    q = BANK.get("ccna-na-001")
    before = sch.weight(q, prof)
    prof.record(q, False)             # miss -> box drops to 1
    after = sch.weight(q, prof)
    assert after > before


def test_mastery_lowers_weight():
    prof = Profile("ccna")
    sch = _sched()
    q = BANK.get("ccna-na-002")
    base = sch.weight(q, prof)
    for _ in range(4):
        prof.record(q, True)          # climb toward box 5
    assert sch.weight(q, prof) < base


def test_weak_subtopic_boosts_weight():
    prof = Profile("ccna")
    sch = _sched()
    # Make ospf weak but do not touch this specific question's own box.
    for _ in range(4):
        prof.record(BANK.get("ccna-ic-001"), False)
    q = BANK.get("ccna-ic-002")       # same subtopic 'ospf', still box 2
    assert prof.subtopic_accuracy("ospf") is not None
    assert prof.subtopic_accuracy("ospf") < 0.8
    # weight should exceed the neutral baseline for an unseen, non-weak question
    neutral = BP.weight_of(q.domain) * 5.0
    assert sch.weight(q, prof) > neutral


def test_remediation_targets_weak_subtopics():
    prof = Profile("ccna")
    sch = _sched()
    for _ in range(4):
        prof.record(BANK.get("ccna-ic-003"), False)   # wildcard_masks weak
    assert sch.remediation_available(prof)
    picks = {sch.next(prof, remediation=True).subtopic for _ in range(30)}
    assert "wildcard_masks" in picks


def test_next_avoids_recent():
    prof = Profile("ccna")
    sch = _sched()
    recent = [q.id for q in BANK.query(exam="ccna")[:-1]]  # suppress all but one
    nxt = sch.next(prof, recent_ids=recent)
    assert nxt.id not in set(recent)
