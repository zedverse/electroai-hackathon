# Starter Prompt

You are an AI agent working on the electroai-hackathon project.

## On startup

1. Read `/home/daniel/git/electroai-hackathon/work-diary.md` in full.
2. Report back: "Ready for work." — along with a one-sentence summary of the most recent diary entry so the user knows you are oriented.

## Work diary entries

You **must** add a new dated entry to `work-diary.md` in **two situations**:

1. **After completing a significant amount of work** — e.g. a feature implemented, a set of files created or substantially edited, a report produced, or a task sequence finished.
2. **When the user explicitly asks you to log work** — do it immediately, regardless of how much work was done.

### Entry format

```
## YYYY-MM-DD

- <concise bullet describing what was done and any key decisions>
- ...

*Signed: <your model name or agent identifier>*
```

Use today's date (ISO 8601). Sign every entry you write. Do not sign entries written by others. Append new entries at the bottom of the file; do not edit existing entries.

## General guidance

- Keep entries factual and brief — what changed, what was produced, and why if non-obvious.
- If a single session spans multiple dates, use the date on which the work was completed.
- After writing a diary entry, confirm to the user that it has been logged.
