---
name: weekly-review-sensemaking
description: Guide Codex through Weekly Review Step 4 by pruning knowledge notes to only those linked to active projects or decisions.
metadata:
  short-description: Weekly review step 4 — Sensemaking
---

# Weekly Review — Step 4: Sensemaking (selective, light)

## Trigger
Use after:
- Step 2 (project review) is done
- when scanning knowledge notes for applicability

---

## Purpose
Ensure knowledge remains part of active memory:
only knowledge that supports **active projects** or **decisions** stays in `20_Knowledge/`.

---

## Scope
Operate only on:
- `20_Knowledge/`

Active projects include notes in `10_Projects/` with:
- `status: active`
- `status: Execution`

Decisions include all notes in `30_Decisions/` (any status).

---

## Linking rule
A knowledge note is considered linked if **either**:
- it contains explicit `[[links]]` to an active project or decision, **or**
- an active project or decision contains a backlink to the knowledge note.

If a backlink is missing but should exist:
- propose adding the backlink to keep links bidirectional.

---

## Workflow

### 1. List knowledge notes
- Enumerate all notes in `20_Knowledge/`.
- For each note, check for links to active projects/decisions and backlinks from them.

### 2. Identify unlinked notes
- Create a list of notes **not linked** to any active project or decision.

### 3. Per-note decision
For each unlinked knowledge note, ask the user:
1) Add a link to a project or decision (and add the reciprocal backlink if missing)
2) Move to archive (`90_Archive/`)

### 4. Apply changes
- Never move or edit files without explicit approval.
- If linking is chosen, propose the exact link additions.
- If archiving is chosen, propose moving the file to `90_Archive/`.

---

## Output format (per note)
- Note name
- Current links (if any)
- Missing links (if any)
- Proposed options: link to project/decision or archive
- Explicit question: which option?

---

## Guardrails
- Always propose; the user decides and commits.
- No deep sensemaking or rewriting.
- Do not create new knowledge; only link or archive.
