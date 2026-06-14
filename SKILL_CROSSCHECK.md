# Skill Migration Cross-Check

## Scope
- Plan reviewed: `SKILL_MIGRATION_PLAN_FINAL.md`
- Files scanned: **715** `SKILL.md` files under `~/.hermes`
- Method: compared the plan against the filesystem skill tree, then grouped nested subskills/aliases into workflow families so the output is deduped by function instead of raw file count.

## Already covered by the plan
I did **not** flag skills already present in the plan, including:
- `hermes-agent`, `local-subagent-routing`, `process-first-routing`, `native-mcp`
- `claude-code`, `codex`, `opencode`, `github-workflow`, `systematic-debugging`
- `ai-film-runbook`, `ai-media-generation`, `comfyui`, `cinematic-prompt`
- `production-orchestrator`, `video-gen-pipeline`, `image-gen-pipeline`, `higgsfield-generate`, `notion`

## Missed production-relevant skills — keep
These are present in the filesystem but missing from the final plan, and they are production-relevant enough that I would **keep** them.

### High-priority creative / film families
- **`seedance-20` family** — **keep**
  - root + subskills found: `seedance-prompt`, `seedance-recipes`, `seedance-interview`, `seedance-cinematic-realism`, `seedance-troubleshoot`, `seedance-antislop`, `seedance-pipeline`, `seedance-vfx`, `seedance-characters`, `seedance-audio`, `seedance-copyright`, `seedance-motion`, `seedance-style`, `seedance-camera`, `seedance-lighting`, `seedance-examples-zh`, `seedance-vocab-ja`, `seedance-vocab-ru`, `seedance-vocab-es`, `seedance-vocab-zh`, `seedance-vocab-ko`
  - evidence: `shared-skills/creative-production/openclaw-imports/seedance-20/...`
- **`kling-30`** — **keep**
  - evidence: `shared-skills/creative-production/openclaw-imports/kling-30/SKILL.md`
- **`ai-film-production`** — **keep**
  - evidence: `shared-skills/creative-production/openclaw-imports/ai-film-production/SKILL.md`
- **`directors-cut` family** — **keep**
  - root + subskills found: `directors-interview`, `directors-refs`, `directors-project`, `directors-profiles`, `directors-iterate`
  - evidence: `shared-skills/creative-production/openclaw-imports/directors-cut/...`
- **`script-forge` family** — **keep**
  - root + subskills found: `forge-creative`, `forge-recall`, `forge-graph`, `forge-teaser`, `forge-intelligence`, `forge-temporal`, `forge-continuity`
  - evidence: `shared-skills/creative-production/openclaw-imports/script-forge/...`
- **`storyboard-continuity-audit`** — **keep**
  - evidence: `shared-skills/creative-production/openclaw-imports/storyboard-continuity-audit/SKILL.md`
- **`creative-human-loop`** — **keep**
  - evidence: `shared-skills/creative-production/openclaw-imports/creative-human-loop/SKILL.md`
- **`prompt-scope-classifier`** — **keep**
  - evidence: `shared-skills/creative-production/openclaw-imports/prompt-scope-classifier/SKILL.md`
- **`agent-voice`** — **keep**
  - evidence: `shared-skills/creative-production/creative/agent-voice/SKILL.md`
- **`brainstorm-script-pipeline`** — **keep**
  - evidence: `shared-skills/creative-production/creative/brainstorm-script-pipeline/SKILL.md`
- **`video-generation-pipeline`** — **keep**
  - evidence: `shared-skills/library/creative/video-generation-pipeline/SKILL.md`
- **`video-pipeline`** — **keep**
  - evidence: `shared-skills/library/creative/video-pipeline/SKILL.md`
- **Higgsfield family** — **keep**
  - missing subskills found: `higgsfield-marketplace-cards`, `higgsfield-product-photoshoot`, `higgsfield-soul-id`
  - evidence: `shared-skills/creative-production/...`

### High-priority knowledge / agent-learning
- **`knowledge-graph-setup`** — **keep**
  - evidence: `skills/autonomous-ai-agents/knowledge-graph-setup/SKILL.md`
- **`agent-growth-protocol`** — **keep**
  - evidence: `skills/autonomous-ai-agents/agent-growth-protocol/SKILL.md`

## Missed production-relevant skills — optional
These are useful production/support skills, but I would keep them **on-demand** rather than in the always-loaded core.

### Ops / coordination / meetings / docs
- **`morning-briefing-cron`** — optional
- **`notion-status-operations`** — optional
- **`link-plus-library`** — optional
- **`teams-meeting-pipeline`** — optional
- **`ocr-and-documents`** — optional
- **`deck-refresh`** — optional
- **`datapack-builder`** — optional
- **`ai-readiness`** — optional
- **`webhook-subscriptions`** — optional

### Office / document authoring
- **PowerPoint family** (`powerpoint`, `pptx`, `pptx-author`) — optional
- **`docx`** — optional
- **XLSX family** (`xlsx`, `xlsx-author`) — optional
- **PDF family** (`pdf`, `nano-pdf`) — optional

### Writing / meta / review
- **Writing family** (`writing-clearly-and-concisely`, `writing-skills`, `writing-plans`, `research-paper-writing`) — optional
- **`skill-creator`** — optional
- **`project-framework-setup`** — optional
- **`project-postmortem-to-skill-backlog`** — optional
- **`competitive-analysis`** — optional
- **`audit-plan-and-execution`** — optional
- **`brainstorming`** — optional

## Retired or intentionally excluded
These align with the retirement policy and do **not** need to be migrated into the lean production profile:
- gaming
- social media
- smart home
- novelty / entertainment-only skills

## Bottom line
The final plan is missing several important production families, especially:
1. **Seedance** video generation family
2. **Kling** video generation
3. **Director’s Cut** film-production family
4. **Script Forge** writing / continuity family
5. **Knowledge graph / agent-growth** infrastructure
6. **Ops/document utilities** that should stay optional, not core

If you want, I can turn this into a revised migration plan with the missing keep/optional families inserted in the right lanes.
