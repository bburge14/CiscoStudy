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


def test_milestones_and_diagnostic_add_xp():
    p = Profile("ccna")
    base = compute_xp(p)
    p.baseline = {"overall": 60}
    p.passed_milestones.add("unit-1")
    p.completed_lessons.add("lesson-1")
    assert compute_xp(p) == base + 50 + 120 + 25
