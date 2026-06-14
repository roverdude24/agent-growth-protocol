# Hermes Skill Migration Plan V3

## Purpose
Rebuild the final migration plan so it covers:
- **all 46 production skills**
- **all sub-skill families**
- **personal utilities kept on-demand**
- **retired families explicitly excluded**

This version is the full inventory plan, not the lean 18-skill cutdown.

---

## Inventory at a glance

### Production skills by lane
- **Core:** 9
- **Code:** 9
- **Creative:** 23
- **Ops:** 3
- **Review:** 2

**Total production skills: 46**

### Personal utilities
Retained, but **on-demand only**.

### Retired
Gaming, social media, smart home, and novelty / toy families.

---

## Lane structure

### Core lane — always loaded
Always-on orchestration, routing, and infrastructure skills.

### Code lane
Coding assistants, GitHub workflow, debugging, testing, and skill authoring.

### Creative lane
AI film, image, video, prompt, pipeline, and family-based generation systems.

### Ops lane
Notion and production coordination utilities.

### Review lane
Verification, analysis, audit, and quality-control workflows.

### Personal lane — on demand
Useful daily tools that should not bloat the always-loaded profile.

---

## 46 production skills

### 1) Core lane — 9 skills

1. **hermes-agent**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/core/autonomous-ai-agents/hermes-agent/SKILL.md`
   - Role: universal Hermes assistant behavior and core routing

2. **local-subagent-routing**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/core/autonomous-ai-agents/local-subagent-routing/SKILL.md`
   - Role: local worker routing and delegation

3. **process-first-routing**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/core/autonomous-ai-agents/process-first-routing/SKILL.md`
   - Role: process-first task handling and workflow selection

4. **native-mcp**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/core/mcp/native-mcp/SKILL.md`
   - Role: MCP-native operations and tool orchestration

5. **gbrain-onebrain**
   - Planned target: `/Users/vinhlamphuoc/.hermes/skills/autonomous-ai-agents/gbrain-onebrain/SKILL.md`
   - Status: not materialized as a standalone SKILL.md in the current tree
   - Role: knowledge infrastructure / semantic memory layer
   - Note: implement from the existing knowledge-graph setup pattern

6. **oh-my-opencode-hermes-adaptation**
   - Source: `/Users/vinhlamphuoc/.hermes/skills/autonomous-ai-agents/oh-my-opencode-hermes-adaptation/SKILL.md`
   - Role: orchestration policy adaptation layer

7. **agent-growth-protocol**
   - Source repo copy: `/Users/vinhlamphuoc/agent-growth-protocol/SKILL.md`
   - Deployment target: `/Users/vinhlamphuoc/.hermes/skills/autonomous-ai-agents/agent-growth-protocol/SKILL.md`
   - Role: promotion path from repeated workflow to reusable skill

8. **knowledge-graph-setup**
   - Source: `/Users/vinhlamphuoc/.hermes/skills/autonomous-ai-agents/knowledge-graph-setup/SKILL.md`
   - Role: GBrain / OneBrain bootstrap and knowledge plumbing

9. **caveman**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/core/productivity/caveman/SKILL.md`
   - Role: grounded, low-friction, direct execution discipline

---

### 2) Code lane — 9 skills

1. **claude-code**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/library/autonomous-ai-agents/claude-code/SKILL.md`

2. **codex**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/library/autonomous-ai-agents/codex/SKILL.md`

3. **opencode**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/library/autonomous-ai-agents/opencode/SKILL.md`

4. **github-workflow**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/review-board/github/github-workflow/SKILL.md`

5. **systematic-debugging**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/review-board/software-development/systematic-debugging/SKILL.md`

6. **requesting-code-review**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/review-board/software-development/requesting-code-review/SKILL.md`

7. **test-driven-development**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/builder/software-development/test-driven-development/SKILL.md`

8. **spike**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/builder/software-development/spike/SKILL.md`

9. **hermes-agent-skill-authoring**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/library/software-development/hermes-agent-skill-authoring/SKILL.md`

---

### 3) Creative lane — 23 skills

#### Foundation creative skills

1. **ai-film-runbook**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/creative/ai-film-runbook/SKILL.md`

2. **ai-media-generation**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/creative/ai-media-generation/SKILL.md`

3. **comfyui**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/creative/comfyui/SKILL.md`

4. **cinematic-prompt**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/cinematic-prompt/SKILL.md`

5. **production-orchestrator**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/creative/production-orchestrator/SKILL.md`

6. **video-gen-pipeline**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/creative/video-gen-pipeline/SKILL.md`

7. **image-gen-pipeline**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/creative/image-gen-pipeline/SKILL.md`

8. **higgsfield-generate**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/higgsfield-generate/SKILL.md`

9. **kling-30**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/kling-30/SKILL.md`

10. **ai-film-production**
    - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/ai-film-production/SKILL.md`

11. **storyboard-continuity-audit**
    - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/storyboard-continuity-audit/SKILL.md`

12. **creative-human-loop**
    - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/creative-human-loop/SKILL.md`

13. **prompt-scope-classifier**
    - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/prompt-scope-classifier/SKILL.md`

14. **agent-voice**
    - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/creative/agent-voice/SKILL.md`

15. **brainstorm-script-pipeline**
    - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/creative/brainstorm-script-pipeline/SKILL.md`

16. **video-generation-pipeline**
    - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/library/creative/video-generation-pipeline/SKILL.md`

17. **video-pipeline**
    - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/library/creative/video-pipeline/SKILL.md`

18. **higgsfield-marketplace-cards**
    - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/higgsfield-marketplace-cards/SKILL.md`

19. **higgsfield-product-photoshoot**
    - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/higgsfield-product-photoshoot/SKILL.md`

20. **higgsfield-soul-id**
    - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/higgsfield-soul-id/SKILL.md`

#### Seedance-20 family — root + 21 sub-skills

21. **seedance-20**
   - Root: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/SKILL.md`
   - Subskills:
     - `seedance-antislop` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-antislop/SKILL.md`
     - `seedance-audio` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-audio/SKILL.md`
     - `seedance-camera` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-camera/SKILL.md`
     - `seedance-characters` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-characters/SKILL.md`
     - `seedance-cinematic-realism` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-cinematic-realism/SKILL.md`
     - `seedance-copyright` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-copyright/SKILL.md`
     - `seedance-examples-zh` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-examples-zh/SKILL.md`
     - `seedance-interview` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-interview/SKILL.md`
     - `seedance-lighting` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-lighting/SKILL.md`
     - `seedance-motion` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-motion/SKILL.md`
     - `seedance-pipeline` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-pipeline/SKILL.md`
     - `seedance-prompt` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-prompt/SKILL.md`
     - `seedance-recipes` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-recipes/SKILL.md`
     - `seedance-style` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-style/SKILL.md`
     - `seedance-troubleshoot` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-troubleshoot/SKILL.md`
     - `seedance-vfx` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-vfx/SKILL.md`
     - `seedance-vocab-es` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-vocab-es/SKILL.md`
     - `seedance-vocab-ja` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-vocab-ja/SKILL.md`
     - `seedance-vocab-ko` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-vocab-ko/SKILL.md`
     - `seedance-vocab-ru` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-vocab-ru/SKILL.md`
     - `seedance-vocab-zh` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/seedance-20/skills/seedance-vocab-zh/SKILL.md`

#### Director's Cut family — root + 5 sub-skills

22. **directors-cut**
   - Root: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/directors-cut/SKILL.md`
   - Subskills:
     - `directors-interview` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/directors-cut/skills/directors-interview/SKILL.md`
     - `directors-iterate` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/directors-cut/skills/directors-iterate/SKILL.md`
     - `directors-profiles` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/directors-cut/skills/directors-profiles/SKILL.md`
     - `directors-project` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/directors-cut/skills/directors-project/SKILL.md`
     - `directors-refs` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/directors-cut/skills/directors-refs/SKILL.md`

#### Script Forge family — root + 7 sub-skills

23. **script-forge**
   - Root: `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/script-forge/SKILL.md`
   - Subskills:
     - `forge-creative` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/script-forge/skills/forge-creative/SKILL.md`
     - `forge-continuity` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/script-forge/skills/forge-continuity/SKILL.md`
     - `forge-graph` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/script-forge/skills/forge-graph/SKILL.md`
     - `forge-intelligence` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/script-forge/skills/forge-intelligence/SKILL.md`
     - `forge-recall` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/script-forge/skills/forge-recall/SKILL.md`
     - `forge-teaser` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/script-forge/skills/forge-teaser/SKILL.md`
     - `forge-temporal` — `/Users/vinhlamphuoc/.hermes/shared-skills/creative-production/openclaw-imports/script-forge/skills/forge-temporal/SKILL.md`

---

### 4) Ops lane — 3 skills

1. **notion**
   - Source: `/Users/vinhlamphuoc/.hermes/skills/executive-ops/productivity/notion/SKILL.md`

2. **morning-briefing-cron**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/library/productivity/morning-briefing-cron/SKILL.md`

3. **notion-status-operations**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/library/productivity/notion-status-operations/SKILL.md`

---

### 5) Review lane — 2 skills

1. **competitive-analysis**
   - Source: `/Users/vinhlamphuoc/.hermes/shared-skills/review-board/openclaw-imports/competitive-analysis/SKILL.md`

2. **audit-plan-and-execution**
   - Source: `/Users/vinhlamphuoc/.hermes/skills-cold-storage/default-root-bloat-20260614-064031/meta/audit-plan-and-execution/SKILL.md`
   - Status: present in cold storage, not yet promoted into the active shared-skills tree

---

## Personal utilities — on-demand only

These are kept, but they do **not** belong in the always-loaded critical path.

### Apple / device automation
- `apple/apple-notes`
- `apple/apple-reminders`
- `apple/findmy`
- `apple/imessage`
- `apple/macos-computer-use`

### Email
- `email/himalaya`

### Research / discovery
- `research/arxiv`
- `research/blogwatcher`
- `research/llm-wiki`
- `research/polymarket`

### Productivity / coordination
- `productivity/airtable`
- `productivity/google-workspace`
- `productivity/linear`
- `productivity/link-plus-library`
- `productivity/maps`
- `productivity/notion`
- `productivity/notion-status-operations`
- `productivity/morning-briefing-cron`
- `productivity/teams-meeting-pipeline`

### Office / document toolchain
- OCR / document family
- PowerPoint family: `powerpoint`, `pptx`, `pptx-author`, `ppt-template-creator`
- DOCX family
- XLSX family: `xlsx`, `xlsx-author`
- PDF family: `pdf`, `nano-pdf`
- Writing family: `writing-clearly-and-concisely`, `writing-skills`, `writing-plans`, `research-paper-writing`
- `project-framework-setup`
- `project-postmortem-to-skill-backlog`
- `skill-creator`
- `datapack-builder`
- `deck-refresh`
- `ai-readiness`
- `webhook-subscriptions`
- `link-plus-library`

### Media
- `media/spotify`
- `media/youtube-content`
- `media/heartmula`
- `media/songsee`
- `media/gif-search`

### Notes / knowledge / vault tooling
- `note-taking/obsidian`
- `research/llm-wiki`
- `productivity/notion-status-operations`
- `productivity/morning-briefing-cron`

---

## Retired section

Retire these families from the always-loaded production profile:
- **Gaming**: `minecraft`, `pokemon`
- **Social media**: `xurl`
- **Smart home**: `openhue`
- **Novelty / entertainment**: `ascii-art`, `p5js`, `manim`, `songwriting`, `touchdesigner`, `pixel-art`

Retired means:
- do not keep them in the critical always-loaded lane
- do not migrate them into the unified production profile unless a real workflow re-justifies them later

---

## Migration order

### Phase 0 — freeze and back up
1. Snapshot the current skill tree.
2. Record source paths and ownership for every production skill.
3. Preserve the old profile until all lanes verify cleanly.

### Phase 1 — core infrastructure
1. Migrate the always-on core lane first.
2. Create or promote `gbrain-onebrain` from the knowledge-graph setup pattern.
3. Keep `agent-growth-protocol` and `knowledge-graph-setup` together, since they define the learning / promotion loop.
4. Validate routing, session continuity, and MCP wiring before moving on.

### Phase 2 — code lane
1. Move code assistants and debugging workflows.
2. Ensure GitHub workflow and code-review tools resolve correctly.
3. Validate TDD and spike workflows.

### Phase 3 — creative lane
Migrate creative families in this order:
1. Foundation creative skills
2. Seedance-20 family
3. Kling-30
4. AI film / storyboard / human-loop helpers
5. Director's Cut family
6. Script Forge family
7. Higgsfield family

Reason: the family roots should be present before their sub-skills are relied on.

### Phase 4 — ops lane
1. Move Notion and briefing / status coordination skills.
2. Validate recurring automation and production coordination.

### Phase 5 — review lane
1. Move review / audit skills.
2. Confirm verification outputs are strict and evidence-based.

### Phase 6 — personal utilities
1. Keep personal utilities available, but load them only when requested.
2. Prefer category-level mounts over always-on expansion.

### Phase 7 — retire obsolete families
1. Remove gaming, social media, smart home, and novelty families from the active production profile.
2. Keep backups until the unified plan has passed verification.

---

## Rollback plan

Rollback must be lane-local and reversible.

### If a single skill fails
- restore just that skill from the snapshot
- keep the rest of the lane in place

### If a family fails
- restore the root skill and all sub-skills together
- do not leave a partial family mounted

### If a lane fails
- revert the whole lane to the previous working version
- keep the other lanes intact

### If the unified profile becomes unstable
- restore the last known-good multi-profile setup
- re-run migration one lane at a time
- do not delete old mounts until the verification checklist passes

---

## Verification checklist

### Inventory completeness
- [ ] All **46 production skills** appear in the plan
- [ ] Core lane includes all 9 entries
- [ ] Code lane includes all 9 entries
- [ ] Creative lane includes all 23 entries
- [ ] Ops lane includes all 3 entries
- [ ] Review lane includes all 2 entries

### Family completeness
- [ ] Seedance-20 root is present
- [ ] All **21 Seedance sub-skills** are present
- [ ] Director's Cut root is present
- [ ] All **5 Director's Cut sub-skills** are present
- [ ] Script Forge root is present
- [ ] All **7 Script Forge sub-skills** are present
- [ ] Higgsfield family root and sub-skills are present

### Infrastructure completeness
- [ ] `gbrain-onebrain` is represented, even if still being created
- [ ] `knowledge-graph-setup` is included as the implementation anchor
- [ ] `oh-my-opencode-hermes-adaptation` is retained as orchestration policy
- [ ] `agent-growth-protocol` is retained as the promotion workflow skill

### Personal utilities
- [ ] Apple utilities are listed as on-demand
- [ ] Research utilities are listed as on-demand
- [ ] Productivity utilities are listed as on-demand
- [ ] Office / document families are listed as on-demand
- [ ] Media utilities are listed as on-demand

### Retirement
- [ ] Gaming is excluded from the active production profile
- [ ] Social media is excluded from the active production profile
- [ ] Smart home is excluded from the active production profile
- [ ] Novelty / entertainment-only skills are excluded from the active production profile

### Safety and rollback
- [ ] Snapshot exists before migration
- [ ] Each lane can be restored independently
- [ ] Family roots are restored before their subskills
- [ ] No old mount is deleted before verification passes

---

## Final migration intent

- Preserve the full production capability set.
- Keep personal utilities available without bloating the always-on profile.
- Explicitly retire dead-end families.
- Make the migration reversible at every step.

This is the full production migration plan to use as the final reference.
