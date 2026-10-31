# SAP SDD workspace

Three selectable VS Code Copilot agents support your workflow. This is a
local workspace starter, not a deployed cloud automation or an SAP connection.
No model is pinned and there is no automatic multi-agent orchestration.

## Contents

- `.github/agents/`: Story_Refiner, Technical_Spec_Writer, SDD_Implementer.
- `.github/skills/`: story refinement, technical specification, implementation,
  and Excel test-document preparation.
- `.github/copilot-instructions.md`: shared evidence and operational rules.
- `templates/`: ALM story, technical specification, and test-case JSON templates.
- `specs/for-implementation/`: generated specifications; no draft status.
- `specs/implemented/`: saved, activated, source-verified implementations.
- `testing/<story-id>/`: revision-specific human test workbooks and inputs.

## Install

1. Extract the starter and open `sdd-workspace/` as a folder in VS Code,
   or merge its contents into your repository. Preserve existing files:
   integrate existing shared instructions rather than replacing them blindly.
2. With the Copilot harness selected, open Chat: Open Customizations.
   Confirm the three agents and four skills are discovered without errors.
3. Configure each agent's actual tools with the editor's tool selector and
   save the resulting reviewed allowlist in its agent configuration.
   The initial lists contain only the documented `read`, `search`, and `edit`
   tool sets. They do NOT grant SAP, ALM, editor-opening, or local script execution.
4. Configure your installed SAP/ALM integrations separately. Use the actual
   installed tool identifiers; do not paste invented MCP names. Never store
   passwords, tokens, or SAP credentials in these files or Git.
5. Where policy permits, approve reviewed tools for the session/workspace.
   Instructions cannot preapprove tools or bypass organizational controls.
   Do not enable all-tools/bypass approval mode as a shortcut.

## Tool configuration by role

| Role | Additional configured capabilities |
|---|---|
| Story_Refiner | ALM read/create/update only when publishing is part of the task |
| Technical_Spec_Writer | Read-only SAP source/metadata, if not supplied in chat |
| SDD_Implementer | SAP source/metadata read, exact target editing/saving/activation, VS Code source opening |
| SDD_Implementer, optional operations | Creation/copy only if explicitly in scope; local execution for the bundled documentation script or a reviewed XLSX-generation tool |

An execution-capable tool is broader than permission to run one documentation
script. If narrow execution approval is unavailable, use manual review or a
dedicated document tool. Never interpret workbook generation permission as
permission to execute SAP programs/tests or unrelated commands.

Tool lists limit available tools, not SAP object-level access. Enforce the
original/ZIS boundaries using SAP roles and connector controls as well as
instructions. A tool with combined execution/transport side effects is not
suitable. If a required editor-opening or activation capability is unavailable,
the implementer reports a blocker instead of silently substituting another flow.

## Human-directed workflow

1. User raises an SCR; BA validates and clarifies scope.
2. BA selects Story_Refiner, reviews requirements, and explicitly requests
   ALM creation/update if desired. BA verifies the saved ALM record.
3. Developer reviews the approved story, identifies affected objects, and
   manually prepares the ZIS copies.
4. Developer selects Technical_Spec_Writer and requests the technical
   specification. It writes `specs/for-implementation/<story-id>.md`.
5. Developer reviews alignment with ALM and confirms targets/technical scope.
6. Developer selects SDD_Implementer and explicitly requests implementation.
   That one request covers opening, editing, saving, activation, verification,
   test-workbook generation, and the specification move. There is no separate
   approval checkpoint before save or activation.
7. Developer executes tests and records actual results/evidence in Excel.
   BA business testing and subsequent release controls remain human-owned.

No draft status is needed. The folder alone is not approval: the explicit
implementation request is the task authorization.

## Example requests

### BA story refinement

```text
Refine this change request into ALM-ready content using our story template.
Prepare acceptance criteria and business scenarios. Do not publish yet.
[Attach request and confirmed business rules.]
```

After review, explicitly request creation/update of the exact ALM project/record
if the corresponding integration is configured.

### Developer specification

```text
Generate specs/for-implementation/ST685528.md from the attached approved
ALM story and source. Record its reviewed ALM revision.
Target system/client: [system/client].
ZIS objects prepared by developer: [objects], package $TMP.
Do not modify SAP. Identify essential blockers rather than inventing rules.
```

For a new program, state "Create new program [exact name], no original copy"
instead of claiming that an existing ZIS copy has been prepared.

### Developer implementation

```text
Implement specs/for-implementation/ST685528.md, revision [revision].
The specification has been reviewed against the approved ALM story.
Use its exact system/client, ZIS targets, package, and defined operation.

Proceed end to end without routine conversational confirmations:
inspect, open in VS Code, edit, save to SAP, activate, verify, generate
the Excel test workbook, and move the specification to implemented.

Ask only for essential ambiguity, unauthorized overwrite, or scope expansion.
Do not execute SAP programs/tests, modify originals, transport, or commit.
Report actual outcomes and any blocker.
```

## Specification lifecycle

Generated specifications go directly to `specs/for-implementation/`.
No draft folder/status is used. Missing essentials are explicit blockers.

Move a specification to `specs/implemented/` only after every required target
is saved, activated, and source-verified. Never use an existing destination as
permission to overwrite it. Documentation failures must be reported separately;
implemented never means tests passed, BA approved, transported, or released.

For a requested requirement revision, move the existing specification back
to for-implementation, increment its revision, and update the ALM reference.
Keep one active copy and preserve previous implementation/evidence references.
Once the developer commits changes, Git history retains earlier versions.
No agent commits automatically.

## Excel documentation

The bundled Python 3 script uses only the standard library. It creates a real
XLSX with Tests and Metadata sheets from the JSON template. It rejects missing
fields, duplicate IDs, unresolved angle-bracket placeholders, invalid cell
text, and existing output files. It writes text cells, not Excel formulas.
No Python dependencies or SAP connectivity are needed.

The implementer automatically uses it through an approved local execution tool,
or uses a configured document-generation tool. Without either capability it
reports the blocker, not a fictional workbook.

New workbooks have expected results, blank actual results/evidence/execution
metadata, and Not executed statuses. Do not overwrite an existing workbook.
Use specification revisions or uniquely named supplements for new test lists.
Actual ZIS and original-object executions require separate evidence.

## Pilot acceptance checks for your team

- Confirm agent and skill discovery in the intended VS Code harness.
- Confirm each role has only the reviewed tools it needs.
- Verify that story/specification requests do not cause SAP writes.
- Use a permitted sandbox ZIS target to verify editor opening, SAP save,
  activation, and source readback with no routine conversational approvals.
- Confirm missing capability and scope-expansion cases report honest blockers.
- Confirm the workbook opens and has blank actual results, with no SAP tests run.
- Confirm platform approval prompts still obey your organization policy.

These are human-run setup checks; this starter has not connected to your SAP
or ALM systems.

## References

- VS Code agents: https://code.visualstudio.com/docs/agent-customization/custom-agents
- VS Code skills: https://code.visualstudio.com/docs/agent-customization/agent-skills
