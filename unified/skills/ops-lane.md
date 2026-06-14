# Ops Lane

This lane handles automation, runtime maintenance, and session/state management.

## When to use
- cron jobs
- session recovery
- memory updates
- profile maintenance
- background worker management
- workspace automation
- repeatable operational scripts

## Operating style
- Treat operations as idempotent unless proven otherwise.
- Prefer explicit state inspection before mutation.
- Use background monitoring for long jobs.
- Keep logs, outputs, and retries structured.
- Separate the control plane from the work being performed.

## Ops patterns
- inspect active sessions before resuming work
- keep automation small and reversible
- schedule recurring tasks only when they have a clear owner and purpose
- promote verified repeated workflows into skills or cron jobs
- use notifications for completion, not for every log line

## Ops lane rules
- Do not mutate operational state without confirming scope.
- Do not clear history, memory, or sessions unless the user explicitly asks.
- If a long-running task is running, monitor it instead of blocking the parent.
- If a workflow is likely to repeat, capture it as a reusable operational pattern.

## Best tools
- process
- terminal background jobs
- session and memory utilities
- config and file editing tools
- cron-related commands

## Good outputs
- state summary
- automation checklist
- exact commands
- schedule definition
- recovery steps
