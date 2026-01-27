---
name: clean-formatting
description: Reformat a markdown note for readability and translate it to English while preserving the original meaning and structure (no content changes beyond formatting and translation).
metadata:
  short-description: Clean formatting + English translation
---

# Clean Formatting

## Trigger
Use when the user asks to improve readability, apply broad formatting rules, or translate a note to English.

## Goal
- Improve readability with consistent structure and reduced whitespace.
- Translate content to English.
- Preserve the original meaning and intent (no substantive changes).

## Formatting rules
- Use plain headers (no bold inside headings).
- Use `#` for title, `##` for major sections, `###` for subsections.
- Remove excessive blank lines; keep a single blank line between sections.
- Normalize bullet indentation to two spaces for nested items.
- Keep blockquotes as blockquotes.
- Avoid adding or removing sections; only reorganize for consistency if content is already out of place.

## Translation rules
- Translate to natural English.
- Keep names, references, and links intact (do not translate filenames or wiki links).
- Preserve numbers, dates, and structure.
- Do not add or remove meaning.

## Workflow
1. Read the target note.
2. Apply formatting rules.
3. Translate to English.
4. Present the proposed changes for confirmation before editing.

## Guardrails
- Do not change meaning, add content, or drop content.
- Always propose changes before applying them.
