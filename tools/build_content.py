#!/usr/bin/env python3
"""Validate the authored item pools and emit data/questions/*.json.

Run from the repo root:  python tools/build_content.py
Validation mirrors tests/test_data_integrity.py so a bad edit fails fast here.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from studyengine.blueprints import get_blueprint  # noqa: E402
from studyengine.models import Question  # noqa: E402

import content_ccna  # noqa: E402
import content_encor  # noqa: E402

SOURCES = {"ccna": content_ccna.QUESTIONS, "encor": content_encor.QUESTIONS}


def validate(exam: str, raw_items: list[dict]) -> list[dict]:
    bp = get_blueprint(exam)
    valid_domains = set(bp.domain_keys)
    valid_subtopics = {st for d in bp.domains for st in d.subtopics}
    seen_ids: set[str] = set()
    errors: list[str] = []

    for item in raw_items:
        qid = item.get("id", "<no-id>")
        if item.get("exam") != exam:
            errors.append(f"{qid}: exam != {exam}")
        if qid in seen_ids:
            errors.append(f"{qid}: duplicate id")
        seen_ids.add(qid)
        if item.get("domain") not in valid_domains:
            errors.append(f"{qid}: domain {item.get('domain')!r} not in blueprint")
        if item.get("subtopic") not in valid_subtopics:
            errors.append(f"{qid}: subtopic {item.get('subtopic')!r} not in blueprint")
        try:
            q = Question.from_dict(item)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{qid}: cannot build Question: {exc}")
            continue
        if q.type in ("mcq", "multi"):
            opt_ids = {o.id for o in q.options}
            if len(opt_ids) < 2:
                errors.append(f"{qid}: needs >= 2 options")
            for c in q.correct:
                if c not in opt_ids:
                    errors.append(f"{qid}: correct id {c!r} not among options")
            for dk in q.explanation.distractors:
                if dk not in opt_ids:
                    errors.append(f"{qid}: distractor note {dk!r} not an option id")
            if q.type == "multi" and len(q.correct) < 2:
                errors.append(f"{qid}: multi needs >= 2 correct")
        elif q.type == "fill":
            if not q.correct:
                errors.append(f"{qid}: fill needs at least one accepted answer")
        if not q.explanation.correct:
            errors.append(f"{qid}: missing explanation.correct")

    # baseline feasibility: >= 5 items per domain
    counts: dict[str, int] = {}
    for item in raw_items:
        counts[item.get("domain", "?")] = counts.get(item.get("domain", "?"), 0) + 1
    for d in bp.domains:
        if counts.get(d.key, 0) < 5:
            errors.append(f"domain {d.key} has {counts.get(d.key, 0)} items (<5 for baseline)")

    if errors:
        print(f"[{exam}] VALIDATION ERRORS:")
        for e in errors:
            print("   -", e)
        raise SystemExit(1)
    return raw_items


def main() -> None:
    out_dir = ROOT / "data" / "questions"
    out_dir.mkdir(parents=True, exist_ok=True)
    grand_total = 0
    for exam, items in SOURCES.items():
        validate(exam, items)
        payload = {"exam": exam, "count": len(items), "questions": items}
        path = out_dir / f"{exam}.json"
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        # per-domain summary
        counts: dict[str, int] = {}
        for it in items:
            counts[it["domain"]] = counts.get(it["domain"], 0) + 1
        grand_total += len(items)
        print(f"[{exam}] {len(items)} questions -> {path.relative_to(ROOT)}")
        for dk, n in sorted(counts.items()):
            print(f"      {dk}: {n}")
    print(f"TOTAL: {grand_total} questions")


if __name__ == "__main__":
    main()
