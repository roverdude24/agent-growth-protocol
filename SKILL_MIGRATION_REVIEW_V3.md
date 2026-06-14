# Skill Migration Plan Review V3 — Full Inventory Review

**Verdict: 8.5/10 (Highly comprehensive, but requires minor structural, naming, and sequencing corrections before execution)**

This document reviews the updated [SKILL_MIGRATION_PLAN_V3.md](file:///Users/vinhlamphuoc/agent-growth-protocol/SKILL_MIGRATION_PLAN_V3.md) against the actual skill ecosystem and [SKILL_CROSSCHECK.md](file:///Users/vinhlamphuoc/agent-growth-protocol/SKILL_CROSSCHECK.md) findings.

---

## 1. Production Skills & Lane Assignments (46 Skills)

**Status: Pass with Minor Inconsistencies**
*   **Total Count:** The 46 active production skills are successfully listed across the 5 super-lanes (9 Core, 9 Code, 23 Creative, 3 Ops, 2 Review).
*   **Lane Alignment:** All skills are correctly aligned to their respective lanes (e.g., Core handles routing/knowledge orchestration; Code handles git/debugging/tests; Creative handles film/video pipelines).
*   **Critique & Duplicate Listings:** 
    *   `notion`, `morning-briefing-cron`, and `notion-status-operations` are listed as active skills in the **Ops lane** (items 1, 2, 3), but are also listed as **Personal utilities — on-demand only** (under the `productivity` and `note-taking` subsections).
    *   This duplicate classification creates operational ambiguity. If they are active production crons/interfaces, they should be removed from the on-demand list.

---

## 2. Sub-Skill Family Completeness

**Status: Pass (with grouping recommendation)**
*   **Seedance-20 family:** Complete (root + 21 subskills are accurately identified and listed).
*   **Director's Cut family:** Complete (root + 5 subskills are accurately identified and listed).
*   **Script Forge family:** Complete (root + 7 subskills are accurately identified and listed).
*   **Higgsfield family:** Complete in terms of skill presence, but **structurally inconsistent**.
    *   Instead of being grouped as a root + 3 subskills family (similar to Seedance/Script Forge), `higgsfield-generate` (root), `higgsfield-marketplace-cards` (sub), `higgsfield-product-photoshoot` (sub), and `higgsfield-soul-id` (sub) are dispersed as individual entries in the "Foundation creative skills" list.
    *   *Recommendation:* Group these under a unified `Higgsfield family` heading to align with the rest of the plan's family structure.

---

## 3. Migration Order Sequence

**Status: Needs Adjustment**
*   **The Sequencing Problem:** The proposed order moves Core (Phase 1) $\rightarrow$ Code (Phase 2) $\rightarrow$ Creative (Phase 3) $\rightarrow$ Ops (Phase 4) $\rightarrow$ Review (Phase 5).
*   *Why this fails:* The Review lane contains [audit-plan-and-execution](file:///Users/vinhlamphuoc/.hermes/skills-cold-storage/default-root-bloat-20260614-064031/meta/audit-plan-and-execution/SKILL.md), which is the primary system verification utility. Leaving Review to Phase 5 means you lack automated audit capability while actively migrating the highly complex Code, Creative, and Ops lanes.
*   *Recommendation:* Promote the Review lane to **Phase 2** (immediately after Core infrastructure is active), enabling the audit toolset to verify subsequent lane migrations.
*   **Core Materialization:** The plan notes that `gbrain-onebrain` is "not materialized as a standalone SKILL.md in the current tree." Phase 1 should explicitly specify the materialization step as a blocking gate before routing validation begins.

---

## 4. Rollback Plan Realism

**Status: Realistic and Sound (needs execution details)**
*   **Strengths:** The rollback strategy is correctly segmented by granularity (single skill $\rightarrow$ family $\rightarrow$ lane $\rightarrow$ full profile).
*   **Critical Best Practice:** The requirement to rollback a family as a single block (root + subskills together) is highly realistic. Subskills frequently rely on relative imports, shared vocabularies, or custom configurations inside the root folder, so partial rollbacks would introduce broken dependencies.
*   **Critique:** 
    *   **Vague snapshot definition:** Phase 0 simply says "Snapshot the current skill tree." It should suggest a concrete command like:
        `cp -r ~/.hermes ~/.hermes_backup_$(date +%Y%m%d_%H%M%S)` or a local Git branch freeze.
    *   **Lack of test triggers:** The rollback does not define the validation queries or commands needed to verify if a rollback succeeded.

---

## 5. Crosscheck Discrepancies & Missing Skills

Comparing the plan against [SKILL_CROSSCHECK.md](file:///Users/vinhlamphuoc/agent-growth-protocol/SKILL_CROSSCHECK.md) reveals the following discrepancies:

1.  **Missing Skill:** The skill `brainstorming` (listed as optional/on-demand in crosscheck line 83) is entirely missing from the V3 personal utilities list.
2.  **Naming Discrepancy:** The crosscheck lists `ocr-and-documents` (line 64), but the plan uses the generic description `OCR / document family` (line 304). This should be corrected to reference the exact skill directory name: `ocr-and-documents`.
3.  **On-Demand Duplication:** `link-plus-library` is listed twice under the personal utilities section (lines 296 and 317).

---

## 6. Score and Final Action Items

### Overall Score: **8.5 / 10**

To turn this into a **10/10** production-ready plan, make the following edits to [SKILL_MIGRATION_PLAN_V3.md](file:///Users/vinhlamphuoc/agent-growth-protocol/SKILL_MIGRATION_PLAN_V3.md):

1.  **Re-sequence Phase 5 (Review):** Move Review to Phase 2 (Core $\rightarrow$ Review $\rightarrow$ Code $\rightarrow$ Creative $\rightarrow$ Ops).
2.  **Add Missing Skill:** Insert `brainstorming` under the Personal Utilities on-demand list.
3.  **Unify Higgsfield:** Group the 4 Higgsfield entries into a root + 3 subskills family layout.
4.  **Deduplicate:** Clean up the duplicate listings of `notion`, `morning-briefing-cron`, `notion-status-operations`, and `link-plus-library`.
5.  **Refine Snapshot commands:** Specify explicit backup shell commands in Phase 0 and Phase 7.
