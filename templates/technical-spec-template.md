# <story-id> - <title>

## 1. Traceability

- Specification revision: <number>
- ALM story/reference: <identifier/link>
- ALM revision reviewed: <revision/timestamp>
- Approved requirements evidence: <reference>
- Developer: <name>

No draft status is used. Developer alignment review precedes the request to
implement this specification.

## 2. Business requirements and acceptance criteria

<Preserve approved behavior and ALM criterion IDs. Separate any proposed
regression criteria from BA-approved business criteria.>

## 3. Target environment and object scope

| Item | Confirmed value |
|---|---|
| SAP system/client | <exact target> |
| Original objects, reference only | <names or Not applicable> |
| ZIS targets | <exact names> |
| Operation | <update prepared ZIS / explicitly create new / explicitly copy> |
| Package | <$TMP or explicitly approved local package> |
| Source location/editor connection | <verified location/connection> |
| Source baseline | <version/hash/timestamp or stated limitation> |
| Dependencies and object boundaries | <relevant dependencies> |

## 4. Current behavior and evidence

<Relevant flow, downstream behavior, source locations, and evidence.
Label direct findings versus developer-confirmed facts.>

## 5. Technical changes

<Exact change locations, proposed logic/diffs, data access, error handling,
and mapping to acceptance criteria. Resolve routine technical choices here.>

## 6. Preserved behavior and exclusions

<Unrelated fields/validations, existing edits, shared dependencies,
and explicit out-of-scope work.>

## 7. Implementation checklist

- [ ] Inspect targets, baseline, and dependencies.
- [ ] Open the authorized ZIS source in VS Code.
- [ ] Apply the scoped changes.
- [ ] Save to SAP.
- [ ] Activate every required target.
- [ ] Verify saved/active source and returned outcomes.
- [ ] Generate the human test workbook.
- [ ] Record actual implementation outcomes.
- [ ] Move this specification to implemented after verified SAP completion.

## 8. Proposed human tests

| ID | Criterion/reason | Preconditions | Input/steps | Expected result |
|---|---|---|---|---|
| T-01 | <AC-ID or regression reason> | <setup> | <input/actions> | <outcome> |

Workbook: `testing/<story-id>/<story-id>-r<revision>-tests.xlsx`

Developers review, extend, and execute tests. Actual results and evidence
remain in Excel. No execution result is implied by this proposed list.

## 9. Implementation authorization policy

An explicit developer request to implement this specification authorizes
the in-scope editor opening, editing, SAP saving, activation, source
verification, local test-document generation, and specification move.
Creation/copying is included only when explicitly defined in section 3.
No separate conversational confirmation is required for these steps.

Tool approval controls and SAP permissions still apply. Essential ambiguity,
unauthorized overwrite, scope expansion, or unresolved blockers must be
reported rather than guessed. Program/test execution, original-object
changes, transports, and unrequested Git operations are prohibited.

## 10. Open questions and blockers

<Unresolved essentials only; never silently convert these into assumptions.>

## 11. Implementation record

- Implemented specification revision: <not yet implemented or exact revision>
- Actual system/client and target objects: <not performed or verified values>
- Create/copy/reuse outcome: <not performed or actual outcome>
- Editor-open outcome: <not performed or actual outcome>
- Changes applied: <not performed or actual changes>
- SAP save outcome/evidence: <not performed or actual outcome>
- Activation outcome/evidence: <not performed or actual outcome>
- Saved/active-source verification: <not performed or actual outcome>
- Test-workbook path/outcome: <not generated or actual path/outcome>
- Remaining blockers: <actual blockers>
- Human testing: Not executed by AI.

Program and tests were not executed by AI.

Implemented means verified SAP implementation, not testing, BA approval,
transport, or release. Preserve earlier implementation/version references
when revising this story.
