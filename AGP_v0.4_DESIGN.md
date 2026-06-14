# Agent Growth Protocol v0.4 Design

## Goal
Make AGP a thin Hermes-native policy layer: keep only growth-specific policy and reporting, while delegating memory, hooks, cron, skills, and promotion plumbing to Hermes built-ins.

## Architecture
```text
User / Agent session
   │
   ├─ Hermes skills system loads AGP SKILL.md (policy only)
   │
   ├─ Hermes hooks auto-capture growth signals
   │     ├─ tool errors / repeated failures
   │     ├─ user corrections / preferences
   │     ├─ successful reusable workflows
   │     └─ checkpoints / session-end summaries
   │
   ├─ Hermes native memory
   │     ├─ MEMORY.md  -> working lessons, conventions, workflows
   │     ├─ USER.md    -> user preferences and style
   │     └─ Mnemosyne  -> long-term searchable recall / dashboard
   │
   ├─ Hermes cron
   │     └─ scheduled growth report generation
   │
   └─ Promotion flow
         ├─ verify evidence in session transcripts / lore
         ├─ gate on seen >= 3 and confidence >= 0.8
         ├─ promote via skill_manage + memory updates
         └─ write human-readable AGENT_GROWTH.md report
```

## What v0.4 SKILL.md should contain
### 1) Purpose
- State that AGP is a Hermes-native growth policy layer.
- Emphasize no standalone event store and no custom sync layer.

### 2) When to capture
- Capture reusable learnings from tool failures, corrections, successful workflows, and checkpoints.
- Prefer structured records only for growth-relevant items.

### 3) Topic naming
- `hermes-config:` for Hermes configuration issues
- `tool:` for tool-specific failures or quirks
- `workflow:` for multi-step reusable procedures
- `project:` for project-specific learnings

### 4) Capture policy
- Write to Hermes memory first, not to a separate AGP database.
- Keep entries short, concrete, and actionable.
- Avoid noise and one-off ephemeral details.

### 5) Promotion policy
- Promote only when verified, seen >= 3, confidence >= 0.8, and reusable.
- Distinguish working memory from long-term skill material.

### 6) Reporting contract
- Maintain / update `AGENT_GROWTH.md` as the human-readable report.
- Include current promoted learnings, open checkpoints, and recent growth activity.

### 7) Hermes-native integration notes
- Use hooks for capture.
- Use cron for periodic reporting.
- Use `skill_manage` for skill promotion.
- Use `memory` / Mnemosyne for persistence and recall.

### 8) Verification
- Require evidence before promotion.
- Prefer concrete examples, file paths, command names, and reproducible outcomes.

## What v0.4 should NOT contain
- No `events.jsonl` or separate event store.
- No Mnemosyne sync fallback logic.
- No quick-command wrapper duplication for Hermes slash commands.
- No auto-trigger logic embedded in skill instructions.
- No custom persistence pipeline that competes with Hermes memory.
- No shell scripts inside SKILL.md.
- No full implementation code; policy only.
- No redundant routing around `USER.md`, `MEMORY.md`, hooks, or cron.

## Hook integration
### Gateway / plugin / shell hooks
- Use Hermes hooks as the auto-capture layer.
- Hook targets:
  - `tool` failures and repeated retries
  - `agent:end` for success summaries and checkpoints
  - `command:*` for skill-related invocation patterns if useful

### Capture strategy
1. Hook observes a growth-worthy event.
2. Normalize it into a small structured record.
3. Write the record into Hermes-native memory or the growth report pipeline.
4. Do not maintain a second source of truth.

### Safety rules
- Hooks should be non-blocking.
- Hook failures must never crash the agent.
- Capture only growth-relevant events; ignore noise.

## Promotion flow
1. Capture candidate learning from hooks or session transcript.
2. Verify the evidence using Hermes session search / lore.
3. Check maturity gate:
   - `verified == true`
   - `seen >= 3`
   - `confidence >= 0.8`
4. Promote through Hermes native tools:
   - `skill_manage` for reusable procedural knowledge
   - `memory` updates for durable notes in `MEMORY.md` / `USER.md`
   - `Mnemosyne` for long-term searchable recall
5. Append/update `AGENT_GROWTH.md` with the promoted item and proof.

## Migration plan from v0.3.1 to v0.4
### Phase 1: Freeze legacy behavior
- Stop adding new logic to the old script/store model.
- Mark `events.jsonl` as deprecated.

### Phase 2: Map old data to Hermes-native stores
- Convert useful events into memory entries, skills, or report items.
- Preserve topic prefixes during conversion.

### Phase 3: Replace automation hooks
- Move auto-capture into Hermes hooks.
- Move periodic reporting into Hermes cron.

### Phase 4: Retire duplication
- Remove sync fallback code.
- Remove quick-command wrappers that mirror Hermes slash commands.
- Remove split-brain persistence paths.

### Phase 5: Promote and verify
- Reclassify the best repeated learnings into skills.
- Keep only one canonical route per concern: memory, skill, hook, or cron.

## Estimated token savings
### Current v0.3.1 footprint
- `SKILL.md`: 7,889 chars (~1,972 tokens at ~4 chars/token)
- `README.md`: 7,923 chars (~1,981 tokens)
- Combined visible docs: ~15,812 chars (~3,953 tokens)

### Expected v0.4 footprint
- Thin policy SKILL.md only: ~1,800–2,500 chars (~450–625 tokens)
- Supporting report file: separate, but not loaded as always-on policy

### Savings estimate
- Rough reduction from always-on policy text: ~68%–77%
- Net session-token savings after removing redundant quick commands / scripts / sync instructions: likely ~1,300–1,600 tokens per load

## Practical outcome
v0.4 should feel like a policy shim over Hermes rather than a parallel memory system.
It should tell Hermes **what growth means**, not reimplement **how Hermes stores or promotes knowledge**.
