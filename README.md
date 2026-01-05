# Clarity OS

A decision-first personal operating system for knowledge work.

Clarity OS helps you think clearly, make explicit decisions, and execute without mixing tasks and knowledge or accumulating unnecessary notes.

---

## Quick start (10 minutes)

### 1. Prerequisites
Install:
- **Obsidian** — https://obsidian.md  
- **Visual Studio Code** — https://code.visualstudio.com  
- **AI agent** (choose one):
  - **Codex** — https://platform.openai.com/docs/guides/codex
  - **Claude Code** — https://docs.anthropic.com/en/docs/claude-code
(!) A live subscription is necessary to integrate the AI agent in the workflow. 

---

### 2. Create your vault
Ask your AI agent to execute: `_ai/launch-vault.md`

This initializes:
- folder structure
- canonical templates
- AI guardrails

Do not create folders or templates manually.

---

### 3. Read the principles
Before using the system, read: `manifesto.md`

This explains the underlying philosophy and guardrails.

---

### 4. Start using the system
- Capture raw input into `00_Inbox/`
- Use your AI agent to distil, analyse, and propose next steps
- Decide explicitly
- Execute tasks outside Obsidian

You always remain the final authority.

---

## What this system is (and is not)

**Clarity OS is:**
- decision-driven
- minimal by design
- AI-assisted, not AI-operated

**Clarity OS is not:**
- a productivity system
- a task manager
- a second brain
- a note archive

If your goal is to track more tasks or store more information, this system will feel restrictive.

---

## Operating model 
Capture → Sensemaking → Decide → Execute

- Capture is raw and temporary  
- Sensemaking reduces and distils  
- Decisions are explicit  
- Tasks exist only to support decisions or execution  

Details and rationale live in `manifesto.md`.

---

## Tool boundaries

- **Obsidian** — thinking, sensemaking, project control  
- **AI agent (Codex / Claude Code)** — analysis, distillation, challenge  
- **Todoist (or equivalent)** — execution only  

---

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
Each note lives in exactly one folder.

## What defines an active project

An active project is:
- a deliberate effort with a clear target condition
- at least one open core decision

Projects exist to resolve uncertainty, not to manage tasks.

---

## Using AI (practical)

Interact with your AI agent to help you:
- distil raw input
- surface assumptions
- frame decisions
- propose next actions

Create reusable prompts through skills for jobs you repeat often.

Extend your AI agent capabilities through MCP integrations.

## Guardrails

- Markdown files are the source of truth
- AI never edits files autonomously

Enforced via: `_ai/constitution.md`

We highly advise integrating git for tracking and version control. 

## License

MIT License.

This repository provides a framework and templates only.
No advice, guarantees, or outcomes are implied.

