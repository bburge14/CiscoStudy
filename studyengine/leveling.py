"""XP and levels, derived from a Profile's real progress — no separate state.

XP is weighted toward getting answers RIGHT and MASTERING sub-topics, so a
learner's level reflects genuine competence rather than raw grinding. Because XP
is computed from the existing profile stats, it can never drift out of sync with
actual progress (and an open-book "peek", recorded as a miss, simply earns less).
"""
from __future__ import annotations

from dataclasses import dataclass

from .progress import MASTERY_THRESHOLD, Profile

# --- XP weights -------------------------------------------------------------
# Most XP is earned per-answer (streaks, mastery, penalties) and accumulated on
# the profile by Profile.record_study(). Passing structured content adds a
# derived, idempotent bonus on top.
XP_PER_MILESTONE = 120         # passing a structured milestone
XP_PER_LESSON = 25             # passing a lesson quiz
MASTERY_MIN_ATTEMPTS = 4       # study attempts before a sub-topic counts as mastered
# Note: the diagnostic benchmark earns NO XP, and a wrong answer COSTS XP.
# Leveling reflects getting better over time, not raw volume of attempts.

# (minimum cumulative XP, rank title). Original, networking-themed ranks — not
# any vendor's trademarked certification names.
LEVELS: list[tuple[int, str]] = [
    (0,      "Cable Apprentice"),
    (400,    "Patch Panel Rookie"),
    (1000,   "LAN Technician"),
    (2000,   "Network Associate"),
    (3500,   "Routing Specialist"),
    (5500,   "Senior Network Engineer"),
    (8000,   "Network Architect"),
    (11500,  "Principal Architect"),
    (16000,  "Network Sage"),
]


@dataclass(frozen=True)
class LevelInfo:
    level: int               # 1-based rank index
    title: str               # rank title
    xp: int                  # total XP
    floor: int               # XP at which this level began
    ceil: int | None         # XP needed for the next level (None at max level)
    into: int                # XP earned into the current level
    span: int                # XP width of the current level (0 at max)
    pct: float               # 0..1 progress toward the next level (1.0 at max)
    next_title: str | None   # next rank's title (None at max)

    @property
    def is_max(self) -> bool:
        return self.ceil is None

    @property
    def to_next(self) -> int:
        """XP remaining to the next level (0 at max)."""
        return 0 if self.ceil is None else max(self.ceil - self.xp, 0)


def mastered_subtopics(profile: Profile, min_attempts: int = MASTERY_MIN_ATTEMPTS) -> list[str]:
    """Sub-topics answered at least `min_attempts` times at >= mastery accuracy,
    counting STUDY attempts only (the diagnostic benchmark is excluded)."""
    out = []
    for stp, (seen, _correct, acc) in profile.study_subtopic_stats().items():
        if seen >= min_attempts and acc >= MASTERY_THRESHOLD:
            out.append(stp)
    return out


def compute_xp(profile: Profile) -> int:
    """Total XP = accumulated per-answer study XP (streaks, mastery, penalties;
    see Profile.record_study) plus a derived bonus for passing lessons and
    milestones. The diagnostic benchmark earns nothing."""
    xp = float(getattr(profile, "xp", 0.0))
    xp += len(profile.passed_milestones) * XP_PER_MILESTONE
    xp += len(profile.completed_lessons) * XP_PER_LESSON
    return int(xp)


def level_info(xp: int) -> LevelInfo:
    """Resolve a raw XP total into the current rank and progress to the next."""
    xp = max(int(xp), 0)
    idx = 0
    for i, (thr, _title) in enumerate(LEVELS):
        if xp >= thr:
            idx = i
    floor, title = LEVELS[idx]
    if idx + 1 < len(LEVELS):
        ceil, next_title = LEVELS[idx + 1]
        span = ceil - floor
        into = xp - floor
        pct = into / span if span else 1.0
    else:
        ceil, next_title, span, into, pct = None, None, 0, xp - floor, 1.0
    return LevelInfo(idx + 1, title, xp, floor, ceil, into, span, min(max(pct, 0.0), 1.0),
                     next_title)


def profile_level(profile: Profile) -> LevelInfo:
    """Convenience: the LevelInfo for a profile."""
    return level_info(compute_xp(profile))
