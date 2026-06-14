# Hook Policy for Unified Hermes

This file maps the V2 hook set into Hermes-native policy, cron, skills, and config behavior.

## Implementation rules
- Prompt policy hooks live in the always-on profile prompt / SKILL.md.
- Cron hooks live in the profile cron config.
- Skill hooks live in on-demand skill packs.
- Config hooks live in model, tool, browser, and safety settings.
- Memory hooks write only verified reusable learnings.

## Hook map

| Hook | Hermes equivalent | Implementation | Behavior |
|---|---|---|---|
| todo-continuation-enforcer | Continuity policy | prompt + session memory | carry unfinished tasks forward |
| context-window-monitor | Compaction guard | context stats + summary policy | compact before quality drops |
| session-recovery | Resume policy | `--resume`, session lookup | restore plan and open loops |
| comment-checker | Review lane | diff inspection | ensure comments match changes |
| grep-output-truncator | Search discipline | search_files pagination | keep only useful search windows |
| tool-output-truncator | Tool-output guard | tool caps + process logs | prevent raw dump overload |
| directory-agents-injector | Lane pack loader | skill pack selection | load the right pack from the directory context |
| empty-task-response-detector | Clarification gate | prompt policy | ask for missing objective or route to planner |
| think-mode | Private reasoning discipline | parent-only reasoning budget | keep deep reasoning in parent until split |
| ralph-loop | Iteration loop | wrapper + process monitoring | inspect → act → verify → repeat |
| preemptive-compaction | Early compaction | summary cron + compaction skill | compact before hard limit |
| delegate-task-retry | Fallback chain | delegation retry policy | reroute after worker failure |
| atlas | Multi-lane orchestration | orchestration skill | coordinate fan-out / fan-in |
| start-work | Plan-to-execute trigger | Prometheus mode | move from plan to execution |
| ulw-trigger | Fast-mode trigger | Ultrawork mode | skip long interview when safe |
| plan-gate | Mutation gate | plan review hook | require plan before risky mutation |
| verification-before-completion | Verification gate | review lane | require fresh proof before close |
| process-first-routing | Split execution | routing policy | separate execution and verification lanes |
| lane-budget-enforcer | Surface-area guard | prompt + config limits | keep active tools/skills small |
| provider-ban-enforcer | Provider filter | routing policy | remove forbidden providers from actual routes |
| research-fanout | Parallel research | Explore + Librarian fan-out | gather multiple sources in parallel |
| background-job-monitor | Background worker control | process poll/log/wait | monitor without blocking parent |
| long-run-notify | Completion notify | notify_on_complete | notify once on exit |
| read-only-guard | Read-only review | tool policy | disallow writes in Oracle/review mode |
| file-mutation-guard | Safe mutation policy | patch-first / backup-aware edits | prefer diff-based changes |
| bulk-write-splitter | Bulk-operation splitter | process-first routing | require plan + execute + verify |
| notion-bulk-op-guard | Workspace mutation safety | inspection + verification | split inspection, mutation, verification |
| browser-safety-guard | Browser safety | browser config + policy | obey private URL and dialog limits |
| vision-router | Multimodal routing | creative lane / local vision | route image/PDF work to the visual lane first |
| skill-pack-loader | On-demand skill loading | skill selection policy | load only the pack needed for the turn |
| model-override-resolver | Exact model selection | delegation route map | choose the right model chain per lane |
| plan-promotion-hook | Workflow promotion | AGP / skills | promote stable workflows into a skill |
| memory-promotion-hook | Memory promotion | verified memory write | store reusable learnings only after proof |
| cron-report-hook | Scheduled reporting | cron job | produce daily/weekly status and learning reports |
| cleanup-on-close | End-of-session wrap-up | session summary policy | persist the short summary and next anchor |

## Notes
- This profile intentionally avoids Google/Gemini-backed providers in active routes.
- If a hook is not representable directly in Hermes core, implement the behavior in this policy skill or a small wrapper.
- When two hooks overlap, prefer the stricter safety rule.
