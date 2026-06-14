# Unified Hermes Profile v2 Implementation Review

This document provides a comprehensive review of the Unified Hermes Profile V2 implementation at `~/.hermes/profiles/unified/` compared against the [HERMES_UNIFIED_PROFILE_V2.md](file:///Users/vinhlamphuoc/agent-growth-protocol/HERMES_UNIFIED_PROFILE_V2.md) design specification.

---

## Executive Summary

- **Overall Verdict**: **PASS WITH RECOMMENDATIONS**. 
- The implementation successfully collapses the four-profile Hermes stack into a single unified profile and complies with major requirements: it is highly token-efficient, contains no active cloud Google/Gemini routes, maps all hooks, and utilizes local Gemma for multimodal tasks.
- **Critical Action Items**:
  1. Create the missing `research-lane.md` (Research/Librarian) skill pack.
  2. Correct the `auxiliary.vision` provider configuration mismatch in `config.yaml`.
  3. Map the sub-skills lists under `skills` in `config.yaml` as per the V2 design spec blueprint.
  4. Implement the command wrappers in `~/.hermes/bin/` to make the slash commands fully executable.

---

## 1. config.yaml Evaluation

- **YAML Validity**: **PASS**. Verified syntactically valid YAML via programmatic parser check.
- **Specification Alignment**: **PARTIAL PASS**.
  - **Model & Category Routing**: Matches the 8 OMO categories and fallback chains perfectly in `delegation.category_routes` and `model.routing`.
  - **Security/Safety Guards**: Correctly configures `no_google_models: true` and maps fallback/local routes.
  - **Discrepancy (Skills Section)**: The implemented [config.yaml](file:///Users/vinhlamphuoc/.hermes/profiles/unified/config.yaml#L170-L179) contains only skills engine configurations (e.g., `external_dirs`, `template_vars`). It completely lacks the `core`, `code`, `research`, `ops`, and `review` skill listings defined in the [V2 Design Spec Blueprint](file:///Users/vinhlamphuoc/agent-growth-protocol/HERMES_UNIFIED_PROFILE_V2.md#L720-L735).
  - **Discrepancy (Vision Provider)**: Under `auxiliary.vision` (line 123), the provider is set to `openai-codex` for the model `gemma-4-26b-a4b-qat`. However, `openai-codex` does not host Gemma. It should be configured to use the `local-gemma` provider, similar to `delegation.category_routes.visual-engineering` (line 201).

---

## 2. SKILL.md Evaluation

- **File Link**: [SKILL.md](file:///Users/vinhlamphuoc/.hermes/profiles/unified/SKILL.md)
- **Token Budget Compliance**: **PASS**. The file is **4,958 bytes (~4.8 KB)**, which is well below the **18 KB** ceiling set for the always-on core.
- **Routing Rules Coverage**: **PARTIAL PASS**.
  - While it outlines the lane selection, modes, and escalation pathways, it misses a few specific guardrails from the V2 design spec:
    - *Collapse Guard*: "Never silently collapse a weak lane back into the parent unless no viable worker path remains."
    - *Provider Ban*: "If the user bans a provider family, remove it from the chain entirely."
    - *Research Recommendation*: "Fast research / doc extraction should prefer `deepseek-v4-flash` or `qwen3.6-plus` before escalating."

---

## 3. Lane Skill Packs Evaluation

- **Folder Link**: [Skills Directory](file:///Users/vinhlamphuoc/.hermes/profiles/unified/skills)
- **Completeness & Actionability**: **PARTIAL PASS**.
  - The existing lane files are highly structured, actionable, and clear:
    - [code-lane.md](file:///Users/vinhlamphuoc/.hermes/profiles/unified/skills/code-lane.md) (1.7 KB)
    - [creative-lane.md](file:///Users/vinhlamphuoc/.hermes/profiles/unified/skills/creative-lane.md) (1.6 KB)
    - [ops-lane.md](file:///Users/vinhlamphuoc/.hermes/profiles/unified/skills/ops-lane.md) (1.4 KB)
    - [prometheus-lane.md](file:///Users/vinhlamphuoc/.hermes/profiles/unified/skills/prometheus-lane.md) (1.3 KB)
    - [review-lane.md](file:///Users/vinhlamphuoc/.hermes/profiles/unified/skills/review-lane.md) (1.3 KB)
    - [ultrawork-lane.md](file:///Users/vinhlamphuoc/.hermes/profiles/unified/skills/ultrawork-lane.md) (0.8 KB)
  - **Critical Gap (Missing Research/Librarian Pack)**: The V2 design spec requires a `Research / librarian pack` (described in sections 7.2 & 7.4 of the design doc). This pack is **completely missing** from the `skills/` folder. A `research-lane.md` file needs to be created to document tools like `mcp_fetch` and patterns for evidence collection.

---

## 4. Hooks Policy Evaluation

- **File Link**: [hooks-policy.md](file:///Users/vinhlamphuoc/.hermes/profiles/unified/skills/hooks-policy.md)
- **Mapping Completeness**: **PASS**. 
  - The V2 design spec text states "34 hooks" but actually lists 35 hooks in its table.
  - The [hooks-policy.md](file:///Users/vinhlamphuoc/.hermes/profiles/unified/skills/hooks-policy.md#L14) file maps **all 35 hooks** successfully, ensuring full OMO-style depth is captured.
  - **Configuration Mapping**: All 35 hooks are listed and enabled in the `hooks.enabled` list in [config.yaml](file:///Users/vinhlamphuoc/.hermes/profiles/unified/config.yaml#L259-L294).

---

## 5. Missing Pieces from V2 Design

1. **Research Lane Pack**: Missing `research-lane.md` in `/Users/vinhlamphuoc/.hermes/profiles/unified/skills/`.
2. **Skill Imports in config.yaml**: Lack of the category skill pack references (`core`, `code`, `research`, `ops`, `review`) under `skills:` in `config.yaml`.
3. **Executable Slash Commands**: The slash commands listed in section 10 of the design spec (such as `/init-deep`, `/start-work`, `/ulw-loop`, etc.) are documented in `SKILL.md` but are **not present** as executable wrappers or aliases in the `~/.hermes/bin/` folder.

---

## 6. Token Budget Compliance

- **Current Unified Profile Overhead**:
  - `SKILL.md`: 4,958 bytes (~4.8 KB)
  - `config.yaml`: 7,286 bytes (~7.1 KB)
  - **Total Profile Shell Size**: **12,244 bytes (~12.0 KB)**
- **Comparison to Spec Targets**:
  - Max existing OMO shell size target: **18,078 bytes**
  - Always-on core budget: **<= 18 KB**
  - Active profile size is well within the budget!
- **Token Savings**:
  - Redundant shell bytes removed: `67,868 bytes (total four OMO profiles) - 12,244 bytes (unified profile) = 55,624 bytes`
  - Total tokens saved (at 4 bytes per token): **13,906 tokens** (exceeding the design spec target of 12,448 tokens saved).

---

## 7. Security Concerns

- **No Active Cloud Google/Gemini Routes**: **PASS**. 
  - Verified that neither `google` nor `gemini` API endpoints exist in active routes or delegation configs.
  - **Local Gemma implementation**: The `gemma-4-26b-a4b-qat` model is correctly routed through the `local-gemma` provider mapped to a local address (`http://127.0.0.1:1234/v1`), maintaining full data privacy guidelines.

---

## Recommended Action Plan

### 1. Correct Provider Mismatch in `config.yaml`
Modify the `auxiliary.vision` block to map to the local Gemma provider:
```diff
 auxiliary:
   vision:
-    provider: openai-codex
+    provider: local-gemma
     model: gemma-4-26b-a4b-qat
     timeout: 120
```

### 2. Map Core/Lane Skills in `config.yaml`
Add the skill directories configuration in the `skills` section:
```diff
 skills:
   external_dirs:
     - /Users/vinhlamphuoc/.hermes/profiles/unified/skills
+  core:
+    - autonomous-ai-agents/hermes-agent
+    - autonomous-ai-agents/process-first-routing
+    - openclaw-imports/verification-before-completion
+    - autonomous-ai-agents/local-subagent-routing
+    - autonomous-ai-agents/agent-growth-protocol
+  code:
+    - autonomous-ai-agents/codex
+  research:
+    - mcp/native-mcp
+  ops:
+    - autonomous-ai-agents/agent-growth-protocol
+  review:
+    - openclaw-imports/verification-before-completion
```

### 3. Add `research-lane.md` Skill Pack
Create `/Users/vinhlamphuoc/.hermes/profiles/unified/skills/research-lane.md` to establish the research and librarian patterns.
