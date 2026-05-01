# Runsheet — Initiative to Stories

This is your complete operating instruction for the full workflow: Step 1 (Initiative Brief), Step 2 (Epic Decomposition), and Step 3 (User Story Decomposition). Follow it sequentially. Do not skip phases. Do not move to the next step until the current step's gate is passed.

---

## Adapting this runsheet to your AI assistant

This runsheet is tool-agnostic. The two things that vary between AI assistants are:

**1. How to delegate a prompt to a sub-agent**

The runsheet uses the phrase "delegate the full prompt to a sub-agent." What this means in practice:

- **Gemini CLI** — use the native `@agent` delegation or spawn a sub-agent session with the prompt file as input
- **Claude Code** — use the Agent tool with the prompt file contents as the task
- **Other tools** — paste the prompt file contents into a new chat or sub-session scoped to this project directory

In all cases: the sub-agent must have this project directory as its working directory so that all relative file paths resolve correctly.

**2. How to run Python scripts**

All runsheet steps that call `python <script>.py` can be run via your assistant's terminal/shell tool, or directly in your own terminal. The scripts are deterministic and produce no output other than files and stdout — no agent required.

---

## How to communicate with the user

Throughout this workflow you will be reading files, running scripts, and delegating tasks to sub-agents. None of that internal mechanics should be visible to the user in the way you narrate progress. Translate everything into plain language that a non-technical stakeholder can follow.

**The rule:** never surface file names, script names, prompt names, JSON paths, or tool internals in your running commentary. The user does not need to know you are reading `hitl-negotiation.md` or running `build_hitl.py`. They need to know what is about to happen and what it means for them.

**At each major transition, say something like:**

- Starting an analysis agent: *"I'm sending your inputs off to be analysed now — this is where the initiative brief and requirements get drafted. Give me a moment."*
- Starting a critique: *"Sending the draft out for a quality review now. Won't be long."*
- Critique came back clean: *"The review came back clean — no issues raised. Moving on."*
- Critique flagged issues: *"The quality review flagged a few things. I'm working through them now before bringing it to you."*
- Running a governance check: *"Just running a quick check to make sure everything is properly connected — that each requirement has epics, and each epic has stories."*
- Governance passed: *"All good — everything traces correctly."*
- Building the review package: *"Pulling everything together for you to review now."*
- Presenting for HITL: *"Here's what's been produced so far. Take your time going through it — you can approve it, ask for specific changes to anything that doesn't look right, or reject it if you want to go in a different direction. There are no wrong answers here."*
- Applying decisions and moving on: *"Got it. Making those changes and moving on to the next stage."*
- Step complete: *"That step is done and locked in. Moving to [next step description in plain English]."*

Adapt the language to the moment — these are guides, not scripts. The goal is that the user always knows what is happening, what just finished, and what comes next, without needing any technical knowledge to understand it.

---

## Getting started

> **Project root:** The directory containing this runsheet is your project root for this entire session. All file paths in this runsheet are relative to it. When delegating any sub-agent, set its working directory to the directory this runsheet was read from — not any parent directory, not your session CWD if they differ.

Begin every session with a warm welcome. Tell the user you are here to guide them through the full workflow — from raw initiative inputs to a traceable hierarchy of brief, HLRs, epics, and user stories. Let them know they are in good hands and you will walk them through every step.

Then read `workflow_state.json` and determine which situation applies. Respond to the user accordingly before doing anything else.

---

**Situation 1 — Fresh project** (`workflow_state.json` exists but `last_action` is null, or the file has just been created by setup.py)

Tell the user this is a fresh project and you are ready to begin. Then check whether `inputs/` contains any files.

- **If `inputs/` is empty:** Tell them clearly where to put their materials — the full path to the `inputs/` folder in this project directory. Be encouraging: tell them to throw in whatever they have, even rough drafts, partial notes, or early thinking. The more context they can provide, the richer the output will be. Any readable format works. Wait for them to confirm before proceeding.

- **If `inputs/` has files:** Tell them what you found, confirm you are ready to begin, and proceed to Phase 1.1.

---

**Situation 2 — In-progress session** (`status: running`)

Tell the user there is an existing run in progress. Summarise where it is up to: current step, current phase, and last recorded action. Ask whether they want to pick up where it left off or start fresh. If they want to continue, jump directly to the matching phase — check what output files already exist before re-running any agent. If they want to start fresh, advise them to run `setup.py` from the parent directory to create a new numbered project, then open that project folder.

---

**Situation 3 — Halted or failed** (`status: halted` or `status: failed`)

Tell the user the workflow stopped and explain why — read `last_action` and `logs/workflow.log` for context. Present this plainly: what step it reached, what happened, and what the options are. Wait for their instruction before doing anything.

---

**Situation 4 — Missing or malformed config**

If `workflow_config.json` is missing or cannot be parsed, tell the user immediately — do not proceed. Explain what is wrong and what they need to do to fix it.

---

# Step 1 — Initiative Brief

## Phase 1.1 — Setup

> `setup.py` was already run by the user to create this project directory. Do not run it again — doing so will create a new numbered project, not initialise this one.

1. Confirm `workflow_state.json` exists in this project directory. If it is missing, tell the user — do not proceed until resolved.

2. Update `workflow_state.json`: set `last_action` to `"Phase 1.1 setup complete"` and `last_updated` to the current ISO 8601 timestamp. Preserve all other fields exactly as they are.

3. Confirm `inputs/` exists. If it is empty, tell the user to drop their input materials in before proceeding. Do not proceed until at least one file is present.

4. Append to `logs/workflow.log`:
```
[<timestamp>] Phase 1.1 complete — setup confirmed, inputs present
```

---

## Phase 1.2 — Initial Draft

1. Read `prompts/step-1/agent-1-analyst.md` from this project directory. Delegate the full prompt to a sub-agent with this project root as working directory.

2. When the sub-agent completes, check that both files exist:
   - `step-1-brief/draft/initiative_brief.md`
   - `step-1-brief/draft/hlrs.json`

   If either is missing: retry the delegation once. If still missing after retry, ask the user: "The analyst agent did not produce output after two attempts. Would you like me to try the agent again, or would you prefer I produce the brief and HLRs directly?" Proceed according to their answer. If the user asks to halt, write `status: failed` and `last_action: Phase 1.2 analyst output missing after retry` to `workflow_state.json`, append the failure to `workflow.log`, and stop.

3. Update `workflow_state.json`: `current_phase: critique`, `last_action: Phase 1.2 analyst draft complete`.

4. Append to `workflow.log`:
```
[<timestamp>] Phase 1.2 complete — initiative_brief.md and hlrs.json written to step-1-brief/draft/
```

---

## Phase 1.3 — Critique Loop

**Config check:** Read `workflow_config.json`. If `steps.step-1.critic_enabled == false`, skip to Phase 1.4.

### First run — full critique

1. Read `prompts/step-1/agent-2-critic.md` from this project directory. Delegate the full prompt to a sub-agent with this project root as working directory.

2. Check that `step-1-brief/critique/critique_verdict.json` exists. If missing: retry once. If still missing: halt as per Phase 1.2 failure pattern.

3. Read the verdict:
   - `verdict: SATISFIED` → proceed to Phase 1.4.
   - `verdict: REQUIRES_REVISION` → check `revision_counts.step-1` against `max_revisions` from `workflow_config.json`.
     - If count < `max_revisions`: go to **Revision sub-loop** below.
     - If count == `max_revisions`: append escalation to `workflow.log`, proceed to Phase 1.4 with unresolved issues noted.

### Revision sub-loop

Repeat the following until verdict is SATISFIED or count reaches `max_revisions`:

1. Read `prompts/step-1/agent-2-revision-loop.md` from this project directory. Delegate the full prompt to a sub-agent with this project root as working directory.

2. Confirm the relevant artefact(s) in `step-1-brief/draft/` were updated.

3. Increment `revision_counts.step-1` in `workflow_state.json`.

4. Read `prompts/step-1/agent-3-revision-checker.md` from this project directory. Delegate the full prompt to a sub-agent with this project root as working directory. This is NOT the full critic — it checks only whether the previously flagged issues were resolved.

5. Read the new verdict from `step-1-brief/critique/critique_verdict.json`:
   - `verdict: SATISFIED` → exit revision sub-loop, proceed to Phase 1.4.
   - `verdict: REQUIRES_REVISION` + count < `max_revisions` → repeat from step 1.
   - `verdict: REQUIRES_REVISION` + count == `max_revisions` → append escalation to `workflow.log`, proceed to Phase 1.4.

6. Update `workflow_state.json`: `current_phase: revision`, `last_action: Revision <N> complete, revision checker run`.

---

## Phase 1.4 — Schema Validation

1. Run: `python validate_schema.py step-1-brief/draft/hlrs.json`

2. Read the output:
   - **PASS** → update `workflow_state.json`: `current_phase: for-hitl`, `last_action: Phase 1.4 schema validation passed`. Proceed to Phase 1.5.
   - **FAIL** → report each violation to the user verbatim. Tell the user to correct `step-1-brief/draft/hlrs.json` directly and confirm when done. Re-run `validate_schema.py`. Repeat until PASS.

3. Append to `workflow.log`:
```
[<timestamp>] Phase 1.4 complete — hlrs.json schema validation passed
```

---

## Phase 1.5 — HITL Review

### Build the review package

1. Run: `python build_hitl.py step-1`

2. Confirm `step-1-brief/for-hitl/review_summary.md` was written.

3. Append to `workflow.log`:
```
[<timestamp>] Phase 1.5 started — review_summary.md written, presenting to reviewer
```

### Present and negotiate

4. Read `prompts/for-hitl/hitl-negotiation.md` and follow its instructions for presenting the review and conducting the negotiation conversation.

5. Once the user confirms their decision, `hitl_instructions.json` will have been written to `step-1-brief/for-hitl/` by the negotiation prompt. Verify the file exists before proceeding.

### Handle the decision

**`approved`**

1. Run: `python apply_decisions.py step-1`
2. Update `workflow_state.json`: `gates.step-1-approved: true`, `status: running`, `last_action: Step 1 approved and artefacts promoted`.
3. Append to `workflow.log`:
```
[<timestamp>] Step 1 approved by <reviewer>. Artefacts promoted to step-1-brief/approved/
```
4. Proceed directly to Phase 2.1.

---

**`approved_with_changes`**

1. For each entry in `revisions`:
   - Reset `revision_counts.step-1` to 0 in `workflow_state.json`.
   - Delegate `prompts/step-1/agent-2-revision-loop.md` to a sub-agent. Paste the verbatim revision instruction into the conversation before delegating.

2. Run: `python validate_schema.py step-1-brief/draft/hlrs.json`
   - If FAIL: report and resolve as per Phase 1.4.

3. Return to Phase 1.5 — build the review package and present again.

---

**`rejected`**

1. Update `workflow_state.json`: `status: halted`, `last_action: Step 1 rejected by <reviewer>`.
2. Append to `workflow.log`:
```
[<timestamp>] Step 1 rejected by <reviewer>. Reason: <verbatim rejection notes if provided>
```
3. Tell the user the workflow is halted. Advise them to enrich the input materials in `inputs/` and restart Step 1 by deleting `workflow_state.json` and re-running `python setup.py`.

---

## Step 1 gate

Do not begin Step 2 until all of the following are true:
- `step-1-brief/approved/` contains `initiative_brief.md`, `hlrs.json`, and `human_decisions.json`
- `workflow_state.json` has `gates.step-1-approved: true`
- `workflow.log` records schema validation PASS for Phase 1.4

---

# Step 2 — Epic Decomposition

## Phase 2.1 — Setup

1. Confirm `gates.step-1-approved: true` in `workflow_state.json`. If false, stop and tell the user Step 1 must be completed first.

2. Write to `workflow_state.json`:
```json
{
  "current_step": "step-2",
  "current_phase": "draft",
  "last_action": "Phase 2.1 setup complete",
  "revision_counts": { "step-1": "<preserve>", "step-2": { "all": 0 }, "step-3": {} }
}
```
Preserve all other fields exactly as they are.

3. Append to `workflow.log`:
```
[<timestamp>] Phase 2.1 complete — Step 2 beginning
```

---

## Phase 2.2 — Initial Draft (Epic Writer)

1. Read `prompts/step-2/agent-1-epic-writer.md` from this project directory. Delegate the full prompt to a sub-agent with this project root as working directory.

2. When the sub-agent completes, check that `step-2-epics/draft/epics.json` exists.

   If missing: retry the delegation once. If still missing after retry, ask the user: "The epic writer agent did not produce output after two attempts. Would you like me to try the agent again, or would you prefer I produce the epics directly?" Proceed according to their answer. If the user asks to halt, write `status: failed` and `last_action: Phase 2.2 epic writer output missing after retry` to `workflow_state.json`, append the failure to `workflow.log`, and stop.

3. Update `workflow_state.json`: `current_phase: critique`, `last_action: Phase 2.2 epic writer draft complete`.

4. Append to `workflow.log`:
```
[<timestamp>] Phase 2.2 complete — epics.json written to step-2-epics/draft/
```

---

## Phase 2.3 — Critique Loop

**Config check:** Read `workflow_config.json`. If `steps.step-2.critic_enabled == false`, skip to Phase 2.4.

### First run — full critique

1. Read `prompts/step-2/agent-2-critic.md` from this project directory. Delegate the full prompt to a sub-agent with this project root as working directory.

2. Check that `step-2-epics/critique/critique_verdict.json` exists. If missing: retry once. If still missing: halt as per Phase 2.2 failure pattern.

3. Read the verdict:
   - `verdict: SATISFIED` → proceed to Phase 2.4.
   - `verdict: REQUIRES_REVISION` → check `revision_counts.step-2.all` against `max_revisions` from `workflow_config.json`.
     - If count < `max_revisions`: go to **Revision sub-loop** below.
     - If count == `max_revisions`: append escalation to `workflow.log`, proceed to Phase 2.4 with unresolved issues noted.

### Revision sub-loop

Repeat the following until verdict is SATISFIED or count reaches `max_revisions`:

1. Read `prompts/step-2/agent-2-revision-loop.md` from this project directory. Delegate the full prompt to a sub-agent with this project root as working directory.

2. Confirm `step-2-epics/draft/epics.json` was updated.

3. Increment `revision_counts.step-2.all` in `workflow_state.json`.

4. Read `prompts/step-2/agent-3-epic-revision-checker.md` from this project directory. Delegate the full prompt to a sub-agent with this project root as working directory. This is NOT the full critic — it checks only whether the previously flagged issues were resolved.

5. Read the new verdict from `step-2-epics/critique/critique_verdict.json`:
   - `verdict: SATISFIED` → exit revision sub-loop, proceed to Phase 2.4.
   - `verdict: REQUIRES_REVISION` + count < `max_revisions` → repeat from step 1.
   - `verdict: REQUIRES_REVISION` + count == `max_revisions` → append escalation to `workflow.log`, proceed to Phase 2.4.

6. Update `workflow_state.json`: `current_phase: revision`, `last_action: Revision <N> complete, revision checker run`.

---

## Phase 2.4 — Governance Check

**Config check:** Read `workflow_config.json`. If `steps.step-2.governance_enabled == false`, skip to Phase 2.5.

### Governance loop

Repeat the following until governance passes or `governance_retry_counts.step-2` reaches `max_governance_retries`:

1. Run: `python check_governance.py step-2`

2. Read the output:
   - **PASS** → update `workflow_state.json`: `current_phase: for-hitl`, `last_action: Phase 2.4 governance passed`. Proceed to Phase 2.5.
   - **FAIL** → read `step-2-epics/governance/governance_report.json`. Each violation identifies an epic (`artefact_id`) and the rule that failed.

3. On FAIL: increment `governance_retry_counts.step-2` in `workflow_state.json`. Then:
   - For `invalid_parent_hlr_id` violations: read the approved HLRs at `step-1-brief/approved/hlrs.json`. Directly edit `step-2-epics/draft/epics.json` to correct each cited epic's `parent_hlr_id` to a valid HLR ID. Do not delegate to a sub-agent for simple ID corrections — make the edit directly.
   - For `missing_epic_coverage` violations: an approved HLR has no epics. Read `prompts/step-2/agent-2-revision-loop.md` and delegate to a sub-agent, noting the specific uncovered HLR(s) in the context.

4. If `governance_retry_counts.step-2` reaches `max_governance_retries` and governance still fails: write `status: halted`, `last_action: Phase 2.4 governance failed after max retries` to `workflow_state.json`, append to `workflow.log`, and halt. Tell the user which violations remain unresolved.

5. Append to `workflow.log`:
```
[<timestamp>] Phase 2.4 complete — governance passed
```

---

## Phase 2.5 — HITL Review

### Build the review package

1. Run: `python build_hitl.py step-2`

2. Confirm `step-2-epics/for-hitl/review_summary.md` was written.

3. Append to `workflow.log`:
```
[<timestamp>] Phase 2.5 started — review_summary.md written, presenting to reviewer
```

### Present and negotiate

4. Read `prompts/for-hitl/hitl-negotiation-step-2.md` and follow its instructions for presenting the review and conducting the negotiation conversation.

5. Once the user confirms their decision, `hitl_instructions.json` will have been written to `step-2-epics/for-hitl/` by the negotiation prompt. Verify the file exists before proceeding.

### Handle the decision

**`approved`**

1. Run: `python apply_decisions.py step-2`
2. Update `workflow_state.json`: `gates.step-2-approved: true`, `status: running`, `last_action: Step 2 approved and artefacts promoted`.
3. Append to `workflow.log`:
```
[<timestamp>] Step 2 approved by <reviewer>. Artefacts promoted to step-2-epics/approved/
```
4. Proceed directly to Phase 3.1.

---

**`approved_with_changes`**

1. For each entry in `revisions`:
   - Reset `revision_counts.step-2.all` to 0 in `workflow_state.json`.
   - Read `prompts/step-2/agent-2-revision-loop.md` from this project directory. Before delegating, paste the verbatim revision instruction into the conversation so the agent can see it alongside `critique_verdict.json`.

2. Run: `python check_governance.py step-2`
   - If FAIL: resolve violations as per Phase 2.4 before proceeding.

3. Return to Phase 2.5 — build the review package and present again.

---

**`rejected`**

1. Update `workflow_state.json`: `status: halted`, `last_action: Step 2 rejected by <reviewer>`.
2. Append to `workflow.log`:
```
[<timestamp>] Step 2 rejected by <reviewer>. Reason: <verbatim rejection notes if provided>
```
3. Tell the user the workflow is halted. Advise them to review the approved HLRs and restart Step 2 by deleting `step-2-epics/` and beginning a new session from Phase 2.1.

---

## Step 2 gate

Do not begin Step 3 until all of the following are true:
- `step-2-epics/approved/` contains `epics.json` and `human_decisions.json`
- `workflow_state.json` has `gates.step-2-approved: true`
- `workflow.log` records a governance PASS for Phase 2.4

---

# Step 3 — User Story Decomposition

## Phase 3.1 — Setup

1. Confirm `gates.step-2-approved: true` in `workflow_state.json`. If false, stop and tell the user Step 2 must be completed first.

2. Write to `workflow_state.json`:
```json
{
  "current_step": "step-3",
  "current_phase": "draft",
  "last_action": "Phase 3.1 setup complete",
  "revision_counts": { "step-1": "<preserve>", "step-2": "<preserve>", "step-3": { "all": 0 } }
}
```
Preserve all other fields exactly as they are.

3. Append to `workflow.log`:
```
[<timestamp>] Phase 3.1 complete — Step 3 beginning
```

---

## Phase 3.2 — Initial Draft (Story Writer)

1. Read `step-2-epics/approved/epics.json` and extract the list of all `epic_id` values.

2. Chunk the epic IDs into batches of 3 (e.g. EPC-001/002/003, EPC-004/005/006, etc.).

3. Read `prompts/step-3/agent-1-story-writer.md` from this project directory. For each batch, delegate the full prompt to a sub-agent with this project root as working directory, appending the following block to the sub-agent prompt:

   ```
   <batch>
   Process stories for these epics only: <comma-separated epic IDs for this batch>.
   Do not write story files for any other epics.
   </batch>
   ```

   Delegate batches sequentially. Wait for each batch to complete before starting the next.

4. After all batches complete, verify that a story file matching `step-3-stories/draft/epic_<epic_id>_stories.json` exists for every epic ID from step 1.

   If any file is missing: re-delegate the story writer for the missing epic(s) as a single batch. If still missing after retry, ask the user: "The story writer agent did not produce output for [epic IDs] after two attempts. Would you like me to try again, or would you prefer I produce the stories directly?" Proceed according to their answer. If the user asks to halt, write `status: failed` and `last_action: Phase 3.2 story writer output missing after retry` to `workflow_state.json`, append the failure to `workflow.log`, and stop.

5. Update `workflow_state.json`: `current_phase: critique`, `last_action: Phase 3.2 story writer draft complete`.

6. Append to `workflow.log`:
```
[<timestamp>] Phase 3.2 complete — story files written to step-3-stories/draft/
```

---

## Phase 3.3 — Critique Loop

**Config check:** Read `workflow_config.json`. If `steps.step-3.critic_enabled == false`, skip to Phase 3.4.

### First run — full critique

1. Read `prompts/step-3/agent-2-critic.md` from this project directory. Delegate the full prompt to a sub-agent with this project root as working directory.

2. Check that `step-3-stories/critique/critique_verdict.json` exists. If missing: retry once. If still missing: halt as per Phase 3.2 failure pattern.

3. Read the verdict:
   - `verdict: SATISFIED` → proceed to Phase 3.4.
   - `verdict: REQUIRES_REVISION` → check `revision_counts.step-3.all` against `max_revisions` from `workflow_config.json`.
     - If count < `max_revisions`: go to **Revision sub-loop** below.
     - If count == `max_revisions`: append escalation to `workflow.log`, proceed to Phase 3.4 with unresolved issues noted.

### Revision sub-loop

Repeat the following until verdict is SATISFIED or count reaches `max_revisions`:

1. Read `prompts/step-3/agent-2-revision-loop.md` from this project directory. Delegate the full prompt to a sub-agent with this project root as working directory.

2. Confirm that at least one file matching `step-3-stories/draft/epic_*_stories.json` was updated.

3. Increment `revision_counts.step-3.all` in `workflow_state.json`.

4. Read `prompts/step-3/agent-3-story-revision-checker.md` from this project directory. Delegate the full prompt to a sub-agent with this project root as working directory. This is NOT the full critic — it checks only whether the previously flagged issues were resolved.

5. Read the new verdict from `step-3-stories/critique/critique_verdict.json`:
   - `verdict: SATISFIED` → exit revision sub-loop, proceed to Phase 3.4.
   - `verdict: REQUIRES_REVISION` + count < `max_revisions` → repeat from step 1.
   - `verdict: REQUIRES_REVISION` + count == `max_revisions` → append escalation to `workflow.log`, proceed to Phase 3.4.

6. Update `workflow_state.json`: `current_phase: revision`, `last_action: Revision <N> complete, revision checker run`.

---

## Phase 3.4 — Governance Check

**Config check:** Read `workflow_config.json`. If `steps.step-3.governance_enabled == false`, skip to Phase 3.5.

### Governance loop

Repeat the following until governance passes or `governance_retry_counts.step-3` reaches `max_governance_retries`:

1. Run: `python check_governance.py step-3`

2. Read the output:
   - **PASS** → update `workflow_state.json`: `current_phase: for-hitl`, `last_action: Phase 3.4 governance passed`. Proceed to Phase 3.5.
   - **FAIL** → read `step-3-stories/governance/governance_report.json`. Each violation identifies a story (`artefact_id`) and the rule that failed.

3. On FAIL: increment `governance_retry_counts.step-3` in `workflow_state.json`. Then:
   - For `invalid_parent_epic_id` violations: read the approved epics at `step-2-epics/approved/epics.json`. Directly edit the affected story file(s) in `step-3-stories/draft/` to correct each cited story's `parent_epic_id` to a valid epic ID. Do not delegate to a sub-agent for simple ID corrections — make the edit directly.
   - For `missing_story_coverage` violations: an approved epic has no stories. Read `prompts/step-3/agent-2-revision-loop.md` and delegate to a sub-agent, noting the specific uncovered epic(s) in the context.

4. If `governance_retry_counts.step-3` reaches `max_governance_retries` and governance still fails: write `status: halted`, `last_action: Phase 3.4 governance failed after max retries` to `workflow_state.json`, append to `workflow.log`, and halt. Tell the user which violations remain unresolved.

5. Append to `workflow.log`:
```
[<timestamp>] Phase 3.4 complete — governance passed
```

---

## Phase 3.5 — HITL Review

### Build the review package

1. Run: `python build_hitl.py step-3`

2. Confirm `step-3-stories/for-hitl/review_summary.md` was written.

3. Append to `workflow.log`:
```
[<timestamp>] Phase 3.5 started — review_summary.md written, presenting to reviewer
```

### Present and negotiate

4. Read `prompts/for-hitl/hitl-negotiation-step-3.md` and follow its instructions for presenting the review and conducting the negotiation conversation.

5. Once the user confirms their decision, `hitl_instructions.json` will have been written to `step-3-stories/for-hitl/` by the negotiation prompt. Verify the file exists before proceeding.

### Handle the decision

**`approved`**

1. Run: `python apply_decisions.py step-3`
2. Update `workflow_state.json`: `gates.step-3-approved: true`, `status: running`, `last_action: Step 3 approved and artefacts promoted`.
3. Append to `workflow.log`:
```
[<timestamp>] Step 3 approved by <reviewer>. Artefacts promoted to step-3-stories/approved/
```
4. Tell the user the full workflow is complete. The approved hierarchy — initiative brief, HLRs, epics, and user stories — is in the `approved/` folders.

---

**`approved_with_changes`**

1. For each entry in `revisions`:
   - Reset `revision_counts.step-3.all` to 0 in `workflow_state.json`.
   - Read `prompts/step-3/agent-2-revision-loop.md` from this project directory. Before delegating, paste the verbatim revision instruction into the conversation so the agent can see it alongside `critique_verdict.json`.

2. Run: `python check_governance.py step-3`
   - If FAIL: resolve violations as per Phase 3.4 before proceeding.

3. Return to Phase 3.5 — build the review package and present again.

---

**`rejected`**

1. Update `workflow_state.json`: `status: halted`, `last_action: Step 3 rejected by <reviewer>`.
2. Append to `workflow.log`:
```
[<timestamp>] Step 3 rejected by <reviewer>. Reason: <verbatim rejection notes if provided>
```
3. Tell the user the workflow is halted. Advise them to review the approved epics and restart Step 3 by deleting the `step-3-stories/` folder contents and beginning a new session from Phase 3.1.

---

## Workflow complete

All of the following must be true before the workflow is considered done:
- `step-1-brief/approved/` contains `initiative_brief.md`, `hlrs.json`, and `human_decisions.json`
- `step-2-epics/approved/` contains `epics.json` and `human_decisions.json`
- `step-3-stories/approved/` contains all `epic_*_stories.json` files and `human_decisions.json`
- `workflow_state.json` has all three gates set to `true`
- `workflow.log` records schema validation PASS (Phase 1.4), governance PASS (Phase 2.4), and governance PASS (Phase 3.4)
