# Routing review cases

Default models are GPT-6 Luna, GPT-6.1 Sol and GPT-6 Astra; GPT-6 Sol and GPT-5.6 models are legacy-only. Reviewed 2026-10-04.

These are manual acceptance cases, not measured model-quality benchmarks or automated behavioral test results. Use each prompt in a fresh conversation, then repeat the complex prompts after several small-edit turns. Require a single three-line recommendation with a task-specific reason.

| Task | Base route expectation | US$20 final expectation |
| --- | --- | --- |
| Convert three supplied meeting notes into a table; do not infer missing data. | Luna Low or Medium | Unchanged |
| Change one specified CSS font size from 14px to 16px in a known selector. | Luna Low | Unchanged |
| Add a scrolling caption during audio playback, handling pause, resume, next track and missing captions. | Sol Medium/High; no Luna | Unchanged |
| A notification still cannot open fullscreen after two attempted fixes; investigate the cause. | Sol Medium/High; no Luna | Unchanged |
| Implement publisher roles, capture controls, content types, scheduling, role-based templates and simulated review states, then verify the interacting publishing flow. | GPT-6.1 Sol High for explicit requirements with strong checks; Astra Medium if coordination/context difficulty meets the gate. No Luna. | Sol High unchanged; Sol XHigh for base Astra Medium |
| Research a production payment failure, coordinate fixes across services, test recovery and deploy with costly external effects and weak validation. | Astra High or above if the Astra gate is met | Astra Low |

Check that the final Astra Low in the last case is NOT remapped again to Sol XHigh. The allowance policy is applied once.

The publisher-role case remains excluded from Luna even when framed as a demo or divided into implementation stages. A short follow-up such as “continue fixing it” inherits the unresolved task scope rather than becoming a new trivial task.

Additional acceptance checks:

- Ordinary scoped coding starts at GPT-6.1 Sol Medium, not a GPT-5.6 default.
- A new release alone does not make a coupled publishing workflow eligible for Luna.
- Every Astra base effort is mapped once: Low/Medium to GPT-6.1 Sol XHigh; High/XHigh/Max/Ultra to GPT-6 Astra Low in the US$20 profile.
- Sol Max does not automatically outrank Sol XHigh; a benchmark score alone cannot justify an effort upgrade.
- A picker lacking GPT-6.1 Sol must produce an availability mismatch, not silently recommend GPT-5.6 Sol or invent GPT-6 Terra.
- API None and Luna Ultra must not appear in recommendations for the reviewed Codex catalog.
- Chinese recommendations use Chinese effort labels; English recommendations use English only except official names.
