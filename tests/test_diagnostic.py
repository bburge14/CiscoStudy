import random

from studyengine import (
    build_baseline,
    get_blueprint,
    load_bank,
    recommend_focus,
    score_session,
)

BANK = load_bank()


def test_baseline_is_five_per_domain():
    for exam in ("ccna", "encor"):
        bp = get_blueprint(exam)
        base = build_baseline(BANK, bp, per_domain=5, rng=random.Random(7))
        assert len(base) == 30
        per = {}
        for q in base:
            per[q.domain] = per.get(q.domain, 0) + 1
        for d in bp.domains:
            assert per[d.key] == 5


def test_baseline_items_belong_to_exam():
    bp = get_blueprint("encor")
    base = build_baseline(BANK, bp, rng=random.Random(8))
    assert all(q.exam == "encor" for q in base)


def test_recommend_focus_orders_weakest_first():
    bp = get_blueprint("ccna")
    base = build_baseline(BANK, bp, rng=random.Random(9))
    # Simulate: everything right except two domains made weak.
    attempts = []
    for q in base:
        ok = q.domain not in ("ip_connectivity", "security_fundamentals")
        attempts.append((q.id, ok))
    score = score_session(attempts, BANK)
    recs = recommend_focus(score, bp, threshold=0.8)
    weak_domains = {r.domain for r in recs}
    assert "ip_connectivity" in weak_domains
    assert "security_fundamentals" in weak_domains
    # strongest (passed) domains are not flagged
    assert "automation" not in weak_domains
    # sorted weakest (lowest pct) first
    pcts = [r.pct for r in recs]
    assert pcts == sorted(pcts)
