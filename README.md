# Agent Growth Protocol

Instrumented learning loops for Hermes agents. This turns repeated mistakes into verified rules, tracks new capabilities, and compacts stale notes before memory turns into junk.

v0.2 is stricter than v0.1:

- No raw learnings in `USER.md`
- No bloating main `MEMORY.md`
- No pretending prompt instructions are full automation
- Dedicated store: `~/.hermes/memories/AGENT_GROWTH.md`
- Helper script: `agent_growth.py`
- Adds missing loops: verification + forgetting/compaction

## How It Works

```text
┌─────────────────────────────────────────────────────────────┐
│                    AGENT GROWTH SYSTEM                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. WORK HAPPENS                                             │
│     tool error | user correction | workaround | new workflow │
│                          │                                  │
│                          ▼                                  │
│  2. CAPTURE                                                  │
│     agent or script appends structured entry                 │
│                          │                                  │
│                          ▼                                  │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ ~/.hermes/memories/AGENT_GROWTH.md                  │    │
│  │                                                     │    │
│  │ Open Learnings      [LRN] status=open               │    │
│  │ Verified Learnings  [LRN] status=verified           │    │
│  │ Growth Events       [GROW]                          │    │
│  │ Checkpoints         [CHECKPOINT]                    │    │
│  │ Promotion Candidates [PROMOTE]                      │    │
│  │ Archived            stale / low-impact entries       │    │
│  └─────────────────────────────────────────────────────┘    │
│                          │                                  │
│                          ▼                                  │
│  3. VERIFY                                                  │
│     did this learning help next time?                        │
│                          │                                  │
│                          ▼                                  │
│  4. COMPACT / PROMOTE                                       │
│     seen >= 3 + verified + medium/high impact                │
│                          │                                  │
│                          ▼                                  │
│  skills / POLICY.md / USER.md / archived                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Automation Levels

| Level | Mechanism | Works Today? | Use |
|------|-----------|--------------|-----|
| 1 | Skill prompt policy | Yes | Agent self-triggers when skill is loaded |
| 2 | `agent_growth.py` helper | Yes | Reliable append/report/compact |
| 3 | Cron heartbeat | Yes | Daily report + weekly compaction |
| 4 | Hermes shell hooks | Future | Automatic tool-error interception |

Important: prompt policy is **best-effort**, not real instrumentation. The reliable path is script + cron.

## Installation

### 1. Clone

```bash
git clone https://github.com/roverdude24/agent-growth-protocol.git
cd agent-growth-protocol
```

### 2. Install Hermes skill

```bash
mkdir -p ~/.hermes/skills/autonomous-ai-agents/agent-growth-protocol
cp SKILL.md ~/.hermes/skills/autonomous-ai-agents/agent-growth-protocol/SKILL.md
```

### 3. Install helper script

```bash
mkdir -p ~/.hermes/scripts
cp scripts/agent_growth.py ~/.hermes/scripts/agent_growth.py
chmod +x ~/.hermes/scripts/agent_growth.py
```

### 4. Verify

```bash
hermes skills list | grep agent-growth
python ~/.hermes/scripts/agent_growth.py report
```

The first report creates:

```text
~/.hermes/memories/AGENT_GROWTH.md
```

## Usage

### Add a learning

```bash
python ~/.hermes/scripts/agent_growth.py add-learning \
  --topic hermes-config \
  --impact high \
  --text 'Root config write-protected → use hermes config set, not patch'
```

### Add a growth event

```bash
python ~/.hermes/scripts/agent_growth.py add-growth \
  --topic hermes \
  --text 'Can audit and patch multi-profile Hermes configs'
```

### Add a checkpoint

```bash
python ~/.hermes/scripts/agent_growth.py checkpoint \
  --task 'agent-growth-protocol v0.2' \
  --decisions 'Use dedicated AGENT_GROWTH.md store' \
  --blockers 'Shell hooks not wired yet' \
  --next 'Add cron job for weekly compaction'
```

### Report

```bash
python ~/.hermes/scripts/agent_growth.py report
```

### Compact

```bash
python ~/.hermes/scripts/agent_growth.py compact
```

## Store Schema

```markdown
# Agent Growth Log

## Open Learnings
- [LRN-001] status=open | date=2026-06-14 | topic=agy | impact=medium | seen=1 | `agy` TUI input unreliable → use `agy -p`

## Verified Learnings
- [LRN-002] status=verified | date=2026-06-14 | topic=hermes-config | impact=high | seen=3 | Root config write-protected → use `hermes config set`

## Growth Events
- [GROW-001] date=2026-06-14 | topic=hermes | Can now audit and patch multi-profile configs

## Promotion Candidates
- [PROMOTE] topic=hermes-config | seen=3 | Rule: use `hermes config set` for root config edits

## Checkpoints
- [CHECKPOINT] date=2026-06-14T18:20 | task=repo update | decisions=v0.2 store | blockers=none | next=push

## Archived
```

## Promotion Rules

Promote only when all are true:

- `status=verified`
- `seen >= 3`
- impact is `medium` or `high`
- rule is stable, reusable, and not task-specific

Destination:

| Type | Destination |
|------|-------------|
| User preference | `USER.md` |
| Agent operating rule | `POLICY.md` or profile SOUL.md |
| Procedure | Hermes skill via `skill_manage` |
| Tool-specific fix | Relevant skill Pitfalls section |
| One-off workaround | Stay in `AGENT_GROWTH.md` |

Do not promote raw tool errors into `USER.md`.

## Mnemosyne Integration

Mnemosyne is recall/search support, not primary write storage for this skill.

```text
AGENT_GROWTH.md = durable structured store
Mnemosyne       = recall/search/session context
Cron            = report + compaction automation
```

If Mnemosyne write APIs become available, mirror verified `[LRN]` and `[GROW]` entries there. Until then, keep durable writes in `AGENT_GROWTH.md`.

## Cron Automation

### Daily report

```bash
python ~/.hermes/scripts/agent_growth.py report
```

Use this in your morning briefing prompt:

```text
Run `python ~/.hermes/scripts/agent_growth.py report`. Summarize open learnings, verified learnings, growth events, and promotion candidates in under 10 bullets.
```

### Weekly compaction

```bash
python ~/.hermes/scripts/agent_growth.py compact
```

Use this in a weekly cron prompt:

```text
Run `python ~/.hermes/scripts/agent_growth.py compact`, then report new promotion candidates. Do not edit USER.md, POLICY.md, or skills without user approval.
```

## Strengths

- Dedicated learning store keeps `USER.md` and `MEMORY.md` clean
- Structured entries are easy to grep, compact, and promote
- Adds verification before promotion
- Adds forgetting/compaction loop
- Works now with plain files + script + cron

## Weaknesses

- Prompt-based auto-trigger is best-effort
- Script cannot intercept every tool call unless wired into hooks
- Compaction is simple; it does not cluster semantically yet
- Promotion still needs human approval
- Metrics are basic counts, not true error-rate reduction

## Roadmap

- Wire Hermes `post_tool_call` / `transform_tool_result` hooks once schema is verified
- Add semantic clustering for duplicate learnings
- Add `verify-learning` command
- Add error-rate metrics before/after promotion
- Mirror verified entries into Mnemosyne when write API exists

## Origin

Adapted from [AI Persona OS](https://clawhub.ai/jeffjhunter/ai-persona-os), but narrowed for Hermes. AI Persona OS has many persona and workspace patterns. This repo keeps only the parts Hermes needed: learning, verification, growth, and compaction.

## License

MIT
