"""XP + levels derived from profile progress."""
from studyengine import compute_xp, level_info, mastered_subtopics, profile_level
from studyengine.leveling import LEVELS
from studyengine.progress import Profile
from studyengine import load_bank

BANK = load_bank()


def _q(qid):
    return BANK.get(qid)


def test_zero_progress_is_level_one_no_xp():
    li = profile_level(Profile("ccna"))
    assert li.level == 1 and li.xp == 0 and li.title == LEVELS[0][1]
    assert li.pct == 0.0 and not li.is_max


def test_correct_answers_earn_more_than_misses():
    p_right = Profile("ccna")
    p_wrong = Profile("ccna")
    q = _q("ccna-nf-001")
    p_right.record(q, True)
    p_wrong.record(q, False)
    assert compute_xp(p_right) > compute_xp(p_wrong)
    # a miss still earns a little participation XP
    assert compute_xp(p_wrong) > 0


def test_mastered_subtopic_awards_bonus():
    p = Profile("ccna")
    # 4 correct answers in the same subtopic -> mastered (>=4 attempts, 100%)
    for qid in ("ccna-ic-001", "ccna-ic-002", "ccna-ic-007", "ccna-ic-009"):
        p.record(_q(qid), True)
    mastered = mastered_subtopics(p)
    assert "ospf" in mastered
    # XP should exceed the plain correct+participation total thanks to the bonus
    base = 4 * 10 + 4 * 2
    assert compute_xp(p) >= base + 60


def test_level_thresholds_match_table():
    for i, (thr, title) in enumerate(LEVELS):
        li = level_info(thr)
        assert li.level == i + 1 and li.title == title
        # one XP below the next threshold is still the current level
        if i + 1 < len(LEVELS):
            below = level_info(LEVELS[i + 1][0] - 1)
            assert below.level == i + 1


def test_progress_fraction_is_bounded_and_max_level_caps():
    mid = level_info((LEVELS[0][0] + LEVELS[1][0]) // 2)
    assert 0.0 < mid.pct < 1.0 and mid.to_next > 0
    top = level_info(LEVELS[-1][0] + 5000)
    assert top.is_max and top.level == len(LEVELS) and top.pct == 1.0 and top.to_next == 0


def test_milestones_and_lessons_add_xp_but_diagnostic_does_not():
    p = Profile("ccna")
    base = compute_xp(p)
    p.baseline = {"overall": 60}          # taking the benchmark earns NO XP
    assert compute_xp(p) == base
    p.passed_milestones.add("unit-1")
    p.completed_lessons.add("lesson-1")
    assert compute_xp(p) == base + 120 + 25


def _ccna_ids(n):
    return [q.id for q in BANK.all() if q.exam == "ccna"][:n]


def test_diagnostic_answers_excluded_from_study_and_xp():
    p = Profile("ccna")
    ids = _ccna_ids(12)
    bench, study_q = ids[:10], ids[10]
    # simulate the diagnostic: record AND mark as a benchmark answer
    for qid in bench:
        q = _q(qid)
        p.record(q, True)
        p.note_baseline_answer(q, True)
    # benchmark alone: no study progress, no XP, still level 1
    assert p.study_overall() == (0, 0)
    assert compute_xp(p) == 0
    assert profile_level(p).level == 1
    # a real study answer (not a benchmark) now counts
    p.record(_q(study_q), True)
    assert p.study_overall() == (1, 1)
    assert compute_xp(p) == 12          # 1*10 + 1*2


def test_mastery_counts_study_attempts_only():
    p = Profile("ccna")
    ospf = [q.id for q in BANK.all() if q.exam == "ccna" and q.subtopic == "ospf"][:5]
    # 4 correct in ospf, but the FIRST was a benchmark answer -> only 3 study attempts
    for i, qid in enumerate(ospf[:4]):
        q = _q(qid)
        p.record(q, True)
        if i == 0:
            p.note_baseline_answer(q, True)
    assert "ospf" not in mastered_subtopics(p)   # 3 study attempts < 4
    # a 4th STUDY answer reaches the mastery threshold
    p.record(_q(ospf[4]), True)
    assert "ospf" in mastered_subtopics(p)


def test_legacy_baseline_backfilled_on_load():
    # An old profile that took the diagnostic before the split has no
    # baseline_stats; from_dict should backfill so the benchmark is excluded.
    p = Profile("ccna")
    # Realistic diagnostic spread: one question from each of 30 distinct
    # sub-topics (the real baseline samples per-domain, not clustered).
    seen_subs: set[str] = set()
    ids: list[str] = []
    for q in BANK.all():
        if q.exam == "ccna" and q.subtopic not in seen_subs:
            seen_subs.add(q.subtopic)
            ids.append(q.id)
        if len(ids) == 30:
            break
    for qid in ids:
        p.record(_q(qid), True)           # the old diagnostic recorded these
    p.baseline = {"overall": 100, "total": 30, "ts": 0}
    raw = p.to_dict()
    raw["baseline_stats"] = None           # simulate the pre-split format
    p2 = Profile.from_dict(raw)
    assert p2.baseline_stats is not None
    assert p2.study_overall() == (0, 0)    # all 30 were the benchmark
    assert compute_xp(p2) == 0
