# Process Map Tool — Concept Note

## The idea

A browser-based tool that lets you describe a process in plain English and have it generate a visual process map. You type something like "a customer submits a support ticket, it gets triaged by the helpdesk team, escalated to Tier 2 if unresolved after 4 hours, then closed and a satisfaction survey is sent" — and the tool produces a structured, editable process map from that description.

The output should be something you can actually use — not a rough sketch — something you could drop into a design document or hand to a dev team.

## The problem it solves

Drawing process maps is tedious. The tools that exist are good at rendering but they put all the layout burden on the user. You spend more time dragging boxes than thinking about the process. And when the process changes, updating the diagram is almost as much work as starting fresh.

The real constraint is that most people who need to document processes are not visual thinkers — they think in words. They can describe a process fluently but stall when asked to represent it as a diagram. The tool should meet them where they are.

## How it should work (rough concept)

1. User types or pastes a natural language description of the process — any length, any format
2. The tool parses the description and identifies: steps, decision points, roles/actors, and flow sequences
3. A process map is rendered in the browser — standard notation (swimlanes, decision diamonds, flow arrows)
4. User can edit the map directly — drag to reorder, rename nodes, add/remove steps — and the underlying structured representation updates accordingly
5. User can also edit by typing — "add an approval step between step 3 and step 4 where the manager signs off" — and the map updates
6. Export to common formats: PNG, SVG, and a structured JSON representation that could be consumed by other tools

## Who uses this

Primary user: business analysts, process improvement leads, operations managers — anyone who needs to document or redesign a process as part of their work. These are people who understand process deeply but find diagramming tools slow and frustrating.

Secondary user: developers and technical writers who receive process documentation and need to understand or implement it. The structured JSON export is specifically for this audience.

## What makes it different from existing tools

Existing tools are diagram editors with optional AI features bolted on. This is an AI-first tool where the diagram is the output, not the starting point. The natural language interface is the primary interaction model, not a shortcut.

Also: browser-native. No install, no account required to try it. Paste a process description and see a map in under 10 seconds.

## Open questions / things to figure out

- What process notation to use by default? BPMN is standard but heavy for casual users. A simplified swimlane format might have broader appeal but alienates formal process practitioners.
- How to handle ambiguous descriptions — where the process is underspecified or contradictory — without breaking the rendering or producing a misleading map.
- Collaboration features: is real-time multi-user editing in scope? Feels like a Phase 2 concern.
- Where does the AI processing happen? Client-side is not realistic for LLM inference, so there's a backend requirement. That changes the privacy and latency considerations.
- Pricing model: freemium with export locked behind account, or fully free with a usage cap?

## Why now

LLMs are good enough to parse process descriptions reliably. The rendering piece (structured diagram from structured data) is a solved problem. The missing piece has always been the natural language-to-structure layer — and that's now viable. This is a tool that could have been imagined three years ago but couldn't have been built well until now.
