# Review Summary — step-3

## Artefacts for Review

### Stories — EPC-001

```json
{
  "epic_id": "EPC-001",
  "stories": [
    {
      "story_id": "EPC-001-US-001",
      "title": "Submit plain English process description for parsing",
      "narrative": "As a business analyst, I want to submit a free-form description of a process in plain English and receive a structured representation in return, so that I can move from a verbal description to a usable process model without manually specifying steps, roles, or connections.",
      "parent_epic_id": "EPC-001",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Well-formed description produces a complete structured representation",
          "steps": "Given I have entered a process description that names at least two steps and one role, when I submit the description, then the system returns a structured representation that includes all steps, at least one role or actor, and the flow sequence connecting those steps."
        },
        {
          "title": "Scenario 2: Decision points in the description are captured in the structured output",
          "steps": "Given I have entered a process description that includes a conditional branch (for example 'if approved, then... otherwise...'), when I submit the description, then the structured representation includes a decision point with outgoing paths corresponding to each branch stated in the description."
        },
        {
          "title": "Scenario 3: Multiple roles in the description are each captured as distinct actors",
          "steps": "Given I have entered a process description that names two or more distinct roles performing different steps, when I submit the description, then the structured representation assigns each step to its correct actor and each actor appears once as a distinct entity."
        },
        {
          "title": "Scenario 4: Empty input is rejected without producing a structured representation",
          "steps": "Given I have submitted an empty input field with no process description, when the submission is processed, then no structured representation is returned and I receive a message indicating that a description is required."
        },
        {
          "title": "Scenario 5: Very short input lacking process structure is handled without silent failure",
          "steps": "Given I have entered a single word or a phrase that does not describe any process steps or sequence, when I submit the description, then the system does not return a representation claiming to capture a process and instead indicates that the input does not contain enough information to extract a process."
        }
      ],
      "rationale": "Directly delivers the NL-to-structure parsing layer EPC-001 identifies as its core capability - accepting a free-form description and extracting steps, decision points, roles, and flow sequences."
    }
  ]
}
```

### Stories — EPC-002

```json
{
  "epic_id": "EPC-002",
  "stories": [
    {
      "story_id": "EPC-002-US-001",
      "title": "View structured process rendered as a visual diagram",
      "narrative": "As a business analyst, I want to see my structured process representation rendered as a visual diagram in the browser, so that I have a publication-quality process map I can review, share, or include in a document without any manual layout effort.",
      "parent_epic_id": "EPC-002",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: A structured representation with sequential steps renders as a connected flow diagram",
          "steps": "Given a structured representation containing three or more sequential steps has been produced by parsing, when diagram rendering completes, then all steps appear as distinct labelled nodes connected by directional arrows in the correct sequence order."
        },
        {
          "title": "Scenario 2: Decision points render with the correct branching notation",
          "steps": "Given a structured representation contains one or more decision points with two outgoing paths, when the diagram is rendered, then each decision point is visually distinct from a regular step and each outgoing path is shown as a separate labelled arrow."
        },
        {
          "title": "Scenario 3: Roles or actors are represented as distinct swimlanes",
          "steps": "Given a structured representation assigns steps to two or more distinct actors, when the diagram is rendered, then each actor appears in a distinct labelled swimlane and each step appears in the swimlane of its assigned actor."
        },
        {
          "title": "Scenario 4: Rendering completes without requiring any user layout input",
          "steps": "Given parsing has produced a structured representation and I have not adjusted any layout settings, when diagram rendering completes, then the diagram is displayed in a legible arrangement with no overlapping nodes or unreadable connections, and I have not been asked to position any element."
        },
        {
          "title": "Scenario 5: A structured representation with a single step and no decision points renders without error",
          "steps": "Given a structured representation containing exactly one step and no decision points or actors, when diagram rendering is triggered, then a diagram containing that single labelled step is displayed and no error or blank state is shown."
        }
      ],
      "rationale": "Directly delivers the visual rendering capability EPC-002 describes - transforming structured data into a browser-displayed process map using standard notation, without manual layout work from the user."
    },
    {
      "story_id": "EPC-002-US-002",
      "title": "Confirm rendered diagram represents the submitted process faithfully",
      "narrative": "As a business analyst, I want the rendered diagram to accurately reflect every step, decision, actor, and flow connection from my original description, so that I can trust the visual output as a correct representation of the process I described before sharing or using it.",
      "parent_epic_id": "EPC-002",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: All steps from the structured representation appear in the rendered diagram",
          "steps": "Given a structured representation contains five named steps, when the diagram is rendered, then all five steps appear in the diagram with labels matching the names in the structured representation."
        },
        {
          "title": "Scenario 2: No steps or connections are present in the diagram that are absent from the structured representation",
          "steps": "Given the structured representation contains a specific set of steps and connections, when the diagram is rendered, then no additional steps, nodes, or connections appear that were not present in the structured representation."
        },
        {
          "title": "Scenario 3: The flow sequence in the diagram matches the sequence in the structured representation",
          "steps": "Given the structured representation defines a specific order of steps and branching paths, when the diagram is rendered, then the directional arrows connecting nodes reflect exactly the same flow sequence as the structured representation."
        },
        {
          "title": "Scenario 4: A structured representation that has been corrected by the user renders with the corrected content",
          "steps": "Given a structured representation was initially produced by parsing and then a step label was corrected by the user before rendering, when the diagram is rendered, then the corrected label appears in the diagram and the original label does not."
        }
      ],
      "rationale": "Addresses the publication-quality requirement in EPC-002 - a diagram that can be handed to a team or included in a document must faithfully represent the process without omissions or additions."
    }
  ]
}
```

### Stories — EPC-003

```json
{
  "epic_id": "EPC-003",
  "stories": [
    {
      "story_id": "EPC-003-US-001",
      "title": "Rename a step in the rendered diagram",
      "narrative": "As a business analyst, I want to rename a step directly on the rendered diagram, so that I can correct or refine step labels without starting the process description over.",
      "parent_epic_id": "EPC-003",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Renaming a step updates the label visible in the diagram",
          "steps": "Given a rendered diagram contains a step with a specific label, when I rename that step to a new label, then the diagram displays the new label for that step and the old label is no longer visible."
        },
        {
          "title": "Scenario 2: The underlying structured representation reflects the renamed step",
          "steps": "Given I have renamed a step in the rendered diagram, when I inspect the underlying structured representation, then the step's name in the structured representation matches the new label I entered and the original label is not present."
        },
        {
          "title": "Scenario 3: Renaming one step does not alter any other step's label or connections",
          "steps": "Given a diagram has four steps, when I rename one step, then the remaining three steps retain their original labels and all flow connections between steps remain unchanged."
        },
        {
          "title": "Scenario 4: Attempting to save a step with an empty label is prevented",
          "steps": "Given I have selected a step to rename and cleared the label to leave it blank, when I attempt to confirm the rename, then the empty label is not accepted, the original label is retained, and I receive an indication that a label is required."
        }
      ],
      "rationale": "Delivers the rename-nodes direct manipulation capability EPC-003 names explicitly, with the requirement that the underlying structured representation is updated to stay in sync with the visual change."
    },
    {
      "story_id": "EPC-003-US-002",
      "title": "Reorder steps in the rendered diagram",
      "narrative": "As a business analyst, I want to reorder the steps in my rendered diagram by direct manipulation, so that I can correct the sequence of a process without re-entering the original description.",
      "parent_epic_id": "EPC-003",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Moving a step to a new position updates the visible sequence in the diagram",
          "steps": "Given a rendered diagram shows steps in a specific sequence, when I move a step to a different position in that sequence, then the diagram redraws to show the step in its new position with flow arrows updated to reflect the new order."
        },
        {
          "title": "Scenario 2: The structured representation reflects the new step order after reordering",
          "steps": "Given I have moved a step to a new sequence position, when I inspect the underlying structured representation, then the flow sequence in the representation matches the new order shown in the diagram."
        },
        {
          "title": "Scenario 3: Reordering a step that feeds a decision point updates the connections correctly",
          "steps": "Given a diagram contains a step immediately before a decision point, when I move that step to a position after the decision point, then the flow connections before and after the decision point are updated in both the diagram and the structured representation to reflect the new arrangement."
        },
        {
          "title": "Scenario 4: Attempting to reorder when only one step exists produces no change",
          "steps": "Given a diagram contains exactly one step and no decision points, when I attempt to reorder that step, then the diagram remains unchanged and no error is shown."
        }
      ],
      "rationale": "Delivers the reorder-steps direct manipulation capability EPC-003 names explicitly, with the requirement that sequence changes propagate back into the structured representation."
    },
    {
      "story_id": "EPC-003-US-003",
      "title": "Add a new step to the rendered diagram",
      "narrative": "As a business analyst, I want to add a new step to my rendered diagram at a position I choose, so that I can extend or correct a process without returning to the original description.",
      "parent_epic_id": "EPC-003",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: A new step added between two existing steps appears in the diagram with correct connections",
          "steps": "Given a rendered diagram contains a sequence of steps, when I add a new step between step 2 and step 3, then the diagram shows the new step positioned between those steps and the flow arrows connect step 2 to the new step and the new step to step 3."
        },
        {
          "title": "Scenario 2: The new step is added to the structured representation at the correct position",
          "steps": "Given I have added a new step between two existing steps in the diagram, when I inspect the structured representation, then the new step appears in the flow sequence at the correct position and the connections from and to adjacent steps are updated."
        },
        {
          "title": "Scenario 3: A new step can be added at the end of a process",
          "steps": "Given a rendered diagram contains a sequence ending at a terminal step, when I add a new step after the terminal step, then the new step appears in the diagram as the new terminal step and the previous terminal step connects to it."
        },
        {
          "title": "Scenario 4: Adding a step with no label is prevented",
          "steps": "Given I have initiated adding a new step and left the label blank, when I attempt to confirm the addition, then the step is not added to the diagram or the structured representation and I receive an indication that a label is required."
        }
      ],
      "rationale": "Delivers the add-steps direct manipulation capability EPC-003 names explicitly, including the requirement that additions are propagated into the structured representation with correct flow connections."
    },
    {
      "story_id": "EPC-003-US-004",
      "title": "Remove a step from the rendered diagram",
      "narrative": "As a business analyst, I want to remove a step from my rendered diagram, so that I can eliminate steps that were captured incorrectly or are no longer part of the process without re-entering the full description.",
      "parent_epic_id": "EPC-003",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Removing a step from the middle of a sequence reconnects the surrounding steps",
          "steps": "Given a rendered diagram shows steps A, B, and C in sequence, when I remove step B, then the diagram shows A connected directly to C and step B no longer appears."
        },
        {
          "title": "Scenario 2: The structured representation no longer contains the removed step",
          "steps": "Given I have removed a step from the rendered diagram, when I inspect the structured representation, then the removed step is absent and the flow sequence connects the steps that preceded and followed it."
        },
        {
          "title": "Scenario 3: Removing a step that is the sole outgoing path from a decision point updates the decision point",
          "steps": "Given a decision point has two outgoing paths and one of those paths leads only to the step being removed, when I remove that step, then the diagram updates the decision point to show only one remaining outgoing path and the structured representation is updated accordingly."
        },
        {
          "title": "Scenario 4: Removing the only step in a diagram leaves a valid empty state",
          "steps": "Given a diagram contains exactly one step, when I remove that step, then the diagram shows an empty state with no nodes or connections and the structured representation contains no steps."
        }
      ],
      "rationale": "Delivers the remove-steps direct manipulation capability EPC-003 names explicitly, including the requirement that removals are propagated into the structured representation with flow connections healed appropriately."
    }
  ]
}
```

### Stories — EPC-004

```json
{
  "epic_id": "EPC-004",
  "stories": [
    {
      "story_id": "EPC-004-US-001",
      "title": "Insert a new step via natural language instruction",
      "narrative": "As a business analyst, I want to insert a new process step into an existing diagram by describing it in plain language, so that I can refine a process map without switching away from the natural language interaction model I used to create it.",
      "parent_epic_id": "EPC-004",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Inserting a step between two existing steps",
          "steps": "Given an existing diagram with at least two sequential steps, when the analyst instructs the tool to add a new step between two named existing steps, then the diagram shows the new step positioned between those two steps and connected by flow arrows in the correct sequence."
        },
        {
          "title": "Scenario 2: Inserting a step that carries a role assignment",
          "steps": "Given an existing diagram and a natural language instruction that names both a new step and a responsible actor, when the instruction is submitted, then the new step appears in the diagram attributed to the specified actor and the surrounding flow is preserved intact."
        },
        {
          "title": "Scenario 3: Instruction references a step name that does not exist in the diagram",
          "steps": "Given an existing diagram, when the analyst issues an instruction that references an anchor step whose name does not match any step currently in the diagram, then the tool surfaces a message indicating the reference could not be resolved and no change is applied to the diagram."
        }
      ],
      "rationale": "Traces directly to the EPC-004 capability of accepting natural language instructions that insert a step into an existing diagram and applying the modification to the visual output."
    },
    {
      "story_id": "EPC-004-US-002",
      "title": "Remove a step from a diagram via natural language instruction",
      "narrative": "As a business analyst, I want to remove a step from an existing diagram by describing the change in plain language, so that I can eliminate redundant or cancelled process steps without rebuilding the diagram from scratch.",
      "parent_epic_id": "EPC-004",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Removing an existing step by name and rejoining the surrounding flow",
          "steps": "Given an existing diagram containing a named step with steps before and after it, when the analyst issues an instruction to remove that step, then the step is no longer present in the diagram and the flow that previously connected through it is rejoined between the preceding and following steps."
        },
        {
          "title": "Scenario 2: Instruction to remove the only remaining step is declined",
          "steps": "Given an existing diagram containing only one step, when the analyst issues an instruction to remove that step, then the tool declines the operation and informs the analyst that a process map must contain at least one step."
        }
      ],
      "rationale": "Traces to the EPC-004 capability of accepting natural language instructions that remove a step from an existing diagram and updating both the visual output and underlying representation accordingly."
    },
    {
      "story_id": "EPC-004-US-003",
      "title": "Structured representation stays in sync after natural language edits",
      "narrative": "As a business analyst, I want the underlying process data to reflect every natural language edit I make to the diagram, so that exported or downstream-consumed process data matches what I see in the diagram without requiring a separate update step.",
      "parent_epic_id": "EPC-004",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Structured data reflects a newly inserted step immediately after the instruction is applied",
          "steps": "Given an existing diagram to which a new step has been inserted via a natural language instruction, when the analyst exports the process data, then the exported data includes the newly inserted step in the correct position within the flow sequence."
        },
        {
          "title": "Scenario 2: Structured data reflects a removed step immediately after the instruction is applied",
          "steps": "Given an existing diagram from which a step has been removed via a natural language instruction, when the analyst exports the process data, then the removed step is absent from the exported data and the surrounding flow sequence is consistent."
        },
        {
          "title": "Scenario 3: Natural language instruction that fails validation does not alter the structured data",
          "steps": "Given an existing diagram and a natural language instruction that the tool cannot resolve - such as an ambiguous reference or an invalid operation - when the instruction is rejected, then the structured representation is identical to what it was before the instruction was submitted."
        }
      ],
      "rationale": "Traces to the EPC-004 requirement that modifications are applied to both the visual diagram and the underlying structured representation, ensuring the two remain consistent after every natural language edit."
    },
    {
      "story_id": "EPC-004-US-004",
      "title": "Reassign a step to a different actor via natural language instruction",
      "narrative": "As a business analyst, I want to reassign responsibility for a step to a different actor by describing the change in plain language, so that I can correct or update ownership in a process map without rebuilding it.",
      "parent_epic_id": "EPC-004",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Reassigning a step to a named actor already present in the diagram",
          "steps": "Given an existing diagram where a step is attributed to a named actor, when the analyst issues an instruction to reassign that step to a different named actor who already appears elsewhere in the diagram, then the step is displayed attributed to the new actor and the previous actor attribution is removed from that step."
        },
        {
          "title": "Scenario 2: Instruction references a step that does not exist in the diagram",
          "steps": "Given an existing diagram, when the analyst issues a reassignment instruction that names a step not present in the diagram, then the tool surfaces a message indicating the step could not be found and no change is applied."
        }
      ],
      "rationale": "Traces to the EPC-004 capability of accepting natural language instructions that reassign an actor to a step in an existing diagram and updating the visual output and structured representation accordingly."
    }
  ]
}
```

### Stories — EPC-005

```json
{
  "epic_id": "EPC-005",
  "stories": [
    {
      "story_id": "EPC-005-US-001",
      "title": "Export completed process map as a raster image",
      "narrative": "As a business analyst, I want to export my completed process map as a raster image file, so that I can embed it in documents and presentations without the recipient needing access to the diagramming tool.",
      "parent_epic_id": "EPC-005",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Exporting a completed map produces a downloadable raster image",
          "steps": "Given a completed process map displayed in the tool, when the analyst triggers a raster image export, then a file in PNG format is downloaded to the analyst's device containing a visual representation of the full diagram."
        },
        {
          "title": "Scenario 2: Exported raster image preserves all visible diagram elements",
          "steps": "Given a process map containing steps, decision points, flow arrows, and actor labels, when the map is exported as a raster image, then the downloaded file includes all of those elements at a resolution sufficient to read all text without magnification at standard document viewing sizes."
        },
        {
          "title": "Scenario 3: Export is attempted when the diagram is empty",
          "steps": "Given the tool with no process map rendered, when the analyst attempts to trigger an export, then the export action is unavailable and the analyst is informed that a process map must be present before exporting."
        }
      ],
      "rationale": "Traces directly to the EPC-005 capability of exporting a process map as a PNG raster image for embedding in design documents and team handoffs."
    },
    {
      "story_id": "EPC-005-US-002",
      "title": "Export completed process map as a scalable vector image",
      "narrative": "As a business analyst, I want to export my completed process map as a vector image file, so that I can embed it in documents and presentations at any size without the image becoming pixelated or losing legibility.",
      "parent_epic_id": "EPC-005",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Exporting a completed map produces a downloadable vector image",
          "steps": "Given a completed process map displayed in the tool, when the analyst triggers a vector image export, then a file in SVG format is downloaded to the analyst's device containing a complete representation of the diagram."
        },
        {
          "title": "Scenario 2: Exported vector image scales without quality loss",
          "steps": "Given an SVG file exported from a completed process map, when the file is rendered at a size significantly larger than its original display dimensions, then all diagram elements - including text, arrows, and shapes - remain sharp and fully legible."
        },
        {
          "title": "Scenario 3: Export of a map that was modified after initial generation",
          "steps": "Given a process map that was generated from natural language input and subsequently edited, when the analyst exports the map as a vector image, then the exported file reflects the current edited state of the diagram, not the original generated version."
        },
        {
          "title": "Scenario 4: Export is attempted when the diagram is empty",
          "steps": "Given the tool with no process map rendered, when the analyst attempts to trigger a vector export, then the export action is unavailable and the analyst is informed that a process map must be present before exporting."
        }
      ],
      "rationale": "Traces directly to the EPC-005 capability of exporting a process map as an SVG vector image for embedding in presentations and documents where resolution-independence is required."
    }
  ]
}
```

### Stories — EPC-006

```json
{
  "epic_id": "EPC-006",
  "stories": [
    {
      "story_id": "EPC-006-US-001",
      "title": "Export process map as a machine-readable structured file",
      "narrative": "As a developer, I want to export a completed process map as a structured data file, so that I can ingest the process model into my own tools and workflows without manually transcribing diagram content.",
      "parent_epic_id": "EPC-006",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Exporting a completed map produces a downloadable structured data file",
          "steps": "Given a completed process map displayed in the tool, when the developer triggers a structured data export, then a JSON file is downloaded containing a representation of the process map's current state."
        },
        {
          "title": "Scenario 2: Exported file reflects a map that was modified after initial generation",
          "steps": "Given a process map that was generated from natural language input and subsequently edited, when the developer exports the structured data file, then the file represents the current state of the diagram including all edits, not the original generated version."
        },
        {
          "title": "Scenario 3: Export is attempted when no process map has been produced",
          "steps": "Given the tool with no process map rendered, when the developer attempts to trigger a structured data export, then the export action is unavailable and the developer is informed that a process map must be present before exporting."
        }
      ],
      "rationale": "Traces to the EPC-006 capability of exporting a completed process map as a structured JSON representation that developers can consume in external tools and workflows."
    },
    {
      "story_id": "EPC-006-US-002",
      "title": "Exported data file contains all structural process elements",
      "narrative": "As a developer, I want the exported process data to include all steps, decision points, actors, and flow sequences from the diagram, so that I can reconstruct or analyse the full process model without any elements being omitted.",
      "parent_epic_id": "EPC-006",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: All step elements are present in the exported data",
          "steps": "Given a process map containing three or more named steps, when the map is exported as structured data, then the exported file contains a representation of each step that corresponds to what is shown in the diagram, with no steps omitted."
        },
        {
          "title": "Scenario 2: Decision points and their branches are represented in the exported data",
          "steps": "Given a process map containing at least one decision point with two outgoing branches, when the map is exported as structured data, then the exported file contains an entry for the decision point and separate entries for each outgoing branch with their destinations identified."
        },
        {
          "title": "Scenario 3: Actor attributions are represented in the exported data",
          "steps": "Given a process map in which at least one step has an assigned actor, when the map is exported as structured data, then each step entry in the exported file includes the actor attributed to that step where one is assigned."
        },
        {
          "title": "Scenario 4: A map with no actors assigned exports without actor fields causing an error",
          "steps": "Given a process map in which no steps have assigned actors, when the map is exported as structured data, then the export completes successfully and actor-related fields are either absent or explicitly null rather than causing a parse error."
        }
      ],
      "rationale": "Traces to the EPC-006 requirement that the exported JSON represents steps, decision points, actors, and flow sequences in a form that enables programmatic consumption by external tools."
    }
  ]
}
```

### Stories — EPC-007

```json
{
  "epic_id": "EPC-007",
  "stories": [
    {
      "story_id": "EPC-007-US-001",
      "title": "Ambiguous process description flagged before diagram is produced",
      "narrative": "As a business analyst, I want the tool to recognise when my process description could be interpreted in more than one way, so that I am not handed a diagram that reflects a guess I did not intend.",
      "parent_epic_id": "EPC-007",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Single description with multiple plausible interpretations is detected",
          "steps": "Given a process description in which a step or flow branch can be interpreted in at least two meaningfully different ways, when I submit the description for processing, then the system identifies the ambiguity and produces a detection signal rather than silently choosing one interpretation."
        },
        {
          "title": "Scenario 2: Unambiguous description is not incorrectly flagged",
          "steps": "Given a process description with clear, unambiguous steps and a single coherent flow, when I submit the description for processing, then the system does not raise an ambiguity signal and proceeds normally to produce a diagram."
        },
        {
          "title": "Scenario 3: Description with ambiguous actor assignment is detected",
          "steps": "Given a process description in which a step mentions two possible actors without specifying which is responsible, when I submit the description for processing, then the system detects the actor ambiguity and flags it specifically rather than arbitrarily assigning responsibility."
        },
        {
          "title": "Scenario 4: Ambiguity involving a decision branch with no stated outcome paths is detected",
          "steps": "Given a process description that includes a decision point but does not specify what happens on one or more outcome paths, when I submit the description for processing, then the system detects the incomplete decision branch and signals it as ambiguous."
        }
      ],
      "rationale": "Delivers the detection signal capability EPC-007 identifies as the prerequisite for appropriate response behaviour - the system must identify ambiguity before it can surface it to the user."
    },
    {
      "story_id": "EPC-007-US-002",
      "title": "Underspecified process description identified as incomplete",
      "narrative": "As a business analyst, I want the tool to recognise when my process description is too sparse to produce a meaningful map, so that I am prompted to add detail rather than receiving an empty or near-empty diagram.",
      "parent_epic_id": "EPC-007",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Description too sparse to extract meaningful structure is detected",
          "steps": "Given a process description that names a process but provides insufficient detail to identify distinct steps, decision points, or flow sequences, when I submit the description for processing, then the system produces an underspecification signal rather than attempting to render a near-empty diagram."
        },
        {
          "title": "Scenario 2: Partially underspecified description identifies only the incomplete sections",
          "steps": "Given a process description that is fully specified for some sections but missing required detail in others, when I submit the description for processing, then the system identifies only the underspecified portions and signals them distinctly, leaving the well-specified portions unaffected."
        },
        {
          "title": "Scenario 3: Adequately specified description is not flagged as underspecified",
          "steps": "Given a process description that contains enough detail to identify all steps, at least one flow sequence, and any relevant decision points, when I submit the description for processing, then the system does not raise an underspecification signal."
        }
      ],
      "rationale": "Delivers the underspecification detection variant of EPC-007's input quality assessment capability, distinguishing sparse input from ambiguous input so that the appropriate response behaviour can be triggered."
    },
    {
      "story_id": "EPC-007-US-003",
      "title": "Internally contradictory process description detected before rendering",
      "narrative": "As a business analyst, I want the tool to identify when different parts of my process description contradict each other, so that I can resolve the conflict before a logically impossible diagram is produced.",
      "parent_epic_id": "EPC-007",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Description where one statement negates another is detected",
          "steps": "Given a process description in which two statements describe the same step or transition in mutually exclusive terms, when I submit the description for processing, then the system detects the contradiction and produces a contradiction signal identifying the conflicting elements."
        },
        {
          "title": "Scenario 2: Description with circular flow that cannot be resolved is detected",
          "steps": "Given a process description that implies a flow sequence with no termination path - where following the steps would produce an unresolvable loop with no exit condition - when I submit the description for processing, then the system identifies this as a structural contradiction and flags it."
        },
        {
          "title": "Scenario 3: Description with redundant but non-contradictory repetition is not flagged as contradictory",
          "steps": "Given a process description that restates the same step in different words without changing its meaning or creating a logical conflict, when I submit the description for processing, then the system does not raise a contradiction signal and proceeds to extract a deduplicated representation."
        },
        {
          "title": "Scenario 4: Detection signal distinguishes contradiction from ambiguity",
          "steps": "Given a process description that contains a genuine logical contradiction between two stated steps, when I submit the description for processing, then the detection signal produced is categorised as a contradiction rather than an ambiguity, so that the appropriate downstream response can be selected."
        }
      ],
      "rationale": "Delivers the contradiction detection variant of EPC-007's input quality assessment capability, ensuring that logically impossible process descriptions are flagged before they proceed to rendering."
    }
  ]
}
```

### Stories — EPC-008

```json
{
  "epic_id": "EPC-008",
  "stories": [
    {
      "story_id": "EPC-008-US-001",
      "title": "Clarification requested when input cannot be resolved",
      "narrative": "As a business analyst, I want the tool to ask me a specific question when it cannot interpret part of my process description, so that I can supply the missing information rather than accepting a diagram that silently misrepresents my intent.",
      "parent_epic_id": "EPC-008",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Clarification question targets the specific unresolvable element",
          "steps": "Given a process description that contains an ambiguous or underspecified element the system cannot resolve on its own, when I submit the description for processing, then the system presents me with a clarification question that identifies the specific element it cannot interpret - rather than a generic error or a request to rewrite the whole description."
        },
        {
          "title": "Scenario 2: Providing a clarification answer allows processing to complete",
          "steps": "Given that the system has presented me with a clarification question about a specific element, when I supply an answer that resolves the ambiguity, then the system uses my answer to complete the parsing and produces a diagram that reflects my clarified intent."
        },
        {
          "title": "Scenario 3: Providing an answer that does not resolve the ambiguity prompts a follow-up",
          "steps": "Given that the system has presented me with a clarification question, when I supply an answer that is itself ambiguous or incomplete, then the system recognises the answer is insufficient and prompts me again with a more specific question rather than proceeding to produce a potentially incorrect diagram."
        },
        {
          "title": "Scenario 4: Unambiguous description does not trigger a clarification request",
          "steps": "Given a process description that is fully specified and internally consistent, when I submit the description for processing, then the system does not present any clarification question and proceeds directly to producing the diagram."
        }
      ],
      "rationale": "Delivers the clarification prompting response mode EPC-008 identifies as the user-facing behaviour when detected ambiguity cannot be resolved without additional input from the user."
    },
    {
      "story_id": "EPC-008-US-002",
      "title": "Partial map produced with unresolved sections visually marked",
      "narrative": "As a business analyst, I want to receive a partial process map with explicit visual markers on any sections the tool could not confidently interpret, so that I can see the overall shape of the process while understanding exactly where it is incomplete.",
      "parent_epic_id": "EPC-008",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Unresolved sections in a partial map are visually distinguishable from resolved sections",
          "steps": "Given a process description with some sections that are well-specified and others that are ambiguous or underspecified, when the system renders a partial map, then the unresolved sections are visually distinct from the resolved sections in a way I can identify at a glance - without needing to read surrounding text to know which parts are uncertain."
        },
        {
          "title": "Scenario 2: Each marker identifies what is unresolved about that section",
          "steps": "Given a rendered partial map containing at least one marked unresolved section, when I examine a marker, then I can determine what the system was unable to resolve about that specific section - such as which actor is responsible, or what happens on a particular outcome path - rather than receiving only a generic indication of incompleteness."
        },
        {
          "title": "Scenario 3: Resolved sections of the partial map are accurate and usable",
          "steps": "Given a rendered partial map in which some sections are marked as unresolved, when I examine the sections that carry no unresolved marker, then those sections accurately represent the process I described and are not degraded or excluded due to the presence of unresolved sections elsewhere."
        },
        {
          "title": "Scenario 4: A fully specified description produces a map with no unresolved markers",
          "steps": "Given a process description that is complete and unambiguous, when the system renders the resulting map, then no sections carry unresolved markers and the entire map is presented as a confirmed representation."
        },
        {
          "title": "Scenario 5: A fully unresolvable description does not produce a misleading diagram",
          "steps": "Given a process description so sparse or contradictory that no section can be confidently interpreted, when I submit the description for processing, then the system does not render a misleading full diagram - it either presents a near-empty map with all sections marked as unresolved or withholds the map and requests clarification instead."
        }
      ],
      "rationale": "Delivers the partial map with explicit markers response mode EPC-008 identifies as the mechanism for surfacing ambiguity visually rather than masking it with a silently incorrect diagram."
    },
    {
      "story_id": "EPC-008-US-003",
      "title": "Contradictory input surfaces the conflicting statements to the user",
      "narrative": "As a business analyst, I want the tool to show me which specific parts of my description contradict each other when a conflict is detected, so that I can resolve the conflict myself rather than receiving a diagram built on an arbitrary resolution.",
      "parent_epic_id": "EPC-008",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Both conflicting elements are identified in the response to the user",
          "steps": "Given a process description in which two stated elements are mutually contradictory, when the system detects the contradiction and presents a response to me, then both of the conflicting elements are identified in that response so I can see what is in conflict rather than being told only that a problem exists."
        },
        {
          "title": "Scenario 2: User can correct one contradicting element and receive a valid map",
          "steps": "Given that the system has surfaced two contradicting elements to me, when I update my description to remove the contradiction and resubmit, then the system processes the corrected description without raising a contradiction signal and produces a diagram."
        },
        {
          "title": "Scenario 3: Non-contradictory description does not trigger a contradiction response",
          "steps": "Given a process description that contains no logical contradictions, when I submit the description for processing, then the system does not present a contradiction response and proceeds to produce a diagram normally."
        }
      ],
      "rationale": "Delivers the user-facing contradiction response behaviour EPC-008 requires - ensuring the user receives enough information to resolve a detected conflict rather than an opaque refusal to proceed."
    }
  ]
}
```

### Stories — EPC-009

```json
{
  "epic_id": "EPC-009",
  "stories": [
    {
      "story_id": "EPC-009-US-001",
      "title": "Tool usable immediately from a browser without installing software",
      "narrative": "As a business analyst, I want to open the tool in my browser and start producing a process map without installing any software or plugin, so that I can evaluate and use the tool without any up-front setup cost.",
      "parent_epic_id": "EPC-009",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Tool is fully functional in a standard browser with no prior installation",
          "steps": "Given I am using a current-version standard browser with no additional software, plugins, or extensions installed for this tool, when I navigate to the tool's address, then I can submit a process description and receive a rendered diagram without being prompted to install anything."
        },
        {
          "title": "Scenario 2: Tool does not require a specific browser or operating system",
          "steps": "Given I am using a different current-version standard browser than the one used in the primary test, when I navigate to the tool's address, then I can submit a process description and receive a rendered diagram without any browser-specific installation step."
        },
        {
          "title": "Scenario 3: Attempting to use the tool on an unsupported browser produces an informative message rather than a silent failure",
          "steps": "Given I am using a browser version that the tool does not support, when I navigate to the tool's address, then I receive a clear message explaining the limitation and identifying a supported alternative - rather than a broken or blank experience with no explanation."
        }
      ],
      "rationale": "Delivers the no-install access requirement EPC-009 identifies as a stated differentiator over conventional tools - a user must be able to go from zero to a rendered diagram in a single browser session with no preceding setup."
    },
    {
      "story_id": "EPC-009-US-002",
      "title": "Process map produced without creating or logging into an account",
      "narrative": "As a business analyst, I want to produce and view a process map without creating an account or logging in, so that I can evaluate the tool's value before committing to any registration step.",
      "parent_epic_id": "EPC-009",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Full map generation available without account creation",
          "steps": "Given I have not created an account or provided any credentials, when I navigate to the tool and submit a process description, then the system processes my input and renders a complete process map without redirecting me to a registration or sign-in step."
        },
        {
          "title": "Scenario 2: Account creation is offered but not required to proceed",
          "steps": "Given I have just received a rendered process map without signing in, when the tool presents an option to save or create an account, then I can dismiss or ignore that option and continue using the tool for the current session without the session being blocked or degraded."
        },
        {
          "title": "Scenario 3: Map functionality is not reduced for unauthenticated users within session scope",
          "steps": "Given I am using the tool without an account during a single session, when I edit my process map and export it, then I have access to the same generation, editing, and export capabilities as an account holder - except for capabilities that are explicitly described as account-only features."
        },
        {
          "title": "Scenario 4: Unauthenticated session does not require personal information to begin",
          "steps": "Given I arrive at the tool for the first time with no account, when I begin a session, then the tool does not require me to provide an email address, name, or any other personal information before I can submit a process description."
        }
      ],
      "rationale": "Delivers the no-mandatory-account access requirement EPC-009 identifies as central to frictionless evaluation - a user must be able to reach full map-generation value before any account or registration gate is encountered."
    }
  ]
}
```

### Stories — EPC-010

```json
{
  "epic_id": "EPC-010",
  "stories": [
    {
      "story_id": "EPC-010-US-001",
      "title": "Receive diagram without perceiving delay after submitting input",
      "narrative": "As a business analyst, I want to receive a rendered process map promptly after submitting my description, so that the tool feels responsive and does not interrupt my thinking with unexplained waiting.",
      "parent_epic_id": "EPC-010",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Diagram produced within an acceptable duration for a typical process description",
          "steps": "Given a user has entered a well-formed process description of moderate length (five to ten steps), when the user submits the description, then a completed process map is displayed within 10 seconds."
        },
        {
          "title": "Scenario 2: No unexplained wait when processing takes longer than typical",
          "steps": "Given a user has submitted a complex or lengthy process description that requires more processing time, when the system is still processing, then the user sees a visible indication that work is in progress rather than a blank or unresponsive interface."
        },
        {
          "title": "Scenario 3: Output accuracy is not degraded in exchange for faster response",
          "steps": "Given the system is processing a process description that contains distinct steps, decision points, and actor assignments, when the diagram is returned, then the diagram accurately represents all extracted elements and does not omit or misrepresent content in order to respond faster."
        },
        {
          "title": "Scenario 4: Empty or trivially short input does not cause a prolonged wait",
          "steps": "Given a user submits a description of one or two words that cannot produce a meaningful diagram, when the system evaluates the input, then a response is returned immediately indicating the input is insufficient, without the user waiting as if a full parsing cycle were running."
        }
      ],
      "rationale": "Traces directly to the epic's requirement that the processing pipeline be experienced as responsive, with the user receiving results without unnecessary delay."
    },
    {
      "story_id": "EPC-010-US-002",
      "title": "See visible progress feedback during processing",
      "narrative": "As a business analyst, I want to see clear feedback that my input is being processed, so that I know the tool is working and can judge whether to wait or investigate a problem.",
      "parent_epic_id": "EPC-010",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Feedback appears immediately after input is submitted",
          "steps": "Given a user has submitted a process description, when the submission is received by the tool, then a visible indicator of activity appears before any result is returned."
        },
        {
          "title": "Scenario 2: Feedback is dismissed when the result is ready",
          "steps": "Given the processing indicator is visible, when the diagram has been fully prepared, then the indicator is replaced by the completed diagram without the user taking any additional action."
        },
        {
          "title": "Scenario 3: Feedback remains visible if processing takes longer than a short threshold",
          "steps": "Given processing has been underway for more than a few seconds, when the result has not yet been returned, then the activity indicator remains visible and does not disappear prematurely."
        },
        {
          "title": "Scenario 4: No feedback shown when no submission has been made",
          "steps": "Given the user has not yet submitted any input, when the tool is in its initial idle state, then no processing indicator is visible."
        }
      ],
      "rationale": "Traces to the epic's explicit requirement that where processing takes time the tool provides visible progress feedback rather than leaving the user with a blank or frozen interface."
    }
  ]
}
```

### Stories — EPC-011

```json
{
  "epic_id": "EPC-011",
  "stories": [
    {
      "story_id": "EPC-011-US-001",
      "title": "Access published schema documentation before writing integration code",
      "narrative": "As a developer integrating the JSON export into a downstream tool, I want to read a clear, published specification of the export schema before writing any integration code, so that I can design my integration against a known contract rather than reverse-engineering the output.",
      "parent_epic_id": "EPC-011",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Schema documentation is discoverable from the export capability",
          "steps": "Given a developer has obtained a JSON export from the tool, when the developer looks for schema documentation associated with that export, then they can find a published specification that describes each field, its data type, whether it is required or optional, and the values it may contain."
        },
        {
          "title": "Scenario 2: Schema documentation covers all four structural elements",
          "steps": "Given a developer reads the schema specification, when they search it for coverage of steps, decision points, actors, and flow sequences, then all four element types are defined with sufficient detail to write a consuming parser without referencing any other source."
        },
        {
          "title": "Scenario 3: Schema documentation is not available before the export capability is available",
          "steps": "Given the export feature has not yet been released, when a developer attempts to access schema documentation, then no schema documentation is published that could create a false expectation of the contract."
        }
      ],
      "rationale": "Traces to the epic's requirement that external tools can consume the JSON export reliably without reverse-engineering the structure, which depends on schema documentation being available and discoverable."
    },
    {
      "story_id": "EPC-011-US-002",
      "title": "Parse exported JSON without writing custom field-detection logic",
      "narrative": "As a developer integrating the JSON export into a downstream tool, I want the exported file to conform consistently to the documented schema, so that my integration can rely on predictable field names and structures without defensive parsing for unknown layouts.",
      "parent_epic_id": "EPC-011",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: Export produced from a simple linear process conforms to the schema",
          "steps": "Given a process map with a single sequence of steps and no decision points has been exported, when the exported file is validated against the published schema, then all required fields are present, no undocumented fields appear, and all values conform to the specified types."
        },
        {
          "title": "Scenario 2: Export produced from a process with decision branches conforms to the schema",
          "steps": "Given a process map containing at least one decision point with two outgoing branches has been exported, when the exported file is validated against the published schema, then decision points and their associated flow sequences are represented using the structure defined in the schema, not a different or ad-hoc structure."
        },
        {
          "title": "Scenario 3: Export produced from a process with multiple actors conforms to the schema",
          "steps": "Given a process map with steps assigned to more than one distinct actor has been exported, when the exported file is validated against the published schema, then actor assignments are represented consistently for every step, matching the actor field definition in the schema."
        },
        {
          "title": "Scenario 4: Exporting a diagram that was subsequently edited still produces a conformant file",
          "steps": "Given a process map was generated from a description, then modified by adding a step, when the modified diagram is exported, then the exported file conforms to the same schema as an unmodified export."
        },
        {
          "title": "Scenario 5: An empty or minimal process does not produce a structurally invalid export",
          "steps": "Given a process map containing only a single step and no decision points or actors has been exported, when the exported file is evaluated, then it is valid against the schema and contains no null values in fields that the schema defines as required."
        }
      ],
      "rationale": "Traces to the epic's requirement that the schema be stable and sufficient for external tools to consume the output without bespoke parsing, which requires consistent field structure across varied process topologies."
    },
    {
      "story_id": "EPC-011-US-003",
      "title": "Rely on export format remaining consistent across tool updates",
      "narrative": "As a developer who has built an integration against the JSON export, I want the export format to remain consistent over time, so that my integration continues to work as the tool is updated without my needing to monitor for silent changes.",
      "parent_epic_id": "EPC-011",
      "acceptance_criteria": [
        {
          "title": "Scenario 1: An export produced after a non-breaking tool update works with an existing integration",
          "steps": "Given a developer's integration was written against the published schema, when the tool is updated in a way that does not alter the export structure, then an export produced after the update is valid against the same published schema the developer originally used."
        },
        {
          "title": "Scenario 2: A format change that would break existing integrations is communicated before it takes effect",
          "steps": "Given a change is to be made to the export structure that alters or removes elements that existing integrations depend on, when the change is introduced, then the change is documented and communicated in a way that gives existing integrations notice before they would encounter a failure."
        },
        {
          "title": "Scenario 3: An additive change does not break an integration built on the prior structure",
          "steps": "Given optional new data has been added to the export structure and a developer's integration was built against the prior structure, when the integration processes a newer export containing the additional data, then the integration does not fail due to the presence of the new data."
        }
      ],
      "rationale": "Traces to the epic's requirement for a stable schema \u2014 stability is only verifiable if the export structure remains consistent for existing integrations and any changes that would break them are communicated rather than applied silently."
    }
  ]
}
```

## Critique

### Critique verdict

**SATISFIED** — no issues raised.

## Governance

**PASS** — all traceability rules satisfied.
