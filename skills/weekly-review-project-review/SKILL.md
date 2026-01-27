---
name: weekly-review-project-review
description: Guide Codex through Weekly Review Step 2 by forcing explicit review of active projects, validating intent/outcome only when missing, and surfacing pending core decisions.
metadata:
  short-description: Weekly review step 2 — Project review
---

# Weekly Review — Step 2: Review projects

## Trigger
Use after:
- the inbox is empty
- before decision documentation
- when validating which projects remain active

---

## Purpose
Keep only **real, decision-driven projects** active.

A project may only stay active if:
- its intention is clear (or explicitly clarified when missing)
- its target condition is clear (or explicitly clarified when missing)
- it has at least one **open core decision**

---

## Definition (non-negotiable)
A project is:

> An active effort with  
> a clear intention,  
> a clear target condition,  
> and at least one open core decision.

If any of these are missing, the project must be fixed or closed.

**Exception — Execution status:** Projects with `status: Execution` may remain active without core decisions, but must have an explicit `deadline`.

---

## Scope
This skill operates only on:
- notes in `10_Projects/`
- with `status: active`

It does **not**:
- make decisions
- execute actions
- generate tasks

---

## Language
- Default output language: English
- If a project note contains non-English content, propose translating it to English before proceeding.

---

## Workflow

### 1. List active projects
- Enumerate all active projects (`status: active`).
- Process **one project at a time**.
- Require explicit user review for each project.

---

### 2. Validate project intention (only if missing)
Check whether the project note contains clear content under:

- `## Why does this project exist?`
- `## Waarom bestaat dit project?`

If this section is **clear and specific**:
- do not re-validate; continue to Step 3.

If this section is **missing, empty, or vague**:
Ask the user explicitly:
- *Why does this project exist?*
- *What problem or uncertainty is it meant to resolve?*

Propose a concise rewrite for that section (proposal only).

---

### 3. Validate target condition (only if missing)
Check whether the project note contains clear content under:

- `## Target condition (definition of done)`
- `## Target condition`
- `## Target condition (definition of done)` (NL/EN variants)

If this section is **clear and concrete**:
- do not re-validate; continue to Step 4.

If this section is **missing, empty, or vague**:
Ask the user explicitly:
- *What does “done” mean for this project?*
- *What will be true once this project is complete?*

Propose a concise rewrite for that section (proposal only).

A project without a clear target condition may not remain active by default.

---

### 4. Decision review (core step)

#### 4.1 Extract existing decisions
- Locate the project’s `## Core decisions` / `## Kernbeslissingen` section.
- List the current decisions recorded there (including their status if present).

If no decisions are listed:
- explicitly flag: **“No core decisions recorded.”**

#### 4.2 Ask for updates and missing decisions
Ask the user explicitly:
- *Which of these decisions have updates since last review?*
- *Which decisions are still open?*
- *Which core decisions are missing that must be made for this project to progress?*

Validate that proposed items are **real decisions**, not activities.

Valid examples:
- go / no-go
- reduce scope
- stop
- postpone
- commit resources
- change approach

Invalid examples:
- “do more research”
- “think about it”
- “wait and see”

---

### 5. Decision note proposal
For each **pending real decision** that is strategic, durable, or likely to matter later:

- Propose creating a new decision note in `30_Decisions/`
- Propose a clear title:
  - `Decision — <explicit choice>`
- Propose linking the decision note back to the project

Do **not** create decision notes without explicit approval.

(Tactical decisions may remain inside the project note.)

---

### 6. Project validity conclusion
Based on the above, propose **one** of:

- ✅ keep project active
- 🛠 fix project (clarify intention, outcome, or decisions)
- ❌ close / archive project

If **no open/pending decisions** can be named:
- explicitly flag the project as invalid under the OS definition
- default proposal: close / archive (unless the user provides a reason to keep it active)

If archiving is approved, move the project note to `90_Archive/`.

---

## Output format (per project)
For each project reviewed, provide:

- Project name
- Intention: (use existing section content; only ask if missing)
- Target condition: (use existing section content; only ask if missing)
- Existing recorded decisions (as listed in the note)
- User-confirmed: updated decisions / still-open decisions / missing decisions
- Proposed action: keep active / fix / close-archive
- Proposed new decision notes (if any)
- Explicit questions if clarification is needed

---

## Confirmation and pacing
- Present one project at a time
- Require explicit user confirmation
- Only then proceed to the next project
- Do not batch or auto-advance without confirmation

## Project log update
- Always add an entry in the project `## Log` describing all actions taken during the review
  (e.g., decisions added, decisions made, project archived).

---

## Guardrails
- Always propose; the user decides and commits.
- Never make decisions on behalf of the user.
- Never keep a project active without an open/pending decision.
- Never create decision notes without approval.
- Scarcity beats completeness.

## Implicit decisions and postponement
If an implicit decision is detected:
- Propose documenting it explicitly in the project or as a decision note.

If postponement is detected:
- Propose one of:
  - formal postponement (with rationale)
  - escalation to a decision note
  - project closure

Treat unacknowledged postponement as a decision by default.
