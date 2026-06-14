# Skill Migration Plan Review

**Score: 6/10**

## Verdict
The plan is solidly structured and the counts appear internally consistent, but it has a few high-impact classification and rollout issues that make it risky to execute as written.

## What looks good
- The migration is organized into clear phases: classify, dedupe, retire, verify.
- Core-first ordering is sensible.
- The plan recognizes duplicate resolution and avoids deleting old profiles before verification.
- The migration stats add up cleanly: `182 + 14 + 23 = 219` total folder occurrences.

## Flaws, misclassifications, and risks

### 1) Research is missing as a real lane
This is the biggest structural issue.

The unified profile already has a dedicated **research lane** (`profiles/unified/skills/research-lane.md`) and a `/research` command in `profiles/unified/SKILL.md`, but the migration plan says the unified profile only has 5 target lanes: **core, code, creative, ops, review**.

That omission causes a downstream classification problem:
- `research/arxiv`
- `research/blogwatcher`
- `research/llm-wiki`
- `research/polymarket`
- `research/research-paper-writing`

These are all shoved into **ops**, but semantically they belong in the research/librarian lane. Ops is for cron, session state, memory, automation, and maintenance—not literature review or market research.

### 2) Some skills are misclassified into creative
The plan moves these to the creative lane:
- `gaming/minecraft-modpack-server`
- `gaming/pokemon-player`

That is a poor fit. These are gaming/infrastructure skills, not creative content generation. If there is no dedicated gaming lane in the unified profile, they should either be retired, kept in a more neutral utility lane, or explicitly justified as exceptions.

### 3) The path model is inconsistent with the unified profile structure
The context says the unified profile lives at:
- `~/.hermes/profiles/unified/`
- with lane packs in `~/.hermes/profiles/unified/skills/`

But the plan’s target locations still point to:
- `~/.hermes/shared-skills/core/`
- `~/.hermes/shared-skills/code/`
- `~/.hermes/shared-skills/creative/`
- etc.

That is confusing and operationally risky. It is not clear whether the plan is migrating content into the new unified profile tree or merely re-labeling the old shared-skills tree. This needs to be normalized before execution.

### 4) Duplicate resolution is too trusting of the “main” copy
For several core duplicates, the plan says to keep the `main` version because it has the latest customizations.

That is reasonable in some cases, but risky in a shared core lane because it can pull profile-local assumptions into always-on skills. In particular:
- `hermes-agent`
- `local-subagent-routing`
- `process-first-routing`
- `native-mcp`

These are foundational skills. They should be merged carefully, not just treated as “main wins.” The unified core should probably be the cleanest, most generic version, with custom refs grafted in only if they are truly profile-agnostic.

A similar caution applies to builder vs review-board duplicates like:
- `github/codebase-inspection`
- `github/github-workflow`
- `software-development/requesting-code-review`
- `software-development/systematic-debugging`

A builder copy may be more action-oriented, but the review-board copy may encode stricter verification logic. The plan should compare semantics, not just pick a default owner.

### 5) Retirement policy is a bit too aggressive
The plan retires many category directories as “empty skeletons,” but it does not spell out a backup/quarantine step or a check for hidden references.

Risks:
- a “retired” directory might still contain non-obvious reference files
- relative links inside SKILL.md files may break after moving content
- some directories may look empty at the top level but still carry templates, scripts, or references the router expects

The plan should preserve a reversible archive or snapshot before deletion.

### 6) Rollback is not realistic enough
The rollback plan is basically “keep old profiles until tests pass.” That is a start, but it is not a real rollback procedure.

Missing pieces:
- atomic cutover strategy
- backup/snapshot of the old skill tree
- a documented restore path for partial failures
- a way to revert just one lane if a subset breaks

Without that, a failed migration could leave you in an inconsistent half-moved state.

### 7) Verification coverage is incomplete
The verification plan checks general profile functionality and a few lane examples, but it does not explicitly verify:
- the research lane
- duplicated-skill behavior after merge
- retired path cleanup
- hidden reference integrity
- that `/research` still resolves correctly

Given the size of the migration, those need explicit tests.

## Bottom line
This is a good high-level migration plan, but it needs correction before execution:
1. restore the research lane as a first-class target
2. reclassify research skills out of ops
3. fix the gaming/creative mismatch
4. normalize the destination paths to the actual unified profile layout
5. add a real backup/rollback procedure
6. verify duplicate merges semantically, not just by folder ownership

If those are addressed, the plan would move closer to an 8/10.