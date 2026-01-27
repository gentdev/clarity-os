---
name: weekly-review-inbox-cleanup
description: Guide Codex through Weekly Review Step 1 by triaging each inbox note, ensuring minimum clarity, and proposing exactly one outcome per note.
metadata:
  short-description: Weekly review step 1 — Inbox cleanup
---

# Weekly Review — Step 1: Inbox cleanup

## Trigger
Use when the user is performing the Weekly Review and wants to process every note in `00_Inbox`.

---

## Purpose
Empty the inbox by deciding **what each note is** and **where it belongs**.

This step performs:
- classification
- minimum viable sensemaking
- routing

It explicitly avoids deep sensemaking, decision-making, or execution.

---

## Outcomes (exactly one per note)

- ❌ delete
- ➡️ promote to project
- ➡️ distil to knowledge
- ➡️ escalate to decision
- ➡️ send actions to task manager (Todoist)
- ➡️ archive (move to `90_Archive`)

No other outcomes are allowed.

---

## Atomic classification (required)

Each note must have **one dominant atomic concept**:

- Meeting — Time- and context-bound conversation.
- Person — Individual I interact or collaborate with.
- Project — Active effort with a target condition and open decisions.
- Decision — Explicit choice that reduces uncertainty and sets direction.
- Idea — Raw or untested insight requiring exploration.
- Concept — Developed idea that explains or defines something.
- Principle — Guideline that steers behavior across contexts.
- Reference — External source (book, article, talk, document).
- Playbook — Reusable workflow with clear start–end and decision points.

Atomic type answers: *“What is this note?”*  
Outcome answers: *“What happens to it?”*

---

## Workflow

### 1. Preparation
- List all notes in `00_Inbox`.
- Open the first note.
- Do not edit anything yet.

---

### 2. For the current inbox note

#### A. Identify
- Ask: **“What is this?”**
- Propose the dominant `atomic` type.
- If unclear, ask a clarification question before proceeding.

---

#### B. Mixed content check
If the note clearly contains **multiple atomic concepts**:
- Propose splitting it into separate notes
- Each resulting note must have exactly one atomic type
- Do not perform the split without explicit user approval

---

#### C. Project relation check
Always ask:
- Does this relate to an **active project**?

If **yes**, propose one of:
- summarising it into the project note
- distilling it into a knowledge note linked to the project
- archiving it with an explicit backlink from the project

If **no**, continue with outcome selection.

---

#### D. Outcome selection
Propose **exactly one** outcome from the allowed list.

---

### 3. Minimum viable sensemaking (required before archiving)

A note may **only** be archived if:
- the atomic type is clear
- the title is unambiguous
- future-you can understand what this was and why it existed in <10 seconds

If this bar is not met:
- propose a rename or a one-line clarification
- do not archive yet

---

## Routing rules (proposal only)

Based on outcome and atomic type, propose routing:

- **Playbook** → `25_Playbooks/`
- **Project** → `10_Projects/`
- **Decision** → `30_Decisions/`
- **Knowledge (concept / principle / reference)** → `20_Knowledge/`
- **Mental model** → `40_Mental_Models/`
- **Archive** → `90_Archive/`

No files are moved without approval.

---

## Rename rules (when applicable)

Propose a clear, unambiguous name:

- Meeting → `YYYY-MM-DD — Meeting — <topic>`
- Person → `<FirstName LastName>`
- Decision → `Decision — <clear choice>`
- Project → `Project — <outcome-oriented name>`
- Knowledge / Concept / Principle → `<clear, noun-based title>`
- Reference → `<Author or Source> — <Topic>`

Rename proposals must reflect **atomic content**, not context.

---

## Mental model extraction

If the note contains or implies a **mental model**
(a simplified internal representation used to interpret, decide, or predict):

- Propose creating a dedicated mental model note in `40_Mental_Models/`
- Propose a clear name
- Link it to the originating project or knowledge note
- Do not create it without explicit approval

---

## Actions and tasks

If the note contains **executable actions**:
- Propose concrete tasks for the task manager (Todoist)
- Tasks must be specific and actionable
- Do not create tasks inside the vault

---

## Linking

Before finalizing:
- Propose links to related projects, decisions, people, or knowledge
- Links are proposals only
- If linking a note to a project, also propose the reciprocal link in the project:
  - Use `## Log` for meetings
  - Use `## References` for other note types

---

## Confirmation and progression

For each inbox note, present:
- 1–2 line summary
- proposed atomic type
- proposed outcome
- proposed routing
- proposed rename
- proposed links or tasks
- explicit questions if uncertain

After user confirmation:
- apply the approved changes
- automatically proceed to the next inbox note and present its proposed actions (unless the user asks to pause)

Pause only if the user asks to stop or change flow.

---

## Guardrails

- Always propose; the user decides and commits.
- Never edit, move, or create files without approval.
- Do not make decisions on behalf of the user.
- Do not perform deep sensemaking.
- The inbox must be fully empty before moving to the next Weekly Review step.
