#!/usr/bin/env python3
import re
from pathlib import Path

TASK_RE = re.compile(r"^- \[ \] (.+)$")
DUE_RE = re.compile(r"^(.*?)(?:\s+@due\s+(\d{1,2} [A-Za-z]{3} \d{4}))\s*$")


def extract_tasks(text, path):
    tasks = []
    for line in text.splitlines():
        m = TASK_RE.match(line.strip())
        if not m:
            continue
        raw = m.group(1).strip()
        title = raw
        due = None
        dm = DUE_RE.match(raw)
        if dm:
            title = dm.group(1).strip()
            due = dm.group(2)
        tasks.append({"title": title, "due": due, "source": str(path)})
    return tasks


def main():
    root = Path("10_Projects")
    for md in root.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for task in extract_tasks(text, md):
            print(task)


if __name__ == "__main__":
    main()
