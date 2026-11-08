"""CertLab engine: question bank, adaptive scheduling, curriculum, CLI sim.

All exam content in this package is original, written to match the public Cisco
200-301 / 350-401 exam blueprints and real IOS behaviour. It is study material,
not a reproduction of any proprietary exam item bank.
"""
from .bank import QuestionBank, load_bank
from .blueprints import CCNA, ENCOR, EXAMS, LIVE_EXAMS, ExamBlueprint, get_blueprint
from .curriculum import (
    Curriculum,
    lesson_markdown,
    lesson_quiz,
    load_curriculum,
    milestone_exam,
)
from .diagnostic import build_baseline, recommend_focus
from .exam import PASS_SCORE, build_exam, exam_readiness, exam_time_limit
from .grading import Feedback, SessionScore, grade, score_session
from .leveling import LevelInfo, compute_xp, level_info, mastered_subtopics, profile_level
from .models import Lesson, Option, Question, Unit
from .progress import Profile, QStat
from .scheduler import DrillScheduler
from .studyplan import (
    PlanStep,
    build_plan,
    current_step,
    is_mastered,
    next_question_for_subtopic,
    plan_progress,
)

__all__ = [
    "QuestionBank", "load_bank",
    "CCNA", "ENCOR", "EXAMS", "LIVE_EXAMS", "ExamBlueprint", "get_blueprint",
    "Curriculum", "load_curriculum", "lesson_markdown", "lesson_quiz", "milestone_exam",
    "build_baseline", "recommend_focus",
    "PASS_SCORE", "build_exam", "exam_readiness", "exam_time_limit",
    "Feedback", "SessionScore", "grade", "score_session",
    "LevelInfo", "compute_xp", "level_info", "mastered_subtopics", "profile_level",
    "Lesson", "Option", "Question", "Unit",
    "Profile", "QStat",
    "DrillScheduler",
    "PlanStep", "build_plan", "current_step", "is_mastered",
    "next_question_for_subtopic", "plan_progress",
]
