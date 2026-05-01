# Stories - EPC-002

_2 stories._

---

## EPC-002-US-001 - View structured process rendered as a visual diagram

As a business analyst, I want to see my structured process representation rendered as a visual diagram in the browser, so that I have a publication-quality process map I can review, share, or include in a document without any manual layout effort.

**Acceptance criteria:**

**Scenario 1: A structured representation with sequential steps renders as a connected flow diagram**
Given a structured representation containing three or more sequential steps has been produced by parsing, when diagram rendering completes, then all steps appear as distinct labelled nodes connected by directional arrows in the correct sequence order.

**Scenario 2: Decision points render with the correct branching notation**
Given a structured representation contains one or more decision points with two outgoing paths, when the diagram is rendered, then each decision point is visually distinct from a regular step and each outgoing path is shown as a separate labelled arrow.

**Scenario 3: Roles or actors are represented as distinct swimlanes**
Given a structured representation assigns steps to two or more distinct actors, when the diagram is rendered, then each actor appears in a distinct labelled swimlane and each step appears in the swimlane of its assigned actor.

**Scenario 4: Rendering completes without requiring any user layout input**
Given parsing has produced a structured representation and I have not adjusted any layout settings, when diagram rendering completes, then the diagram is displayed in a legible arrangement with no overlapping nodes or unreadable connections, and I have not been asked to position any element.

**Scenario 5: A structured representation with a single step and no decision points renders without error**
Given a structured representation containing exactly one step and no decision points or actors, when diagram rendering is triggered, then a diagram containing that single labelled step is displayed and no error or blank state is shown.

**Rationale:** Directly delivers the visual rendering capability EPC-002 describes - transforming structured data into a browser-displayed process map using standard notation, without manual layout work from the user.

---

## EPC-002-US-002 - Confirm rendered diagram represents the submitted process faithfully

As a business analyst, I want the rendered diagram to accurately reflect every step, decision, actor, and flow connection from my original description, so that I can trust the visual output as a correct representation of the process I described before sharing or using it.

**Acceptance criteria:**

**Scenario 1: All steps from the structured representation appear in the rendered diagram**
Given a structured representation contains five named steps, when the diagram is rendered, then all five steps appear in the diagram with labels matching the names in the structured representation.

**Scenario 2: No steps or connections are present in the diagram that are absent from the structured representation**
Given the structured representation contains a specific set of steps and connections, when the diagram is rendered, then no additional steps, nodes, or connections appear that were not present in the structured representation.

**Scenario 3: The flow sequence in the diagram matches the sequence in the structured representation**
Given the structured representation defines a specific order of steps and branching paths, when the diagram is rendered, then the directional arrows connecting nodes reflect exactly the same flow sequence as the structured representation.

**Scenario 4: A structured representation that has been corrected by the user renders with the corrected content**
Given a structured representation was initially produced by parsing and then a step label was corrected by the user before rendering, when the diagram is rendered, then the corrected label appears in the diagram and the original label does not.

**Rationale:** Addresses the publication-quality requirement in EPC-002 - a diagram that can be handed to a team or included in a document must faithfully represent the process without omissions or additions.

---
