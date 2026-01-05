# Clarity OS — README

Clarity OS is a focused personal operating system for knowledge work.
It provides a structured way to think, make decisions, and execute without mixing tasks and knowledge or accumulating unnecessary notes.

This template is intended for professionals who deal with complex projects, high information load, and ambiguous decisions and who want to use AI to accelerate processing without outsourcing judgment.

It is not a productivity system, task manager, or note-taking method. It's a lightweight framework for project control, sensemaking, and explicit decision-making.

## Why use this approach

- It prioritizes decisions over activity, so progress is measurable by resolved uncertainty.
- It separates capture, sensemaking, decision-making, and execution to prevent clutter and drift.
- It enforces clarity: explicit assumptions, explicit decisions, and minimal output.
- It keeps tools small and purpose-built so each part of the workflow stays sharp.
- It leverages AI to:
-- accelerate information processing
-- distill insights from raw input
-- sharpen thinking and decisions
-- help me learn more effectively

## Key insights

- Markdown is the single source of truth; the human remains the final authority.
- The AI is a sparring partner: precise, critical, and grounded in user input.
- The operating model is Capture → Sensemaking → Decide → Execute, with clear pitfalls.
- Guardrails prevent autonomous restructuring, decision-making, or knowledge creation.
- Decisions are documented explicitly and tied to projects or dedicated decision notes.
- Clarity beats speed; minimal, explicit output is preferred over volume.

## Concrete todos to get started

1. Install VS Code.
2. Set up Claude Code or Cursor.
3. Create the vault by asking your AI agent to execute `_ai/launch-vault.md`.

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

- Todoist MCP integration for actionable tasks outside Obsidian.
- Reusable skills to automate analysis and next-step generation (e.g., “analyze project and generate actions”).

# Disclaimer
Licensed under the MIT License.

This project provides a framework and templates. Adapt to your liking.

It does not provide advice, guarantees, or outcomes.