# Skill Migration Plan Review v2 — Lean Filter

**Verdict: 9/10 for production relevance once slimmed down**

This review applies a **lean, production-first filter** for an **AI Creator / Film Director** who works in:
- AI video generation (Runway, Kling, Higgsfield)
- AI image generation (ComfyUI, Midjourney, Flux)
- Prompt engineering for video/image
- Agent development (Hermes, Codex, OpenCode)
- Notion project management
- GitHub code workflow
- Creative direction and review

## Bottom line
The current migration plan is **too broad** for this user. It includes a lot of skills that are not production-relevant for film/AI creation.

### Clear retire list
Yes — retire all of these categories for this user:
- **Gaming**
- **Social media**
- **Smart home**
- Any other personal/lifestyle utilities that do not support production output

## Answers to the review questions

### 1) Which skills are irrelevant to this user's work?
Irrelevant or effectively irrelevant:
- `gaming/minecraft-modpack-server`
- `gaming/pokemon-player`
- `smart-home/openhue`
- `social-media/xurl`
- Most personal convenience skills that do not help create, manage, review, or ship creative work

Also low relevance for this user unless there is a very specific side workflow:
- `apple/apple-notes`
- `apple/apple-reminders`
- `apple/findmy`
- `apple/imessage`
- `email/himalaya`
- `productivity/airtable`
- `productivity/google-workspace` (unless there is active studio ops use)
- `productivity/linear` (only if they use Linear instead of Notion)
- `research/arxiv`
- `research/blogwatcher`
- `research/llm-wiki`
- `research/polymarket`
- `research/research-paper-writing`
- `media/spotify`
- `media/youtube-content`
- `diagramming`, `gifs`, `ascii-art`, `pixel-art`, `p5js`, `manim-video`, `songwriting-and-ai-music`, `touchdesigner-mcp` unless they are directly part of the studio's deliverables

### 2) Which skills are low value?
Nice-to-have, but not core for this user:
- Most personal/productivity utility skills
- Research and reading-skills that do not feed production output
- Social/media publishing skills
- Music / novelty / visual gimmick skills
- Miscellaneous office automation skills that are not part of the day-to-day creative pipeline

### 3) Which skills are high value?
High value for this user’s actual workflow:
- Creative generation pipelines
- Video/image prompt skills
- ComfyUI / image generation tooling
- AI video platform skills for Runway / Kling / Higgsfield-style work
- Hermes routing / subagent orchestration
- Code workflow skills for GitHub, Codex, OpenCode
- Notion workflow skills for project tracking and production coordination
- Review / debugging / iteration skills for creative and code outputs

### 4) Should we retire ALL gaming skills?
**Yes.**

For this user, gaming skills are not part of the production stack and should be retired.

### 5) Should we retire ALL social media skills?
**Yes.**

Unless the user is explicitly operating a distribution or growth function, social media management is out of scope. Retire it.

### 6) Should we retire smart home skills?
**Yes.**

`smart-home/openhue` is not relevant to film direction or AI content production.

### 7) What's the MINIMUM viable skill set for this user?

#### Core production set
These are the skills that actually support the user’s day-to-day workflow.

**Agent / orchestration**
- `autonomous-ai-agents/hermes-agent`
- `autonomous-ai-agents/local-subagent-routing`
- `autonomous-ai-agents/process-first-routing`
- `mcp/native-mcp`

**Creative / generation**
- `creative/ai-film-runbook`
- `creative/ai-media-generation`
- `creative/comfyui`
- `creative/cinematic-prompt`
- `creative/production-orchestrator`
- `creative/video-gen-pipeline`
- `creative/image-gen-pipeline`
- `higgsfield-generate`

**Code / delivery**
- `autonomous-ai-agents/claude-code`
- `autonomous-ai-agents/codex`
- `autonomous-ai-agents/opencode`
- `github/github-workflow`
- `software-development/systematic-debugging`

**Ops / PM**
- `productivity/notion`

### 8) Recount: how many skills actually matter?

**18 skills** matter in the lean production set above.

That is the practical minimum for this user if we want to preserve real workflow coverage without carrying unrelated categories.

## Recommended action on the migration plan

### Keep
- Core routing / agent skills
- Creative pipeline skills
- Platform skills for AI video/image generation
- GitHub and code-review workflow skills
- Notion workflow skill

### Retire
- Gaming
- Social media
- Smart home
- Personal/lifestyle utilities that do not support production
- Broad research / novelty / entertainment skills unless they are explicitly used in a studio deliverable

### Demote to optional
If the user ever needs them, they can be restored later:
- email
- Apple personal utilities
- maps / reminders / notes / findmy / iMessage
- music and media publishing
- research tools
- diagramming / ASCII / novelty visual tools
- secondary office automation tools

## Final recommendation
This migration should be rewritten as a **lean creative-production stack** instead of a general-purpose Hermes stack.

The right goal is not “keep everything useful in theory.”
The right goal is:
- keep what is used **weekly or daily** in production,
- retire what is unrelated,
- and keep the skill tree small enough that it is actually maintainable.

**Short version: keep the creative/code/core stack; retire gaming, social media, smart home, and most personal or novelty skills.**
