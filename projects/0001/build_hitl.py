"""
build_hitl.py — assembles the HITL review summary for a given step.

Reads the final draft artefacts, the most recent critique verdict (if present),
and the governance report (if present). Writes review_summary.md to the
step's for-hitl/ folder.

Reads workflow_config.json to determine which phases were enabled. If the
config cannot be read or contains unexpected values, phases are treated as
optional with a disclaimer added to the summary.

Usage: python build_hitl.py <step>
       step: step-1 | step-2 | step-3

Exit codes:
  0 — review_summary.md written successfully
  1 — required artefact missing or usage error
"""

import json
import sys
from pathlib import Path

VALID_STEPS = {"step-1", "step-2", "step-3"}

STEP_PATHS = {
    "step-1": {
        "draft_files": [
            "step-1-brief/draft/initiative_brief.md",
            "step-1-brief/draft/hlrs.json",
        ],
        "critique_glob": "step-1-brief/critique/*_verdict.json",
        "critique_single": "step-1-brief/critique/critique_verdict.json",
        "governance": None,
        "output": "step-1-brief/for-hitl/review_summary.md",
        "config_step_key": "step-1",
    },
    "step-2": {
        "draft_files": ["step-2-epics/draft/epics.json"],
        "critique_glob": "step-2-epics/critique/*_verdict.json",
        "critique_single": None,
        "governance": "step-2-epics/governance/governance_report.json",
        "output": "step-2-epics/for-hitl/review_summary.md",
        "config_step_key": "step-2",
    },
    "step-3": {
        "draft_files_glob": "step-3-stories/draft/epic_*_stories.json",
        "critique_glob": "step-3-stories/critique/*_verdict.json",
        "critique_single": None,
        "governance": "step-3-stories/governance/governance_report.json",
        "output": "step-3-stories/for-hitl/review_summary.md",
        "config_step_key": "step-3",
    },
}


def load_config(root):
    """
    Returns (config dict or None, disclaimer string or None).
    If config cannot be reliably read, returns (None, disclaimer message).
    """
    config_path = root / "workflow_config.json"
    if not config_path.exists():
        return None, "workflow_config.json not found — phase status unknown; including available artefacts only."
    try:
        with open(config_path, encoding="utf-8") as f:
            config = json.load(f)
        if not isinstance(config, dict):
            raise ValueError("config is not a JSON object")
        return config, None
    except (json.JSONDecodeError, ValueError) as e:
        return None, f"workflow_config.json could not be read ({e}) — phase status unknown; including available artefacts only."


def get_flag(config, step_key, flag):
    """
    Returns (value: bool or None, reliable: bool).
    reliable=False means the flag value was missing or not a boolean.
    """
    if config is None:
        return None, False
    try:
        value = config["steps"][step_key][flag]
        if not isinstance(value, bool):
            return None, False
        return value, True
    except (KeyError, TypeError):
        return None, False


def read_file_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def read_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def format_json_block(data):
    return "```json\n" + json.dumps(data, indent=2) + "\n```"


def collect_draft_content(root, step, paths):
    """Returns list of (label, content) tuples for draft artefacts."""
    sections = []

    if step == "step-3":
        files = sorted(root.glob(paths["draft_files_glob"]))
        if not files:
            raise FileNotFoundError(f"No draft story files found at {paths['draft_files_glob']}")
        for f in files:
            epic_id = f.stem.replace("epic_", "").replace("_stories", "")
            data = read_json(f)
            sections.append((f"Stories — {epic_id}", format_json_block(data)))
    else:
        for rel in paths["draft_files"]:
            p = root / rel
            if not p.exists():
                raise FileNotFoundError(f"Required draft artefact not found: {rel}")
            if p.suffix == ".json":
                sections.append((p.name, format_json_block(read_json(p))))
            else:
                sections.append((p.name, read_file_text(p)))

    return sections


def collect_critique_sections(root, step, paths, config, config_disclaimer):
    """
    Returns list of (label, content) tuples for critique verdicts,
    plus any phase-level disclaimer strings.
    """
    sections = []
    disclaimers = []

    critic_flag, critic_reliable = get_flag(config, paths["config_step_key"], "critic_enabled")

    if not critic_reliable and config_disclaimer is None:
        disclaimers.append(
            f"'critic_enabled' flag could not be read for {paths['config_step_key']} — "
            f"critique included if verdict file found."
        )

    # Step 1 has a single verdict file; Steps 2-3 have one per artefact
    if paths.get("critique_single"):
        verdict_files = [root / paths["critique_single"]]
    else:
        verdict_files = sorted(root.glob(paths["critique_glob"]))

    verdict_files = [f for f in verdict_files if f.exists()]

    if verdict_files:
        for vf in verdict_files:
            data = read_json(vf)
            verdict = data.get("verdict", "UNKNOWN")
            issues = data.get("issues", [])
            label = f"Critique verdict — {vf.stem}" if len(verdict_files) > 1 else "Critique verdict"
            if verdict == "SATISFIED":
                content = f"**{verdict}** — no issues raised."
            else:
                issue_lines = "\n".join(
                    f"- {i['issue']} ({i['artefact_id']})" if isinstance(i, dict) else f"- {i}"
                    for i in issues
                )
                content = f"**{verdict}**\n\n{issue_lines}" if issue_lines else f"**{verdict}**"
            sections.append((label, content))
    else:
        if critic_flag is True:
            disclaimers.append("Critique was enabled but no verdict file was found.")
        elif critic_flag is None and not critic_reliable:
            pass  # already covered by flag disclaimer above

    return sections, disclaimers


def collect_governance_section(root, step, paths, config, config_disclaimer):
    """
    Returns (label, content) or None, plus any disclaimer string.
    """
    if paths["governance"] is None:
        return None, None

    gov_flag, gov_reliable = get_flag(config, paths["config_step_key"], "governance_enabled")

    disclaimer = None
    if not gov_reliable and config_disclaimer is None:
        disclaimer = (
            f"'governance_enabled' flag could not be read for {paths['config_step_key']} — "
            f"governance included if report found."
        )

    gov_path = root / paths["governance"]
    if gov_path.exists():
        data = read_json(gov_path)
        status = data.get("status", "UNKNOWN")
        violations = data.get("violations", [])
        if status == "PASS":
            content = f"**{status}** — all traceability rules satisfied."
        else:
            lines = "\n".join(
                f"- [{v.get('artefact_id', '?')}] {v.get('rule', '')}: {v.get('detail', '')}"
                for v in violations
            )
            content = f"**{status}**\n\n{lines}" if lines else f"**{status}**"
        return ("Governance", content), disclaimer
    else:
        if gov_flag is True:
            return None, "Governance was enabled but no governance report was found."
        return None, disclaimer


def build_summary(step, draft_sections, critique_sections, governance_section, disclaimers):
    lines = [f"# Review Summary — {step}", ""]

    if disclaimers:
        lines.append("> **Note:** " + " ".join(disclaimers))
        lines.append("")

    lines.append("## Artefacts for Review")
    lines.append("")
    for label, content in draft_sections:
        lines.append(f"### {label}")
        lines.append("")
        lines.append(content)
        lines.append("")

    if critique_sections:
        lines.append("## Critique")
        lines.append("")
        for label, content in critique_sections:
            lines.append(f"### {label}")
            lines.append("")
            lines.append(content)
            lines.append("")

    if governance_section:
        label, content = governance_section
        lines.append(f"## {label}")
        lines.append("")
        lines.append(content)
        lines.append("")

    return "\n".join(lines)


def run(step, root=None):
    root = Path(root) if root else Path.cwd()

    if step not in VALID_STEPS:
        print(f"Invalid step '{step}'. Must be one of: {', '.join(sorted(VALID_STEPS))}")
        sys.exit(1)

    paths = STEP_PATHS[step]
    config, config_disclaimer = load_config(root)
    disclaimers = [config_disclaimer] if config_disclaimer else []

    try:
        draft_sections = collect_draft_content(root, step, paths)
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    critique_sections, critique_disclaimers = collect_critique_sections(
        root, step, paths, config, config_disclaimer
    )
    disclaimers.extend(critique_disclaimers)

    governance_section, gov_disclaimer = collect_governance_section(
        root, step, paths, config, config_disclaimer
    )
    if gov_disclaimer:
        disclaimers.append(gov_disclaimer)

    summary = build_summary(step, draft_sections, critique_sections, governance_section, disclaimers)

    output_path = root / paths["output"]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(summary, encoding="utf-8")

    print(f"DONE — review_summary.md written to {output_path}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python build_hitl.py <step>")
        sys.exit(1)
    run(sys.argv[1])


if __name__ == "__main__":
    main()
