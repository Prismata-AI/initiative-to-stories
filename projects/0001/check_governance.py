"""
check_governance.py — validates traceability and coverage of the epic/story hierarchy.

Step 2: checks every epic traces to a valid approved HLR, and every HLR has at least one epic.
Step 3: checks every story traces to a valid approved epic, and every epic has at least one story.

Usage: python check_governance.py <step>
       step: step-2 | step-3

Exit codes:
  0 — PASS (governance_report.json written)
  1 — FAIL (violations found, governance_report.json written) or usage/file error
"""

import json
import sys
from pathlib import Path

VALID_STEPS = {"step-2", "step-3"}


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_report(path, step, violations):
    path.parent.mkdir(parents=True, exist_ok=True)
    status = "PASS" if not violations else "FAIL"
    report = {"step": step, "status": status, "violations": violations}
    path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return status


def check_step2(root):
    epics_path = root / "step-2-epics/draft/epics.json"
    hlrs_path = root / "step-1-brief/approved/hlrs.json"

    if not epics_path.exists():
        print(f"ERROR: {epics_path} not found")
        sys.exit(1)
    if not hlrs_path.exists():
        print(f"ERROR: {hlrs_path} not found")
        sys.exit(1)

    epics_data = load_json(epics_path)
    hlrs_data = load_json(hlrs_path)

    approved_hlr_ids = {hlr["hlr_id"] for hlr in hlrs_data.get("hlrs", [])}
    epics = epics_data.get("epics", [])

    violations = []

    # Rule 1: every epic must cite a valid parent HLR
    for epic in epics:
        epic_id = epic.get("epic_id", "UNKNOWN")
        parent = epic.get("parent_hlr_id", "")
        if not parent or parent not in approved_hlr_ids:
            violations.append({
                "artefact_id": epic_id,
                "rule": "invalid_parent_hlr_id",
                "detail": f"parent_hlr_id '{parent}' not found in approved hlrs.json",
            })

    # Rule 2: every approved HLR must have at least one epic
    covered_hlr_ids = {epic.get("parent_hlr_id") for epic in epics}
    for hlr_id in sorted(approved_hlr_ids):
        if hlr_id not in covered_hlr_ids:
            violations.append({
                "artefact_id": hlr_id,
                "rule": "missing_epic_coverage",
                "detail": f"no epic found with parent_hlr_id '{hlr_id}'",
            })

    return violations


def check_step3(root):
    approved_epics_path = root / "step-2-epics/approved/epics.json"
    stories_glob = "step-3-stories/draft/epic_*_stories.json"

    if not approved_epics_path.exists():
        print(f"ERROR: {approved_epics_path} not found")
        sys.exit(1)

    story_files = sorted(root.glob(stories_glob))
    if not story_files:
        print(f"ERROR: no story files found at {stories_glob}")
        sys.exit(1)

    epics_data = load_json(approved_epics_path)
    approved_epic_ids = {epic["epic_id"] for epic in epics_data.get("epics", [])}

    violations = []
    covered_epic_ids = set()

    # Rule 1: every story must cite a valid parent epic
    for story_file in story_files:
        file_data = load_json(story_file)
        stories = file_data.get("stories", [])
        for story in stories:
            story_id = story.get("story_id", "UNKNOWN")
            parent = story.get("parent_epic_id", "")
            if parent:
                covered_epic_ids.add(parent)
            if not parent or parent not in approved_epic_ids:
                violations.append({
                    "artefact_id": story_id,
                    "rule": "invalid_parent_epic_id",
                    "detail": f"parent_epic_id '{parent}' not found in approved epics.json",
                })

    # Rule 2: every approved epic must have at least one story
    for epic_id in sorted(approved_epic_ids):
        if epic_id not in covered_epic_ids:
            violations.append({
                "artefact_id": epic_id,
                "rule": "missing_story_coverage",
                "detail": f"no story found with parent_epic_id '{epic_id}'",
            })

    return violations


def run(step, root=None):
    root = Path(root) if root else Path.cwd()

    if step == "step-2":
        violations = check_step2(root)
        output_path = root / "step-2-epics/governance/governance_report.json"
    else:
        violations = check_step3(root)
        output_path = root / "step-3-stories/governance/governance_report.json"

    status = write_report(output_path, step, violations)
    print(f"{status} — governance_report.json written to {output_path}")
    if violations:
        for v in violations:
            print(f"  [{v['artefact_id']}] {v['rule']}: {v['detail']}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in VALID_STEPS:
        print(f"Usage: python check_governance.py <step>")
        print(f"       step: {' | '.join(sorted(VALID_STEPS))}")
        sys.exit(1)
    run(sys.argv[1])


if __name__ == "__main__":
    main()
