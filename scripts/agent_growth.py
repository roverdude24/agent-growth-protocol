#!/usr/bin/env python3
"""Agent Growth Protocol v0.3.

Source of truth:
  ~/.hermes/memories/agent_growth/events.jsonl

Human report:
  ~/.hermes/memories/AGENT_GROWTH.md

Commands:
  add-learning --topic TOPIC --impact low|medium|high --problem TEXT --fix TEXT
  add-growth --topic TOPIC --capability TEXT --evidence TEXT
  checkpoint --task TASK --decisions TEXT --blockers TEXT --next TEXT
  verify --id LRN-001 --evidence TEXT
  seen --id LRN-001
  compact
  promotions
  sync-mnemosyne
  render-md
  report
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path
from typing import Any

BASE = Path.home() / ".hermes" / "memories"
DATA_DIR = BASE / "agent_growth"
EVENTS = DATA_DIR / "events.jsonl"
REPORT = BASE / "AGENT_GROWTH.md"
MEMORY = BASE / "MEMORY.md"


def now() -> str:
    return dt.datetime.now().isoformat(timespec="seconds")


def today() -> str:
    return dt.date.today().isoformat()


def ensure_dirs() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    BASE.mkdir(parents=True, exist_ok=True)
    EVENTS.touch(exist_ok=True)


def read_events() -> list[dict[str, Any]]:
    ensure_dirs()
    events: list[dict[str, Any]] = []
    for line in EVENTS.read_text().splitlines():
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return events


def write_events(events: list[dict[str, Any]]) -> None:
    ensure_dirs()
    EVENTS.write_text("\n".join(json.dumps(e, ensure_ascii=False, sort_keys=True) for e in events) + ("\n" if events else ""))


def append_event(event: dict[str, Any]) -> None:
    ensure_dirs()
    with EVENTS.open("a") as f:
        f.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")


def next_id(prefix: str, events: list[dict[str, Any]]) -> str:
    nums = []
    for e in events:
        eid = str(e.get("id", ""))
        m = re.match(rf"{prefix}-(\d+)$", eid)
        if m:
            nums.append(int(m.group(1)))
    return f"{prefix}-{max(nums, default=0) + 1:03d}"


def find_event(events: list[dict[str, Any]], eid: str) -> dict[str, Any] | None:
    for e in events:
        if e.get("id") == eid:
            return e
    return None


def add_learning(args) -> None:
    events = read_events()
    duplicate_key = args.duplicate_key or args.topic.lower().replace(" ", "-") + ":" + re.sub(r"\W+", "-", args.problem.lower()).strip("-")[:60]
    for e in events:
        if e.get("type") == "learning" and e.get("duplicate_key") == duplicate_key:
            e["seen"] = int(e.get("seen", 1)) + 1
            e["updated_at"] = now()
            e.setdefault("history", []).append({"at": now(), "event": "seen", "note": args.problem})
            write_events(events)
            print(f"updated {e['id']} seen={e['seen']}")
            return
    event = {
        "id": next_id("LRN", events),
        "type": "learning",
        "status": "open",
        "topic": args.topic,
        "impact": args.impact,
        "problem": args.problem,
        "fix": args.fix,
        "duplicate_key": duplicate_key,
        "seen": 1,
        "reuse_count": 0,
        "success_count": 0,
        "confidence": 0.0,
        "created_at": now(),
        "updated_at": now(),
        "sync_status": "not_synced",
    }
    append_event(event)
    print(f"added {event['id']}")


def add_growth(args) -> None:
    events = read_events()
    event = {
        "id": next_id("GROW", events),
        "type": "growth",
        "topic": args.topic,
        "capability": args.capability,
        "evidence": args.evidence,
        "created_at": now(),
        "sync_status": "not_synced",
    }
    append_event(event)
    print(f"added {event['id']}")


def checkpoint(args) -> None:
    events = read_events()
    event = {
        "id": next_id("CHK", events),
        "type": "checkpoint",
        "task": args.task,
        "decisions": args.decisions,
        "blockers": args.blockers,
        "next": args.next,
        "created_at": now(),
        "expires_at": (dt.datetime.now() + dt.timedelta(hours=48)).isoformat(timespec="seconds"),
    }
    append_event(event)
    print(f"added {event['id']}")


def verify(args) -> None:
    events = read_events()
    e = find_event(events, args.id)
    if not e:
        raise SystemExit(f"not found: {args.id}")
    if e.get("type") != "learning":
        raise SystemExit(f"not a learning: {args.id}")
    e["status"] = "verified"
    e["reuse_count"] = int(e.get("reuse_count", 0)) + 1
    e["success_count"] = int(e.get("success_count", 0)) + 1
    e["confidence"] = min(0.95, 0.4 + 0.15 * int(e.get("success_count", 1)) + 0.1 * int(e.get("seen", 1)))
    e["updated_at"] = now()
    e.setdefault("verification", []).append({"at": now(), "evidence": args.evidence})
    write_events(events)
    print(f"verified {args.id} confidence={e['confidence']:.2f}")


def seen(args) -> None:
    events = read_events()
    e = find_event(events, args.id)
    if not e:
        raise SystemExit(f"not found: {args.id}")
    e["seen"] = int(e.get("seen", 1)) + 1
    e["updated_at"] = now()
    write_events(events)
    print(f"seen {args.id}={e['seen']}")


def promotion_candidates(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for e in events:
        if e.get("type") != "learning":
            continue
        if e.get("status") != "verified":
            continue
        if int(e.get("seen", 1)) < 3:
            continue
        if e.get("impact") not in {"medium", "high"}:
            continue
        if float(e.get("confidence", 0.0)) < 0.8:
            continue
        dest = "relevant skill Pitfalls"
        topic = str(e.get("topic", ""))
        if "user" in topic or "preference" in topic:
            dest = "USER.md"
        elif "policy" in topic or "routing" in topic:
            dest = "POLICY.md"
        out.append({
            "source_id": e["id"],
            "topic": e.get("topic"),
            "rule": f"{e.get('problem')} → {e.get('fix')}",
            "destination": dest,
            "confidence": e.get("confidence"),
        })
    return out


def compact(_args=None) -> None:
    events = read_events()
    cutoff = dt.datetime.now() - dt.timedelta(days=30)
    archived = 0
    for e in events:
        if e.get("type") != "learning" or e.get("status") != "open":
            continue
        created = dt.datetime.fromisoformat(str(e.get("created_at", now())).split("Z")[0])
        if created < cutoff and e.get("impact") == "low" and int(e.get("seen", 1)) <= 1:
            e["status"] = "archived"
            e["archive_reason"] = "stale low-impact unverified learning"
            e["updated_at"] = now()
            archived += 1
    write_events(events)
    render_md(None)
    print(f"compact complete archived={archived} promotions={len(promotion_candidates(events))}")


def promotions(_args=None) -> None:
    cands = promotion_candidates(read_events())
    if not cands:
        print("no promotion candidates")
        return
    for c in cands:
        print(f"[{c['source_id']}] topic={c['topic']} confidence={c['confidence']:.2f} -> {c['destination']}")
        print(f"  rule: {c['rule']}")


def sync_mnemosyne(_args=None) -> None:
    """Sync filtered memories to long-term fallback block in MEMORY.md.

    Current Hermes setup exposes Mnemosyne read/dashboard tools, but no direct write tool here.
    So this command writes a compact [AGENT_LEARNING_SYNC] block to MEMORY.md.
    Hermes/Mnemosyne ingestion can then recall it as durable memory.
    """
    events = read_events()
    syncable = []
    for e in events:
        if e.get("sync_status") == "synced":
            continue
        if e.get("type") == "learning" and e.get("status") == "verified":
            if float(e.get("confidence", 0)) >= 0.8 or e.get("impact") == "high":
                syncable.append(e)
        elif e.get("type") == "growth":
            syncable.append(e)
    if not syncable:
        print("nothing to sync")
        return
    lines = ["§", "## Agent Growth Sync"]
    for e in syncable:
        if e["type"] == "learning":
            lines.append(f"- [AGENT_LEARNING] {e['topic']}: {e['problem']} → {e['fix']}")
        elif e["type"] == "growth":
            lines.append(f"- [AGENT_CAPABILITY] {e['topic']}: {e['capability']} — evidence: {e['evidence']}")
        e["sync_status"] = "synced"
        e["synced_at"] = now()
    if MEMORY.exists():
        content = MEMORY.read_text().rstrip()
        MEMORY.write_text(content + "\n" + "\n".join(lines) + "\n")
    else:
        MEMORY.write_text("\n".join(lines) + "\n")
    write_events(events)
    print(f"synced {len(syncable)} entries to MEMORY.md fallback")


def render_md(_args=None) -> None:
    events = read_events()
    lines = [
        "# Agent Growth Log",
        "",
        f"Generated: {now()}",
        "",
        "## Open Learnings",
    ]
    for e in events:
        if e.get("type") == "learning" and e.get("status") == "open":
            lines.append(f"- [{e['id']}] topic={e['topic']} | impact={e['impact']} | seen={e.get('seen', 1)} | {e['problem']} → {e['fix']}")
    lines += ["", "## Verified Learnings"]
    for e in events:
        if e.get("type") == "learning" and e.get("status") == "verified":
            lines.append(f"- [{e['id']}] topic={e['topic']} | confidence={float(e.get('confidence', 0)):.2f} | seen={e.get('seen', 1)} | {e['problem']} → {e['fix']}")
    lines += ["", "## Growth Events"]
    for e in events:
        if e.get("type") == "growth":
            lines.append(f"- [{e['id']}] topic={e['topic']} | {e['capability']} — evidence: {e['evidence']}")
    lines += ["", "## Promotion Candidates"]
    for c in promotion_candidates(events):
        lines.append(f"- [PROMOTE] source={c['source_id']} | topic={c['topic']} | destination={c['destination']} | confidence={c['confidence']:.2f} | {c['rule']}")
    lines += ["", "## Checkpoints"]
    for e in events:
        if e.get("type") == "checkpoint":
            lines.append(f"- [{e['id']}] task={e['task']} | decisions={e['decisions']} | blockers={e['blockers']} | next={e['next']}")
    lines += ["", "## Archived"]
    for e in events:
        if e.get("status") == "archived":
            lines.append(f"- [{e['id']}] topic={e.get('topic')} | reason={e.get('archive_reason')} | {e.get('problem')} → {e.get('fix')}")
    REPORT.write_text("\n".join(lines) + "\n")
    print(f"rendered {REPORT}")


def report(_args=None) -> None:
    events = read_events()
    counts = {}
    for e in events:
        key = e.get("type", "unknown") + ":" + str(e.get("status", "active"))
        counts[key] = counts.get(key, 0) + 1
    print("Agent Growth Report")
    print(f"Events: {EVENTS}")
    print(f"Markdown: {REPORT}")
    for k in sorted(counts):
        print(f"{k}: {counts[k]}")
    print(f"promotion_candidates: {len(promotion_candidates(events))}")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Agent Growth Protocol v0.3")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add-learning")
    a.add_argument("--topic", required=True)
    a.add_argument("--impact", choices=["low", "medium", "high"], default="medium")
    a.add_argument("--problem", required=True)
    a.add_argument("--fix", required=True)
    a.add_argument("--duplicate-key")
    a.set_defaults(func=add_learning)

    g = sub.add_parser("add-growth")
    g.add_argument("--topic", required=True)
    g.add_argument("--capability", required=True)
    g.add_argument("--evidence", required=True)
    g.set_defaults(func=add_growth)

    c = sub.add_parser("checkpoint")
    c.add_argument("--task", required=True)
    c.add_argument("--decisions", default="none")
    c.add_argument("--blockers", default="none")
    c.add_argument("--next", default="continue")
    c.set_defaults(func=checkpoint)

    v = sub.add_parser("verify")
    v.add_argument("--id", required=True)
    v.add_argument("--evidence", required=True)
    v.set_defaults(func=verify)

    s = sub.add_parser("seen")
    s.add_argument("--id", required=True)
    s.set_defaults(func=seen)

    sub.add_parser("compact").set_defaults(func=compact)
    sub.add_parser("promotions").set_defaults(func=promotions)
    sub.add_parser("sync-mnemosyne").set_defaults(func=sync_mnemosyne)
    sub.add_parser("render-md").set_defaults(func=render_md)
    sub.add_parser("report").set_defaults(func=report)
    return p


def main() -> None:
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
