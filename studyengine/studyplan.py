"""Personalized study plan: turn a learner's results into an ordered, enforced
sequence of "master this sub-topic" steps, weakest-first.

The plan is derived live from the profile each time it is built, so it
re-prioritizes automatically as the learner improves: a sub-topic drops to
"done" the moment they reach the mastery bar, and the next weak area becomes
the current step.
"""
from __future__ import annotations

import random
from dataclasses import dataclass, field

from .bank import QuestionBank
from .blueprints import ExamBlueprint
from .curriculum import Curriculum
from .progress import Profile

MASTERY_TARGET = 0.8      # accuracy needed in a sub-topic to count as mastered
MIN_ATTEMPTS = 4          # how many questions you must answer there first


@dataclass
class PlanStep:
    subtopic: str
    domain: str
    domain_name: str
    weight: float
    seen: int
    correct: int
    accuracy: float | None       # None if never attempted
    mastered: bool
    need: int                    # attempts required to be eligible for mastery
    lesson_ids: list[str] = field(default_factory=list)
    status: str = "upcoming"     # "done" | "current" | "upcoming"

    @property
    def label(self) -> str:
        return self.subtopic.replace("_", " ")

    @property
    def pct(self) -> int | None:
        return round(self.accuracy * 100) if self.accuracy is not None else None

    def reason(self) -> str:
        """Plain-language why-this-is-here, for the learner."""
        if self.accuracy is None:
            return "You haven't been tested on this yet."
        if self.accuracy <= 0.0:
            return f"You missed this on the diagnostic (0%)."
        if self.accuracy < MASTERY_TARGET:
            return f"You're at {self.pct}% here — below the 80% target."
        return f"You're at {self.pct}% — almost there; lock it in."


def _domain_for(blueprint: ExamBlueprint, subtopic: str):
    for d in blueprint.domains:
        if subtopic in d.subtopics:
            return d
    return None


def is_mastered(seen: int, correct: int, need: int, target: float = MASTERY_TARGET) -> bool:
    return seen >= need and seen > 0 and (correct / seen) >= target


def build_plan(
    profile: Profile,
    bank: QuestionBank,
    curriculum: Curriculum,
    blueprint: ExamBlueprint,
    target: float = MASTERY_TARGET,
    min_attempts: int = MIN_ATTEMPTS,
) -> list[PlanStep]:
    """Build the ordered plan. Not-yet-mastered steps come first, weakest-first
    (lowest accuracy, then highest exam weight); mastered steps sit at the end."""
    stats = profile.subtopic_stats()  # {subtopic: (seen, correct, acc)}

    # Which lessons teach each sub-topic (for the "Read the lesson" action).
    lessons_by_sub: dict[str, list[str]] = {}
    for unit in curriculum.units_for(blueprint.code):
        for lesson in unit.lessons:
            for s in lesson.subtopics:
                lessons_by_sub.setdefault(s, [])
                if lesson.id not in lessons_by_sub[s]:
                    lessons_by_sub[s].append(lesson.id)

    steps: list[PlanStep] = []
    for st in bank.subtopics(blueprint.code):
        d = _domain_for(blueprint, st)
        if d is None:
            continue
        seen, correct, _ = stats.get(st, (0, 0, 0.0))
        available = len(bank.query(exam=blueprint.code, subtopic=st))
        need = max(1, min(min_attempts, available))
        acc = (correct / seen) if seen else None
        steps.append(PlanStep(
            subtopic=st, domain=d.key, domain_name=d.name, weight=d.weight,
            seen=seen, correct=correct, accuracy=acc,
            mastered=is_mastered(seen, correct, need, target), need=need,
            lesson_ids=lessons_by_sub.get(st, []),
        ))

    def urgency(step: PlanStep):
        # lower accuracy = more urgent; unseen sits at the target line; higher
        # exam weight breaks ties so high-impact domains surface sooner.
        acc = step.accuracy if step.accuracy is not None else target
        return (acc, -step.weight, step.subtopic)

    pending = sorted((s for s in steps if not s.mastered), key=urgency)
    done = sorted((s for s in steps if s.mastered), key=lambda s: s.subtopic)

    ordered = pending + done
    assigned_current = False
    for s in ordered:
        if s.mastered:
            s.status = "done"
        elif not assigned_current:
            s.status = "current"
            assigned_current = True
        else:
            s.status = "upcoming"
    return ordered


def plan_progress(steps: list[PlanStep]) -> tuple[int, int]:
    return sum(1 for s in steps if s.mastered), len(steps)


def current_step(steps: list[PlanStep]) -> PlanStep | None:
    return next((s for s in steps if s.status == "current"), None)


def next_question_for_subtopic(
    bank: QuestionBank,
    profile: Profile,
    exam: str,
    subtopic: str,
    rng: random.Random | None = None,
    exclude_id: str | None = None,
):
    """Pick the next drill question within one sub-topic, biased toward items the
    learner has missed (via the Leitner miss weight), avoiding an immediate repeat."""
    rng = rng or random.Random()
    pool = bank.query(exam=exam, subtopic=subtopic)
    if not pool:
        return None
    candidates = [q for q in pool if q.id != exclude_id] or pool
    weights = [profile.miss_weight(q.id) for q in candidates]
    return rng.choices(candidates, weights=weights, k=1)[0]
