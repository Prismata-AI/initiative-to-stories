# Stories - EPC-004

_4 stories._

---

## EPC-004-US-001 — Insert a new step via natural language instruction

As a business analyst, I want to insert a new process step into an existing diagram by describing it in plain language, so that I can refine a process map without switching away from the natural language interaction model I used to create it.

**Acceptance criteria:**

**Scenario 1: Inserting a step between two existing steps**
Given an existing diagram with at least two sequential steps, when the analyst instructs the tool to add a new step between two named existing steps, then the diagram shows the new step positioned between those two steps and connected by flow arrows in the correct sequence.

**Scenario 2: Inserting a step that carries a role assignment**
Given an existing diagram and a natural language instruction that names both a new step and a responsible actor, when the instruction is submitted, then the new step appears in the diagram attributed to the specified actor and the surrounding flow is preserved intact.

**Scenario 3: Instruction references a step name that does not exist in the diagram**
Given an existing diagram, when the analyst issues an instruction that references an anchor step whose name does not match any step currently in the diagram, then the tool surfaces a message indicating the reference could not be resolved and no change is applied to the diagram.

**Rationale:** Traces directly to the EPC-004 capability of accepting natural language instructions that insert a step into an existing diagram and applying the modification to the visual output.

---

## EPC-004-US-002 — Remove a step from a diagram via natural language instruction

As a business analyst, I want to remove a step from an existing diagram by describing the change in plain language, so that I can eliminate redundant or cancelled process steps without rebuilding the diagram from scratch.

**Acceptance criteria:**

**Scenario 1: Removing an existing step by name and rejoining the surrounding flow**
Given an existing diagram containing a named step with steps before and after it, when the analyst issues an instruction to remove that step, then the step is no longer present in the diagram and the flow that previously connected through it is rejoined between the preceding and following steps.

**Scenario 2: Instruction to remove the only remaining step is declined**
Given an existing diagram containing only one step, when the analyst issues an instruction to remove that step, then the tool declines the operation and informs the analyst that a process map must contain at least one step.

**Rationale:** Traces to the EPC-004 capability of accepting natural language instructions that remove a step from an existing diagram and updating both the visual output and underlying representation accordingly.

---

## EPC-004-US-003 — Structured representation stays in sync after natural language edits

As a business analyst, I want the underlying process data to reflect every natural language edit I make to the diagram, so that exported or downstream-consumed process data matches what I see in the diagram without requiring a separate update step.

**Acceptance criteria:**

**Scenario 1: Structured data reflects a newly inserted step immediately after the instruction is applied**
Given an existing diagram to which a new step has been inserted via a natural language instruction, when the analyst exports the process data, then the exported data includes the newly inserted step in the correct position within the flow sequence.

**Scenario 2: Structured data reflects a removed step immediately after the instruction is applied**
Given an existing diagram from which a step has been removed via a natural language instruction, when the analyst exports the process data, then the removed step is absent from the exported data and the surrounding flow sequence is consistent.

**Scenario 3: Natural language instruction that fails validation does not alter the structured data**
Given an existing diagram and a natural language instruction that the tool cannot resolve - such as an ambiguous reference or an invalid operation - when the instruction is rejected, then the structured representation is identical to what it was before the instruction was submitted.

**Rationale:** Traces to the EPC-004 requirement that modifications are applied to both the visual diagram and the underlying structured representation, ensuring the two remain consistent after every natural language edit.

---

## EPC-004-US-004 — Reassign a step to a different actor via natural language instruction

As a business analyst, I want to reassign responsibility for a step to a different actor by describing the change in plain language, so that I can correct or update ownership in a process map without rebuilding it.

**Acceptance criteria:**

**Scenario 1: Reassigning a step to a named actor already present in the diagram**
Given an existing diagram where a step is attributed to a named actor, when the analyst issues an instruction to reassign that step to a different named actor who already appears elsewhere in the diagram, then the step is displayed attributed to the new actor and the previous actor attribution is removed from that step.

**Scenario 2: Instruction references a step that does not exist in the diagram**
Given an existing diagram, when the analyst issues a reassignment instruction that names a step not present in the diagram, then the tool surfaces a message indicating the step could not be found and no change is applied.

**Rationale:** Traces to the EPC-004 capability of accepting natural language instructions that reassign an actor to a step in an existing diagram and updating the visual output and structured representation accordingly.

---
