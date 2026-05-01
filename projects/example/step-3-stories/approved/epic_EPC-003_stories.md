# Stories - EPC-003

_4 stories._

---

## EPC-003-US-001 - Rename a step in the rendered diagram

As a business analyst, I want to rename a step directly on the rendered diagram, so that I can correct or refine step labels without starting the process description over.

**Acceptance criteria:**

**Scenario 1: Renaming a step updates the label visible in the diagram**
Given a rendered diagram contains a step with a specific label, when I rename that step to a new label, then the diagram displays the new label for that step and the old label is no longer visible.

**Scenario 2: The underlying structured representation reflects the renamed step**
Given I have renamed a step in the rendered diagram, when I inspect the underlying structured representation, then the step's name in the structured representation matches the new label I entered and the original label is not present.

**Scenario 3: Renaming one step does not alter any other step's label or connections**
Given a diagram has four steps, when I rename one step, then the remaining three steps retain their original labels and all flow connections between steps remain unchanged.

**Scenario 4: Attempting to save a step with an empty label is prevented**
Given I have selected a step to rename and cleared the label to leave it blank, when I attempt to confirm the rename, then the empty label is not accepted, the original label is retained, and I receive an indication that a label is required.

**Rationale:** Delivers the rename-nodes direct manipulation capability EPC-003 names explicitly, with the requirement that the underlying structured representation is updated to stay in sync with the visual change.

---

## EPC-003-US-002 - Reorder steps in the rendered diagram

As a business analyst, I want to reorder the steps in my rendered diagram by direct manipulation, so that I can correct the sequence of a process without re-entering the original description.

**Acceptance criteria:**

**Scenario 1: Moving a step to a new position updates the visible sequence in the diagram**
Given a rendered diagram shows steps in a specific sequence, when I move a step to a different position in that sequence, then the diagram redraws to show the step in its new position with flow arrows updated to reflect the new order.

**Scenario 2: The structured representation reflects the new step order after reordering**
Given I have moved a step to a new sequence position, when I inspect the underlying structured representation, then the flow sequence in the representation matches the new order shown in the diagram.

**Scenario 3: Reordering a step that feeds a decision point updates the connections correctly**
Given a diagram contains a step immediately before a decision point, when I move that step to a position after the decision point, then the flow connections before and after the decision point are updated in both the diagram and the structured representation to reflect the new arrangement.

**Scenario 4: Attempting to reorder when only one step exists produces no change**
Given a diagram contains exactly one step and no decision points, when I attempt to reorder that step, then the diagram remains unchanged and no error is shown.

**Rationale:** Delivers the reorder-steps direct manipulation capability EPC-003 names explicitly, with the requirement that sequence changes propagate back into the structured representation.

---

## EPC-003-US-003 - Add a new step to the rendered diagram

As a business analyst, I want to add a new step to my rendered diagram at a position I choose, so that I can extend or correct a process without returning to the original description.

**Acceptance criteria:**

**Scenario 1: A new step added between two existing steps appears in the diagram with correct connections**
Given a rendered diagram contains a sequence of steps, when I add a new step between step 2 and step 3, then the diagram shows the new step positioned between those steps and the flow arrows connect step 2 to the new step and the new step to step 3.

**Scenario 2: The new step is added to the structured representation at the correct position**
Given I have added a new step between two existing steps in the diagram, when I inspect the structured representation, then the new step appears in the flow sequence at the correct position and the connections from and to adjacent steps are updated.

**Scenario 3: A new step can be added at the end of a process**
Given a rendered diagram contains a sequence ending at a terminal step, when I add a new step after the terminal step, then the new step appears in the diagram as the new terminal step and the previous terminal step connects to it.

**Scenario 4: Adding a step with no label is prevented**
Given I have initiated adding a new step and left the label blank, when I attempt to confirm the addition, then the step is not added to the diagram or the structured representation and I receive an indication that a label is required.

**Rationale:** Delivers the add-steps direct manipulation capability EPC-003 names explicitly, including the requirement that additions are propagated into the structured representation with correct flow connections.

---

## EPC-003-US-004 - Remove a step from the rendered diagram

As a business analyst, I want to remove a step from my rendered diagram, so that I can eliminate steps that were captured incorrectly or are no longer part of the process without re-entering the full description.

**Acceptance criteria:**

**Scenario 1: Removing a step from the middle of a sequence reconnects the surrounding steps**
Given a rendered diagram shows steps A, B, and C in sequence, when I remove step B, then the diagram shows A connected directly to C and step B no longer appears.

**Scenario 2: The structured representation no longer contains the removed step**
Given I have removed a step from the rendered diagram, when I inspect the structured representation, then the removed step is absent and the flow sequence connects the steps that preceded and followed it.

**Scenario 3: Removing a step that is the sole outgoing path from a decision point updates the decision point**
Given a decision point has two outgoing paths and one of those paths leads only to the step being removed, when I remove that step, then the diagram updates the decision point to show only one remaining outgoing path and the structured representation is updated accordingly.

**Scenario 4: Removing the only step in a diagram leaves a valid empty state**
Given a diagram contains exactly one step, when I remove that step, then the diagram shows an empty state with no nodes or connections and the structured representation contains no steps.

**Rationale:** Delivers the remove-steps direct manipulation capability EPC-003 names explicitly, including the requirement that removals are propagated into the structured representation with flow connections healed appropriately.

---
