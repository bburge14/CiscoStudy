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
XP_PER_CORRECT = 10            # the main driver: getting answers right
XP_PER_ANSWER = 2              # small participation credit (even on a miss)
XP_PER_MASTERED_SUBTOPIC = 60  # sustained accuracy in a sub-topic
XP_PER_MILESTONE = 120         # passing a structured milestone
XP_PER_LESSON = 25             # passing a lesson quiz
XP_FOR_DIAGNOSTIC = 50         # taking the baseline once
MASTERY_MIN_ATTEMPTS = 4       # attempts before a sub-topic can count as mastered

# (minimum cumulative XP, rank title). Original, networking-themed ranks — not
# any vendor's trademarked certification names.
LEVELS: list[tuple[int, str]] = [
    (0,     "Cable Apprentice"),
    (150,   "Patch Panel Rookie"),
    (400,   "LAN Technician"),
    (800,   "Network Associate"),
    (1400,  "Routing Specialist"),
    (2200,  "Senior Network Engineer"),
    (3200,  "Network Architect"),
    (4600,  "Principal Architect"),
    (6400,  "Network Sage"),
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
    """Sub-topics answered at least `min_attempts` times at >= mastery accuracy."""
    out = []
    for stp, (seen, _correct, acc) in profile.subtopic_stats().items():
        if seen >= min_attempts and acc >= MASTERY_THRESHOLD:
            out.append(stp)
    return out


def compute_xp(profile: Profile) -> int:
    """Total XP for a profile, derived entirely from its recorded progress."""
    seen, correct = profile.overall()
    xp = correct * XP_PER_CORRECT + seen * XP_PER_ANSWER
    xp += len(mastered_subtopics(profile)) * XP_PER_MASTERED_SUBTOPIC
    xp += len(profile.passed_milestones) * XP_PER_MILESTONE
    xp += len(profile.completed_lessons) * XP_PER_LESSON
    if profile.baseline:
        xp += XP_FOR_DIAGNOSTIC
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
