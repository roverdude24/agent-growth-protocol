# Agent Growth Protocol

A lightweight system for agent self-improvement. Three loops that run alongside normal work — no extra tools, no complex setup.

Most AI agents forget everything between sessions. They repeat the same mistakes, burn credits fixing solved problems, and never get better at what they do. This protocol fixes that with three simple loops: learn from errors, track growth, and never lose context.

## What It Does

| Loop | Purpose | Where It Lives |
|------|---------|----------------|
| **Learning** | Turn errors into permanent knowledge | MEMORY.md |
| **Growth** | Track new capabilities as they emerge | MEMORY.md |
| **Never-Forget** | Checkpoint context before it's lost | Mnemosyne (ephemeral) |

## How It Works

### Loop 1: Learning (Error → Asset)

When you make a mistake or get corrected:

```
[LRN-001] agy TUI input unreliable → use `agy -p` non-interactive
```

Format: `[LRN-NNN] What happened → root cause → fix applied`

After the same pattern appears 3+ times, promote it to USER.md or POLICY.md as a permanent rule:

```
[LRN-PROMOTED] Always use hermes config set for root config — learned from 3 yaml.dump failures
```

### Loop 2: Growth (Capability Tracking)

When you learn something new:

```
[GROW-001] Can now audit and patch hermes configs across 4+ profiles
```

Format: `[GROW-NNN] Can now do X — learned from Y`

Growth events should be concrete. "Can run ComfyUI workflows via terminal" is good. "Got smarter" is not.

### Loop 3: Never-Forget (Context Checkpoint)

When context hits 70% or you're about to start a long task, flush critical state:

```
[CHECKPOINT] Active task: Mirror MV VFX. Decisions: Character track locked. Blockers: Need source footage from Vinh.
```

On session start, read your last 3 checkpoints to resume where you left off.

## Setup

### Option 1: Manual

Add this section to your MEMORY.md:

```markdown
## Learnings

## Growth
```

Start logging. That's it.

### Option 2: With Cron (Morning Briefing)

Add to your existing morning briefing cron:

```
1. Read MEMORY.md, count [LRN] entries by topic
2. If any topic has 3+ entries → flag for promotion to USER.md
3. Report: "Active learnings: N. Growth events: M. Promotions pending: [list]"
```

### Option 3: Hermes Skill

Copy `SKILL.md` to `~/.hermes/skills/autonomous-ai-agents/agent-growth-protocol/`. The agent will self-trigger on errors and session boundaries.

## Storage

| Loop | Location | Format | Retention |
|------|----------|--------|-----------|
| Learning | MEMORY.md | `[LRN] what → cause → fix` | Permanent |
| Growth | MEMORY.md | `[GROW] capability → source` | Permanent |
| Checkpoint | Mnemosyne | `[CHECKPOINT] task decisions blockers` | 48h |

## Manual Triggers

Say any of these to your agent:

- **"learn from this"** → logs a learning entry
- **"what have I learned?"** → shows recent learnings
- **"checkpoint now"** → saves current context
- **"growth report"** → summarizes recent growth

## Why This Exists

I adapted this from [AI Persona OS](https://clawhub.ai/jeffjhunter/ai-persona-os) — an agent operating system for OpenClaw 5.x with 24 personalities, SOUL.md makers, heartbeat protocols, and more. Most of it overlapped with what Hermes already does (Mnemosyne memory, config-driven personalities, cron automation).

Three things didn't have equivalents:

1. **Learning loops** — systematic error → knowledge conversion
2. **Growth tracking** — concrete capability records over time
3. **Never-forget protocol** — threshold-based context checkpointing

This skill extracts those three ideas into a minimal system that works with Hermes's existing memory infrastructure.

## Strengths

- **Zero setup** — add a section to MEMORY.md, start logging
- **Works with existing tools** — MEMORY.md for storage, Mnemosyne for recall, cron for automation
- **Concrete, not abstract** — every entry has format, location, and retention rules
- **Self-improving** — recurring errors automatically become permanent rules
- **Lightweight** — three loops, no complex state machines

## Limitations

- **Manual logging** — agent must self-trigger or be prompted; no automatic error detection
- **MEMORY.md size** — entries accumulate; need periodic pruning or archiving
- **No cross-session learning** — each session starts fresh; checkpoints help but don't replace persistent memory
- **Pattern detection is manual** — counting 3+ entries requires reading MEMORY.md; no automated promotion
- **No metrics** — tracks what was learned but not how often it's applied or whether it reduced errors

## What's Next

- [ ] Auto-detect errors from tool failures (pipe tool_output errors to learning loop)
- [ ] Add metrics: track error rate before/after learning promotions
- [ ] Integrate with Mnemosyne API for richer recall (when API supports writes)
- [ ] Add "learning velocity" metric: entries per week, promotion rate

## License

MIT
