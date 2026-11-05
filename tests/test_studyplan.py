from studyengine import (
    build_plan,
    current_step,
    get_blueprint,
    load_bank,
    load_curriculum,
    plan_progress,
)
from studyengine.progress import Profile

BANK = load_bank()
CUR = load_curriculum()
BP = get_blueprint("ccna")


def test_plan_covers_exam_subtopics():
    steps = build_plan(Profile("ccna"), BANK, CUR, BP)
    subs = {s.subtopic for s in steps}
    assert subs == set(BANK.subtopics("ccna"))


def test_fresh_profile_first_step_is_current():
    steps = build_plan(Profile("ccna"), BANK, CUR, BP)
    cur = current_step(steps)
    assert cur is steps[0]
    assert cur.status == "current"
    assert all(not s.mastered for s in steps)  # nothing mastered yet
    done, total = plan_progress(steps)
    assert done == 0 and total == len(steps)


def test_missed_topic_sorts_before_unseen():
    prof = Profile("ccna")
    prof.record(BANK.get("ccna-ic-003"), False)  # wildcard_masks -> 0%
    steps = build_plan(prof, BANK, CUR, BP)
    pending = [s.subtopic for s in steps if not s.mastered]
    seen_subs = {s.subtopic for s in steps if s.seen > 0}
    unseen = [s for s in pending if s not in seen_subs]
    assert "wildcard_masks" in pending
    assert unseen, "expected some not-yet-seen subtopics"
    assert pending.index("wildcard_masks") < pending.index(unseen[0])


def test_subtopic_becomes_mastered_and_done():
    prof = Profile("ccna")
    sub = "ospf"
    qs = BANK.query(exam="ccna", subtopic=sub)
    need = min(4, len(qs))
    for i in range(need):
        prof.record(qs[i % len(qs)], True)   # answer correctly enough times
    steps = build_plan(prof, BANK, CUR, BP)
    by_sub = {s.subtopic: s for s in steps}
    assert by_sub[sub].mastered is True
    assert by_sub[sub].status == "done"
    # mastered steps sink below the still-pending ones
    statuses = [s.status for s in steps]
    assert statuses.index("done") > statuses.index("current")


def test_mastered_step_not_current():
    prof = Profile("ccna")
    # master a high-weight subtopic; current should be something else
    sub = "ospf"
    for q in BANK.query(exam="ccna", subtopic=sub)[:4]:
        prof.record(q, True)
    steps = build_plan(prof, BANK, CUR, BP)
    cur = current_step(steps)
    assert cur is not None and cur.subtopic != sub
