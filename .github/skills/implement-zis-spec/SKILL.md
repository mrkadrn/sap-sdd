---
name: implement-zis-spec
description: Carry an explicitly authorized SAP technical specification through ZIS editing, saving, activation, source verification, and implementation filing without routine approval questions.
---

# Implement ZIS specification

## Authorization and preflight

An explicit implementation request authorizes all defined steps below.
Do not request per-step confirmations. A review/explanation request does not.

1. Read the exact specification and revision. Establish targets, system/client,
   local package, scope, acceptance criteria, and permitted operation.
2. Inspect current source and dependencies within authorized read scope.
   Verify target identity and whether material source drift invalidates the
   specification. Preserve unrelated edits.
3. Use only actual configured SAP/editor tools. Verify their semantics;
   never assume a local save persists to SAP or that activation runs no tests.
   If a required tool is missing, report that blocker honestly.

## Prepare and open

4. Normally reuse the developer-prepared ZIS object. If creation/copy is
   explicitly in scope, use supported SAP operations and the specified local
   package (`$TMP` unless another local package was approved). Check target
   existence first. Do not overwrite or recreate an existing object without
   explicit authorization for that operation.
5. Verify package and connection. Inspect includes/shared dependencies;
   do not edit originals or add objects outside the scope.
6. Open the exact ZIS source in VS Code using supported editor integration
   before editing. Confirm the returned identity/connection. Do not substitute
   an unrelated local export or claim an unconfirmed editor-open operation.

## Edit, save, activate

7. Apply the smallest complete changes satisfying the specification.
   Use established naming, formatting, helpers, and error handling.
   No speculative refactoring or broad replacements.
8. Save to SAP and activate only the authorized targets. Verify diagnostics
   and results. Fix errors caused by your edits within the same approved
   scope without another confirmation; report unrelated blocking errors.
9. For an uncertain write, inspect saved/active state first. Retry only when
   the operation is still authorized and confirmed incomplete. Do not
   blindly repeat copy, save, or activation.
10. Read back saved/active source as supported and compare with the intended
    change. Report the limits if active state cannot be verified. Do not
    claim completion based solely on a successful tool invocation.

## Document and file

11. Use `prepare-test-workbook` automatically. Record expected results only;
    no SAP program/test execution. Report any document-generation blocker.
12. Record actual implementation facts and evidence in the specification,
    including its revision and save/activation/verification outcomes.
13. Once all required SAP targets are saved, activated, and source-verified,
    move the specification to `specs/implemented/<story-id>.md`. Inspect the
    destination first; never overwrite another active record. If blocked by
    a destination conflict, report the actual SAP completion and filing blocker.
    No Git commit is implied by moving a file.
14. If SAP completion is incomplete or uncertain, retain the specification in
    for-implementation with the actual partial outcome and remaining work.
15. Report target/environment, changes, editor-open/save/activation/verification
    outcomes, workbook and specification paths, and blockers.

Always state: "Program and tests were not executed by AI."

## Stop only for genuine exceptions

Essential business ambiguity, unknown/ambiguous target, unauthorized overwrite,
material contradiction, scope expansion, unavailable capability, or unresolved
operation outcome. Continue safe independent work where possible. Do not ask
about routine implementation choices or already authorized operations.
