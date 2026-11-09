#!/usr/bin/env python3
"""Validate the authored item pools and emit data/questions/*.json.

Run from the repo root:  python tools/build_content.py
Validation mirrors tests/test_data_integrity.py so a bad edit fails fast here.
"""
from __future__ import annotations

import json
import random
import string
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from studyengine.blueprints import get_blueprint  # noqa: E402
from studyengine.models import Question  # noqa: E402

import importlib  # noqa: E402

import content_ccna  # noqa: E402
import content_encor  # noqa: E402
import content_secplus  # noqa: E402
import content_netplus  # noqa: E402
import content_aplus1  # noqa: E402
import content_aplus2  # noqa: E402
import content_clf  # noqa: E402
import content_az900  # noqa: E402
import content_cysa  # noqa: E402
import content_pentest  # noqa: E402
import content_isc2cc  # noqa: E402
import content_cbrops  # noqa: E402
import content_sc900  # noqa: E402
import content_cissp  # noqa: E402
import content_cism  # noqa: E402
import content_cisa  # noqa: E402
import content_sscp  # noqa: E402
import content_ceh  # noqa: E402
import content_sc200  # noqa: E402
import content_az500  # noqa: E402
import content_securityx  # noqa: E402

# Base item pool per track. Any number of expansion pools named
# tools/content_<exam>_*.py (e.g. content_ccna_2.py, content_secplus_gsc.py) are
# auto-discovered and merged, so a track's bank can be deepened by dropping in
# more files without touching this script.
BASE = {
    "ccna": content_ccna, "encor": content_encor, "secplus": content_secplus,
    "netplus": content_netplus, "aplus1": content_aplus1, "aplus2": content_aplus2,
    "clf": content_clf, "az900": content_az900, "cysa": content_cysa,
    "pentest": content_pentest, "isc2cc": content_isc2cc, "cbrops": content_cbrops,
    "sc900": content_sc900, "cissp": content_cissp, "cism": content_cism,
    "cisa": content_cisa, "sscp": content_sscp, "ceh": content_ceh,
    "sc200": content_sc200, "az500": content_az500, "securityx": content_securityx,
}


def _expansions(exam: str) -> list[dict]:
    """Every tools/content_<exam>_*.py expansion pool, concatenated (name-sorted)."""
    out: list[dict] = []
    for path in sorted((ROOT / "tools").glob(f"content_{exam}_*.py")):
        mod = importlib.import_module(path.stem)
        out += list(getattr(mod, "QUESTIONS", []))
    return out


SOURCES = {exam: list(mod.QUESTIONS) + _expansions(exam) for exam, mod in BASE.items()}


def shuffle_options(item: dict) -> dict:
    """Randomise the A/B/C/D order of an MCQ/multi item so the correct answer
    isn't always in the same slot. Seeded by the question id, so the order is
    deterministic and stable across rebuilds (no churn), while spreading the
    answer key evenly across positions instead of defaulting to 'A'."""
    if item.get("type") not in ("mcq", "multi") or not item.get("options"):
        return item
    correct = set(item.get("correct", []))
    notes = (item.get("explanation") or {}).get("distractors", {}) or {}
    bundle = [{"text": o["text"], "ok": o["id"] in correct, "note": notes.get(o["id"], "")}
              for o in item["options"]]
    random.Random(item["id"]).shuffle(bundle)
    new_item = dict(item)
    new_item["options"] = []
    new_item["correct"] = []
    new_notes: dict[str, str] = {}
    for i, b in enumerate(bundle):
        nid = string.ascii_uppercase[i]
        new_item["options"].append({"id": nid, "text": b["text"]})
        if b["ok"]:
            new_item["correct"].append(nid)
        new_notes[nid] = b["note"]
    new_item["explanation"] = {**(item.get("explanation") or {}), "distractors": new_notes}
    return new_item


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
        items = [shuffle_options(it) for it in items]
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
