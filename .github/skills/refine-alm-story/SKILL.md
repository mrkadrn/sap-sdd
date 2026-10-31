---
name: refine-alm-story
description: Refine a change request with the BA into ALM-ready requirements and numbered acceptance criteria. Use for backlog creation, story refinement, and approved ALM publishing.
---

# Refine ALM story

1. Read the supplied request and reuse confirmed context.
2. Establish the business problem, role, action, measurable or estimated
   value, scope, and exclusions. Distinguish estimates from measured outcomes.
3. Clarify rules that change observable behavior. Consider boundaries,
   missing data, error outcomes, dates/time zones, and existing behavior.
   Do not ask implementation-detail questions that belong to technical analysis.
4. Prepare content using
   [the story template](../../../templates/alm-story-template.md).
5. Write independently verifiable Given/When/Then criteria with stable IDs.
   Preserve existing ALM IDs when refining a story.
6. Propose business examples and tests linked to the criteria. Mark unresolved
   expectations explicitly; do not disguise them as approved criteria.
7. Present the content for BA review. Do not call it approved without evidence.
8. If explicitly requested to publish, use the configured ALM integration.
   Establish the target project/record, inspect existing content for updates,
   and submit only the authorized changes. Do not infer publication permission
   from a general acknowledgment of the wording.
9. Verify the returned ALM record or read it back when available. Report its
   identifier/revision and any uncertainty. On an uncertain creation result,
   search/read the target before retrying to avoid duplicate stories.
10. Hand over the BA-approved story and unresolved questions. The BA verifies
    the created record; the developer identifies objects and prepares ZIS.

No SAP implementation or test execution is part of this skill.
