# Vault Launch Instructions — Personal Operating System

You are instructed to initialize a new Obsidian-compatible Markdown vault
according to the following specifications.

Do not deviate from these instructions unless explicitly asked.

---

## 1. Vault Folder Structure (Mandatory)

Create the following folder structure exactly as written:

```
00_Inbox/
10_Projects/
20_Knowledge/
25_Playbooks/
30_Decisions/
90_Archive/
99_Templates/
_ai/
```

### Semantic Meaning

- **00_Inbox**  
  Raw capture only. Temporary. Must be emptied regularly.

- **10_Projects**  
  Active efforts that aim to change something in the world.

- **20_Knowledge**  
  Distilled, reusable understanding.

- **25_Playbooks**  
  Reusable, procedural ways of working.

- **30_Decisions**  
  Explicit, durable decisions.

- **90_Archive**  
  Closed or inactive material.

- **99_Templates**  
  Canonical templates only.

- **_ai**  
  AI constitution, prompts, and pattern references.

Each note must live in **exactly one folder**.

---

## 2. Canonical Templates

Create the following templates in `99_Templates/`.

### Project Note Template

**File:** `99_Templates/Project Note.md`

```md
---
type: project
status: active
created: {{date}}
area:
target_condition:
---

# Project — {{title}}

## Why does this project exist?
What change am I trying to make?

## Target condition (definition of done)
Wanneer is dit project klaar?

## As-is
What is the current situation?

## Core decisions
> A decision is a choice that reduces uncertainty and commits the path.

| Decision | Status | Criteria | Input |
|----------|--------|----------|-------|

## Next actions
Only executable, no thinking, <60 min.  
→ To task manager

## Open questions / risks
- …

## Log
- {{date}} — …
```

### Knowledge Note Template

**File:** `99_Templates/Knowledge Note.md`

```md
---
type: knowledge
kind: principle | playbook | reference
created: {{date}}
---

# {{title}}

## What did I learn?
Maximum three sentences.

## Why is this relevant to me?
Concrete impact on thinking or action.

## Where do I apply this?
**Projects**
- [[Project — …]]

**Decisions**
- [[Decision — …]]

## Core points
- …
- …

## Next step (optional)
Only if this is a real action.
```

### Article Template

**File:** `99_Templates/Article.md`

```md
---
type: article
created: {{date}}
---

# Article — {{title}}

## Link
- 

## Raw impression
- 
```

### Idea Template

**File:** `99_Templates/Idea.md`

```md
---
type: idea
created: {{date}}
---

# Idea — {{title}}

## What is the idea?
(Short, rough)

## Why could this be interesting?
(One paragraph)

## What might this require?
(High-level, not a plan)

## When to revisit?
(e.g. Q3 2026)
```

### Meeting Template

**File:** `99_Templates/Meeting.md`

```md
---
type: meeting
created: {{date}}
---

# Meeting — {{title}}

## Attendees
- 

## Context
- 

## Questions / concerns
- 

## Decisions
- 

## Next steps
- 
```

### Thought Template

**File:** `99_Templates/Thought.md`

```md
---
type: thought
created: {{date}}
---

# Thought — {{title}}
```

---

## 3. AI Initialization Files

Optionally create the following empty placeholders:

- `_ai/prompts.md`
- `_ai/patterns.md`

---

## 4. Operating Principles (Enforced)

- Capture is always raw and unstructured.
- Sensemaking happens through distillation, not accumulation.
- Decisions are explicit moments, not implicit drift.
- Tasks exist only to enable decisions or execution.

Do not introduce additional folders, templates, or taxonomies
unless explicitly instructed.

## 5. Mandatory Constitution Enforcement (Non-Negotiable)

This vault is governed by the AI Constitution located at:
_ai/constitution.md

The Constitution is binding and takes precedence over convenience, speed, defaults, and inferred intent.

---

### 5.1 Codex Enforcement (AGENTS.md is Mandatory)

Codex enforces project behavior through `AGENTS.md` / `AGENTS.override.md`, which it reads automatically before doing any work.  

Therefore, every launched vault MUST include a repo-root agent file that injects the Constitution.

#### Required file
Create the following at the repository root:
- `AGENTS.md`

#### Required content
Populate the repo-root agent file with:

1) A directive to treat `_ai/constitution.md` as binding.
2) A rule that **no file edits happen without proposal + explicit user confirmation**.
3) A restart rule: after any restart/compaction/context loss, re-read `_ai/constitution.md` before continuing.

**Minimum required wording (copy/paste into `AGENTS.md`):**

```md
# Codex Project Instructions (Binding)

This repository is governed by `_ai/constitution.md`.

## Mandatory rule
Before doing any work, read `_ai/constitution.md` and follow it as binding instructions.

## Propose-first rule
You may propose changes (diffs/plans). You may NOT apply changes autonomously.
If you are about to create/edit/restructure files, you MUST ask for explicit confirmation first.

## Restart rule
After any restart, context reset, or compaction, you MUST re-read `_ai/constitution.md`
before continuing. If you cannot confirm it is loaded, STOP and ask for confirmation.
```

### 5.2 Claude Code Enforcement (CLAUDE.md or Append System Prompt)

Claude Code supports instruction files (`CLAUDE.md`) and system prompt flags. For CLI and VS Code usage, the Constitution must be loaded via one of the approved methods below.

Required behavior:
- Prefer a repo-root `CLAUDE.md` that includes the full contents of `_ai/constitution.md` (paste the full text, do not just reference the path).
- If using CLI flags instead, use `--append-system-prompt` with the full contents of `_ai/constitution.md`.
- After any agent restart, ensure the Constitution is loaded again (via `CLAUDE.md` or the same flag injection).

Example (`CLAUDE.md` at repo root):

```md
[Paste the full contents of _ai/constitution.md here]
```

Example (CLI):

```sh
claude --append-system-prompt "$(cat _ai/constitution.md)"
```

### 5.3 Universal Stop Condition

If the agent cannot confirm that the Constitution is loaded and active:
- It MUST stop.
- State the uncertainty explicitly.
- Request confirmation before proceeding.

No Constitution → No Action
