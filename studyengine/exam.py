"""Timed exam simulation + readiness estimate.

Neither is a promise about the real exam: the readiness number is an estimate
from the learner's own practice accuracy, weighted by the official domain
weights, and the pass line is a study proxy (Cisco's real cut score is a scaled
value that is not published).
"""
from __future__ import annotations

import random

from .bank import QuestionBank
from .blueprints import ExamBlueprint

# Study proxy. The real CCNA/ENCOR cut score is a scaled ~825/1000 and the exact
# mapping is not published, so we hold learners to a conservative 80%.
PASS_SCORE = 0.80


def exam_readiness(profile, blueprint: ExamBlueprint,
                   strong: float = 0.85, ok: float = 0.78) -> dict:
    """Estimate readiness from practice accuracy, weighted by domain weight."""
    dstats = profile.domain_stats()  # {domain: (seen, correct, acc)}
    covered = 0.0
    weighted = 0.0
    rows = []
    for d in blueprint.domains:
        seen, correct, _ = dstats.get(d.key, (0, 0, 0.0))
        acc = (correct / seen) if seen else None
        rows.append({"domain": d.key, "name": d.name, "weight": d.weight,
                     "seen": seen, "accuracy": acc})
        if seen:
            weighted += d.weight * (correct / seen)
            covered += d.weight

    estimate = round(weighted / covered * 100) if covered else None
    coverage = round(covered * 100)

    if estimate is None or coverage < 40:
        verdict, ready = "Not enough practice yet for a reliable estimate", False
    elif estimate >= round(strong * 100) and coverage >= 80:
        verdict, ready = "On track to pass", True
    elif estimate >= round(ok * 100):
        verdict, ready = "Close — tighten your weak domains", False
    else:
        verdict, ready = "Keep studying", False

    return {"estimate": estimate, "coverage": coverage, "verdict": verdict,
            "ready": ready, "rows": rows}


def exam_time_limit(n_questions: int, per_question: int = 75) -> int:
    """Seconds for a mock of n questions (~1.25 min each, like the real pace)."""
    return n_questions * per_question


def build_exam(bank: QuestionBank, blueprint: ExamBlueprint,
               size: int = 40, rng: random.Random | None = None):
    """A domain-weighted, shuffled question set for a mock exam."""
    rng = rng or random.Random()
    items = []
    for d in blueprint.domains:
        pool = bank.query(exam=blueprint.code, domain=d.key)
        n = min(max(1, round(size * d.weight)), len(pool))
        items.extend(rng.sample(pool, n))
    # Top up toward the requested size from whatever is left, without duplicates.
    if len(items) < size:
        chosen = {q.id for q in items}
        extra = [q for q in bank.query(exam=blueprint.code) if q.id not in chosen]
        rng.shuffle(extra)
        items.extend(extra[: size - len(items)])
    rng.shuffle(items)
    return items[:size]
