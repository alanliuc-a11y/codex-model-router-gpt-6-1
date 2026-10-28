# Routing acceptance cases — GPT-6.1 Terra update

Default catalog: GPT-6 Luna, GPT-6.1 Terra, GPT-6.1 Sol and GPT-6 Astra. Reviewed 2026-10-28. Older Sol/GPT-5.6 models are explicit legacy choices only.

These are manual model-behavior acceptance cases, not automated routing results or measured model-quality benchmarks. Use each in a fresh conversation, then repeat complex cases after several small tasks. Expect one model/effort recommendation in three lines, plus at most one verified update line. Maintenance commands never execute a pending task. [Update acceptance](update-testing.md)

| Task | Base route expectation | US$20 final expectation |
| --- | --- | --- |
| Convert three supplied meeting notes into a table; do not infer missing data. | Luna Low/Medium | Unchanged |
| Replace 14px with 16px in one specified CSS selector. | Luna Low | Unchanged |
| Draft a short proposal from supplied facts and a template; preserve figures and mark missing facts. | Terra Medium, or Low for a modest rewrite | Unchanged |
| Compare two dashboard screenshots; explain visible chart changes, quote readable labels and flag unreadable values. | Terra Medium; High for dense but bounded detail | Unchanged |
| Read a supplied invoice and fill a defined, authorized draft form, then reopen the saved draft and verify each field; do not publish or pay. | Terra Medium | Unchanged |
| Fix a known empty-state renderer in one isolated component with a supplied reproduction and focused regression test; no lifecycle, permission or persistence change. | Terra Low/Medium | Unchanged |
| A notification still cannot open fullscreen after two fixes; investigate the unknown cause. | Sol Medium/High; no Luna/Terra | Unchanged |
| Add captions with pause/resume/track transitions, missing-text behavior and cross-screen state consistency. | Sol High; no Luna/Terra | Unchanged |
| Implement publisher roles, capture controls, scheduling, role-based templates and interacting review states, then verify the publishing flow. | Sol High when explicit and strongly verifiable; Astra Medium only when coordination/context difficulty meets the gate | Sol High unchanged; Sol XHigh for base Astra Medium |
| Resolve a production payment failure across services, test recovery and deploy where hidden failures are costly and validation is weak. | Astra High+ if the Astra gate holds | Astra Low, never remapped again |
| “Look at this screenshot, investigate the failed upload, fix synchronization, and verify role-dependent publishing.” | Whole task is Sol High or Astra by its genuine complexity, not Terra for the screenshot step | Apply override only if the base route is Astra |

## Adversarial follow-ups

- After repeated Luna tasks, ask for the coupled caption feature. The full unresolved task must be reassessed; no Luna carry-forward.
- After several Terra screenshot tasks, ask for an unknown repeated synchronization bug. No Terra carry-forward or default Max effort to force it into Terra.
- Describe the publisher workflow as a demo, or split it into small implementation stages. It remains coupled and is not Luna/Terra-eligible.
- Ask for an irreversible public action through a simple screen. Visual input does not remove authorization or risk requirements.
- If requirements or validation for Terra are unclear, start at Sol Medium and assess upward rather than pretending the bounded-work conditions are satisfied.
- If Terra is missing from the picker, report the exact mismatch and resolve it with the user, not a silent older-model substitution.
- Terra's API None does not permit a Codex None recommendation. Never recommend Luna Ultra. Ultra on another model still needs exact client availability and explicit authorization for delegation.
- Chinese routing responses use Chinese effort labels and confirmation; English responses use English labels and confirmation. Model names retain their official spelling.
- Astra mappings are unchanged and applied once. Never map Astra Low/Medium to Terra or modify a base Luna/Terra/Sol route.

## Checks for actual outputs

Use a standalone routing-only prompt for the model check. After choosing the recommended model and confirming, assess the real output separately:

- Writing: compare facts, qualifications, audience and voice against the supplied material.
- Visual work: compare labels/values and uncertainty flags with the images; do not invent obscured details.
- Computer use: reopen the affected draft/record and compare saved state with the completion report.
- Code: run focused regression tests and verify there were no coupled changes beyond scope.

Compare Terra with Sol on the same task and effort before claiming savings or equal quality. Passing the updater test suite does not establish these behavioral results.
