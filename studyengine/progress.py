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

# --- study XP event weights (see Profile.record_study) ----------------------
# XP rewards getting BETTER (improving/mastering) and streaks, and penalizes
# misses. Just attempting earns nothing — a wrong answer costs XP.
XP_CORRECT_BASE = 4        # + the question's difficulty (1-3)
XP_STREAK_CAP = 12         # max streak bonus added to a correct answer
XP_LEARN_BONUS = 6         # correct on a weak/new item (box <= 2): knowledge gained
XP_MASTER_BONUS = 20       # correct that pushes an item to box 5 (mastered)
XP_MASTERED_MAINTAIN = 1   # re-answering an already-mastered item: negligible
XP_MISS_PENALTY = -6       # first miss of a question (or first after getting it right)
XP_MISS_ESCALATION = -3    # each ADDITIONAL consecutive miss of the SAME question...
XP_MISS_ESCALATION_CAP = 3 # ...up to this many extra steps (so -6, -9, -12, -15 floor)


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
    # Attempts that came from the diagnostic benchmark, tracked separately so
    # they can be EXCLUDED from study metrics (questions answered, accuracy, XP).
    # The diagnostic still records into `q` to seed the adaptive scheduler/plan.
    baseline_stats: dict | None = None
    completed_lessons: set[str] = field(default_factory=set)
    passed_milestones: set[str] = field(default_factory=set)
    created: float = field(default_factory=time.time)
    # Accumulated study XP (event-based: streak bonuses, mastery/learning
    # bonuses, miss penalties). See record_study(). The diagnostic earns none.
    xp: float = 0.0
    answer_streak: int = 0     # current consecutive correct (study only)
    best_streak: int = 0       # longest streak reached
    # Self-reported certification status for this track (the "credential wallet"):
    # "" (none), "planned", "studying", or "earned". "earned" grants a one-time
    # XP bonus via leveling.compute_xp. cert_date is an ISO date string (earned).
    cert_status: str = ""
    cert_date: str = ""

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

    def record_study(self, question: Question, correct: bool, *,
                     xp_scale: float = 1.0, miss_scale: float = 1.0) -> dict:
        """Record a STUDY answer (drill, plan, quiz, open-book, exam) and award
        event-based XP. Rewards getting better (improving weak items, mastering
        them) and streaks; penalizes misses — and missing the SAME question again
        and again hurts progressively more (getting it right resets that). The
        diagnostic benchmark uses record()+note_baseline_answer() and earns no XP.

        xp_scale multiplies a correct answer's reward (open-book uses < 1 when the
        book was used, scaled by how much help the mode gave). miss_scale multiplies
        a miss's penalty: 1.0 is the normal cost, 0.0 makes the miss free (open-book
        when the book stayed shut), and open-book scales it up with how much the
        book helped — missing one you had the answer for stings more.

        Returns {delta, streak, learned, mastered, regressed} for UI feedback."""
        pre_box = self.box_of(question.id)
        qstat = self.record(question, correct)
        flags = {"learned": False, "mastered": False, "regressed": False}
        misses_in_row = 0
        if correct:
            self.answer_streak += 1
            self.best_streak = max(self.best_streak, self.answer_streak)
            if pre_box >= 5:
                delta = XP_MASTERED_MAINTAIN        # already mastered — negligible
            else:
                delta = XP_CORRECT_BASE + int(question.difficulty)
                delta += min(self.answer_streak, XP_STREAK_CAP)   # streak bonus
                if pre_box <= 2:                    # improving a weak / new item
                    delta += XP_LEARN_BONUS
                    flags["learned"] = True
                if pre_box == 4:                    # box 4 -> 5: just mastered it
                    delta += XP_MASTER_BONUS
                    flags["mastered"] = True
            delta = round(delta * max(xp_scale, 0.0))
        else:
            self.answer_streak = 0
            # qstat.streak is now negative; its size is how many times THIS
            # question has been missed in a row. Each repeat hurts more, up to a
            # floor; a correct answer flips the streak positive and resets it, so
            # an isolated slip is always just the base penalty.
            misses_in_row = max(1, -qstat.streak)
            steps = min(misses_in_row - 1, XP_MISS_ESCALATION_CAP)
            delta = 0                                # miss_scale 0 -> a free miss
            if miss_scale > 0:
                delta = round((XP_MISS_PENALTY + XP_MISS_ESCALATION * steps) * miss_scale)
                flags["regressed"] = misses_in_row >= 2   # a repeat miss, getting worse
        self.xp = max(0.0, self.xp + delta)
        return {"delta": int(delta), "streak": self.answer_streak,
                "misses": misses_in_row, **flags}

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

    # -- diagnostic separation --------------------------------------------
    def note_baseline_answer(self, question: Question, correct: bool) -> None:
        """Mark an answer as part of the diagnostic benchmark so it is excluded
        from study metrics. Called alongside record() by the diagnostic only."""
        bs = self.baseline_stats
        if bs is None:
            bs = self.baseline_stats = {"seen": 0, "correct": 0, "subtopic": {}}
        bs["seen"] += 1
        if correct:
            bs["correct"] += 1
        sub = bs.setdefault("subtopic", {}).setdefault(question.subtopic, [0, 0])
        sub[0] += 1
        if correct:
            sub[1] += 1

    def _baseline_seen_correct(self) -> tuple[int, int]:
        bs = self.baseline_stats or {}
        return int(bs.get("seen", 0)), int(bs.get("correct", 0))

    def study_overall(self) -> tuple[int, int]:
        """Answered/correct counting ONLY study activity — the diagnostic
        benchmark is excluded (it measures you, it isn't study progress)."""
        seen, correct = self.overall()
        bseen, bcorrect = self._baseline_seen_correct()
        return max(seen - bseen, 0), max(correct - bcorrect, 0)

    def study_subtopic_stats(self) -> dict[str, tuple[int, int, float]]:
        """Per-subtopic (seen, correct, accuracy) excluding the diagnostic."""
        bsub = (self.baseline_stats or {}).get("subtopic", {})
        out: dict[str, tuple[int, int, float]] = {}
        for key, (seen, correct) in self._agg("subtopic").items():
            b = bsub.get(key, [0, 0])
            s = max(seen - b[0], 0)
            c = max(correct - b[1], 0)
            out[key] = (s, c, (c / s if s else 0.0))
        return out

    # -- (de)serialisation -------------------------------------------------
    def to_dict(self) -> dict:
        return {
            "exam": self.exam,
            "created": self.created,
            "baseline": self.baseline,
            "baseline_stats": self.baseline_stats,
            "completed_lessons": sorted(self.completed_lessons),
            "passed_milestones": sorted(self.passed_milestones),
            "xp": self.xp,
            "answer_streak": self.answer_streak,
            "best_streak": self.best_streak,
            "cert_status": self.cert_status,
            "cert_date": self.cert_date,
            "q": {qid: asdict(st) for qid, st in self.q.items()},
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Profile":
        prof = cls(exam=d["exam"])
        prof.created = d.get("created", time.time())
        prof.baseline = d.get("baseline")
        prof.baseline_stats = d.get("baseline_stats")
        prof.completed_lessons = set(d.get("completed_lessons", []))
        prof.passed_milestones = set(d.get("passed_milestones", []))
        prof.answer_streak = int(d.get("answer_streak", 0))
        prof.best_streak = int(d.get("best_streak", 0))
        prof.cert_status = str(d.get("cert_status", "") or "")
        prof.cert_date = str(d.get("cert_date", "") or "")
        for qid, st in d.get("q", {}).items():
            prof.q[qid] = QStat(**st)
        # Legacy backfill: a profile that took the diagnostic before study/
        # benchmark stats were split has no baseline_stats. Approximate the
        # benchmark's contribution (standard 30-question baseline) so it is
        # excluded from study metrics going forward.
        if prof.baseline_stats is None and prof.baseline:
            total = int(prof.baseline.get("total", 30))
            pct = prof.baseline.get("overall", 0) or 0
            prof.baseline_stats = {"seen": total, "correct": round(pct / 100 * total),
                                   "subtopic": {}}
        # XP: stored going forward. For a profile from before event-XP existed,
        # estimate a fair starting XP from study progress (no streak/penalty
        # history to replay) so the learner keeps a sensible rank.
        if "xp" in d:
            prof.xp = float(d.get("xp") or 0.0)
        else:
            _, s_correct = prof.study_overall()
            mastered = sum(1 for (s, _c, a) in prof.study_subtopic_stats().values()
                           if s >= 4 and a >= MASTERY_THRESHOLD)
            prof.xp = float(s_correct * 6 + mastered * 40)
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
