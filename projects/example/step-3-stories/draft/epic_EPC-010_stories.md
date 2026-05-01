# Stories - EPC-010

_2 stories._

---

## EPC-010-US-001 - Receive diagram without perceiving delay after submitting input

As a business analyst, I want to receive a rendered process map promptly after submitting my description, so that the tool feels responsive and does not interrupt my thinking with unexplained waiting.

**Acceptance criteria:**

**Scenario 1: Diagram produced within an acceptable duration for a typical process description**
Given a user has entered a well-formed process description of moderate length (five to ten steps), when the user submits the description, then a completed process map is displayed within 10 seconds.

**Scenario 2: No unexplained wait when processing takes longer than typical**
Given a user has submitted a complex or lengthy process description that requires more processing time, when the system is still processing, then the user sees a visible indication that work is in progress rather than a blank or unresponsive interface.

**Scenario 3: Output accuracy is not degraded in exchange for faster response**
Given the system is processing a process description that contains distinct steps, decision points, and actor assignments, when the diagram is returned, then the diagram accurately represents all extracted elements and does not omit or misrepresent content in order to respond faster.

**Scenario 4: Empty or trivially short input does not cause a prolonged wait**
Given a user submits a description of one or two words that cannot produce a meaningful diagram, when the system evaluates the input, then a response is returned immediately indicating the input is insufficient, without the user waiting as if a full parsing cycle were running.

**Rationale:** Traces directly to the epic's requirement that the processing pipeline be experienced as responsive, with the user receiving results without unnecessary delay.

---

## EPC-010-US-002 - See visible progress feedback during processing

As a business analyst, I want to see clear feedback that my input is being processed, so that I know the tool is working and can judge whether to wait or investigate a problem.

**Acceptance criteria:**

**Scenario 1: Feedback appears immediately after input is submitted**
Given a user has submitted a process description, when the submission is received by the tool, then a visible indicator of activity appears before any result is returned.

**Scenario 2: Feedback is dismissed when the result is ready**
Given the processing indicator is visible, when the diagram has been fully prepared, then the indicator is replaced by the completed diagram without the user taking any additional action.

**Scenario 3: Feedback remains visible if processing takes longer than a short threshold**
Given processing has been underway for more than a few seconds, when the result has not yet been returned, then the activity indicator remains visible and does not disappear prematurely.

**Scenario 4: No feedback shown when no submission has been made**
Given the user has not yet submitted any input, when the tool is in its initial idle state, then no processing indicator is visible.

**Rationale:** Traces to the epic's explicit requirement that where processing takes time the tool provides visible progress feedback rather than leaving the user with a blank or frozen interface.

---
