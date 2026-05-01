# Stories - EPC-011

_3 stories._

---

## EPC-011-US-001 - Access published schema documentation before writing integration code

As a developer integrating the JSON export into a downstream tool, I want to read a clear, published specification of the export schema before writing any integration code, so that I can design my integration against a known contract rather than reverse-engineering the output.

**Acceptance criteria:**

**Scenario 1: Schema documentation is discoverable from the export capability**
Given a developer has obtained a JSON export from the tool, when the developer looks for schema documentation associated with that export, then they can find a published specification that describes each field, its data type, whether it is required or optional, and the values it may contain.

**Scenario 2: Schema documentation covers all four structural elements**
Given a developer reads the schema specification, when they search it for coverage of steps, decision points, actors, and flow sequences, then all four element types are defined with sufficient detail to write a consuming parser without referencing any other source.

**Scenario 3: Schema documentation is not available before the export capability is available**
Given the export feature has not yet been released, when a developer attempts to access schema documentation, then no schema documentation is published that could create a false expectation of the contract.

**Rationale:** Traces to the epic's requirement that external tools can consume the JSON export reliably without reverse-engineering the structure, which depends on schema documentation being available and discoverable.

---

## EPC-011-US-002 - Parse exported JSON without writing custom field-detection logic

As a developer integrating the JSON export into a downstream tool, I want the exported file to conform consistently to the documented schema, so that my integration can rely on predictable field names and structures without defensive parsing for unknown layouts.

**Acceptance criteria:**

**Scenario 1: Export produced from a simple linear process conforms to the schema**
Given a process map with a single sequence of steps and no decision points has been exported, when the exported file is validated against the published schema, then all required fields are present, no undocumented fields appear, and all values conform to the specified types.

**Scenario 2: Export produced from a process with decision branches conforms to the schema**
Given a process map containing at least one decision point with two outgoing branches has been exported, when the exported file is validated against the published schema, then decision points and their associated flow sequences are represented using the structure defined in the schema, not a different or ad-hoc structure.

**Scenario 3: Export produced from a process with multiple actors conforms to the schema**
Given a process map with steps assigned to more than one distinct actor has been exported, when the exported file is validated against the published schema, then actor assignments are represented consistently for every step, matching the actor field definition in the schema.

**Scenario 4: Exporting a diagram that was subsequently edited still produces a conformant file**
Given a process map was generated from a description, then modified by adding a step, when the modified diagram is exported, then the exported file conforms to the same schema as an unmodified export.

**Scenario 5: An empty or minimal process does not produce a structurally invalid export**
Given a process map containing only a single step and no decision points or actors has been exported, when the exported file is evaluated, then it is valid against the schema and contains no null values in fields that the schema defines as required.

**Rationale:** Traces to the epic's requirement that the schema be stable and sufficient for external tools to consume the output without bespoke parsing, which requires consistent field structure across varied process topologies.

---

## EPC-011-US-003 - Rely on export format remaining consistent across tool updates

As a developer who has built an integration against the JSON export, I want the export format to remain consistent over time, so that my integration continues to work as the tool is updated without my needing to monitor for silent changes.

**Acceptance criteria:**

**Scenario 1: An export produced after a non-breaking tool update works with an existing integration**
Given a developer's integration was written against the published schema, when the tool is updated in a way that does not alter the export structure, then an export produced after the update is valid against the same published schema the developer originally used.

**Scenario 2: A format change that would break existing integrations is communicated before it takes effect**
Given a change is to be made to the export structure that alters or removes elements that existing integrations depend on, when the change is introduced, then the change is documented and communicated in a way that gives existing integrations notice before they would encounter a failure.

**Scenario 3: An additive change does not break an integration built on the prior structure**
Given optional new data has been added to the export structure and a developer's integration was built against the prior structure, when the integration processes a newer export containing the additional data, then the integration does not fail due to the presence of the new data.

**Rationale:** Traces to the epic's requirement for a stable schema — stability is only verifiable if the export structure remains consistent for existing integrations and any changes that would break them are communicated rather than applied silently.

---
