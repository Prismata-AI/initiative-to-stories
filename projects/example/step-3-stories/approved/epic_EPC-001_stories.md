# Stories - EPC-001

_1 story._

---

## EPC-001-US-001 — Submit plain English process description for parsing

As a business analyst, I want to submit a free-form description of a process in plain English and receive a structured representation in return, so that I can move from a verbal description to a usable process model without manually specifying steps, roles, or connections.

**Acceptance criteria:**

**Scenario 1: Well-formed description produces a complete structured representation**
Given I have entered a process description that names at least two steps and one role, when I submit the description, then the system returns a structured representation that includes all steps, at least one role or actor, and the flow sequence connecting those steps.

**Scenario 2: Decision points in the description are captured in the structured output**
Given I have entered a process description that includes a conditional branch (for example 'if approved, then... otherwise...'), when I submit the description, then the structured representation includes a decision point with outgoing paths corresponding to each branch stated in the description.

**Scenario 3: Multiple roles in the description are each captured as distinct actors**
Given I have entered a process description that names two or more distinct roles performing different steps, when I submit the description, then the structured representation assigns each step to its correct actor and each actor appears once as a distinct entity.

**Scenario 4: Empty input is rejected without producing a structured representation**
Given I have submitted an empty input field with no process description, when the submission is processed, then no structured representation is returned and I receive a message indicating that a description is required.

**Scenario 5: Very short input lacking process structure is handled without silent failure**
Given I have entered a single word or a phrase that does not describe any process steps or sequence, when I submit the description, then the system does not return a representation claiming to capture a process and instead indicates that the input does not contain enough information to extract a process.

**Rationale:** Directly delivers the NL-to-structure parsing layer EPC-001 identifies as its core capability - accepting a free-form description and extracting steps, decision points, roles, and flow sequences.

---
