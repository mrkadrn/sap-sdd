---
name: write-technical-spec
description: Convert an approved ALM story and authorized SAP source into a developer-reviewable technical specification with implementation steps and proposed human tests.
---

# Write technical specification

1. Establish the ALM identifier, approved requirements, and reviewed revision.
   If approval is unknown, identify that blocker rather than claiming approval.
2. Read developer-supplied original/ZIS identities and the authorized source.
   Establish system/client, local package, target operation, source locations,
   dependencies, and a reliable source baseline where available.
3. Trace the relevant processing through its downstream outcome. An
   intermediate assignment alone does not establish persisted behavior.
   Reuse existing helpers and data before adding lookups or abstractions.
4. Use [the specification template](../../../templates/technical-spec-template.md).
   Write `specs/for-implementation/<story-id>.md` when generation is requested.
   Do not introduce a draft status, separate plan document, or draft folder.
5. Specify exact changes, preserved behavior, errors, and object boundaries.
   State whether ZIS already exists, or whether creation/copy is explicitly
   included. Treat `$TMP` as an SAP package, not a local directory.
6. Map each change to an ALM criterion or justified technical necessity.
   Keep developer-proposed regression criteria separate from BA-approved ones.
7. Propose human tests covering each criterion, relevant boundaries, errors,
   recurrence/processing paths where applicable, and preserved behavior.
   Expected results must be defined, not guessed.
8. List only genuine blockers and open decisions. Resolve routine technical
   details from source/standards without repeatedly consulting the developer.
9. For changes to an implemented story, inspect the existing specification
   and increment its revision. Move it back to for-implementation as part of
   an authorized revision; do not overwrite a conflicting pending revision.
   Preserve earlier implementation records and test-workbook references.
10. Return the path and blockers for developer alignment review.

The implementation request, not the file's location, authorizes implementation.
Do not copy, edit, save, or activate SAP objects in this skill.
