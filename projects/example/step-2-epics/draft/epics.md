# Epics

_11 epics across 9 HLRs._

---

## EPC-001 - Natural language extraction of structured process elements

*Traces to: HLR-001 | Persona: Business analyst*

This epic delivers the capability to accept a free-form natural language description of a process and extract from it a structured representation of steps, decision points, roles or actors, and flow sequences. The extracted representation must be complete and well-formed enough to drive rendering and editing without further user intervention.

**Why:** Delivers the NL-to-structure parsing layer that HLR-001 identifies as the core differentiating capability upon which all rendering and editing depends.

---

## EPC-002 - In-browser visual process map rendering from structured data

*Traces to: HLR-002 | Persona: Business analyst*

This epic delivers the capability to render a structured process representation as a visual process map in the browser, using standard process notation including swimlanes, decision diamonds, and flow arrows. The rendered output must be publication-quality and require no manual layout work from the user.

**Why:** Delivers the visual output layer HLR-002 requires - transforming structured data into a diagram the user can hand to a team or include in a document without additional formatting effort.

---

## EPC-003 - Direct visual editing of diagrams with representation sync

*Traces to: HLR-003 | Persona: Business analyst*

This epic delivers the capability for users to edit a rendered process diagram through direct manipulation - reordering steps, renaming nodes, adding and removing steps - with every change propagated back into the underlying structured representation so the two remain in sync.

**Why:** Delivers the direct manipulation editing capability HLR-003 requires to address post-generation maintenance, ensuring visual changes are reflected in the data model rather than creating divergence.

---

## EPC-004 - Natural language modification of existing process diagrams

*Traces to: HLR-004 | Persona: Business analyst*

This epic delivers the capability to accept natural language instructions against an existing diagram - such as inserting a step, reassigning an actor, or removing a branch - and apply those modifications to both the visual diagram and the underlying structured representation. This operates on an already-rendered diagram rather than producing one from scratch.

**Why:** Delivers the conversational editing mode HLR-004 requires to preserve the NL-first interaction model during process updates, not just initial creation.

---

## EPC-005 - Image format export for document and presentation embedding

*Traces to: HLR-005 | Persona: Business analyst*

This epic delivers the capability to export a completed process map as a PNG raster image and as an SVG vector image, producing files suitable for embedding in design documents, presentations, and team handoffs.

**Why:** Delivers the image export formats HLR-005 identifies as meeting the primary user need - embeddable, shareable diagrams that exist outside the tool.

---

## EPC-006 - Structured JSON export of process data for downstream consumption

*Traces to: HLR-005 | Persona: Developer*

This epic delivers the capability to export a completed process map as a structured JSON representation of the process data, enabling developers and technical writers to consume the process model in external tools and workflows.

**Why:** Delivers the machine-readable export format HLR-005 identifies as meeting the secondary user need - process data that can be consumed programmatically by external tools.

---

## EPC-007 - Detection of ambiguous and contradictory natural language input

*Traces to: HLR-006 | Persona: Business analyst*

This epic delivers the capability to identify when a natural language process description is ambiguous, underspecified, or internally contradictory during parsing - producing a detection signal that can drive appropriate response behaviour rather than proceeding silently to a misleading diagram.

**Why:** Delivers the input quality assessment capability HLR-006 identifies as the prerequisite for honest output - the system cannot respond appropriately to bad input if it cannot detect it.

---

## EPC-008 - Clarification prompting and partial map marking for unresolved sections

*Traces to: HLR-006 | Persona: Business analyst*

This epic delivers the user-facing response capability when ambiguous or contradictory input is detected - either prompting the user for clarification before proceeding, or rendering a partial map with explicit visual markers on unresolved sections, ensuring the user understands where the process representation is incomplete rather than receiving a silently wrong diagram.

**Why:** Delivers the response behaviour HLR-006 requires to prevent misleading output - the interaction model that surfaces ambiguity to the user rather than masking it.

---

## EPC-009 - Browser-native access without installation or mandatory account

*Traces to: HLR-007 | Persona: Business analyst*

This epic delivers a product access model that requires no software installation and no mandatory account creation, allowing a user to arrive via browser and produce a process map without any preceding friction or sign-up step.

**Why:** Delivers the zero-friction access model HLR-007 identifies as a stated differentiator over conventional tools and the enabler of casual evaluation and word-of-mouth adoption.

---

## EPC-010 - Low-latency NL parsing and diagram generation experience

*Traces to: HLR-008 | Persona: Business analyst*

This epic delivers a processing pipeline that users experience as responsive — NL input is parsed and diagrams are rendered without unnecessary delay, and where processing takes time the tool provides visible progress feedback rather than leaving the user with a blank or frozen interface. Output accuracy takes precedence over speed, but the system avoids latency that is not warranted by the quality of the result.

**Why:** HLR-008 requires response latency to be treated as a quality characteristic in backend and infrastructure design — this epic represents the user-observable result: a tool that processes input and returns results promptly, with honest feedback when processing takes longer.

---

## EPC-011 - Documented stable schema for JSON export interoperability

*Traces to: HLR-009 | Persona: Developer*

This epic delivers a documented, stable JSON schema for process exports - covering steps, decision points, actors, and flow sequences - with sufficient specification that external tools can consume the output reliably without bespoke parsing or reverse-engineering of the structure.

**Why:** Delivers the schema contract HLR-009 requires to make the JSON export an integration point rather than an opaque data dump - the stability and documentation that enable the downstream tool consumption use case.

---
