# Initiative to Stories

Transforms raw initiative inputs — strategy documents, stakeholder notes, transcripts, business cases, a loose concept or any combination — into a fully traceable hierarchy of Initiative Brief, High-Level Requirements, Epics, and User Stories.

You drop in whatever you have. The workflow synthesises it, drafts it, critiques it, and brings it to you for review at every step before moving forward.

## What it produces

- **Initiative Brief** — a clear problem statement, goals, DVF assessment, and open questions synthesised from your inputs
- **High-Level Requirements (HLRs)** — solution-independent capability statements derived from your inputs and the brief
- **Epics** — structured decomposition of HLRs into deliverable capability slices
- **User Stories** — sprint-sized, INVEST-tested stories with BDD acceptance criteria, traceable to their parent epic

Each artefact goes through an automated critique and revision loop before it reaches you. You review and approve (or request changes) at each step — nothing progresses without your sign-off.

The workflow tracks its own state, so you can close your session at any point — to clarify objectives, get stakeholder sign-off, or just pick it up later — and resume exactly where you left off.

All generative work is delegated to sub-agents, keeping your main context window free. That means you can have a real conversation with your coding agent throughout — asking questions, refining outputs, or thinking out loud — without the workflow getting in the way.

## Works with any coding agent*
Paste the runsheet path as your opening prompt; the workflow was designed to be platform agnostic (*tested on Claude Code & Gemini CLI)

## Getting started

1. Run `setup.py` from the directory where you want your `projects/` folder to live. This creates `projects/0001/` (or the next available number).
2. Drop your input files into `projects/0001/inputs/`. Any readable format works — docs, PDFs, markdown, plain text.
3. Open your AI assistant and point it at the project:

```
"Open with the following prompt"
Read runsheet.md in <your project directory> and pick up the workflow from the current state.
```

That's it. The runsheet guides you and your assistant through each step.

## Running setup again

Each run of `setup.py` creates a new numbered project (`projects/0001/`, `projects/0002/`, etc.). Previous projects are not affected.
