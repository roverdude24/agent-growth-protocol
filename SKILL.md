---
name: agent-growth-protocol
description: "Instrumented learning, growth, forgetting, and verification loops for Hermes agents. Uses a dedicated AGENT_GROWTH.md store plus optional cron/script automation."
version: 0.2.0
author: Vinh Lam
license: MIT
tags: [agent, growth, learning, memory, mnemosyne, automation]
---

# Agent Growth Protocol

Make agent improvement operational, not vibes. Capture errors, verify fixes, compact stale entries, and promote proven rules.

## Core Change in v0.2

Do **not** use `USER.md` or main `MEMORY.md` as the raw learning store.

Use a dedicated file:

```text
~/.hermes/memories/AGENT_GROWTH.md
```

Why:
- `USER.md` is for user preferences and has tight context budget.
- `MEMORY.md` is working memory and should stay lean.
- Agent learnings need lifecycle: open → verified → promoted → archived.

## Automation Reality

This skill has three automation levels:

1. **Best-effort prompt policy** — active when skill is loaded. Agent self-triggers after tool errors, user corrections, or repeated retries.
2. **Scripted helper** — `scripts/agent_growth.py` writes structured entries, reports patterns, compacts old entries, and exports promotion candidates.
3. **Cron heartbeat** — daily/weekly job runs report + compaction. This is the minimum reliable automation today.

Shell hooks are not required for v0.2. They are future work when Hermes hook schema is wired and tested.

## Store Schema

Entries live in `AGENT_GROWTH.md`.

```markdown
# Agent Growth Log

## Open Learnings
- [LRN-001] status=open | topic=agy | impact=medium | seen=1 | `agy` TUI input unreliable → use `agy -p` for scripted prompts

## Verified Learnings
- [LRN-002] status=verified | topic=hermes-config | impact=high | seen=3 | Root config write-protected → use `hermes config set`, not patch

## Growth Events
- [GROW-001] topic=hermes | Can now audit and patch multi-profile Hermes configs

## Promotion Candidates
- [PROMOTE] topic=hermes-config | seen=3 | Rule: use `hermes config set` for root config edits

## Archived
```

## Loop 1 — Learning

Trigger:
- Tool error
- User correction
- Same failed approach retried 2+ times
- Workaround discovered

Action:
1. Append `[LRN]` to `AGENT_GROWTH.md` with `status=open`.
2. If similar topic exists, increment `seen` instead of adding duplicate.
3. After successful reuse, mark `status=verified`.

Format:

```text
[LRN-###] status=open | topic=<topic> | impact=<low|medium|high> | seen=<n> | <problem> → <fix>
```

## Loop 2 — Verification

Trigger:
- Agent encounters same topic later
- Agent applies previous fix
- Task succeeds after using learning

Action:
- Change `status=open` → `status=verified`
- Add short evidence after entry: `verified=<date>: <what succeeded>`

Rule:
- Do not promote unverified learnings.
- Do not count anecdote as improvement until reused successfully.

## Loop 3 — Forgetting / Compaction

Trigger:
- `AGENT_GROWTH.md` exceeds 80 entries
- Weekly cron runs
- Entries older than 30 days remain unverified

Action:
- Merge duplicate topics
- Archive stale low-impact entries
- Keep high-impact verified entries
- Generate promotion candidates when `seen >= 3` and `status=verified`

## Loop 4 — Growth

Trigger:
- New toolchain works
- New workflow becomes repeatable
- Agent completes task class it failed before

Action:
Append `[GROW]` entry.

Format:

```text
[GROW-###] topic=<domain> | capability=<concrete ability> | evidence=<task/result>
```

## Loop 5 — Checkpoint

Trigger:
- Context > 70%
- Long multi-step task starts
- Before risky/bulk mutation

Action:
Append `[CHECKPOINT]` to `AGENT_GROWTH.md` or use Hermes/Mnemosyne session memory if available.

Format:

```text
[CHECKPOINT] task=<task> | decisions=<decisions> | blockers=<blockers> | next=<next action>
```

## Promotion Rules

Promote only when all true:
- `status=verified`
- `seen >= 3`
- impact is `medium` or `high`
- rule is stable and not task-specific

Destination:
- User preference → `USER.md`
- Agent operating rule → `POLICY.md` or profile SOUL.md
- Procedure → create/update a Hermes skill with `skill_manage`
- Tool-specific fix → keep in `AGENT_GROWTH.md` or relevant skill Pitfalls section

Never promote raw errors directly into `USER.md`.

## Mnemosyne Integration

Mnemosyne is recall/search layer, not primary write layer for this skill.

Use:
- `AGENT_GROWTH.md` = durable structured store
- Mnemosyne/session memory = recall context and ephemeral checkpoints
- Cron = compaction/report automation

If Mnemosyne write API becomes available later, mirror verified `[LRN]` and `[GROW]` entries there.

## Script Helper

Install helper:

```bash
mkdir -p ~/.hermes/scripts
cp scripts/agent_growth.py ~/.hermes/scripts/agent_growth.py
chmod +x ~/.hermes/scripts/agent_growth.py
```

Use:

```bash
python ~/.hermes/scripts/agent_growth.py add-learning --topic agy --impact medium --text "TUI input unreliable → use agy -p"
python ~/.hermes/scripts/agent_growth.py add-growth --topic hermes --text "Can audit multi-profile config"
python ~/.hermes/scripts/agent_growth.py report
python ~/.hermes/scripts/agent_growth.py compact
```

## Cron Automation

Daily report:

```text
Read ~/.hermes/memories/AGENT_GROWTH.md. Report open learnings, verified learnings, growth events, and promotion candidates. Keep under 10 bullets.
```

Weekly compaction:

```text
Run ~/.hermes/scripts/agent_growth.py compact. Then summarize promotion candidates and ask user before promoting any rule.
```

## Pitfalls

- Do not log every minor error. Log only reusable lessons.
- Do not promote unverified learnings.
- Do not put agent/tool tactics in `USER.md` unless they reflect user preference.
- Do not claim full automation unless hooks or cron are installed and tested.
- Do not let `AGENT_GROWTH.md` become second `MEMORY.md`; compact weekly.
