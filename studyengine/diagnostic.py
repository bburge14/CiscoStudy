"""Diagnostic baseline: 5 questions per official domain (30 total)."""
from __future__ import annotations

import random
from dataclasses import dataclass

from .bank import QuestionBank
from .blueprints import ExamBlueprint
from .grading import SessionScore
from .models import Question


def build_baseline(
    bank: QuestionBank,
    blueprint: ExamBlueprint,
    per_domain: int = 5,
    rng: random.Random | None = None,
) -> list[Question]:
    """One sample of `per_domain` items from each blueprint domain, shuffled."""
    rng = rng or random.Random()
    items: list[Question] = []
    for d in blueprint.domains:
        pool = bank.query(exam=blueprint.code, domain=d.key)
        if len(pool) <= per_domain:
            items.extend(pool)
        else:
            items.extend(rng.sample(pool, per_domain))
    rng.shuffle(items)
    return items


@dataclass
class DomainRecommendation:
    domain: str
    name: str
    pct: int
    weight: float
    seen: int


def recommend_focus(
    score: SessionScore,
    blueprint: ExamBlueprint,
    threshold: float = 0.8,
) -> list[DomainRecommendation]:
    """Blueprint domains scoring below `threshold`, weakest-first.

    Ties are broken by exam weight so the learner's time goes where it buys the
    most score on the real exam.
    """
    recs: list[DomainRecommendation] = []
    for d in blueprint.domains:
        ds = score.by_domain.get(d.key)
        if ds is None or ds.seen == 0:
            continue
        if ds.accuracy < threshold:
            recs.append(DomainRecommendation(d.key, d.name, ds.pct, d.weight, ds.seen))
    recs.sort(key=lambda r: (r.pct, -r.weight))
    return recs
