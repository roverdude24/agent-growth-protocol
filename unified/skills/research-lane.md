# Research / Librarian Lane

## Purpose
External documentation search, OSS examples, library docs, remote codebase analysis.

## Agent Mapping
- **Librarian** → `deepseek-v4-flash` (fast, cheap, good at docs)
- **Explore** → `claude-haiku-4-5` (fast grep, codebase search)

## When to Use
- Looking up library documentation
- Finding OSS examples
- Searching remote codebases
- Researching best practices

## Tools
- `mcp_fetch` — fetch docs/APIs
- `search_files` — local codebase grep
- `read_file` — read specific files
- `mcp_context_mode_ctx_fetch_and_index` — index docs for search

## Execution Pattern
1. Fire Explore + Librarian in parallel (background)
2. Explore searches local codebase
3. Librarian searches external docs
4. Parent synthesizes results

## Example
```
delegate_task(category="research", prompt="Find JWT best practices and how this codebase handles auth")
```
