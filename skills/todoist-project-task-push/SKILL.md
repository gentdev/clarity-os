---
name: todoist-project-task-push
description: Detect unchecked tasks in 10_Projects markdown files and push them to Todoist projects using todoist_project_id frontmatter; use when syncing project tasks from the knowledge repo to Todoist.
---

# Todoist Project Task Push

## Overview
Detect unchecked tasks in `10_Projects/**/*.md` and create matching Todoist tasks in the mapped Todoist project.

## Task format
- Markdown checkbox: `- [ ] Title @due 10 Jul 2027`
- Due date is optional and uses `@due 10 Jul 2027`
- Subtasks: ignore for now

## Project mapping
- Each project file must include `todoist_project_id` in frontmatter.
- If missing, stop and ask the user to add it before creating tasks.
- Offer to use Todoist `find-projects` to look up the correct ID.

## Create in Todoist
- Title: task title without the `@due ...` suffix
- Description: source file path
- Due date: parsed from `@due` (optional)
- If `todoist_project_id` is missing, do not create tasks.

## Workflow
1) Scan `10_Projects/**/*.md` for unchecked tasks.
2) For each file, read frontmatter and locate `todoist_project_id`.
3) If missing, ask the user to add it before creating tasks; optionally run Todoist `find-projects` to help.
4) Parse tasks and due dates.
5) Create tasks in Todoist with description = file path.
6) After successful creation, manually mark the source task as completed in the file to avoid duplicates.

## Resources
### scripts/
- `extract_tasks.py`: parse tasks and due dates without editing files.
