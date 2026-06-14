# Agent Growth Protocol

A lightweight system for agent self-improvement. Three loops that run alongside normal work — no extra tools, no complex setup.

Most AI agents forget everything between sessions. They repeat the same mistakes, burn credits fixing solved problems, and never get better at what they do. This protocol fixes that with three simple loops: learn from errors, track growth, and never lose context.

## How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                    AGENT WORK SESSION                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐             │
│  │  ERROR   │    │ NEW SKILL│    │ LONG TASK│             │
│  │ occurred │    │ acquired │    │ starting │             │
│     └──┬─────┘    └────┬─────┘    └────┬─────┘             │
│        │               │               │                    │
│        ▼               ▼               ▼                    │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐             │
│  │  LOOP 1  │    │  LOOP 2  │    │  LOOP 3  │             │
│  │ Learning │    │  Growth  │    │Checkpoint│             │
│  └────┬─────┘    └────┬─────┘    └────┬─────┘             │
│       │               │               │                    │
│       ▼               ▼               ▼                    │
│  ┌─────────────────────────────────────────┐              │
│  │              MEMORY.md                  │              │
│  │  [LRN-001] error → cause → fix         │              │
│  │  [GROW-001] can now do X               │              │
│  └─────────────────────────────────────────┘              │
│       │                                                    │
│       ▼  (3+ recurring)                                    │
│  ┌─────────────────────────────────────────┐              │
│  │              USER.md                    │              │
│  │  [LRN-PROMOTED] permanent rule          │              │
│  └─────────────────────────────────────────┘              │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  MNEMOSYNE (ephemeral)                                     │
│  [CHECKPOINT] task state → auto-prune 48h                  │
└─────────────────────────────────────────────────────────────┘
```

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

## Installation

### Step 1: Copy Skill to Hermes

```bash
# Clone the repo
git clone https://github.com/roverdude24/agent-growth-protocol.git

# Copy skill to Hermes
cp -r agent-growth-protocol/SKILL.md ~/.hermes/skills/autonomous-ai-agents/agent-growth-protocol/

# Verify installation
hermes skills list | grep growth
```

### Step 2: Add Learnings Section to MEMORY.md

```bash
# Open your MEMORY.md
open ~/.hermes/memories/MEMORY.md

# Add these sections at the end:
```

```markdown
§
## Learnings

## Growth
```

### Step 3: Configure Mnemosyne Integration

Mnemosyne dashboard must be running for checkpoint storage:

```bash
# Check if Mnemosyne is running
curl -s http://127.0.0.1:8765/api/auth/status

# If not running, start it
hermes mnemosyne start
```

### Step 4: (Optional) Add to Morning Briefing Cron

```bash
# Add to your existing morning briefing cron prompt:
1. Read MEMORY.md, count [LRN] entries by topic
2. If any topic has 3+ entries → flag for promotion to USER.md
3. Report: "Active learnings: N. Growth events: M. Promotions pending: [list]"
```

## Integration with Mnemosyne

### How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                    STORAGE LAYERS                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PERMANENT (MEMORY.md)          EPHEMERAL (Mnemosyne)      │
│  ┌─────────────────────┐       ┌─────────────────────┐    │
│  │ [LRN-001] ...       │       │ [CHECKPOINT] ...    │    │
│  │ [LRN-002] ...       │       │ [CHECKPOINT] ...    │    │
│  │ [GROW-001] ...      │       │                     │    │
│  │                     │       │ Auto-prune: 48h     │    │
│  │ Manual edit only    │       │ API: read-only      │    │
│  └─────────────────────┘       └─────────────────────┘    │
│           │                               │                 │
│           ▼                               ▼                 │
│  ┌─────────────────────┐       ┌─────────────────────┐    │
│  │ USER.md (promoted)  │       │ Dashboard: view     │    │
│  │ POLICY.md (rules)   │       │ Search: recall      │    │
│  └─────────────────────┘       └─────────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Storage Locations

| Loop | Location | Format | Retention | Access |
|------|----------|--------|-----------|--------|
| Learning | MEMORY.md | `[LRN] what → cause → fix` | Permanent | Manual edit |
| Growth | MEMORY.md | `[GROW] capability → source` | Permanent | Manual edit |
| Checkpoint | Mnemosyne | `[CHECKPOINT] task decisions blockers` | 48h | API read-only |
| Promoted | USER.md | `[LRN-PROMOTED] rule` | Permanent | Manual edit |

### Recall Patterns

1. **Session start:** Read MEMORY.md for recent `[LRN]` and `[GROW]` entries
2. **On error:** Search MEMORY.md for similar `[LRN]` entries before fixing
3. **Weekly:** Count `[LRN]` entries, promote 3+ count patterns to USER.md
4. **Checkpoint resume:** Query Mnemosyne API for recent checkpoints

```bash
# Query Mnemosyne for recent checkpoints
curl -s http://127.0.0.1:8765/api/memories | jq '.items[] | select(.content | contains("CHECKPOINT"))'
```

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
