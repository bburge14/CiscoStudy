"""Adaptive endless-drill scheduler.

Weight of a candidate question = domain blueprint weight (so the stream mirrors
exam proportions) x Leitner miss-boost (missed items resurface ~8x) x subtopic
weakness multiplier (below-80% subtopics are pushed harder). Recently served
items are suppressed to avoid immediate repeats.
"""
from __future__ import annotations

import random

from .bank import QuestionBank
from .blueprints import ExamBlueprint
from .models import Question
from .progress import MASTERY_THRESHOLD, Profile


class DrillScheduler:
    def __init__(
        self,
        bank: QuestionBank,
        exam: str,
        blueprint: ExamBlueprint,
        rng: random.Random | None = None,
    ):
        self.bank = bank
        self.exam = exam
        self.blueprint = blueprint
        self.rng = rng or random.Random()
        self._pool: list[Question] = bank.query(exam=exam)

    def weight(self, q: Question, profile: Profile) -> float:
        try:
            w = self.blueprint.weight_of(q.domain)
        except KeyError:
            w = 0.15
        w *= profile.miss_weight(q.id)
        acc = profile.subtopic_accuracy(q.subtopic)
        if acc is not None and acc < MASTERY_THRESHOLD:
            w *= 1.0 + (MASTERY_THRESHOLD - acc) * 3.0
        return max(w, 1e-6)

    def next(
        self,
        profile: Profile,
        recent_ids: list[str] | tuple[str, ...] = (),
        remediation: bool = False,
    ) -> Question | None:
        if not self._pool:
            return None
        recent = set(recent_ids)
        pool = [q for q in self._pool if q.id not in recent]

        if remediation:
            weak = {s for s, _, _ in profile.weak_subtopics()}
            if weak:
                weak_pool = [q for q in pool if q.subtopic in weak]
                if weak_pool:
                    pool = weak_pool

        if not pool:  # exhausted suppression window -> allow repeats
            pool = self._pool

        weights = [self.weight(q, profile) for q in pool]
        return self.rng.choices(pool, weights=weights, k=1)[0]

    def remediation_available(self, profile: Profile) -> bool:
        weak = {s for s, _, _ in profile.weak_subtopics()}
        if not weak:
            return False
        return any(q.subtopic in weak for q in self._pool)
