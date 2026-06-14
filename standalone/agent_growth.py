#!/usr/bin/env python3
"""Agent Growth Protocol v0.3.2 — Standalone with SQLite memory.

For agents WITHOUT built-in memory (Codex, Antigravity, OpenCode, etc.).

Storage:
  ~/.agent_growth/growth.db    — SQLite event database
  ~/.agent_growth/report.md    — generated human report

Commands:
  init                          — create database and report
  add-learning --topic TOPIC --impact low|medium|high --problem TEXT --fix TEXT
  add-growth --topic TOPIC --capability TEXT --evidence TEXT
  checkpoint --task TASK --decisions TEXT --blockers TEXT --next TEXT
  verify --id LRN-001 --evidence TEXT
  seen --id LRN-001
  compact
  promotions
  report
  render-md
  recall --topic TOPIC          — search learnings by topic
  session-start                 — print relevant prior learnings for current context
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sqlite3
from pathlib import Path

BASE = Path.home() / ".agent_growth"
DB = BASE / "growth.db"
REPORT = BASE / "report.md"


def ensure_db() -> sqlite3.Connection:
    BASE.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id TEXT PRIMARY KEY,
            type TEXT NOT NULL,
            status TEXT DEFAULT 'open',
            topic TEXT,
            impact TEXT DEFAULT 'medium',
            problem TEXT,
            fix TEXT,
            capability TEXT,
            evidence TEXT,
            task TEXT,
            decisions TEXT,
            blockers TEXT,
            next_action TEXT,
            duplicate_key TEXT,
            seen INTEGER DEFAULT 1,
            reuse_count INTEGER DEFAULT 0,
            success_count INTEGER DEFAULT 0,
            confidence REAL DEFAULT 0.0,
            created_at TEXT,
            updated_at TEXT,
            synced INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    return conn


def now() -> str:
    return dt.datetime.now().isoformat(timespec="seconds")


def clean_problem(text: str) -> str:
    return re.sub(r"\W+", "-", text.lower()).strip("-")[:60]


def next_id(conn: sqlite3.Connection, prefix: str) -> str:
    row = conn.execute("SELECT MAX(CAST(SUBSTR(id, length(?) + 2) AS INTEGER)) as mx FROM events WHERE id LIKE ?", (prefix, f"{prefix}-%")).fetchone()
    mx = row["mx"] if row and row["mx"] else 0
    return f"{prefix}-{mx + 1:03d}"


def add_learning(args) -> None:
    conn = ensure_db()
    dup_key = args.duplicate_key or f"{args.topic}:{clean_problem(args.problem)}"
    existing = conn.execute("SELECT id, seen FROM events WHERE duplicate_key = ? AND type = 'learning'", (dup_key,)).fetchone()
    if existing:
        conn.execute("UPDATE events SET seen = ?, updated_at = ? WHERE id = ?", (existing["seen"] + 1, now(), existing["id"]))
        conn.commit()
        print(f"updated {existing['id']} seen={existing['seen'] + 1}")
        return
    eid = next_id(conn, "LRN")
    conn.execute("INSERT INTO events (id, type, status, topic, impact, problem, fix, duplicate_key, seen, created_at, updated_at) VALUES (?, 'learning', 'open', ?, ?, ?, ?, ?, 1, ?, ?)",
                 (eid, args.topic, args.impact, args.problem, args.fix, dup_key, now(), now()))
    conn.commit()
    print(f"added {eid}")


def add_growth(args) -> None:
    conn = ensure_db()
    eid = next_id(conn, "GROW")
    conn.execute("INSERT INTO events (id, type, topic, capability, evidence, created_at, updated_at) VALUES (?, 'growth', ?, ?, ?, ?, ?)",
                 (eid, args.topic, args.capability, args.evidence, now(), now()))
    conn.commit()
    print(f"added {eid}")


def checkpoint(args) -> None:
    conn = ensure_db()
    eid = next_id(conn, "CHK")
    conn.execute("INSERT INTO events (id, type, task, decisions, blockers, next_action, created_at) VALUES (?, 'checkpoint', ?, ?, ?, ?, ?)",
                 (eid, args.task, args.decisions, args.blockers, args.next, now()))
    conn.commit()
    print(f"added {eid}")


def verify(args) -> None:
    conn = ensure_db()
    row = conn.execute("SELECT * FROM events WHERE id = ?", (args.id,)).fetchone()
    if not row:
        raise SystemExit(f"not found: {args.id}")
    if row["type"] != "learning":
        raise SystemExit(f"not a learning: {args.id}")
    new_count = row["success_count"] + 1
    new_conf = min(0.95, 0.4 + 0.15 * new_count + 0.1 * row["seen"])
    conn.execute("UPDATE events SET status = 'verified', success_count = ?, reuse_count = reuse_count + 1, confidence = ?, updated_at = ? WHERE id = ?",
                 (new_count, new_conf, now(), args.id))
    conn.commit()
    print(f"verified {args.id} confidence={new_conf:.2f}")


def seen(args) -> None:
    conn = ensure_db()
    row = conn.execute("SELECT id, seen FROM events WHERE id = ?", (args.id,)).fetchone()
    if not row:
        raise SystemExit(f"not found: {args.id}")
    new_seen = row["seen"] + 1
    conn.execute("UPDATE events SET seen = ?, updated_at = ? WHERE id = ?", (new_seen, now(), args.id))
    conn.commit()
    print(f"seen {args.id}={new_seen}")


def promotion_candidates(conn: sqlite3.Connection) -> list[dict]:
    rows = conn.execute("SELECT * FROM events WHERE type = 'learning' AND status = 'verified' AND seen >= 3 AND impact IN ('medium', 'high') AND confidence >= 0.8").fetchall()
    return [dict(r) for r in rows]


def compact(_args=None) -> None:
    conn = ensure_db()
    cutoff = (dt.datetime.now() - dt.timedelta(days=30)).isoformat()
    archived = conn.execute("UPDATE events SET status = 'archived' WHERE type = 'learning' AND status = 'open' AND created_at < ? AND impact = 'low' AND seen <= 1", (cutoff,)).rowcount
    conn.commit()
    render_md(None)
    print(f"compact complete archived={archived} promotions={len(promotion_candidates(conn))}")


def promotions(_args=None) -> None:
    conn = ensure_db()
    cands = promotion_candidates(conn)
    if not cands:
        print("no promotion candidates")
        return
    for c in cands:
        print(f"[{c['id']}] topic={c['topic']} confidence={c['confidence']:.2f} | {c['problem']} → {c['fix']}")


def render_md(_args=None) -> None:
    conn = ensure_db()
    lines = ["# Agent Growth Log", "", f"Generated: {now()}", ""]
    lines.append("## Open Learnings")
    for r in conn.execute("SELECT * FROM events WHERE type = 'learning' AND status = 'open' ORDER BY created_at DESC"):
        lines.append(f"- [{r['id']}] topic={r['topic']} | impact={r['impact']} | seen={r['seen']} | {r['problem']} → {r['fix']}")
    lines.append("")
    lines.append("## Verified Learnings")
    for r in conn.execute("SELECT * FROM events WHERE type = 'learning' AND status = 'verified' ORDER BY confidence DESC"):
        lines.append(f"- [{r['id']}] topic={r['topic']} | confidence={r['confidence']:.2f} | seen={r['seen']} | {r['problem']} → {r['fix']}")
    lines.append("")
    lines.append("## Growth Events")
    for r in conn.execute("SELECT * FROM events WHERE type = 'growth' ORDER BY created_at DESC"):
        lines.append(f"- [{r['id']}] topic={r['topic']} | {r['capability']} — evidence: {r['evidence']}")
    lines.append("")
    lines.append("## Promotion Candidates")
    for c in promotion_candidates(conn):
        lines.append(f"- [{c['id']}] topic={c['topic']} | confidence={c['confidence']:.2f} | {c['problem']} → {c['fix']}")
    lines.append("")
    lines.append("## Checkpoints")
    for r in conn.execute("SELECT * FROM events WHERE type = 'checkpoint' ORDER BY created_at DESC LIMIT 10"):
        lines.append(f"- [{r['id']}] task={r['task']} | decisions={r['decisions']} | next={r['next_action']}")
    lines.append("")
    lines.append("## Archived")
    for r in conn.execute("SELECT * FROM events WHERE status = 'archived' ORDER BY updated_at DESC LIMIT 20"):
        lines.append(f"- [{r['id']}] topic={r['topic']} | {r['problem']} → {r['fix']}")
    REPORT.write_text("\n".join(lines) + "\n")
    print(f"rendered {REPORT}")


def report(_args=None) -> None:
    conn = ensure_db()
    counts = {}
    for r in conn.execute("SELECT type, status, COUNT(*) as cnt FROM events GROUP BY type, status"):
        counts[f"{r['type']}:{r['status']}"] = r["cnt"]
    cands = promotion_candidates(conn)
    print("Agent Growth Report")
    print(f"Database: {DB}")
    print(f"Report: {REPORT}")
    for k in sorted(counts):
        print(f"  {k}: {counts[k]}")
    print(f"  promotion_candidates: {len(cands)}")


def recall(args) -> None:
    conn = ensure_db()
    pattern = f"%{args.topic}%"
    rows = conn.execute("SELECT * FROM events WHERE topic LIKE ? AND status IN ('open', 'verified') ORDER BY confidence DESC, seen DESC LIMIT 10", (pattern,)).fetchall()
    if not rows:
        print(f"no learnings for topic: {args.topic}")
        return
    for r in rows:
        print(f"[{r['id']}] topic={r['topic']} | seen={r['seen']} | confidence={r['confidence']:.2f} | {r['problem']} → {r['fix']}")


def session_start(_args=None) -> None:
    conn = ensure_db()
    recent = conn.execute("SELECT * FROM events WHERE type = 'learning' AND status = 'verified' ORDER BY updated_at DESC LIMIT 5").fetchall()
    if not recent:
        print("no verified learnings yet")
        return
    print("Recent verified learnings (apply if relevant):")
    for r in recent:
        print(f"  [{r['id']}] {r['topic']}: {r['problem']} → {r['fix']}")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Agent Growth Protocol v0.3.2 (Standalone + SQLite)")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init").set_defaults(func=lambda a: (ensure_db(), print(f"initialized {DB}")))

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
    sub.add_parser("render-md").set_defaults(func=render_md)
    sub.add_parser("report").set_defaults(func=report)

    r = sub.add_parser("recall")
    r.add_argument("--topic", required=True)
    r.set_defaults(func=recall)

    sub.add_parser("session-start").set_defaults(func=session_start)
    return p


def main() -> None:
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
