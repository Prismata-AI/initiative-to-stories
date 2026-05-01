"""
validate_schema.py — validates hlrs.json against the expected schema.

Called by the AI assistant after critique and after HITL approval.
The AI assistant can fix reported violations directly and re-run.

Usage: python validate_schema.py <path-to-hlrs.json>

Exit codes:
  0 — PASS
  1 — FAIL (violations listed) or usage/file error
"""

import json
import re
import sys
from pathlib import Path

HLR_ID_PATTERN = re.compile(r"^HLR-\d+$")


def validate(path):
    """
    Validate hlrs.json at the given path.
    Returns (passed: bool, messages: list[str])
    """
    path = Path(path)

    if not path.exists():
        return False, [f"File not found: {path}"]

    # Rule 1 — valid JSON
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON: {e.msg} at line {e.lineno}, column {e.colno}"]

    violations = []

    # Rule 6 — initiative_id present and non-empty
    if not data.get("initiative_id"):
        violations.append("Missing or empty top-level field 'initiative_id'")

    hlrs = data.get("hlrs")
    if not isinstance(hlrs, list) or len(hlrs) == 0:
        violations.append("'hlrs' must be a non-empty array")
        return False, violations

    seen_ids = {}
    for hlr in hlrs:
        hlr_id = hlr.get("hlr_id", "").strip()

        # Rule 2 — hlr_id matches pattern
        if not hlr_id:
            violations.append(f"HLR entry is missing 'hlr_id'")
        elif not HLR_ID_PATTERN.match(hlr_id):
            violations.append(
                f"'{hlr_id}': hlr_id does not match required pattern HLR-[number] (e.g. HLR-001)"
            )

        # Rule 3 — unique hlr_ids
        if hlr_id:
            seen_ids[hlr_id] = seen_ids.get(hlr_id, 0) + 1

        # Rule 4 — required text fields non-empty
        for field in ("title", "description", "rationale", "impact_if_omitted"):
            if not hlr.get(field, "").strip():
                violations.append(f"{hlr_id or 'unknown'}: missing or empty '{field}'")

    # Rule 3 — report duplicates
    for hlr_id, count in seen_ids.items():
        if count > 1:
            violations.append(f"'{hlr_id}': duplicate hlr_id — appears {count} times")

    if violations:
        return False, violations

    return True, [f"hlrs.json is valid ({len(hlrs)} HLR{'s' if len(hlrs) != 1 else ''})"]


def format_output(path, passed, messages):
    if passed:
        return f"PASS — {messages[0]} in {path}"
    lines = [f"FAIL — {len(messages)} violation(s) found in {path}", ""]
    for i, msg in enumerate(messages, 1):
        lines.append(f"  [{i}] {msg}")
    return "\n".join(lines)


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_schema.py <path-to-hlrs.json>")
        sys.exit(1)

    path = sys.argv[1]
    passed, messages = validate(path)
    print(format_output(path, passed, messages))
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
