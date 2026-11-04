"""Persistent per-learner progress: mastery boxes, accuracy and milestones.

Each question carries a Leitner-style box (1=struggling .. 5=mastered). A miss
drops the box to 1, which the drill scheduler reads as a large frequency boost
so missed items resurface far more often. Accuracy is aggregated by subtopic
and domain to drive the <80% remediation queue.
"""
from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

from .models import Question

# Box -> relative sampling weight. Box 1 (just missed) is sampled 8x a mastered
# item; unseen questions default to box 2.
BOX_WEIGHT: dict[int, float] = {1: 8.0, 2: 5.0, 3: 3.0, 4: 2.0, 5: 1.0}
MASTERY_THRESHOLD = 0.8


@dataclass
class QStat:
    domain: str = ""
    subtopic: str = ""
    seen: int = 0
    correct: int = 0
    box: int = 2
    streak: int = 0           # +ve = consecutive right, -ve = consecutive wrong
    last_seen: float = 0.0

    @property
    def accuracy(self) -> float:
        return self.correct / self.seen if self.seen else 0.0


@dataclass
class Profile:
    exam: str
    q: dict[str, QStat] = field(default_factory=dict)
    baseline: dict | None = None
    completed_lessons: set[str] = field(default_factory=set)
    passed_milestones: set[str] = field(default_factory=set)
    created: float = field(default_factory=time.time)

    # -- recording ---------------------------------------------------------
    def record(self, question: Question, correct: bool) -> QStat:
        st = self.q.get(question.id)
        if st is None:
            st = QStat(domain=question.domain, subtopic=question.subtopic)
            self.q[question.id] = st
        st.domain = question.domain
        st.subtopic = question.subtopic
        st.seen += 1
        st.last_seen = time.time()
        if correct:
            st.correct += 1
            st.streak = st.streak + 1 if st.streak >= 0 else 1
            st.box = min(5, st.box + 1)
        else:
            st.streak = st.streak - 1 if st.streak <= 0 else -1
            st.box = 1
        return st

    # -- scheduler hooks ---------------------------------------------------
    def box_of(self, qid: str) -> int:
        st = self.q.get(qid)
        return st.box if st else 2

    def miss_weight(self, qid: str) -> float:
        return BOX_WEIGHT.get(self.box_of(qid), 5.0)

    # -- aggregation -------------------------------------------------------
    def _agg(self, attr: str) -> dict[str, tuple[int, int]]:
        out: dict[str, list[int]] = {}
        for st in self.q.values():
            key = getattr(st, attr)
            if not key:
                continue
            rec = out.setdefault(key, [0, 0])
            rec[0] += st.seen
            rec[1] += st.correct
        return {k: (s, c) for k, (s, c) in out.items()}

    def subtopic_stats(self) -> dict[str, tuple[int, int, float]]:
        return {k: (s, c, (c / s if s else 0.0)) for k, (s, c) in self._agg("subtopic").items()}

    def domain_stats(self) -> dict[str, tuple[int, int, float]]:
        return {k: (s, c, (c / s if s else 0.0)) for k, (s, c) in self._agg("domain").items()}

    def subtopic_accuracy(self, subtopic: str) -> float | None:
        agg = self._agg("subtopic").get(subtopic)
        if not agg or agg[0] == 0:
            return None
        return agg[1] / agg[0]

    def weak_subtopics(
        self, threshold: float = MASTERY_THRESHOLD, min_seen: int = 3
    ) -> list[tuple[str, float, int]]:
        """Subtopics with enough attempts and accuracy below threshold.

        Returned worst-first as (subtopic, accuracy, seen) — the remediation queue.
        """
        rows: list[tuple[str, float, int]] = []
        for st_key, (seen, correct) in self._agg("subtopic").items():
            if seen < min_seen:
                continue
            acc = correct / seen
            if acc < threshold:
                rows.append((st_key, acc, seen))
        rows.sort(key=lambda r: (r[1], -r[2]))
        return rows

    def overall(self) -> tuple[int, int]:
        seen = sum(st.seen for st in self.q.values())
        correct = sum(st.correct for st in self.q.values())
        return seen, correct

    # -- (de)serialisation -------------------------------------------------
    def to_dict(self) -> dict:
        return {
            "exam": self.exam,
            "created": self.created,
            "baseline": self.baseline,
            "completed_lessons": sorted(self.completed_lessons),
            "passed_milestones": sorted(self.passed_milestones),
            "q": {qid: asdict(st) for qid, st in self.q.items()},
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Profile":
        prof = cls(exam=d["exam"])
        prof.created = d.get("created", time.time())
        prof.baseline = d.get("baseline")
        prof.completed_lessons = set(d.get("completed_lessons", []))
        prof.passed_milestones = set(d.get("passed_milestones", []))
        for qid, st in d.get("q", {}).items():
            prof.q[qid] = QStat(**st)
        return prof

    def save(self, path: str | Path) -> None:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(self.to_dict(), indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: str | Path, exam: str) -> "Profile":
        p = Path(path)
        if p.exists():
            try:
                return cls.from_dict(json.loads(p.read_text(encoding="utf-8")))
            except (json.JSONDecodeError, KeyError):
                pass
        return cls(exam=exam)
