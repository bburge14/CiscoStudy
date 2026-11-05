"""Event-based XP + levels: reward getting better + streaks, penalize misses."""
from studyengine import compute_xp, level_info, mastered_subtopics, profile_level
from studyengine.leveling import LEVELS, XP_PER_LESSON, XP_PER_MILESTONE
from studyengine.progress import Profile
from studyengine import load_bank

BANK = load_bank()


def _q(qid):
    return BANK.get(qid)


def _ccna_ids(n):
    return [q.id for q in BANK.all() if q.exam == "ccna"][:n]


def test_zero_progress_is_level_one_no_xp():
    li = profile_level(Profile("ccna"))
    assert li.level == 1 and li.xp == 0 and li.title == LEVELS[0][1]
    assert li.pct == 0.0 and not li.is_max


def test_correct_earns_xp_but_a_miss_alone_floors_at_zero():
    pr, pw = Profile("ccna"), Profile("ccna")
    q = _q(_ccna_ids(1)[0])
    assert pr.record_study(q, True)["delta"] > 0
    assert pw.record_study(q, False)["delta"] < 0   # a miss COSTS xp
    assert compute_xp(pr) > 0
    assert compute_xp(pw) == 0                       # but xp never goes negative


def test_streak_bonus_grows_the_reward():
    p = Profile("ccna")
    deltas = [p.record_study(_q(qid), True)["delta"] for qid in _ccna_ids(6)]
    assert deltas[-1] > deltas[0]      # later answers in a streak are worth more
    assert p.best_streak == 6 and p.answer_streak == 6


def test_miss_resets_streak_and_reduces_xp():
    p = Profile("ccna")
    ids = _ccna_ids(4)
    for qid in ids[:3]:
        p.record_study(_q(qid), True)
    before = p.xp
    info = p.record_study(_q(ids[3]), False)
    assert info["delta"] < 0 and p.answer_streak == 0 and p.xp < before


def test_regression_costs_more_than_a_fresh_miss():
    p1, p2 = Profile("ccna"), Profile("ccna")
    q1 = _q(_ccna_ids(2)[0])
    p1.record_study(q1, True)          # box 2 -> 3
    p1.record_study(q1, True)          # box 3 -> 4
    reg = p1.record_study(q1, False)   # missing one you had down -> regression
    fresh = p2.record_study(_q(_ccna_ids(2)[1]), False)   # a brand-new miss
    assert reg["regressed"] and not fresh["regressed"]
    assert reg["delta"] < fresh["delta"]


def test_mastering_a_question_awards_a_big_bonus():
    p = Profile("ccna")
    q = _q(_ccna_ids(1)[0])
    infos = [p.record_study(q, True) for _ in range(4)]   # box 2->3->4->5->5
    assert any(i["mastered"] for i in infos)
    mastered_delta = next(i["delta"] for i in infos if i["mastered"])
    assert mastered_delta >= 20
    # re-answering an already-mastered item earns almost nothing (anti-farm)
    assert infos[-1]["delta"] <= 6


def test_diagnostic_earns_no_xp_but_study_does():
    p = Profile("ccna")
    ids = _ccna_ids(12)
    bench, study_q = ids[:10], ids[10]
    for qid in bench:                    # the benchmark path: record + note, NO xp
        q = _q(qid)
        p.record(q, True)
        p.note_baseline_answer(q, True)
    assert p.study_overall() == (0, 0)
    assert compute_xp(p) == 0 and profile_level(p).level == 1
    assert p.record_study(_q(study_q), True)["delta"] > 0
    assert compute_xp(p) > 0


def test_milestones_and_lessons_add_xp_but_diagnostic_does_not():
    p = Profile("ccna")
    p.baseline = {"overall": 60}          # taking the benchmark earns NO xp
    assert compute_xp(p) == 0
    p.passed_milestones.add("unit-1")
    p.completed_lessons.add("lesson-1")
    assert compute_xp(p) == XP_PER_MILESTONE + XP_PER_LESSON


def test_mastery_counts_study_attempts_only():
    p = Profile("ccna")
    ospf = [q.id for q in BANK.all() if q.exam == "ccna" and q.subtopic == "ospf"][:5]
    for i, qid in enumerate(ospf[:4]):
        q = _q(qid)
        p.record(q, True)
        if i == 0:
            p.note_baseline_answer(q, True)   # one was the benchmark
    assert "ospf" not in mastered_subtopics(p)   # 3 study attempts < 4
    p.record(_q(ospf[4]), True)
    assert "ospf" in mastered_subtopics(p)


def test_level_thresholds_match_table():
    for i, (thr, title) in enumerate(LEVELS):
        li = level_info(thr)
        assert li.level == i + 1 and li.title == title
        if i + 1 < len(LEVELS):
            assert level_info(LEVELS[i + 1][0] - 1).level == i + 1


def test_progress_fraction_bounded_and_max_level_caps():
    mid = level_info((LEVELS[0][0] + LEVELS[1][0]) // 2)
    assert 0.0 < mid.pct < 1.0 and mid.to_next > 0
    top = level_info(LEVELS[-1][0] + 9000)
    assert top.is_max and top.level == len(LEVELS) and top.pct == 1.0 and top.to_next == 0


def test_leveling_takes_longer_than_trivial_grinding():
    # answering ~20 questions right should NOT be near the top; level 2 is real work
    p = Profile("ccna")
    for qid in _ccna_ids(20):
        p.record_study(_q(qid), True)
    assert profile_level(p).level <= 2   # a short correct run is early-game only


def test_xp_and_streak_persist_through_serialization():
    p = Profile("ccna")
    for qid in _ccna_ids(3):
        p.record_study(_q(qid), True)
    p2 = Profile.from_dict(p.to_dict())
    assert p2.xp == p.xp and p2.answer_streak == p.answer_streak


def test_legacy_profile_without_xp_is_backfilled():
    # A pre-event-XP profile (no "xp" key) gets a fair starting XP from study.
    p = Profile("ccna")
    ids = _ccna_ids(10)
    for qid in ids:
        p.record(_q(qid), True)           # old-style recording (no xp field)
    raw = p.to_dict()
    raw.pop("xp", None)
    raw.pop("answer_streak", None)
    p2 = Profile.from_dict(raw)
    assert p2.xp > 0                       # backfilled from study-correct count
