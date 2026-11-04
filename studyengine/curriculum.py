"""Structured curriculum: units -> lessons (read + quiz) -> milestone exam.

Lesson quizzes draw from the lesson's own subtopics. Milestone exams are
*cumulative*: they pull from every subtopic taught up to and including the unit,
so later milestones naturally exercise a deeper pool.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

from .bank import QuestionBank
from .models import Question, Unit

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


class Curriculum:
    def __init__(self, units: list[Unit]):
        self._units = sorted(units, key=lambda u: (u.exam, u.order))
        self._by_id = {u.id: u for u in self._units}

    def all(self) -> list[Unit]:
        return list(self._units)

    def units_for(self, exam: str) -> list[Unit]:
        return [u for u in self._units if u.exam == exam]

    def unit(self, unit_id: str) -> Unit:
        return self._by_id[unit_id]

    def lesson(self, lesson_id: str):
        for u in self._units:
            for les in u.lessons:
                if les.id == lesson_id:
                    return les
        raise KeyError(f"unknown lesson {lesson_id!r}")

    def unit_of_lesson(self, lesson_id: str) -> Unit:
        for u in self._units:
            if any(les.id == lesson_id for les in u.lessons):
                return u
        raise KeyError(f"unknown lesson {lesson_id!r}")


def load_curriculum(data_dir: str | Path = DATA_DIR) -> Curriculum:
    cdir = Path(data_dir) / "curriculum"
    units: list[Unit] = []
    for jf in sorted(cdir.glob("*.json")):
        raw = json.loads(jf.read_text(encoding="utf-8"))
        exam = raw["exam"]
        for ud in raw.get("units", []):
            units.append(Unit.from_dict(ud, exam))
    return Curriculum(units)


def lesson_markdown(lesson, data_dir: str | Path = DATA_DIR) -> str:
    path = Path(data_dir) / "lessons" / lesson.markdown_path
    if not path.exists():
        return f"> Lesson content not found at `{lesson.markdown_path}`."
    return path.read_text(encoding="utf-8")


def lesson_quiz(
    bank: QuestionBank,
    lesson,
    size: int | None = None,
    rng: random.Random | None = None,
) -> list[Question]:
    rng = rng or random.Random()
    size = size or lesson.quiz_size
    pool = bank.query(exam=lesson.exam, subtopics=lesson.subtopics)
    k = min(size, len(pool))
    return rng.sample(pool, k) if k else []


def milestone_exam(
    bank: QuestionBank,
    curriculum: Curriculum,
    unit: Unit,
    size: int | None = None,
    rng: random.Random | None = None,
) -> list[Question]:
    rng = rng or random.Random()
    size = size or unit.milestone_size
    subtopics: set[str] = set()
    for u in curriculum.units_for(unit.exam):
        if u.order <= unit.order:
            subtopics.update(u.subtopics)
    pool = bank.query(exam=unit.exam, subtopics=list(subtopics))
    k = min(size, len(pool))
    return rng.sample(pool, k) if k else []
