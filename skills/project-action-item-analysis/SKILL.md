---
name: project-action-item-analysis
description: Analyze project updates to detect missing action items and write proposed next actions into the project note under a Proposed subheading; compare against open and completed actions; scan project plus referenced notes in 00_Inbox, 20_Knowledge, 25_Playbooks.
---

# Project Action Item Analysis

## Overview
Analyze a project note, plus its referenced notes in `00_Inbox`, `20_Knowledge`, and `25_Playbooks`, to detect missing action items. Write suggested actions back into the project note under a **Proposed** subheading in the Next actions section.

## Scope
- Primary files: `10_Projects/**/*.md`
- Referenced notes: links from the project note that point into `00_Inbox`, `20_Knowledge`, `25_Playbooks`.
- Ignore references outside those folders.

## Definition of "missing"
An action is "missing" if it is not already present in the project’s action overview:
- both unchecked (`- [ ]`) and checked (`- [x]`) actions must be considered
- if a suggested action semantically matches an existing action (open or completed), do not add it

## Language
All proposed actions must be in English.

## Where to write
Locate the project’s **Next actions & Milestones** section. Under it:
- If a `### Proposed` subheading exists, append new actions under it.
- If not, create `### Proposed` and add proposed actions beneath it.

## Action format
- Use Markdown checkboxes: `- [ ] Action text`
- Keep each action concise and executable (<= 1 sentence).
- Avoid duplicating or rephrasing existing actions.

## Workflow
1) Read the project note and extract existing action items (checked and unchecked).
2) Parse links in the project note; load only those that resolve to the allowed folders.
3) Scan those referenced notes for signals that imply actionable next steps.
4) Propose new actions in English, filtered against existing actions for semantic duplication.
5) Write proposed actions into the project note under `### Proposed`.
6) Do not modify any other sections.
7) Prompt the user to optionally push the newly proposed actions to Todoist using the `todoist-project-task-push` skill.

## Resources
### scripts/
- (optional) Add a script later if repeated parsing is needed.
