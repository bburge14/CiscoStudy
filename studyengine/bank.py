"""Loads and indexes the authentic question bank from data/questions/*.json."""
from __future__ import annotations

import json
from pathlib import Path

from .models import Question

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


class QuestionBank:
    def __init__(self, questions: list[Question]):
        self._by_id: dict[str, Question] = {}
        dupes: set[str] = set()
        for q in questions:
            if q.id in self._by_id:
                dupes.add(q.id)
            self._by_id[q.id] = q
        if dupes:
            raise ValueError(f"duplicate question ids: {sorted(dupes)}")

    def __len__(self) -> int:
        return len(self._by_id)

    def __iter__(self):
        return iter(self._by_id.values())

    def __contains__(self, qid: str) -> bool:
        return qid in self._by_id

    def get(self, qid: str) -> Question:
        return self._by_id[qid]

    def all(self) -> list[Question]:
        return list(self._by_id.values())

    def query(
        self,
        exam: str | None = None,
        domain: str | None = None,
        subtopic: str | None = None,
        subtopics: list[str] | tuple[str, ...] | None = None,
        difficulty: int | None = None,
        ids: list[str] | None = None,
        exclude_ids: list[str] | set[str] | None = None,
    ) -> list[Question]:
        subset = set(subtopics) if subtopics else None
        idset = set(ids) if ids is not None else None
        exclude = set(exclude_ids) if exclude_ids else set()
        out: list[Question] = []
        for q in self._by_id.values():
            if idset is not None and q.id not in idset:
                continue
            if exam and q.exam != exam:
                continue
            if domain and q.domain != domain:
                continue
            if subtopic and q.subtopic != subtopic:
                continue
            if subset is not None and q.subtopic not in subset:
                continue
            if difficulty is not None and q.difficulty != difficulty:
                continue
            if q.id in exclude:
                continue
            out.append(q)
        return out

    def exams(self) -> list[str]:
        return sorted({q.exam for q in self._by_id.values()})

    def domains(self, exam: str) -> list[str]:
        return sorted({q.domain for q in self._by_id.values() if q.exam == exam})

    def subtopics(self, exam: str, domain: str | None = None) -> list[str]:
        return sorted({
            q.subtopic for q in self._by_id.values()
            if q.exam == exam and (domain is None or q.domain == domain)
        })

    def count_by_domain(self, exam: str) -> dict[str, int]:
        out: dict[str, int] = {}
        for q in self._by_id.values():
            if q.exam == exam:
                out[q.domain] = out.get(q.domain, 0) + 1
        return out


def load_bank(data_dir: str | Path = DATA_DIR) -> QuestionBank:
    """Load every data/questions/*.json file into a single QuestionBank."""
    qdir = Path(data_dir) / "questions"
    questions: list[Question] = []
    for jf in sorted(qdir.glob("*.json")):
        raw = json.loads(jf.read_text(encoding="utf-8"))
        items = raw["questions"] if isinstance(raw, dict) else raw
        for item in items:
            questions.append(Question.from_dict(item))
    return QuestionBank(questions)
