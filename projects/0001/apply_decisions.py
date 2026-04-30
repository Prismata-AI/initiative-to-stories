"""
apply_decisions.py — promotes HITL-approved artefacts to the approved/ folder.

Reads hitl_instructions.json from the step's for-hitl/ folder.
Copies draft artefacts to approved/.
Writes human_decisions.json to approved/.

Usage: python apply_decisions.py <step>
       step: step-1 | step-2 | step-3

Exit codes:
  0 — artefacts promoted successfully
  1 — missing inputs, invalid decision, or schema violation
"""

import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

VALID_STEPS = {"step-1", "step-2", "step-3"}
VALID_DECISIONS = {"approved", "approved_with_changes", "rejected"}

STEP_ARTEFACTS = {
    "step-1": {
        "hitl_instructions": "step-1-brief/for-hitl/hitl_instructions.json",
        "draft_glob": None,
        "draft_files": [
            "step-1-brief/draft/initiative_brief.md",
            "step-1-brief/draft/hlrs.json",
        ],
        "approved_dir": "step-1-brief/approved",
        "human_decisions_step": "initiative_brief",
    },
    "step-2": {
        "hitl_instructions": "step-2-epics/for-hitl/hitl_instructions.json",
        "draft_glob": None,
        "draft_files": [
            "step-2-epics/draft/epics.json",
            "step-2-epics/draft/epics.md",
        ],
        "approved_dir": "step-2-epics/approved",
        "human_decisions_step": "epics",
    },
    "step-3": {
        "hitl_instructions": "step-3-stories/for-hitl/hitl_instructions.json",
        "draft_glob": "step-3-stories/draft/epic_*_stories.*",
        "draft_files": [],
        "approved_dir": "step-3-stories/approved",
        "human_decisions_step": "user_stories",
    },
}


def load_hitl_instructions(path):
    """
    Load and validate hitl_instructions.json.
    Returns (data, error_message).
    """
    if not path.exists():
        return None, f"hitl_instructions.json not found: {path}"

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return None, f"hitl_instructions.json is not valid JSON: {e}"

    if not isinstance(data, dict):
        return None, "hitl_instructions.json must be a JSON object"

    decision = data.get("decision", "")
    if decision not in VALID_DECISIONS:
        return None, (
            f"Invalid decision '{decision}' in hitl_instructions.json. "
            f"Must be one of: {', '.join(sorted(VALID_DECISIONS))}"
        )

    if not data.get("reviewer", "").strip():
        return None, "hitl_instructions.json is missing required field 'reviewer'"

    if not data.get("reviewed_at", "").strip():
        return None, "hitl_instructions.json is missing required field 'reviewed_at'"

    return data, None


def collect_draft_files(root, step, paths):
    """
    Returns list of Path objects for all draft artefacts to promote.
    Raises FileNotFoundError if a required file is missing.
    """
    files = []

    for rel in paths["draft_files"]:
        p = root / rel
        if not p.exists():
            raise FileNotFoundError(f"Required draft artefact not found: {rel}")
        files.append(p)

    if paths["draft_glob"]:
        globbed = sorted(root.glob(paths["draft_glob"]))
        if not globbed:
            raise FileNotFoundError(f"No draft files found matching: {paths['draft_glob']}")
        files.extend(globbed)

    return files


def build_human_decisions(instructions, step_label):
    """
    Build human_decisions.json from hitl_instructions.
    """
    return {
        "step": step_label,
        "reviewed_at": instructions.get("reviewed_at", ""),
        "reviewer": instructions.get("reviewer", ""),
        "decision": instructions.get("decision", ""),
        "changes": [
            {
                "artefact_id": r.get("artefact_id", ""),
                "verbatim": r.get("verbatim", ""),
            }
            for r in instructions.get("revisions", [])
        ],
    }


def run(step, root=None):
    root = Path(root) if root else Path.cwd()

    if step not in VALID_STEPS:
        print(f"Invalid step '{step}'. Must be one of: {', '.join(sorted(VALID_STEPS))}")
        sys.exit(1)

    paths = STEP_ARTEFACTS[step]
    instructions_path = root / paths["hitl_instructions"]

    instructions, error = load_hitl_instructions(instructions_path)
    if error:
        print(f"ERROR: {error}")
        sys.exit(1)

    try:
        draft_files = collect_draft_files(root, step, paths)
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    approved_dir = root / paths["approved_dir"]
    approved_dir.mkdir(parents=True, exist_ok=True)

    for src in draft_files:
        dest = approved_dir / src.name
        shutil.copy2(src, dest)

    human_decisions = build_human_decisions(instructions, paths["human_decisions_step"])
    decisions_path = approved_dir / "human_decisions.json"
    with open(decisions_path, "w", encoding="utf-8") as f:
        json.dump(human_decisions, f, indent=2)

    print(
        f"DONE — {len(draft_files)} artefact(s) promoted to {approved_dir}; "
        f"human_decisions.json written."
    )


def main():
    if len(sys.argv) != 2:
        print("Usage: python apply_decisions.py <step>")
        sys.exit(1)
    run(sys.argv[1])


if __name__ == "__main__":
    main()
