# Hermes Unified Profile v2 — Brutal Critique

## Score: 4/10

This design has good instincts — unify the surface, keep a single orchestrator, and route by task instead of by persona — but in its current form it is more manifesto than system. A large part of the architecture is either unimplemented, semantically inconsistent, or dependent on hidden plumbing that is not present in the code I checked.

## What is actually strong
- The goal is sensible: one profile, clearer routing, fewer profile sprawl problems.
- The lane split is conceptually clean: ultrawork / Prometheus / code / creative / ops / review.
- The profile is trying to preserve verification and avoid “done” without proof, which is the right instinct.

## Real flaws, gaps, and risks

### 1) The routing story is mostly dead config
The profile advertises category routing, model overrides, session reuse, and provider bans, but the repo has **zero code references** for the key knobs:
- `category_routes`
- `default_orchestrator`
- `session_id_reuse`
- `no_google_models`
- `plan_required_for`
- `provider-ban-enforcer`
- `skill-pack-loader`
- `model-override-resolver`

That means the design depends on hooks or wrappers that are not visible in the implementation. As written, this is not a system; it is a wish list.

### 2) The fallback chain is likely broken
`config.yaml` sets:

```yaml
fallback_providers:
  - anthropic
  - fast-pool
  - local-gemma
```

But the fallback loader in `hermes_cli/fallback_config.py` only accepts entries that are dictionaries with **both** `provider` and `model`. Bare strings are ignored. So the chain can collapse to empty / no-op behavior.

That is not a theoretical concern — it means the “if gpt-5.5 is down, cascade to X” story may fail in practice.

### 3) `delegate_task` does not support the claimed model-routing interface
The design implies that `delegate_task` can receive category-driven model overrides. The actual function signature is:

```python
def delegate_task(goal=None, context=None, toolsets=None, tasks=None,
                  max_iterations=None, acp_command=None, acp_args=None,
                  role=None, parent_agent=None)
```

There is **no** model override parameter and no category routing parameter. So the most important part of the “route by category” plan is not actually expressible through the existing delegation API.

### 4) Session continuity looks fictional, not implemented
`SKILL.md` says:
- reuse the same session
- preserve child session IDs
- use `--pass-session-id` for child work

But I found **no code reference** for `--pass-session-id`, and the config key `session_id_reuse` also has no code references. Hermes has session tooling, but this exact continuity model is not supported by the checked implementation. That means the design is leaning on a fantasy interface.

### 5) The profile is semantically overloaded, even if the byte budget looks fine
The always-on core text is about **12.2 KB** (`config.yaml` + `SKILL.md`), but the full unified profile directory is about **25.7 KB** once the lane packs are included. The real issue is not raw size; it is that one profile is trying to encode:
- code work
- creative work
- ops/cron
- research
- review
- fallback/provider policy
- session management
- verification policy

That is too many cross-cutting concerns for a single always-on brain. The prompt may fit, but the cognitive load is high.

### 6) The config has internal inconsistencies
A few examples:
- `model.default: gpt-5.4` is paired with `provider: local-gemma`.
- Top-level `model.api_mode: responses` conflicts with the `local-gemma` provider’s `api_mode: chat_completions`.
- Routing names mix model families and provider labels in a way that looks copied from multiple systems rather than normalized.

This kind of mismatch is how “works on paper” configs become maintenance traps.

### 7) The hook map is hand-wavy where it matters most
`hooks-policy.md` explicitly admits that if a hook is not representable directly in core, it should be “implemented in this policy skill or a small wrapper.” That is exactly the problem: the hardest parts are being delegated to vague glue code.

If the safety / routing / continuation behavior is distributed across:
- config keys,
- prompt policy,
- skills,
- wrappers,
- hidden hooks,

you do not have a unified profile, you have a brittle federation.

### 8) The “no Google/Gemini” policy is not proven enforceable
The profile says not to route through Google/Gemini-backed providers, but I found no enforcement path for that rule in code. If it is only a note in the prompt and a config flag with no runtime enforcement, it is a preference, not a guarantee.

### 9) Migration risk is high
Going from 4 profiles to 1 creates a single point of failure:
- one bad config change breaks all lanes
- one polluted prompt pollutes all tasks
- one bad fallback rule affects code, review, ops, and creative work simultaneously
- you lose the safety of hard separation between specialist profiles

In other words, the migration simplifies the file tree but centralizes risk.

## Bottom line
The design is directionally good, but it is not yet operationally credible.

My blunt read:
- **Concept:** strong
- **Implementation confidence:** weak
- **Enforcement:** inconsistent
- **Fallbacks / continuity:** unreliable as written
- **Maintainability:** risky once this grows

## Final verdict
**4/10** — promising architecture idea, but too much of the actual behavior depends on nonexistent or unverified plumbing. Before this can be trusted, the dead config needs to be removed or wired up, fallback syntax needs to match the loader, and session continuity / model routing need real code-backed proof.
