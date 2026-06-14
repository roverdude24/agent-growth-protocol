---
name: agent-growth-protocol
description: "Learning loops, growth tracking, never-forget checkpointing. Integrates with Mnemosyne memory for persistent agent improvement."
version: 0.1.0
author: Vinh Lam (adapted from AI Persona OS concepts)
tags: [agent, growth, learning, memory, mnemosyne]
---

# Agent Growth Protocol

Lightweight system for agent self-improvement. Three loops that run alongside normal work.

## When to Use

- After errors or corrections (learning loop)
- During session wrap / heartbeat (growth check)
- When context gets long (never-forget checkpoint)

## Loop 1: Learning (Error → Asset)

When agent makes mistake or user corrects:

1. Log to Mnemosyne with dimension `learning`:
   ```
   mnemosyne_remember(
     content="[LRN] What happened → root cause → fix applied",
     category="learning",
     project="<current project path>",
     tags=["error", "<topic>"]
   )
   ```
2. If same pattern appears 3+ times → promote to USER.md or POLICY.md:
   ```
   # In USER.md or POLICY.md
   [LRN-PROMOTED] <rule> — learned from <N> occurrences of <pattern>
   ```
3. Tag with `recurring` when promoting.

**Dimensions:** `learning` (mistake + fix), `pattern` (recurring behavior), `error` (one-off failure)

## Loop 2: Growth (Capability Tracking)

Track what agent can do now vs. couldn't before.

Weekly (via cron or manual):
1. Recall recent learnings:
   ```
   mnemosyne_recall(dimension="learning", limit=10)
   ```
2. Count patterns by topic.
3. If new capability emerged → log growth event:
   ```
   mnemosyne_remember(
     content="[GROW] Can now do <X> — learned from <Y>",
     category="growth",
     tags=["capability", "<domain>"]
   )
   ```

**Growth categories:**
- `capability` — new thing agent can do
- `pattern` — recognized workflow pattern
- `optimization` — faster/cheaper way to do existing thing

## Loop 3: Never-Forget (Context Checkpoint)

When context window > 70% or before long task:

1. Flush critical context to Mnemosyne:
   ```
   mnemosyne_remember(
     content="[CHECKPOINT] Active task: <X>. Key decisions: <Y>. Blockers: <Z>.",
     category="checkpoint",
     project="<path>",
     tags=["checkpoint", "<task>"]
   )
   ```
2. On session start / resume, recall recent checkpoints:
   ```
   mnemosyne_recall(dimension="checkpoint", limit=3, sort="newest")
   ```

**Threshold:** checkpoint when context_pct > 70% OR message_count > 40.

## Integration with Mnemosyne + MEMORY.md

Mnemosyne dashboard (port 8765) is read-only for memories. Storage happens through MEMORY.md files.

### Storage Pattern

| Loop | Where | Format | Retention |
|------|-------|--------|-----------|
| Learning | MEMORY.md § | `[LRN] <what> → <root cause> → <fix>` | permanent (promote to USER.md if recurring) |
| Growth | MEMORY.md § | `[GROW] Can now do <X> — learned from <Y>` | permanent |
| Checkpoint | Mnemosyne via `mnemosyne_remember` | `[CHECKPOINT] <task> <decisions> <blockers>` | 48h (ephemeral) |

### Recall Pattern

1. On session start: read MEMORY.md for recent `[LRN]` and `[GROW]` entries
2. On error: search MEMORY.md for similar `[LRN]` entries before fixing
3. Weekly: count `[LRN]` entries, promote 3+ count patterns to USER.md

### MEMORY.md Section Format

```markdown
§
## Learnings
- [LRN-001] agy TUI input unreliable → use `agy -p` non-interactive
- [LRN-002] yaml.dump corrupts hermes config → use hermes config set for root

## Growth
- [GROW-001] Can now run ComfyUI workflows via terminal
- [GROW-002] Can audit and patch hermes configs across profiles
```

## Manual Triggers

Agent can self-trigger:
- "learn from this" → append `[LRN]` to MEMORY.md
- "what have I learned?" → grep MEMORY.md for `[LRN]`
- "checkpoint now" → mnemosyne_remember with checkpoint content
- "growth report" → grep MEMORY.md for `[GROW]`

## Cron Integration

Add to existing morning briefing cron:
```
1. Read MEMORY.md, count [LRN] entries by topic
2. If any topic has 3+ entries → flag for promotion to USER.md
3. Report: "Active learnings: N. Growth events: M. Promotions pending: [list]"
```

## Pitfalls

- Don't log trivial learnings (e.g., "user likes X") — that's USER.md territory.
- Checkpoints are ephemeral — don't treat them as permanent memory.
- Growth events should be concrete ("can now run ComfyUI workflows") not vague ("got smarter").
- Don't auto-promote to POLICY.md without user approval.
