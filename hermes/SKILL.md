---
name: agent-growth-protocol-hermes
description: "Hermes-native growth policy layer. Uses Hermes hooks, memory, cron, and skill_manage — no standalone event store."
version: 0.4.0
author: Vinh Lam
license: MIT
tags: [agent, growth, learning, memory, hermes-native, policy]
---

# Agent Growth Policy (Hermes-Native)

A thin policy layer that tells Hermes what growth means and when to promote knowledge. Uses Hermes built-ins for everything: memory, hooks, cron, skills, recall.

This is NOT a standalone system. This is policy + reporting on top of Hermes.

## What this does

1. **Capture** — when tool errors, corrections, or reusable workflows happen, write structured lessons to Hermes memory (not a separate database)
2. **Verify** — require evidence before promoting. Use session search / lore to confirm reuse
3. **Promote** — gate on `seen >= 3` + `confidence >= 0.8`. Route through `skill_manage`, `USER.md`, `POLICY.md`
4. **Report** — maintain `AGENT_GROWTH.md` as human-readable growth summary

## What this does NOT do

- No standalone event store (uses Hermes session transcripts + lore)
- No custom script (uses Hermes hooks + cron)
- No quick-command wrappers (uses Hermes native skill commands)
- No memory sync fallback (uses Hermes native memory)
- No auto-trigger logic in this skill (uses Hermes hooks)

## Topic naming convention

Prefix all growth records with:

- `hermes-config:` — configuration issues
- `tool:` — tool-specific failures
- `workflow:` — multi-step procedures
- `project:` — project-specific learnings

## Capture policy

When capturing growth events:

1. Write to Hermes memory first (`MEMORY.md` or `Mnemosyne`)
2. Keep entries short, concrete, actionable
3. Avoid noise and one-off ephemeral details
4. Use topic prefix for organization

Format:

```
[AGENT_LEARNING] <topic>: <problem> → <fix>
[AGENT_CAPABILITY] <topic>: <capability> — evidence: <proof>
```

## Promotion policy

Promote only when ALL true:

- `status=verified` (confirmed working in later session)
- `seen >= 3` (repeatedly useful)
- `confidence >= 0.8` (high confidence)
- Rule is stable, reusable, not task-specific

Route:

| Learning type | Destination |
|---|---|
| User preference | `USER.md` |
| Operating rule | `POLICY.md` or `SOUL.md` |
| Repeatable workflow | Hermes skill via `skill_manage` |
| Tool pitfall | Relevant skill Pitfalls section |
| One-off workaround | Stays in memory, not promoted |

## Verification method

Before promoting, verify using:

1. `session_search` — find where the learning was applied
2. `lore` — search across session transcripts for reuse evidence
3. Concrete proof: file paths, command names, reproducible outcomes

## Reporting contract

Maintain `AGENT_GROWTH.md` with:

- Current promoted learnings
- Open checkpoints
- Recent growth activity
- Promotion candidates

Update via cron or manual trigger.

## Hermes-native integration

| Function | Hermes tool |
|---|---|
| Capture | Hooks (post_tool_call, on_session_end) |
| Storage | MEMORY.md, USER.md, Mnemosyne |
| Recall | session_search, lore |
| Reporting | Cron job → generate AGENT_GROWTH.md |
| Promotion | skill_manage, memory updates |

## Cron setup

Daily report:

```
Read MEMORY.md for [AGENT_LEARNING] entries. Summarize: open learnings, verified learnings, growth events, promotion candidates. Under 10 bullets.
```

Weekly compaction:

```
Review MEMORY.md [AGENT_LEARNING] entries. Archive stale low-impact items. Flag 3+ patterns for promotion. Ask user before editing USER.md/POLICY.md/skills.
```
