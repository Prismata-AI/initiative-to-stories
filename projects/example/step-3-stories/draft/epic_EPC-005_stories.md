# Stories - EPC-005

_2 stories._

---

## EPC-005-US-001 - Export completed process map as a raster image

As a business analyst, I want to export my completed process map as a raster image file, so that I can embed it in documents and presentations without the recipient needing access to the diagramming tool.

**Acceptance criteria:**

**Scenario 1: Exporting a completed map produces a downloadable raster image**
Given a completed process map displayed in the tool, when the analyst triggers a raster image export, then a file in PNG format is downloaded to the analyst's device containing a visual representation of the full diagram.

**Scenario 2: Exported raster image preserves all visible diagram elements**
Given a process map containing steps, decision points, flow arrows, and actor labels, when the map is exported as a raster image, then the downloaded file includes all of those elements at a resolution sufficient to read all text without magnification at standard document viewing sizes.

**Scenario 3: Export is attempted when the diagram is empty**
Given the tool with no process map rendered, when the analyst attempts to trigger an export, then the export action is unavailable and the analyst is informed that a process map must be present before exporting.

**Rationale:** Traces directly to the EPC-005 capability of exporting a process map as a PNG raster image for embedding in design documents and team handoffs.

---

## EPC-005-US-002 - Export completed process map as a scalable vector image

As a business analyst, I want to export my completed process map as a vector image file, so that I can embed it in documents and presentations at any size without the image becoming pixelated or losing legibility.

**Acceptance criteria:**

**Scenario 1: Exporting a completed map produces a downloadable vector image**
Given a completed process map displayed in the tool, when the analyst triggers a vector image export, then a file in SVG format is downloaded to the analyst's device containing a complete representation of the diagram.

**Scenario 2: Exported vector image scales without quality loss**
Given an SVG file exported from a completed process map, when the file is rendered at a size significantly larger than its original display dimensions, then all diagram elements - including text, arrows, and shapes - remain sharp and fully legible.

**Scenario 3: Export of a map that was modified after initial generation**
Given a process map that was generated from natural language input and subsequently edited, when the analyst exports the map as a vector image, then the exported file reflects the current edited state of the diagram, not the original generated version.

**Scenario 4: Export is attempted when the diagram is empty**
Given the tool with no process map rendered, when the analyst attempts to trigger a vector export, then the export action is unavailable and the analyst is informed that a process map must be present before exporting.

**Rationale:** Traces directly to the EPC-005 capability of exporting a process map as an SVG vector image for embedding in presentations and documents where resolution-independence is required.

---
