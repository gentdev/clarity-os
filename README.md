# Clarity OS — README

Clarity OS is a focused personal operating system for knowledge work.
It provides a structured way to think, make decisions, and execute without mixing tasks and knowledge or accumulating unnecessary notes.

This template is intended for professionals who deal with complex projects, high information load, and ambiguous decisions and who want to use AI to accelerate processing without outsourcing judgment.

It is not a productivity system, task manager, or note-taking method. It's a lightweight framework for project control, sensemaking, and explicit decision-making.

## Who this is for

Clarity OS is designed for professionals who:

- work on complex, ambiguous projects
- deal with high information load
- need to make consequential decisions regularly
- want to use AI to accelerate processing **without replacing their own thinking**

Typical users include:
- senior individual contributors
- managers and leaders
- founders and operators
- knowledge workers who feel productive but not always clear


## Key insights

- Markdown is the single source of truth; the human remains the final authority.
- The AI is a sparring partner: precise, critical, and grounded in user input.
- The operating model is Capture → Sensemaking → Decide → Execute, with clear pitfalls.
- Guardrails prevent autonomous restructuring, decision-making, or knowledge creation.
- Decisions are documented explicitly and tied to projects or dedicated decision notes.
- Clarity beats speed; minimal, explicit output is preferred over volume.

For the underlying philosophy and principles, see [`manifesto.md`](./manifesto.md).

## The operating model

This workflows follow this sequence: Capture → Sensemaking → Decide → Execute

Common failure modes:
- Capture too richly → clutter
- Sensemaking without reduction → noise
- Decisions without documentation → drift
- Tasks without decisions → motion without progress

The system is designed to surface and correct these failure modes early.

## How to get started (first-time users)

### Prerequisites

Install and configure the following tools:

- **Obsidian**  
  https://obsidian.md  
  Used as the primary environment for notetaking, thinking, sensemaking, and project control.

- **Visual Studio Code**  
  https://code.visualstudio.com  
  Used as the working environment for AI-assisted analysis and interaction.

- **AI agent (one of the following):**
  - **Codex (CLI + VS Code integration)**  
    https://developers.openai.com/codex/quickstart/
  - **Claude Code**  
    https://code.claude.com/docs/en/setup

  The AI agent is required to analyze notes, distil insights, and propose next steps, always under explicit guardrails.


### Step 1 — Create your vault
Ask your AI agent to execute the following file: _ai/launch-vault.md

This will:
- create the folder structure
- install canonical templates
- initialize AI-related guardrails

⚠️ Do not create folders or templates manually.

### Step 2 — Read the manifesto
Before using the system, read:

This explains the principles behind Clarity OS and how to use it without turning it into another productivity system.

### Step 3 — Start capturing
Use QuickAdd in Obsidian to capture:
- thoughts
- meetings
- articles

All capture is **raw and temporary** and goes into `00_Inbox/`.

Do not organize during capture.

### Step 4 — Interact using your AI agent

Use your AI agent (Codex or Claude Code) to actively work with your vault:

- form understanding from raw input
- analyse context and surface assumptions
- distil insights into knowledge notes
- identify decisions and trade-offs
- propose project updates and next actions

The agent may:
- summarise
- connect
- challenge
- propose

The agent may **not**:
- decide on your behalf
- modify files autonomously
- restructure the vault without approval

All outputs are proposals. You remain the final authority.

## Reusable AI “skills” (recommended)

If you notice yourself repeating the same prompts:

- create reusable **skills** or prompt snippets
- store them in your AI tool of choice (Codex / Claude Code)
- treat them as **personal workflows**, not automation

Examples:
- “Inbox → distillation”
- “Project clarity check”
- “Decision framing”
- “Weekly inbox review"


## Vault structure (high level)
``` 
00_Inbox/        # Raw, temporary capture
10_Projects/     # Active projects with target conditions & decisions
20_Knowledge/    # Distilled, reusable understanding
25_Playbooks/    # Reusable workflows
30_Decisions/    # Explicit, durable decisions
90_Archive/      # Inactive material
99_Templates/    # Canonical templates only
_ai/             # AI constitution, prompts, launch instructions
``` 
## What defines an active project

An active project is strictly defined as:

> A deliberate effort with a clear target condition  
> and at least one open core decision.

Projects exist to **resolve uncertainty**, not to hold tasks.

A project is done when the relevant decisions are made.

## Obsidian setup — configuration & plugins

This vault is intentionally configured to support clear thinking, explicit decisions, and low-friction execution.
The setup is minimal by design: few plugins, strict boundaries, and predictable behavior.

### Core configuration principles

- Markdown is the source of truth.
- Structure over automation.
- Discipline over convenience.
- No duplication between thinking and execution tools.

Obsidian is used for project control and sensemaking, not for task management or dashboards.

### Key Obsidian settings

**Files & Links**
- New notes are created in the current folder.
- Links use standard Markdown (no WikiLinks).
- Relative paths are enabled for portability.
- File extensions are always detected.

**Attachments**
- Attachments are stored per folder in a local `_assets/` directory.
- No global attachment dump.
- Attachments are references, not content.

Example:
```
10_Projects/
Project — Example.md
_assets/
diagram.png
```

**Templates**
- Templates are stored in `99_Templates/`.
- Templates are used only for project notes and knowledge notes.
- No daily note templates.
- No creative or decorative templates.

Templates enforce consistency, not creativity.

### Installed plugins

Only plugins that reduce friction or enforce discipline are enabled.

**Templater**
- Injects dates.
- Standardizes frontmatter.
- Avoids copy-paste errors.

No scripting or advanced logic.

**QuickAdd**
Used exclusively for capture:
- Inbox — Thought
- Inbox — Meeting
- Inbox — Article

All QuickAdd actions:
- Write to `00_Inbox/`.
- Create raw, unstructured notes.
- Avoid premature classification.

Capture is intentionally dumb.

**Linter**
Used lightly to enforce:
- Consistent frontmatter order.
- Clean formatting.

No aggressive auto-formatting.

**Git (optional but recommended)**
Used for:
- Version control.
- Rollback safety.
- AI-assisted editing confidence.

Commits are manual and intentional.

**Dataview (optional, used sparingly)**
Introduced only after the system is stable.

Used for:
- Listing active projects.
- Reviewing open decisions.

Not used for dashboards, KPIs, or analytics.

### Explicitly not installed

- Canvas
- Daily Notes
- Task management plugins
- Calendar plugins
- Graph-focused plugins
- AI plugins inside Obsidian

Obsidian is not a task manager, calendar, or AI playground.

### Operating boundaries

- Inbox notes are temporary and processed weekly.
- Projects are scarce and decision-driven.
- Knowledge must be reusable to stay active.
- Tasks live outside Obsidian.

If something feels unclear, the system favors clarity over speed.

This configuration is stable, portable, and AI-compatible by design.

## Optional integrations and extensions

- Todoist MCP integration to fetch and push actionable tasks
- Reusable skills to automate analysis and next-step generation (e.g., “analyze project and generate actions”).

# Disclaimer
Licensed under the MIT License.

This project provides a framework and templates. Adapt to your liking.

It does not provide advice, guarantees, or outcomes.