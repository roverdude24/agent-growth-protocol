---
name: agent-growth-protocol
description: "Instrumented learning pipeline for standalone agents: SQLite database, generated report, verification, compaction, and recall."
version: 0.3.1
author: Vinh Lam
license: MIT
tags: [agent, growth, learning, memory, mnemosyne, automation, telemetry]
---

# Agent Growth Protocol

Turn repeated agent mistakes into verified long-term knowledge.

This is not a persona system. This is an agent learning pipeline:

```text
tool error / correction / workaround
  → structured event in SQLite database
  → generated report.md report
  → verify reuse and success
  → compact duplicates / stale entries
  → recall / session-start to load learnings

## Core Files

```text
~/.agent_growth/growth.db                     # SQLite database (source of truth)
~/.agent_growth/report.md                     # generated human report
~/.agent_growth/bin/agent_growth.py           # automation helper
```

Do not use `USER.md` or main `MEMORY.md` as the raw learning store.

## Automation Reality

Automation levels:

1. **Skill policy** — best-effort. Active only when skill is loaded.
2. **Script helper** — reliable. Appends, verifies, compacts, renders, reports, syncs.
3. **Cron** — reliable scheduled automation. Daily report + weekly compact/sync.
4. **Shell hooks** — future work. Use only after Hermes hook schema is verified.

Never claim full automation unless script/cron/hooks are installed and tested.

## Event Types

### Learning

```bash
python3 ~/.agent_growth/bin/agent_growth.py add-learning \
  --topic tool-config \
  --impact high \
  --problem 'Root config write-protected from patch' \
  --fix 'Use hermes config set for root config edits'
```

### Growth

```bash
python3 ~/.agent_growth/bin/agent_growth.py add-growth \
  --topic database \
  --capability 'Can audit and patch multi-profile config' \
  --evidence 'Fixed default/review-board/creative/executive profile MCP surfaces'
```

### Checkpoint

```bash
python3 ~/.agent_growth/bin/agent_growth.py checkpoint \
  --task 'long task name' \
  --decisions 'key decisions' \
  --blockers 'current blockers' \
  --next 'next action'
```

### Verify

```bash
python3 ~/.agent_growth/bin/agent_growth.py verify \
  --id LRN-001 \
  --evidence 'Applied fix successfully in later session'
```

### Report / Render / Compact / Sync

```bash
python3 ~/.agent_growth/bin/agent_growth.py report
python3 ~/.agent_growth/bin/agent_growth.py render-md
python3 ~/.agent_growth/bin/agent_growth.py compact
python3 ~/.agent_growth/bin/agent_growth.py session-start
python3 ~/.agent_growth/bin/agent_growth.py recall --topic tool
```


## Promotion Rules

Promote only when all true:
- status is `verified`
- seen >= 3
- confidence >= 0.8
- impact is medium/high
- rule is stable and reusable

Destination:

| Type | Destination |
|---|---|
| User preference | USER.md |
| Agent operating policy | POLICY.md or SOUL.md |
| Repeatable workflow | Hermes skill via skill_manage |
| Tool pitfall | Relevant skill Pitfalls section |
| One-off workaround | Stay in event store |

Do not promote unverified learnings.

## Cron Recommendations

Daily:

```text
Run `python3 ~/.agent_growth/bin/agent_growth.py report`. Summarize open learnings, verified learnings, growth events, and promotion candidates in under 10 bullets.
```

Weekly:

```text
Run compact → promotions. Ask user before editing USER.md, POLICY.md, or skills.
```

## Agent Behavior Rules

When this skill is loaded:

1. After a reusable error or correction, call `add-learning` via terminal.
2. After successfully reusing a previous fix, call `verify` via terminal.
3. Before long work or context risk, call `checkpoint` via terminal.
4. At end of complex work, call `add-growth` if a new repeatable capability emerged.
5. Do not log trivial noise.
6. Do not sync raw unverified entries into long-term memory.
7. Use `agp-` prefix for all commands to avoid collision with other skills.

## Quick Commands

User can trigger with one word. Agent interprets and runs script.

| Command | What it does |
|---------|-------------|
| `/agp-learn` | Log a learning entry |
| `/agp-grow` | Log a growth event |
| `/agp-checkpoint` | Save checkpoint |
| `/agp-report` | Show report |
| `/agp-compact` | Compact stale entries |
| `/agp-session` | Show session-start |

## Auto-Trigger Table

| Event | Action | Command |
|-------|--------|---------|
| Tool returns error | Log learning | `add-learning` |
| User corrects agent | Log learning | `add-learning` |
| Agent retries same tool 2+ times | Log learning | `add-learning` |
| Workaround discovered | Log learning | `add-learning` |
| Agent completes new workflow | Log growth | `add-growth` |
| Context > 70% or long task starts | Checkpoint | `checkpoint` |
| Learning reused successfully | Verify | `verify` |

## Command Templates

```bash
# After tool error
python3 ~/.agent_growth/bin/agent_growth.py add-learning \
  --topic "<topic>" \
  --impact "<low|medium|high>" \
  --problem "<what went wrong>" \
  --fix "<what fixed it>"

# After new capability
python3 ~/.agent_growth/bin/agent_growth.py add-growth \
  --topic "<domain>" \
  --capability "<what agent can now do>" \
  --evidence "<proof>"

# Before long task
python3 ~/.agent_growth/bin/agent_growth.py checkpoint \
  --task "<task name>" \
  --decisions "<key decisions>" \
  --blockers "<blockers>" \
  --next "<next action>"

# After reusing a fix
python3 ~/.agent_growth/bin/agent_growth.py verify \
  --id "<LRN-NNN>" \
  --evidence "<proof it worked>"
```

## Topic Naming Convention

Use prefix to avoid collision with other systems:

```
hermes-config:<subtopic>    — Hermes configuration issues
tool:<tool-name>            — tool-specific failures
workflow:<name>             — workflow learnings
user:<preference>           — user preference learnings
project:<project-name>      — project-specific learnings
```

## Pitfalls

- SQLite is source of truth; markdown report is generated.
- Use `python3`, not `python`, on macOS.
- Keep `USER.md` for user preferences, not tool tactics.
- Keep `report.md` lean; sync only compact verified items.
- Shell hook integration remains future work until tested.
- Public README must avoid local `file://` links and avoid claiming fake automation.
- When using `install.sh`, always push repo changes FIRST before running the script — remote clone may pull old version.
- For creative writing (README, captions), use two-pass pipeline: agy drafts → GPT-5.5 reviews/rewrites → parent polishes. agy is strong at structure, GPT-5.5 at copy quality.

## References

- `references/v0.3-design-notes.md` — session-specific design notes for JSONL source-of-truth, Mnemosyne sync fallback, one-line install, and GitHub README presentation.
- `references/review-pipeline.md` — two-pass agy→GPT-5.5 review pipeline for README/caption writing.
