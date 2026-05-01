# Initiative Brief: Natural Language Process Mapper

**Status:** Draft — single input, no user research or business case on file  
**Source material:** `process-map-tool-concept.md` (concept note, single author)

---

## Problem

Most people who document processes think in words, not diagrams. They can describe a process fluently but stall when asked to represent it visually. Existing diagramming tools — Lucidchart, Miro, Visio and equivalents — are strong renderers but put the full layout burden on the user. The primary interaction model is drag-and-drop, which means time is spent arranging boxes rather than thinking about the process itself.

A secondary but related friction: when a process changes, updating the diagram is nearly as costly as redrawing it from scratch. There is no path from "I changed step 3" to an updated diagram other than manual re-editing.

The concept note does not cite user research, survey data, or usage metrics. The problem is qualitatively well-articulated and credible, but it is asserted rather than evidenced. This is a known gap.

**Who is affected:** Business analysts, process improvement leads, and operations managers who document or redesign processes as part of their role. A secondary audience — developers and technical writers who receive process documentation — is identified, primarily around the structured export need.

**Cost of inaction:** Not quantified in the inputs. The implicit cost is time lost to diagramming overhead and documentation that is either never produced (too slow) or quickly goes stale (too costly to update).

---

## Goals

1. A process documenter can produce a usable, publication-quality process map from a plain English description in under 10 seconds.
2. Produced maps are editable through both direct visual manipulation and subsequent natural language instructions, without requiring the user to start over.
3. Maps can be exported in formats suitable for embedding in design documents (PNG, SVG) and for downstream tool consumption (structured JSON).
4. The tool is accessible without installation or account creation — time-to-value is immediate.

---

## Desirability / Viability / Feasibility

| Dimension | Rating | Basis |
|-----------|--------|-------|
| Desirability | MEDIUM | Problem is real and well-articulated for a clearly defined user group. No user research, interviews, or usage data cited. Asserted, not validated. |
| Viability | UNKNOWN | No pricing model decided. Two options mentioned (freemium with export gating; free with usage cap) but not evaluated. No market sizing, cost-of-serving analysis, or revenue model on file. |
| Feasibility | MEDIUM | NL-to-structure parsing via LLM is explicitly noted as now viable. Diagram rendering from structured data is described as a solved problem. Key risks: handling ambiguous or contradictory natural language input; LLM inference latency meeting the <10 second target; backend architecture and privacy implications. Collaboration features deferred to Phase 2. |

---

## High-Level Requirements

### HLR-001: Natural Language Input to Structured Process Representation

The system must accept a free-form natural language description of a process and extract a structured representation comprising steps, decision points, roles or actors, and flow sequences.

**Rationale:** This is the core differentiating capability — the natural language-to-structure layer that existing tools do not provide. All downstream rendering and editing depends on this structured representation existing.

**Impact if omitted:** The product does not exist in any differentiated form. Without this capability it is indistinguishable from a conventional diagram editor.

---

### HLR-002: Structured Process Rendering as Visual Diagram

The system must render the structured process representation as a visual process map in the browser, using standard process notation (swimlanes, decision diamonds, flow arrows).

**Rationale:** Addresses the primary user goal of producing a usable, publication-quality diagram without manual layout work.

**Impact if omitted:** The tool produces structured data with no human-readable output. The core user value — a diagram you can use — is not delivered.

---

### HLR-003: Direct Visual Diagram Editing

The system must allow users to edit the rendered diagram through direct manipulation — reordering steps, renaming nodes, adding and removing steps — with the underlying structured representation updated to reflect each change.

**Rationale:** Addresses the maintenance friction identified in the problem: processes change, and the tool must support updating a map without starting over.

**Impact if omitted:** The tool is useful for initial generation only. Iterative refinement and process updates revert to the manual overhead of conventional tools.

---

### HLR-004: Natural Language Diagram Editing

The system must accept subsequent natural language instructions that modify an existing diagram (for example: "add an approval step between step 3 and step 4 where the manager signs off") and update both the visual diagram and the underlying structured representation accordingly.

**Rationale:** Preserves the natural language interaction model as the primary editing interface, consistent with the tool's AI-first positioning and its design for verbal thinkers.

**Impact if omitted:** Users who prefer natural language editing are forced to switch to visual manipulation for changes, undermining the core interaction model and differentiator.

---

### HLR-005: Export to PNG, SVG, and Structured JSON

The system must support export of the completed process map in at least three formats: PNG (raster image), SVG (vector image), and a structured JSON representation of the process data.

**Rationale:** Addresses both primary user needs (embeddable diagrams for documents and handoffs) and secondary user needs (developers and technical writers requiring machine-readable process data).

**Impact if omitted:** Maps exist only within the tool. The design document and dev team use cases — explicitly cited as the standard of "actually useful" output — are not met.

---

### HLR-006: Ambiguous Input Handling Without Misleading Output

The system must detect when a natural language description is ambiguous, underspecified, or contradictory, and respond by either prompting the user to clarify or rendering a partial map with explicit markers indicating where the process is unresolved — rather than silently producing a map that misrepresents the described process.

**Rationale:** Ambiguity in NL input is identified in the concept as a known risk. A silently wrong process map is worse than no map — it can be handed to a dev team or included in documentation without the error being apparent.

**Impact if omitted:** The tool produces misleading diagrams from poorly-specified input. Trust in the output degrades and the "publication-quality" claim cannot be sustained.

---

### HLR-007: Browser-Native, No-Install Access

The system shall be accessible in a standard browser without software installation or mandatory account creation. Fast time-to-first-map is a quality target — the tool should feel responsive — but output quality and correctness take precedence over raw latency.

**Rationale:** Zero-install access is an explicitly stated differentiator over conventional tools; immediate time-to-value is central to casual evaluation and word-of-mouth adoption.

**Impact if omitted:** The friction advantage over existing tools is removed. Casual evaluation and word-of-mouth adoption — dependent on frictionless access — are significantly impaired.

---

### HLR-008: NL Parsing and Rendering Latency as a Quality Target

The system shall treat response latency as a quality characteristic to optimise for, not a hard constraint. Backend and infrastructure choices should favour fast NL parsing and rendering, with the understanding that output accuracy and completeness take precedence when they are in tension with speed.

**Rationale:** Fast results are part of the intended user experience, but the concept note is explicit that quality matters more than speed — a 10-second figure is aspirational, not a ceiling the product should compromise correctness to meet.

**Impact if omitted:** Without any latency guidance, backend architecture decisions may not treat responsiveness as a quality dimension at all, producing a tool that is both slow and accurate when a reasonable balance is achievable.

---

### HLR-009: Structured JSON Export Schema Suitable for Downstream Consumption

The system must produce a JSON export that follows a documented, stable schema representing the process structure — steps, decision points, actors, and flow sequences — in a form that can be consumed by external tools without bespoke parsing.

**Rationale:** The secondary user audience (developers, technical writers) requires machine-readable output. An undocumented or unstable schema limits interoperability and undermines the stated use case.

**Impact if omitted:** The JSON export becomes a data dump rather than an integration point. Downstream tool consumption — the explicit secondary user need — is not reliably achievable.

---

## Open Questions

These are specific, answerable questions that a stakeholder or product owner could resolve:

1. **Process notation standard:** BPMN or a simplified swimlane format? The concept identifies this as open. The decision affects which user segments the tool credibly serves (formal process practitioners vs. casual business users) and has implications for the NL parsing rules.

2. **Ambiguous input handling UX:** When the system detects ambiguity, what is the interaction model? Inline prompts within the map? A clarification dialogue? A confidence indicator on nodes? This determines a significant portion of the editing and parsing behaviour.

3. **Session persistence:** Where are maps stored between sessions? Does the tool have any persistence without an account, or are unsaved maps lost on tab close? Not addressed in the concept note.

4. **Edit conflict model:** If a user edits the diagram visually and then issues a natural language instruction that touches the same area, which takes precedence? The interaction contract between the two editing modes is not defined.

5. **Pricing and account model:** The concept presents two options (freemium with export gating; free with usage cap) but does not evaluate them. This has direct implications for backend cost exposure and the no-account-required differentiator.

6. **Privacy and data retention:** Because NL processing requires a backend, user-submitted process descriptions leave the browser. What is the data retention and privacy posture? Relevant for enterprise users documenting sensitive operational processes.

7. **Collaboration scope:** The concept flags real-time multi-user editing as a Phase 2 concern. Is that a firm deferral, or is the data model being designed to accommodate it? The answer affects the initial schema and persistence architecture.
