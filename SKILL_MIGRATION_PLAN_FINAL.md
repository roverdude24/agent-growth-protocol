# Hermes Skill Migration Plan — Lean Unified Profile

## Executive summary
This plan rebuilds the Hermes skill stack around a **lean unified profile** with:
- **18 core production skills** loaded for real daily work
- **personal utilities kept** but treated as **on-demand** rather than always-on
- **gaming, social media, smart-home, and novelty retired**

The goal is to keep the profile small, production-relevant, and maintainable while preserving the workflows that actually ship work.

---

## Decision boundaries

### Keep
- Production-relevant skills
- Personal utilities that support real workflow or quality of life
- All core agent / creative / code / ops capabilities

### Retire
- Gaming
- Social media
- Smart home
- Novelty / experimental / entertainment skills that do not support production output

---

## Unified lane structure

### 1) core — always loaded
Agent and orchestration skills used in every session.

### 2) code
Code delivery, GitHub workflow, agentic coding, and debugging support.

### 3) creative
Video, image, prompt, and generation pipelines.

### 4) ops
Notion and production coordination utilities.

### 5) review
Review / verification / debugging workflow overlay.
- Primary skill: `systematic-debugging`
- Any dedicated `code-review` helper stays here if present

### 6) personal — on demand
Personal utilities that are kept, but not loaded unless needed.

---

## Lean production set: 18 core skills

### core lane — agent / orchestration (4)
1. `hermes-agent`
2. `local-subagent-routing`
3. `process-first-routing`
4. `native-mcp`

### code lane — code delivery (5)
5. `claude-code`
6. `codex`
7. `opencode`
8. `github-workflow`
9. `systematic-debugging`

### creative lane — generation stack (8)
10. `ai-film-runbook`
11. `ai-media-generation`
12. `comfyui`
13. `cinematic-prompt`
14. `production-orchestrator`
15. `video-gen-pipeline`
16. `image-gen-pipeline`
17. `higgsfield-generate`

### ops lane — production coordination (1)
18. `notion`

**Count: 18 core production skills.**

---

## Personal utilities kept, but on-demand
These are retained because they support the user directly, but they are **not part of the always-loaded core**.

### Apple utilities
- `apple` / Apple utilities for notes, reminders, Find My, iMessage

### Email
- `email/himalaya`

### Research
- `research/arxiv`
- `research/blogwatcher`
- `research/llm-wiki`

### Productivity
- `productivity/airtable`
- `productivity/google-workspace`
- `productivity/linear` if actively used

### Media
- `media/spotify` if actively used
- `media/youtube-content` if actively used

**Policy:** keep these available, but do not let them expand the always-loaded profile.

---

## Retire list
Retire these categories entirely for this lean profile:
- `gaming`
- `social-media`
- `smart-home`
- novelty / entertainment skills such as:
  - ASCII / visual gimmicks
  - p5js
  - Manim
  - songwriting / AI music
  - TouchDesigner
  - other non-production creative toys unless explicitly needed for a deliverable

---

## Migration order

### Phase 1 — Core foundation first
Move and validate the 18 core production skills first:
1. core lane
2. code lane
3. creative lane
4. ops lane

### Phase 2 — Review lane
Add review support after the core is stable.
- Keep review workflow minimal
- Prefer reuse of `systematic-debugging` rather than introducing extra review baggage
- Keep review routing lightweight and production-focused

### Phase 3 — Personal utilities
Add personal utilities as optional/on-demand mounts:
- Apple utilities
- Email
- Research
- Productivity
- Media

### Phase 4 — Retire obsolete skills
Remove retired categories only after the lean stack is confirmed working:
- gaming
- social media
- smart home
- novelty/entertainment skills

---

## Lane assignment summary

| Lane | Purpose | Status |
| --- | --- | --- |
| core | Hermes routing and orchestration | Always loaded |
| code | GitHub, coding agents, debugging | Core |
| creative | AI film, image, video, prompting | Core |
| ops | Notion and production ops | Core |
| review | verification / debugging overlay | Minimal / supporting |
| personal | Apple, email, research, media, productivity | On-demand |

---

## Recommended migration policy

### Keep these design rules
- Do not expand the core beyond the 18 production skills
- Do not carry category skeletons that exist only for completeness
- Keep personal utilities accessible, but off the critical path
- Prefer fewer, stronger skills over broad catalog coverage
- Retire anything that does not help create, coordinate, ship, or verify work

### Do not reintroduce retired areas unless there is a real workflow need
- gaming
- social media
- smart home
- novelty / toy skills

---

## Rollback plan
Rollback must be reversible at every phase.

### Before migration
- Snapshot the current skill tree
- Preserve source directories until validation passes
- Record the final mapping of old path → new lane

### If a lane fails
- Restore only the affected lane from backup
- Re-enable the previous profile mount for that lane
- Keep the rest of the unified profile intact

### If the unified profile is unstable
- Revert to the last known-good multi-profile setup
- Restore the old skill directories from snapshot
- Re-run migration one lane at a time

### Verification gates before deleting old paths
- Core routing works
- Code lane resolves correctly
- Creative generation lane resolves correctly
- Ops lane resolves correctly
- Personal utilities work when mounted on demand
- No required workflow depends on retired categories

---

## Final recommendation
Adopt the lean unified profile with:
- **18 core production skills**
- **personal utilities retained on demand**
- **gaming / social / smart-home / novelty retired**

This keeps the Hermes stack focused on actual production work while remaining easy to maintain and easy to roll back.
