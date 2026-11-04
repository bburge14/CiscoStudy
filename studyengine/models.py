"""Core data models for questions, lessons, units and their explanations.

Questions carry the full feedback loop the platform promises: why the key is
correct, why each Cisco distractor is a trap, and the pattern cue for spotting
the item type on the real exam. The grading logic lives on the model so the UI
and the test suite grade answers identically.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field


def _normalize(text: str) -> str:
    """Normalise free-text answers: lowercase, collapse whitespace, strip."""
    return re.sub(r"\s+", " ", str(text).strip().lower())


@dataclass(frozen=True)
class Option:
    id: str
    text: str


@dataclass
class Explanation:
    correct: str
    distractors: dict[str, str] = field(default_factory=dict)
    exam_pattern: str = ""


@dataclass
class Question:
    id: str
    exam: str                 # "ccna" | "encor"
    domain: str               # blueprint domain key
    subtopic: str             # blueprint subtopic key
    type: str                 # "mcq" | "multi" | "fill"
    stem: str
    options: list[Option]
    correct: list[str]        # option ids, or accepted strings for "fill"
    explanation: Explanation
    difficulty: int = 2       # 1 easy .. 3 hard
    exhibit: str = ""         # CLI / show output / topology block (monospace)
    select_count: int = 1     # how many to choose (multi)
    verify_cli: list[str] = field(default_factory=list)
    references: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)

    # -- derived -----------------------------------------------------------
    @property
    def is_multi(self) -> bool:
        return self.type == "multi" or len(self.correct) > 1

    @property
    def is_fill(self) -> bool:
        return self.type == "fill"

    def option(self, oid: str) -> Option:
        for o in self.options:
            if o.id == oid:
                return o
        raise KeyError(f"{self.id}: no option {oid!r}")

    # -- grading -----------------------------------------------------------
    def check(self, selected) -> bool:
        """Return True if `selected` is a fully correct answer.

        For mcq/multi, `selected` is an option id or an iterable of ids and
        must match the key set exactly. For fill, `selected` is a string and
        is matched case/space-insensitively against any accepted answer.
        """
        if self.is_fill:
            if selected is None:
                return False
            norm = _normalize(selected)
            return any(norm == _normalize(c) for c in self.correct)
        if selected is None:
            return False
        if isinstance(selected, (list, set, tuple)):
            chosen = {str(s) for s in selected}
        else:
            chosen = {str(selected)}
        return chosen == {str(c) for c in self.correct}

    # -- (de)serialisation -------------------------------------------------
    @classmethod
    def from_dict(cls, d: dict) -> "Question":
        missing = [k for k in ("id", "exam", "domain", "subtopic", "stem", "correct") if k not in d]
        if missing:
            raise ValueError(f"question {d.get('id', '??')} missing keys: {missing}")

        exp_raw = d.get("explanation", {})
        if isinstance(exp_raw, str):
            explanation = Explanation(correct=exp_raw)
        else:
            explanation = Explanation(
                correct=exp_raw.get("correct", ""),
                distractors=dict(exp_raw.get("distractors", {})),
                exam_pattern=exp_raw.get("exam_pattern", ""),
            )

        options = [Option(o["id"], o["text"]) for o in d.get("options", [])]
        correct = d["correct"]
        if isinstance(correct, str):
            correct = [correct]
        correct = [str(c) for c in correct]

        qtype = d.get("type", "mcq")
        if qtype not in ("mcq", "multi", "fill"):
            raise ValueError(f"question {d['id']}: bad type {qtype!r}")

        default_select = len(correct) if qtype == "multi" else 1
        return cls(
            id=d["id"], exam=d["exam"], domain=d["domain"], subtopic=d["subtopic"],
            type=qtype, stem=d["stem"], options=options, correct=correct,
            explanation=explanation, difficulty=int(d.get("difficulty", 2)),
            exhibit=d.get("exhibit", ""), select_count=int(d.get("select_count", default_select)),
            verify_cli=list(d.get("verify_cli", [])),
            references=list(d.get("references", [])),
            tags=list(d.get("tags", [])),
        )


@dataclass
class Lesson:
    id: str
    unit_id: str
    exam: str
    title: str
    markdown_path: str          # relative to data/lessons
    subtopics: list[str] = field(default_factory=list)
    quiz_size: int = 12

    @classmethod
    def from_dict(cls, d: dict, unit_id: str, exam: str) -> "Lesson":
        return cls(
            id=d["id"], unit_id=unit_id, exam=exam, title=d["title"],
            markdown_path=d["markdown_path"], subtopics=list(d.get("subtopics", [])),
            quiz_size=int(d.get("quiz_size", 12)),
        )


@dataclass
class Unit:
    id: str
    exam: str
    order: int
    title: str
    summary: str
    domains: list[str]
    lessons: list[Lesson]
    milestone_size: int = 30
    pbq_id: str | None = None

    @property
    def subtopics(self) -> list[str]:
        out: list[str] = []
        for lesson in self.lessons:
            out.extend(lesson.subtopics)
        return out

    @classmethod
    def from_dict(cls, d: dict, exam: str) -> "Unit":
        lessons = [Lesson.from_dict(ld, d["id"], exam) for ld in d.get("lessons", [])]
        return cls(
            id=d["id"], exam=exam, order=int(d["order"]), title=d["title"],
            summary=d.get("summary", ""), domains=list(d.get("domains", [])),
            lessons=lessons, milestone_size=int(d.get("milestone_size", 30)),
            pbq_id=d.get("pbq_id"),
        )
