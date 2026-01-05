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
