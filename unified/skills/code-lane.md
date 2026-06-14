# Code Lane

This lane is the implementation path. It combines **Hephaestus** depth with **OpenCode-Builder** speed.

## When to use
- feature work
- bug fixes
- refactors
- tests
- code review follow-up
- build or script repair
- multi-file edits that need real verification

## Operating style
- Start from the repository evidence, not guesses.
- Prefer patch-first edits and small diffs.
- Use terminal, git, search, and file reads as the primary tools.
- Keep the parent informed with short, factual progress updates.
- Split execution and verification when the change is non-trivial.

## Hephaestus patterns
1. inspect the code path end to end
2. identify the smallest safe mutation
3. patch the code
4. run the narrowest useful test
5. expand only if the first check passes

## OpenCode-Builder patterns
- move fast on concrete implementation work
- keep edits localized
- prefer direct terminal execution for build/test loops
- avoid long abstract analysis once the target is known
- use background workers for long builds or watchers

## Code lane rules
- Never claim a code fix without a real verification step.
- Never leave a refactor without checking the affected call sites.
- If a change touches more than one subsystem, introduce a plan and verify each boundary.
- If tests are available, run the smallest relevant set first, then broaden if needed.
- If the work becomes architectural, hand off to Review lane before closure.

## Best tools
- search_files
- read_file
- patch / write_file
- terminal
- process for background jobs
- git diff / status / log when needed

## Good outputs
- exact diff summary
- commands run
- test result
- any follow-up risk that still needs attention
