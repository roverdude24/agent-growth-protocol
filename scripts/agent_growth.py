#!/usr/bin/env python3
"""Agent Growth Protocol helper.

Stores structured learning/growth/checkpoint entries in:
  ~/.hermes/memories/AGENT_GROWTH.md

Commands:
  add-learning --topic TOPIC --impact low|medium|high --text TEXT
  add-growth --topic TOPIC --text TEXT
  checkpoint --task TASK --decisions TEXT --blockers TEXT --next TEXT
  report
  compact
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path

STORE = Path.home() / ".hermes" / "memories" / "AGENT_GROWTH.md"
SECTIONS = [
    "Open Learnings",
    "Verified Learnings",
    "Growth Events",
    "Promotion Candidates",
    "Checkpoints",
    "Archived",
]

TEMPLATE = """# Agent Growth Log

## Open Learnings

## Verified Learnings

## Growth Events

## Promotion Candidates

## Checkpoints

## Archived
"""


def ensure_store() -> str:
    STORE.parent.mkdir(parents=True, exist_ok=True)
    if not STORE.exists():
        STORE.write_text(TEMPLATE)
    text = STORE.read_text()
    changed = False
    for section in SECTIONS:
        if f"## {section}" not in text:
            text += f"\n## {section}\n"
            changed = True
    if changed:
        STORE.write_text(text)
    return text


def next_id(prefix: str, text: str) -> str:
    nums = [int(x) for x in re.findall(rf"\[{prefix}-(\d+)\]", text)]
    n = max(nums, default=0) + 1
    return f"{prefix}-{n:03d}"


def insert_under(section: str, line: str) -> None:
    text = ensure_store()
    marker = f"## {section}"
    idx = text.index(marker) + len(marker)
    next_match = re.search(r"\n## ", text[idx:])
    if next_match:
        insert_at = idx + next_match.start()
        new_text = text[:insert_at].rstrip() + "\n" + line + "\n\n" + text[insert_at:].lstrip()
    else:
        new_text = text.rstrip() + "\n" + line + "\n"
    STORE.write_text(new_text)


def add_learning(args) -> None:
    text = ensure_store()
    ident = next_id("LRN", text)
    today = dt.date.today().isoformat()
    line = f"- [{ident}] status=open | date={today} | topic={args.topic} | impact={args.impact} | seen=1 | {args.text}"
    insert_under("Open Learnings", line)
    print(f"added {ident}")


def add_growth(args) -> None:
    text = ensure_store()
    ident = next_id("GROW", text)
    today = dt.date.today().isoformat()
    line = f"- [{ident}] date={today} | topic={args.topic} | {args.text}"
    insert_under("Growth Events", line)
    print(f"added {ident}")


def checkpoint(args) -> None:
    today = dt.datetime.now().isoformat(timespec="minutes")
    line = f"- [CHECKPOINT] date={today} | task={args.task} | decisions={args.decisions} | blockers={args.blockers} | next={args.next}"
    insert_under("Checkpoints", line)
    print("added checkpoint")


def section_lines(text: str, section: str) -> list[str]:
    marker = f"## {section}"
    if marker not in text:
        return []
    start = text.index(marker) + len(marker)
    m = re.search(r"\n## ", text[start:])
    end = start + m.start() if m else len(text)
    return [l for l in text[start:end].splitlines() if l.strip().startswith("-")]


def report(_args=None) -> None:
    text = ensure_store()
    open_l = section_lines(text, "Open Learnings")
    verified = section_lines(text, "Verified Learnings")
    growth = section_lines(text, "Growth Events")
    promos = section_lines(text, "Promotion Candidates")
    checkpoints = section_lines(text, "Checkpoints")

    print("Agent Growth Report")
    print(f"Store: {STORE}")
    print(f"Open learnings: {len(open_l)}")
    print(f"Verified learnings: {len(verified)}")
    print(f"Growth events: {len(growth)}")
    print(f"Promotion candidates: {len(promos)}")
    print(f"Checkpoints: {len(checkpoints)}")
    if promos:
        print("\nPromotion candidates:")
        for line in promos[:10]:
            print(line)
    if open_l:
        print("\nRecent open learnings:")
        for line in open_l[-5:]:
            print(line)


def compact(_args=None) -> None:
    text = ensure_store()
    open_l = section_lines(text, "Open Learnings")
    verified = section_lines(text, "Verified Learnings")

    candidates = []
    for line in verified:
        seen = re.search(r"seen=(\d+)", line)
        impact = re.search(r"impact=(\w+)", line)
        if seen and int(seen.group(1)) >= 3 and impact and impact.group(1) in {"medium", "high"}:
            topic = re.search(r"topic=([^|]+)", line)
            topic_s = topic.group(1).strip() if topic else "unknown"
            candidates.append(f"- [PROMOTE] topic={topic_s} | source={line[:120]}")

    # Rebuild promotion section by appending new non-duplicates.
    existing = set(section_lines(text, "Promotion Candidates"))
    added = 0
    for c in candidates:
        if c not in existing:
            insert_under("Promotion Candidates", c)
            added += 1

    print(f"compact complete: open={len(open_l)} verified={len(verified)} new_promotions={added}")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Agent Growth Protocol helper")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add-learning")
    a.add_argument("--topic", required=True)
    a.add_argument("--impact", choices=["low", "medium", "high"], default="medium")
    a.add_argument("--text", required=True)
    a.set_defaults(func=add_learning)

    g = sub.add_parser("add-growth")
    g.add_argument("--topic", required=True)
    g.add_argument("--text", required=True)
    g.set_defaults(func=add_growth)

    c = sub.add_parser("checkpoint")
    c.add_argument("--task", required=True)
    c.add_argument("--decisions", default="none")
    c.add_argument("--blockers", default="none")
    c.add_argument("--next", default="continue")
    c.set_defaults(func=checkpoint)

    r = sub.add_parser("report")
    r.set_defaults(func=report)

    x = sub.add_parser("compact")
    x.set_defaults(func=compact)
    return p


def main() -> None:
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
