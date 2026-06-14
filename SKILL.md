---
name: agent-growth-protocol
description: "Instrumented learning pipeline for Hermes agents: JSONL event store, generated report, Mnemosyne sync fallback, verification, compaction, and promotion routing."
version: 0.3.0
author: Vinh Lam
license: MIT
tags: [agent, growth, learning, memory, mnemosyne, automation, telemetry]
---

# Agent Growth Protocol

Turn repeated agent mistakes into verified long-term knowledge.

This is not a persona system. This is an agent learning pipeline:

```text
tool error / correction / workaround
  → structured event in events.jsonl
  → generated AGENT_GROWTH.md report
  → verify reuse and success
  → compact duplicates / stale entries
  → sync verified high-value rules into long-term memory
  → promote stable rules into skills, POLICY.md, or USER.md only when appropriate
```

## Core Files

```text
~/.hermes/memories/agent_growth/events.jsonl   # source of truth
~/.hermes/memories/AGENT_GROWTH.md            # generated human report
~/.hermes/scripts/agent_growth.py             # automation helper
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
python3 ~/.hermes/scripts/agent_growth.py add-learning \
  --topic hermes-config \
  --impact high \
  --problem 'Root config write-protected from patch' \
  --fix 'Use hermes config set for root config edits'
```

### Growth

```bash
python3 ~/.hermes/scripts/agent_growth.py add-growth \
  --topic hermes \
  --capability 'Can audit and patch multi-profile config' \
  --evidence 'Fixed default/review-board/creative/executive profile MCP surfaces'
```

### Checkpoint

```bash
python3 ~/.hermes/scripts/agent_growth.py checkpoint \
  --task 'long task name' \
  --decisions 'key decisions' \
  --blockers 'current blockers' \
  --next 'next action'
```

### Verify

```bash
python3 ~/.hermes/scripts/agent_growth.py verify \
  --id LRN-001 \
  --evidence 'Applied fix successfully in later session'
```

### Report / Render / Compact / Sync

```bash
python3 ~/.hermes/scripts/agent_growth.py report
python3 ~/.hermes/scripts/agent_growth.py render-md
python3 ~/.hermes/scripts/agent_growth.py compact
python3 ~/.hermes/scripts/agent_growth.py sync-mnemosyne
```

## Mnemosyne Sync Rule

Sync only high-value memories into long-term recall.

Sync if:
- learning is `status=verified`
- confidence >= 0.8 OR impact=high
- rule is reusable across future sessions

Do not sync:
- one-off command typos
- transient network/API errors
- user preferences (those belong in USER.md)
- raw checkpoints unless needed for active task recovery

Current implementation:
- If direct Mnemosyne write API is unavailable, `sync-mnemosyne` writes a compact `## Agent Growth Sync` block into `MEMORY.md`.
- Hermes/Mnemosyne can then ingest/recall that durable memory.

Memory format:

```text
[AGENT_LEARNING] hermes-config: Root config write-protected → use hermes config set
[AGENT_CAPABILITY] hermes: Can audit multi-profile Hermes configs — evidence: profile audit fixed
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
Run `python3 ~/.hermes/scripts/agent_growth.py report`. Summarize open learnings, verified learnings, growth events, and promotion candidates in under 10 bullets.
```

Weekly:

```text
Run compact → promotions → sync-mnemosyne. Ask user before editing USER.md, POLICY.md, or skills.
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
| `/agp-sync` | Sync to long-term memory |

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
python3 ~/.hermes/scripts/agent_growth.py add-learning \
  --topic "<topic>" \
  --impact "<low|medium|high>" \
  --problem "<what went wrong>" \
  --fix "<what fixed it>"

# After new capability
python3 ~/.hermes/scripts/agent_growth.py add-growth \
  --topic "<domain>" \
  --capability "<what agent can now do>" \
  --evidence "<proof>"

# Before long task
python3 ~/.hermes/scripts/agent_growth.py checkpoint \
  --task "<task name>" \
  --decisions "<key decisions>" \
  --blockers "<blockers>" \
  --next "<next action>"

# After reusing a fix
python3 ~/.hermes/scripts/agent_growth.py verify \
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

- JSONL is source of truth; markdown report is generated.
- Use `python3`, not `python`, on macOS.
- Keep `USER.md` for user preferences, not tool tactics.
- Keep `MEMORY.md` lean; sync only compact verified items.
- Shell hook integration remains future work until tested.
- Public README must avoid local `file://` links and avoid claiming fake automation.

## References

- `references/v0.3-design-notes.md` — session-specific design notes for JSONL source-of-truth, Mnemosyne sync fallback, one-line install, and GitHub README presentation.
