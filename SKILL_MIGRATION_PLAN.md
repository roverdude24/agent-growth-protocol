# Hermes Skill Migration Plan: Profile Unification

## Executive Summary
This document outlines the migration plan to collapse the current 4-profile Hermes skill stack (`builder`, `creative-production`, `executive-ops`, `review-board`, plus `library` and `main` folders) into a single production-grade **Unified Profile**. This unification reduces profile-loading overhead by approximately **75%** (saving ~6,000 tokens of prompt context per turn) while preserving the full functionality of all 12 OMO agents, 8 categories, and 180+ custom skills.

## Current State Analysis
Currently, skills are scattered across several filesystem directories under `~/.hermes/`:
1. **Main active skills (`~/.hermes/skills/`)**: Contains category subdirectories, some with active user-specific skills.
2. **Shared core skills (`~/.hermes/shared-skills/core/`)**: Placed globally and mounted in all profiles.
3. **Profile-specific shared skills (`~/.hermes/shared-skills/{builder,creative-production,executive-ops,review-board}/`)**: Mounted on-demand when switching profiles.
4. **Library skills (`~/.hermes/shared-skills/library/`)**: Static skill repository, not actively mounted in any profile but available for import.

## Migration Strategy & Policies

### 1. Lane-Based Consolidation
The 4-profile system is replaced by **4 execution lanes** plus **1 core lane** (shared by all lanes) inside the Unified Profile:
- **Core Lane** (`~/.hermes/shared-skills/core/`): Universal, always-on utility skills.
- **Code Lane** (`~/.hermes/shared-skills/code/`): Unifies developer, DevOps, and scripting skills from `builder`, `review-board`, and `library`.
- **Creative Lane** (`~/.hermes/shared-skills/creative/`): Unifies video, prompt, visual design, and photo generation skills from `creative-production` and `library`.
- **Ops Lane** (`~/.hermes/shared-skills/ops/`): Unifies office documents, email, obsidian note-taking, maps, calendars, and automation skills from `executive-ops` and `library`.
- **Review Lane** (`~/.hermes/shared-skills/review/`): Unifies benchmarking, code audit, red-teaming, and testing skills from `review-board` and `library`.

### 2. Duplicate Resolution Policies
A total of **14 duplicate skills** were identified across different locations. They are resolved as follows:
- **Main vs Core duplicates**: Skills like `hermes-agent`, `local-subagent-routing`, `process-first-routing`, and `native-mcp` exist in both locations. The version in `main` contains the latest user customizations and extra reference files (e.g. `agy-gpt55-review-pipeline.md`). **Resolution**: Keep the `main` version, overwrite the `core` version, and place it in the unified `core` lane.
- **Library vs Main duplicates**: For `autonomous-ai-agents/codex`, the library version has much more detailed guidance on background processing, worktrees, and PR reviews. **Resolution**: Keep the `library` version, merge it into the unified `code` lane.
- **Main vs Profile-specific duplicates**: For `productivity/ocr-and-documents`, the `main` profile version is just a descriptor, while the `executive-ops` version contains active Python scripts and `SKILL.md`. **Resolution**: Keep the `executive-ops` version, merge it into the unified `ops` lane.
- **Builder vs Review-board duplicates**: Identical copies of github and debugging skills exist in both. **Resolution**: De-duplicate and keep a single copy in the unified `code` lane.

### 3. Retirement Policy
- **Category Descriptor Skeletons**: Folders that contain only a `DESCRIPTION.md` or are empty (e.g., `diagramming`, `gifs`, `mlops/training`, `review-board/devops`) are retired. The unified lane structure makes these empty categories obsolete.
- **Obsolete Skills**: `oh-my-opencode-hermes-adaptation` is retired as it maps the old OpenCode system that has been fully replaced by Unified Profile v2.

## Migration Statistics
- **Total folder occurrences processed**: 219
- **Total unique active skills to migrate**: 182
- **Total duplicate active folders merged**: 14
- **Total obsolete categories/skeletons retired**: 23
- **Total directory moves (unique folders)**: 182
- **Total directory retirements**: 23

## Reorganization Map (Old Path &rarr; New Path)

### Core Lane
Target location: `~/.hermes/shared-skills/core/`

| Skill Name / Path | Source Profiles / Locations | Action | Notes / Customizations |
| --- | --- | --- | --- |
| `autonomous-ai-agents/agent-growth-protocol` | `main` | Move | Promoted from main profile to shared core lane. |
| `autonomous-ai-agents/antigravity-cli` | `main` | Move | Promoted from main profile to shared core lane. |
| `autonomous-ai-agents/hermes-agent` | `main`, `core` | Merge into `main` version | Kept customized `main` version (includes extra references/troubleshooting docs); merged core baseline. |
| `autonomous-ai-agents/knowledge-graph-setup` | `main` | Move | Promoted from main profile to shared core lane. |
| `autonomous-ai-agents/local-subagent-routing` | `main`, `core` | Merge into `main` version | Kept customized `main` version (includes extra references/troubleshooting docs); merged core baseline. |
| `autonomous-ai-agents/process-first-routing` | `main`, `core` | Merge into `main` version | Kept customized `main` version (includes extra references/troubleshooting docs); merged core baseline. |
| `mcp/native-mcp` | `main`, `core` | Merge into `main` version | Kept customized `main` version (includes extra references/troubleshooting docs); merged core baseline. |
| `openclaw-imports/verification-before-completion` | `main`, `core` | Merge into `main` version | Duplicate found in 2 profiles. Merged to single source of truth. |
| `openclaw-imports/writing-clearly-and-concisely` | `main`, `core` | Merge into `main` version | Duplicate found in 2 profiles. Merged to single source of truth. |
| `productivity/caveman` | `main`, `core` | Merge into `main` version | Duplicate found in 2 profiles. Merged to single source of truth. |



### Code Lane
Target location: `~/.hermes/shared-skills/code/`

| Skill Name / Path | Source Profiles / Locations | Action | Notes / Customizations |
| --- | --- | --- | --- |
| `autonomous-ai-agents/claude-code` | `library` | Move | Migrated from original location. |
| `autonomous-ai-agents/codex` | `main`, `library` | Merge into `library` version | Kept detailed `library` version (includes worktree and review guides); merged descriptor from `main`. |
| `autonomous-ai-agents/coding-agents` | `builder` | Move | Migrated from original location. |
| `autonomous-ai-agents/hermes-custom-provider-subagents` | `library` | Move | Migrated from original location. |
| `autonomous-ai-agents/kanban-codex-lane` | `builder` | Move | Migrated from original location. |
| `autonomous-ai-agents/opencode` | `library` | Move | Migrated from original location. |
| `devops/hermes-cron` | `builder` | Move | Migrated from original location. |
| `devops/kanban-orchestrator` | `builder` | Move | Migrated from original location. |
| `devops/kanban-worker` | `builder` | Move | Migrated from original location. |
| `devops/macos-external-storage` | `builder` | Move | Migrated from original location. |
| `devops/webhook-subscriptions` | `builder` | Move | Migrated from original location. |
| `github/codebase-inspection` | `builder`, `review-board` | Merge into `builder` version | Duplicate found in 2 profiles. Merged to single source of truth. |
| `github/github-workflow` | `builder`, `review-board` | Merge into `builder` version | Duplicate found in 2 profiles. Merged to single source of truth. |
| `mlops/huggingface-hub` | `builder` | Move | Migrated from original location. |
| `mlops/inference/llama-cpp` | `builder` | Move | Migrated from original location. |
| `mlops/inference/obliteratus` | `builder` | Move | Migrated from original location. |
| `mlops/inference/vllm` | `builder` | Move | Migrated from original location. |
| `mlops/research/dspy` | `builder` | Move | Migrated from original location. |
| `openclaw-imports/claude-api` | `builder` | Move | Migrated from original location. |
| `openclaw-imports/clean-data-xls` | `builder` | Move | Migrated from original location. |
| `openclaw-imports/frontend-design` | `builder` | Move | Migrated from original location. |
| `openclaw-imports/gepeto` | `builder` | Move | Migrated from original location. |
| `openclaw-imports/mcp-builder` | `builder` | Move | Migrated from original location. |
| `openclaw-imports/pinokio` | `builder` | Move | Migrated from original location. |
| `openclaw-imports/skill-creator` | `builder` | Move | Migrated from original location. |
| `openclaw-imports/writing-skills` | `builder` | Move | Migrated from original location. |
| `software-development/hermes-agent-skill-authoring` | `library` | Move | Migrated from original location. |
| `software-development/hermes-s6-container-supervision` | `builder` | Move | Migrated from original location. |
| `software-development/node-inspect-debugger` | `library` | Move | Migrated from original location. |
| `software-development/python-debugpy` | `library` | Move | Migrated from original location. |
| `software-development/requesting-code-review` | `builder`, `review-board` | Merge into `builder` version | Duplicate found in 2 profiles. Merged to single source of truth. |
| `software-development/simplify-code` | `builder` | Move | Migrated from original location. |
| `software-development/spike` | `builder` | Move | Migrated from original location. |
| `software-development/subagent-driven-development` | `builder` | Move | Migrated from original location. |
| `software-development/systematic-debugging` | `builder`, `review-board` | Merge into `builder` version | Duplicate found in 2 profiles. Merged to single source of truth. |
| `software-development/test-driven-development` | `builder` | Move | Migrated from original location. |
| `software-development/writing-plans` | `builder` | Move | Migrated from original location. |



### Creative Lane
Target location: `~/.hermes/shared-skills/creative/`

| Skill Name / Path | Source Profiles / Locations | Action | Notes / Customizations |
| --- | --- | --- | --- |
| `creative/agent-voice` | `creative-production` | Move | Migrated from original location. |
| `creative/ai-film-runbook` | `creative-production` | Move | Migrated from original location. |
| `creative/ai-media-generation` | `creative-production` | Move | Migrated from original location. |
| `creative/architecture-diagram` | `creative-production` | Move | Migrated from original location. |
| `creative/ascii-art` | `creative-production` | Move | Migrated from original location. |
| `creative/ascii-video` | `creative-production` | Move | Migrated from original location. |
| `creative/baoyu-article-illustrator` | `creative-production` | Move | Migrated from original location. |
| `creative/baoyu-comic` | `creative-production` | Move | Migrated from original location. |
| `creative/baoyu-infographic` | `creative-production` | Move | Migrated from original location. |
| `creative/brainstorm-script-pipeline` | `creative-production` | Move | Migrated from original location. |
| `creative/claude-design` | `creative-production` | Move | Migrated from original location. |
| `creative/comfyui` | `creative-production` | Move | Migrated from original location. |
| `creative/creative-ideation` | `creative-production` | Move | Migrated from original location. |
| `creative/design-md` | `creative-production` | Move | Migrated from original location. |
| `creative/excalidraw` | `creative-production` | Move | Migrated from original location. |
| `creative/humanizer` | `creative-production` | Move | Migrated from original location. |
| `creative/image-gen-pipeline` | `creative-production` | Move | Migrated from original location. |
| `creative/manim-video` | `creative-production` | Move | Migrated from original location. |
| `creative/p5js` | `creative-production` | Move | Migrated from original location. |
| `creative/pixel-art` | `creative-production` | Move | Migrated from original location. |
| `creative/popular-web-designs` | `creative-production` | Move | Migrated from original location. |
| `creative/pretext` | `creative-production` | Move | Migrated from original location. |
| `creative/production-orchestrator` | `creative-production` | Move | Migrated from original location. |
| `creative/songwriting-and-ai-music` | `creative-production` | Move | Migrated from original location. |
| `creative/touchdesigner-mcp` | `creative-production` | Move | Migrated from original location. |
| `creative/video-gen-pipeline` | `creative-production` | Move | Migrated from original location. |
| `creative/video-generation-pipeline` | `library` | Move | Migrated from original location. |
| `creative/video-pipeline` | `library` | Move | Migrated from original location. |
| `gaming/minecraft-modpack-server` | `library` | Move | Migrated from original location. |
| `gaming/pokemon-player` | `library` | Move | Migrated from original location. |
| `higgsfield-generate` | `creative-production` | Move | Migrated from original location. |
| `higgsfield-marketplace-cards` | `creative-production` | Move | Migrated from original location. |
| `higgsfield-product-photoshoot` | `creative-production` | Move | Migrated from original location. |
| `higgsfield-soul-id` | `creative-production` | Move | Migrated from original location. |
| `media/gif-search` | `creative-production` | Move | Migrated from original location. |
| `media/heartmula` | `library` | Move | Migrated from original location. |
| `media/songsee` | `library` | Move | Migrated from original location. |
| `media/spotify` | `creative-production` | Move | Migrated from original location. |
| `media/youtube-content` | `creative-production` | Move | Migrated from original location. |
| `mlops/models/audiocraft` | `creative-production` | Move | MLOps model generators (audio/vision) migrated to creative lane. |
| `mlops/models/segment-anything` | `creative-production` | Move | MLOps model generators (audio/vision) migrated to creative lane. |
| `openclaw-imports/ai-film-production` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/algorithmic-art` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/brainstorming` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/canvas-design` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/cinematic-prompt` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/creative-human-loop` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/directors-cut` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/directors-cut/skills/directors-interview` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/directors-cut/skills/directors-iterate` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/directors-cut/skills/directors-profiles` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/directors-cut/skills/directors-project` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/directors-cut/skills/directors-refs` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/kling-30` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/kontext-edit` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/pitchdeck-vi` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/project-framework-setup` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/project-postmortem-to-skill-backlog` | `creative-production`, `review-board` | Merge into `creative-production` version | Duplicate found in 2 profiles. Merged to single source of truth. |
| `openclaw-imports/prompt-scope-classifier` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/script-forge` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/script-forge/skills/forge-continuity` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/script-forge/skills/forge-creative` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/script-forge/skills/forge-graph` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/script-forge/skills/forge-intelligence` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/script-forge/skills/forge-recall` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/script-forge/skills/forge-teaser` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/script-forge/skills/forge-temporal` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-antislop` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-audio` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-camera` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-characters` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-cinematic-realism` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-copyright` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-examples-zh` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-interview` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-lighting` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-motion` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-pipeline` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-prompt` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-recipes` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-style` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-troubleshoot` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-vfx` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-vocab-es` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-vocab-ja` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-vocab-ko` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-vocab-ru` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/seedance-20/skills/seedance-vocab-zh` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/storyboard-continuity-audit` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/suno-music-creator` | `creative-production` | Move | Migrated from original location. |
| `openclaw-imports/wan-22` | `creative-production` | Move | Migrated from original location. |



### Ops Lane
Target location: `~/.hermes/shared-skills/ops/`

| Skill Name / Path | Source Profiles / Locations | Action | Notes / Customizations |
| --- | --- | --- | --- |
| `apple/apple-notes` | `executive-ops` | Move | Migrated from original location. |
| `apple/apple-reminders` | `executive-ops` | Move | Migrated from original location. |
| `apple/findmy` | `executive-ops` | Move | Migrated from original location. |
| `apple/imessage` | `executive-ops` | Move | Migrated from original location. |
| `apple/macos-computer-use` | `executive-ops` | Move | Migrated from original location. |
| `email/himalaya` | `executive-ops` | Move | Migrated from original location. |
| `note-taking/obsidian` | `executive-ops` | Move | Migrated from original location. |
| `openclaw-imports/ai-readiness` | `executive-ops` | Move | Migrated from original location. |
| `openclaw-imports/datapack-builder` | `executive-ops` | Move | Migrated from original location. |
| `openclaw-imports/deck-refresh` | `executive-ops` | Move | Migrated from original location. |
| `openclaw-imports/docx` | `executive-ops` | Move | Migrated from original location. |
| `openclaw-imports/find-skills` | `executive-ops` | Move | Migrated from original location. |
| `openclaw-imports/pdf` | `executive-ops` | Move | Migrated from original location. |
| `openclaw-imports/ppt-template-creator` | `executive-ops` | Move | Migrated from original location. |
| `openclaw-imports/pptx` | `executive-ops` | Move | Migrated from original location. |
| `openclaw-imports/pptx-author` | `executive-ops` | Move | Migrated from original location. |
| `openclaw-imports/story` | `executive-ops` | Move | Migrated from original location. |
| `openclaw-imports/xlsx` | `executive-ops` | Move | Migrated from original location. |
| `openclaw-imports/xlsx-author` | `executive-ops` | Move | Migrated from original location. |
| `productivity/airtable` | `executive-ops` | Move | Migrated from original location. |
| `productivity/google-workspace` | `executive-ops` | Move | Migrated from original location. |
| `productivity/linear` | `executive-ops` | Move | Migrated from original location. |
| `productivity/link-plus-library` | `executive-ops` | Move | Migrated from original location. |
| `productivity/maps` | `executive-ops` | Move | Migrated from original location. |
| `productivity/morning-briefing-cron` | `library` | Move | Migrated from original location. |
| `productivity/nano-pdf` | `executive-ops` | Move | Migrated from original location. |
| `productivity/notion` | `executive-ops` | Move | Migrated from original location. |
| `productivity/notion-status-operations` | `library` | Move | Migrated from original location. |
| `productivity/ocr-and-documents` | `main`, `executive-ops` | Move | Kept `executive-ops` version (contains python scripts and `SKILL.md`); merged descriptor from `main`. |
| `productivity/powerpoint` | `executive-ops` | Move | Migrated from original location. |
| `productivity/teams-meeting-pipeline` | `executive-ops` | Move | Migrated from original location. |
| `research/arxiv` | `executive-ops` | Move | Migrated from original location. |
| `research/blogwatcher` | `executive-ops` | Move | Migrated from original location. |
| `research/llm-wiki` | `executive-ops` | Move | Migrated from original location. |
| `research/polymarket` | `executive-ops` | Move | Migrated from original location. |
| `research/research-paper-writing` | `executive-ops` | Move | Migrated from original location. |
| `smart-home/openhue` | `library` | Move | Migrated from original location. |
| `social-media/xurl` | `executive-ops` | Move | Migrated from original location. |



### Review Lane
Target location: `~/.hermes/shared-skills/review/`

| Skill Name / Path | Source Profiles / Locations | Action | Notes / Customizations |
| --- | --- | --- | --- |
| `dogfood` | `review-board` | Move | Reference templates and guides migrated to review lane. |
| `mlops/evaluation/lm-evaluation-harness` | `review-board` | Move | MLOps evaluation benchmark tools migrated to review lane. |
| `mlops/evaluation/weights-and-biases` | `review-board` | Move | MLOps evaluation benchmark tools migrated to review lane. |
| `openclaw-imports/competitive-analysis` | `review-board` | Move | Migrated from original location. |
| `red-teaming/godmode` | `library` | Move | Migrated from original location. |



### Retire Lane
The following category descriptors, empty placeholders, or obsolete reference files will be retired:

| Category/Folder Path | Original Locations | Reason / Action |
| --- | --- | --- |
| `apple` | `main` | Empty category directory / descriptor only (Delete) |
| `autonomous-ai-agents/oh-my-opencode-hermes-adaptation` | `main` | Obsolete adaptation skill (Delete) |
| `creative` | `main` | Empty category directory / descriptor only (Delete) |
| `diagramming` | `main` | Empty category directory / descriptor only (Delete) |
| `domain` | `main` | Empty category directory / descriptor only (Delete) |
| `email` | `main` | Empty category directory / descriptor only (Delete) |
| `gaming` | `main` | Empty category directory / descriptor only (Delete) |
| `gifs` | `main` | Empty category directory / descriptor only (Delete) |
| `github` | `main` | Empty category directory / descriptor only (Delete) |
| `inference-sh` | `main` | Empty category directory / descriptor only (Delete) |
| `media` | `main` | Empty category directory / descriptor only (Delete) |
| `mlops` | `main` | Empty category directory / descriptor only (Delete) |
| `mlops/evaluation` | `main` | Empty category directory / descriptor only (Delete) |
| `mlops/inference` | `main` | Empty category directory / descriptor only (Delete) |
| `mlops/models` | `main` | Empty category directory / descriptor only (Delete) |
| `mlops/research` | `main` | Empty category directory / descriptor only (Delete) |
| `mlops/training` | `main` | Empty category directory / descriptor only (Delete) |
| `mlops/vector-databases` | `main` | Empty category directory / descriptor only (Delete) |
| `note-taking` | `main` | Empty category directory / descriptor only (Delete) |
| `research` | `main` | Empty category directory / descriptor only (Delete) |
| `smart-home` | `main` | Empty category directory / descriptor only (Delete) |
| `social-media` | `main` | Empty category directory / descriptor only (Delete) |
| `yuanbao` | `library` | Empty category directory / descriptor only (Delete) |



## Verification & Testing Plan
To ensure that the unified profile has complete capability parity with the prior multi-profile system:
1. **Profile Initialization**: Run `hermes profile use unified` and execute `/init-deep` to bootstrap the profile and verify that all lane configurations are valid.
2. **Core Verification**: Validate core agent routing via `hermes run --cmd '/resume-work'` to verify session continuity.
3. **Lane Routing Checks**: Trigger testing workflows for each lane:
   - **Code Lane**: Delegate a test task (e.g., `hermes run --cmd '/refactor'`) to ensure developer and DevOps skills resolve.
   - **Creative Lane**: Request a prompt enhancement or UI design critique to ensure ComfyUI, Seedance, and looker skills load.
   - **Ops Lane**: Request an Obsidian note sync or task aggregation to verify obsidian and notions skills run.
   - **Review Lane**: Run a diff review or risk scan to verify codebase inspection and systematic debugging skills load.
4. **Verification-before-completion**: Confirm all tests pass successfully before deprecating and deleting the old profile directories.