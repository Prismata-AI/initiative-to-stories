# Initiative to Stories

Transforms a raw initiative into a traceable hierarchy of Initiative Brief, HLRs, Epics, and User Stories.

## Starting a run

1. Run `setup.py` from the directory where you want your `projects/` folder to live. This creates `projects/0001/` (or the next available number).
2. Drop your input files into `projects/0001/inputs/`.
3. Open the `projects/0001/` folder with your AI assistant — not the parent directory.
4. Paste the following as your opening prompt:

```
Read runsheet.md and pick up the workflow from the current state.
```

That's it. The runsheet will guide you and your assistant through each step.

## Running setup again

Each run of `setup.py` creates a new numbered project (`projects/0001/`, `projects/0002/`, etc.). Previous projects are not affected.
