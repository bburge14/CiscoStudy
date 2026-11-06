"""Guards the authenticity contract: every item is well-formed, blueprint-tagged,
internally consistent, and the pools are deep enough for the baseline/exam modes.
"""
import pytest

from studyengine import get_blueprint, load_bank

BANK = load_bank()


def test_bank_nonempty():
    assert len(BANK) >= 50


@pytest.mark.parametrize("q", BANK.all(), ids=lambda q: q.id)
def test_question_wellformed(q):
    bp = get_blueprint(q.exam)
    valid_subtopics = {st for d in bp.domains for st in d.subtopics}

    assert q.domain in bp.domain_keys, f"{q.id}: domain not in blueprint"
    assert q.subtopic in valid_subtopics, f"{q.id}: subtopic not in blueprint"
    assert q.explanation.correct.strip(), f"{q.id}: missing why-correct explanation"
    assert q.type in ("mcq", "multi", "fill")

    if q.type in ("mcq", "multi"):
        opt_ids = {o.id for o in q.options}
        assert len(opt_ids) >= 2, f"{q.id}: needs >= 2 options"
        assert len(opt_ids) == len(q.options), f"{q.id}: duplicate option ids"
        for c in q.correct:
            assert c in opt_ids, f"{q.id}: correct {c} not an option"
        for dk in q.explanation.distractors:
            assert dk in opt_ids, f"{q.id}: distractor note {dk} not an option"
        if q.type == "multi":
            assert len(q.correct) >= 2, f"{q.id}: multi needs >= 2 correct"
    else:  # fill
        assert q.correct, f"{q.id}: fill needs accepted answers"
        assert not q.options, f"{q.id}: fill should not define options"


@pytest.mark.parametrize("exam", ["ccna", "encor", "secplus", "netplus", "aplus1", "aplus2"])
def test_five_per_domain_for_baseline(exam):
    counts = BANK.count_by_domain(exam)
    bp = get_blueprint(exam)
    for d in bp.domains:
        assert counts.get(d.key, 0) >= 5, f"{exam}:{d.key} has < 5 items"


def test_ids_unique_across_bank():
    ids = [q.id for q in BANK.all()]
    assert len(ids) == len(set(ids))


def test_mcq_has_exactly_one_correct():
    for q in BANK.all():
        if q.type == "mcq":
            assert len(q.correct) == 1, f"{q.id}: mcq must have exactly one key"


def test_hot_topics_present():
    """The brief calls out these specifically — make sure authentic items exist."""
    subtopics = {q.subtopic for q in BANK.all()}
    for required in ("stp_root_election", "ospf", "wildcard_masks", "etherchannel",
                     "netconf_restconf"):
        assert required in subtopics, f"missing required subtopic coverage: {required}"
