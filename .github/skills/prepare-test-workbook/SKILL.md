---
name: prepare-test-workbook
description: Generate an Excel workbook of proposed test cases and expected results for human execution, preserving all existing actual results and evidence.
---

# Prepare human test workbook

Use during implementation handover without another permission checkpoint,
or when the developer explicitly requests test documentation.

1. Read the specification revision and its test scenarios. Cover every
   acceptance criterion plus justified regression scenarios.
2. Write concrete preconditions, inputs/steps, and expected results. Do not
   invent undefined business outcomes. Report uncovered/undefined criteria.
3. Prepare JSON using
   [the input template](../../../templates/test-cases-template.json).
   Replace all placeholders; the template is not an executable test list.
   Each test needs a unique ID and an acceptance-criterion reference or
   explicit regression reason.
4. Use `testing/<story-id>/<story-id>-r<revision>-test-cases.json` and
   `testing/<story-id>/<story-id>-r<revision>-tests.xlsx`.
   Inspect existing files first. Never overwrite an existing workbook or
   human evidence. If a workbook already exists, leave it intact and generate
   a new uniquely named revision/supplement only when needed.
5. Use a configured document-generation tool or the bundled standard-library
   Python script through an approved local execution tool:

   ```text
   python .github/skills/prepare-test-workbook/scripts/create_test_workbook.py --input testing/<story-id>/<story-id>-r<revision>-test-cases.json --output testing/<story-id>/<story-id>-r<revision>-tests.xlsx
   ```

   This only creates documentation; it does not connect to SAP or run tests.
   If local execution is not configured, do not claim an XLSX was created.
   Supply the JSON and report the missing workbook-generation capability.
6. Verify that the XLSX exists, is readable using the available document tool
   or ZIP/XML inspection, and contains the expected cases and metadata.
7. New rows must have blank actual result, evidence, tester, and execution
   date fields, with status `Not executed`. Never prefill a pass result.
8. Link the workbook in the specification. Identify system/client, target
   object/version, source story revision, and specification revision.
   Distinguish intended test target metadata from actual execution evidence.

Developers review and add cases, execute tests, and fill actual results.
BA business testing remains human-controlled. Tests of original objects need
separate execution records; never reuse earlier ZIS results as new evidence.
