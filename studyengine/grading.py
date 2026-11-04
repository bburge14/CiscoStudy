"""Grading and score aggregation shared by every study mode."""
from __future__ import annotations

from dataclasses import dataclass, field

from .bank import QuestionBank
from .models import Question


@dataclass
class Feedback:
    """The full instant-feedback payload shown after an answer."""
    question_id: str
    correct: bool
    selected: object
    correct_ids: list[str]
    why_correct: str
    distractor_notes: dict[str, str]
    exam_pattern: str
    verify_cli: list[str]
    references: list[str]


def grade(question: Question, selected) -> Feedback:
    ok = question.check(selected)
    return Feedback(
        question_id=question.id,
        correct=ok,
        selected=selected,
        correct_ids=list(question.correct),
        why_correct=question.explanation.correct,
        distractor_notes=dict(question.explanation.distractors),
        exam_pattern=question.explanation.exam_pattern,
        verify_cli=list(question.verify_cli),
        references=list(question.references),
    )


@dataclass
class DomainScore:
    domain: str
    seen: int = 0
    correct: int = 0

    @property
    def accuracy(self) -> float:
        return self.correct / self.seen if self.seen else 0.0

    @property
    def pct(self) -> int:
        return round(self.accuracy * 100)


@dataclass
class SessionScore:
    """Aggregate result of a quiz / exam / baseline run."""
    total: int = 0
    correct: int = 0
    by_domain: dict[str, DomainScore] = field(default_factory=dict)
    by_subtopic: dict[str, DomainScore] = field(default_factory=dict)

    @property
    def accuracy(self) -> float:
        return self.correct / self.total if self.total else 0.0

    @property
    def pct(self) -> int:
        return round(self.accuracy * 100)

    def passed(self, threshold: float = 0.8) -> bool:
        return self.total > 0 and self.accuracy >= threshold


def score_session(
    attempts: list[tuple[str, bool]],
    bank: QuestionBank,
) -> SessionScore:
    """Aggregate a list of (question_id, correct) attempts by domain/subtopic."""
    score = SessionScore()
    for qid, ok in attempts:
        q = bank.get(qid)
        score.total += 1
        score.correct += int(ok)

        d = score.by_domain.setdefault(q.domain, DomainScore(q.domain))
        d.seen += 1
        d.correct += int(ok)

        s = score.by_subtopic.setdefault(q.subtopic, DomainScore(q.subtopic))
        s.seen += 1
        s.correct += int(ok)
    return score
