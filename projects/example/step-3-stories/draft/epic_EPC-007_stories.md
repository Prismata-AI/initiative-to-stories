# Stories - EPC-007

_3 stories._

---

## EPC-007-US-001 - Ambiguous process description flagged before diagram is produced

As a business analyst, I want the tool to recognise when my process description could be interpreted in more than one way, so that I am not handed a diagram that reflects a guess I did not intend.

**Acceptance criteria:**

**Scenario 1: Single description with multiple plausible interpretations is detected**
Given a process description in which a step or flow branch can be interpreted in at least two meaningfully different ways, when I submit the description for processing, then the system identifies the ambiguity and produces a detection signal rather than silently choosing one interpretation.

**Scenario 2: Unambiguous description is not incorrectly flagged**
Given a process description with clear, unambiguous steps and a single coherent flow, when I submit the description for processing, then the system does not raise an ambiguity signal and proceeds normally to produce a diagram.

**Scenario 3: Description with ambiguous actor assignment is detected**
Given a process description in which a step mentions two possible actors without specifying which is responsible, when I submit the description for processing, then the system detects the actor ambiguity and flags it specifically rather than arbitrarily assigning responsibility.

**Scenario 4: Ambiguity involving a decision branch with no stated outcome paths is detected**
Given a process description that includes a decision point but does not specify what happens on one or more outcome paths, when I submit the description for processing, then the system detects the incomplete decision branch and signals it as ambiguous.

**Rationale:** Delivers the detection signal capability EPC-007 identifies as the prerequisite for appropriate response behaviour - the system must identify ambiguity before it can surface it to the user.

---

## EPC-007-US-002 - Underspecified process description identified as incomplete

As a business analyst, I want the tool to recognise when my process description is too sparse to produce a meaningful map, so that I am prompted to add detail rather than receiving an empty or near-empty diagram.

**Acceptance criteria:**

**Scenario 1: Description too sparse to extract meaningful structure is detected**
Given a process description that names a process but provides insufficient detail to identify distinct steps, decision points, or flow sequences, when I submit the description for processing, then the system produces an underspecification signal rather than attempting to render a near-empty diagram.

**Scenario 2: Partially underspecified description identifies only the incomplete sections**
Given a process description that is fully specified for some sections but missing required detail in others, when I submit the description for processing, then the system identifies only the underspecified portions and signals them distinctly, leaving the well-specified portions unaffected.

**Scenario 3: Adequately specified description is not flagged as underspecified**
Given a process description that contains enough detail to identify all steps, at least one flow sequence, and any relevant decision points, when I submit the description for processing, then the system does not raise an underspecification signal.

**Rationale:** Delivers the underspecification detection variant of EPC-007's input quality assessment capability, distinguishing sparse input from ambiguous input so that the appropriate response behaviour can be triggered.

---

## EPC-007-US-003 - Internally contradictory process description detected before rendering

As a business analyst, I want the tool to identify when different parts of my process description contradict each other, so that I can resolve the conflict before a logically impossible diagram is produced.

**Acceptance criteria:**

**Scenario 1: Description where one statement negates another is detected**
Given a process description in which two statements describe the same step or transition in mutually exclusive terms, when I submit the description for processing, then the system detects the contradiction and produces a contradiction signal identifying the conflicting elements.

**Scenario 2: Description with circular flow that cannot be resolved is detected**
Given a process description that implies a flow sequence with no termination path - where following the steps would produce an unresolvable loop with no exit condition - when I submit the description for processing, then the system identifies this as a structural contradiction and flags it.

**Scenario 3: Description with redundant but non-contradictory repetition is not flagged as contradictory**
Given a process description that restates the same step in different words without changing its meaning or creating a logical conflict, when I submit the description for processing, then the system does not raise a contradiction signal and proceeds to extract a deduplicated representation.

**Scenario 4: Detection signal distinguishes contradiction from ambiguity**
Given a process description that contains a genuine logical contradiction between two stated steps, when I submit the description for processing, then the detection signal produced is categorised as a contradiction rather than an ambiguity, so that the appropriate downstream response can be selected.

**Rationale:** Delivers the contradiction detection variant of EPC-007's input quality assessment capability, ensuring that logically impossible process descriptions are flagged before they proceed to rendering.

---
