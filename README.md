# Agent Growth Protocol (AGP)

**Turn repeated agent mistakes into verified rules. Works with or without Hermes.**

> Biến lỗi lặp lại thành bài học đã kiểm chứng. Dùng được với mọi agent.

---

## Two paths

| Path | For | What it ships |
|------|-----|--------------|
| **[Standalone](standalone/)** | Any agent (Codex, Antigravity, OpenCode, etc.) | SQLite database + CLI helper + SKILL.md |
| **[Hermes-native](hermes/)** | Hermes Agent only | Thin policy SKILL.md (~500 tokens), uses Hermes built-ins |

**Not sure?** Start with Standalone — it works everywhere.

> VN: Bắt đầu với Standalone nếu chưa chắc — dùng được với mọi agent.

---

## Standalone (v0.3.2)

For agents without built-in memory. Includes its own SQLite memory system.

```bash
curl -fsSL https://raw.githubusercontent.com/roverdude24/agent-growth-protocol/main/standalone/install.sh | bash
```

What you get:
- SQLite database: `~/.agent_growth/growth.db`
- Human-readable report: `~/.agent_growth/report.md`
- CLI helper: `~/.agent_growth/bin/agent_growth.py`
- Session-aware recall: `session-start` prints relevant prior learnings

Commands:
```bash
agent_growth.py add-learning --topic tool:x --problem "..." --fix "..."
agent_growth.py add-growth --topic workflow:y --capability "..." --evidence "..."
agent_growth.py verify --id LRN-001 --evidence "..."
agent_growth.py session-start    # prints relevant learnings for new session
agent_growth.py recall --topic tool
agent_growth.py report
```

> VN: SQLite database chạy local, nhanh, không phụ thuộc external service.

Details: [standalone/](standalone/)

---

## Hermes-native (v0.4)

For Hermes Agent. No standalone infrastructure — uses Hermes hooks, memory, and cron.

```bash
curl -fsSL https://raw.githubusercontent.com/roverdude24/agent-growth-protocol/main/install-hermes.sh | bash
```

What you get:
- Thin policy SKILL.md (~500 tokens)
- Uses Hermes hooks for auto-capture
- Uses Hermes memory for storage
- Uses Hermes cron for reporting
- No scripts, no databases

Details: [hermes/](hermes/)

---

## Which should I choose?

| | Standalone | Hermes-native |
|---|---|---|
| **Agent** | Any | Hermes only |
| **Memory** | SQLite (own database) | Hermes built-in |
| **Setup** | Python 3 + script | Just SKILL.md |
| **Auto-capture** | CLI + cron | Hooks + cron |
| **Best for** | Multi-agent setups | Hermes-only setups |

**Choose Standalone** if you use multiple agents or want portable memory.
**Choose Hermes-native** if you're all-in on Hermes and want zero extra infra.

> VN: Standalone = mọi agent, SQLite riêng. Hermes-native = chỉ Hermes, dùng sẵn memory.

---

## How it works

```
Error / Correction / New workflow
        ↓
    Capture lesson
        ↓
    Verify: did this fix work?
        ↓
    Worth keeping?
        ├── No  → keep local
        └── Yes → promote to long-term memory
```

**Rules:**
- Only verified, reusable, high-value learnings enter long-term memory
- Topic prefixes: `hermes-config:`, `tool:`, `workflow:`, `project:`
- Promotion gate: `seen >= 3` + `confidence >= 0.8` + verified

---

## Origin

Adapted from [AI Persona OS](https://clawhub.ai/jeffjhunter/ai-persona-os), narrowed for practical agent learning.

## License

MIT
