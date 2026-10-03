---
name: model-router-20
description: Recommend a quota-conserving Codex model and reasoning effort for the US$20 allowance tier. Use for model selection, reasoning-level selection, or task routing; it recommends but never switches the already-running root model.
metadata:
  short-description: Recommend efficient routing for the US$20 allowance tier
---

# Model Router — US$20 Profile / 模型路由器（20 美金档）

Catalog revision: 2026-10-04; package release v1.1.0.

Recommend the lowest-cost setup that is likely to complete the task correctly. Treat model choice and reasoning effort as separate decisions. This skill does not change speed settings.

## Plan profile

This package is the US$20 allowance profile. First determine the route using the full rubric below. Then apply the required US$20 override to every Astra route. This is a quota policy chosen by the installer, not an official OpenAI plan name, entitlement, or quality guarantee.

## Hard boundary

- The root model is selected before a turn starts. This skill cannot switch that already-running root model. State a recommendation, not a claim that a switch occurred.
- If the user asks only for routing, do not execute the proposed task. Return the recommendation so the user can select it before resubmitting the work.
- Do not create subagents merely to imitate a model switch for a small task; the coordinator plus subagent can consume more total usage. Use delegation only when the user requested it and the work genuinely divides into useful independent parts.
- Do not claim to know the active UI selection unless current task metadata explicitly exposes it. The configured default may have been overridden per task.

## Managed catalog

In Codex, this package manages `GPT-6 Luna`, `GPT-6.1 Sol`, and `GPT-6 Astra`. Do not implicitly defer to a generic or cross-platform routing skill. Do not silently substitute a different model merely because it appears in the current picker.

## Evaluate the whole task before choosing a model

Reassess each new substantive request using its full scope and relevant conversation context. Do not reuse the previous recommendation merely because several earlier turns used Luna. A short follow-up can refer to a complex unresolved task. Confirmation words continue the accepted task without another routing gate.

Choose Luna only when ALL of these conditions are met:
- One narrow outcome with an explicit solution or transformation rule.
- Inputs and acceptance criteria are already clear; no investigation or design decision is needed.
- No coupled changes to multiple features, screens, roles, state transitions, or data flows.
- Verification is direct and local, with cheap recovery if wrong.

Exclude Luna for unknown-cause or repeatedly failing bugs; new features with lifecycle or interaction state; cross-screen consistency; role-dependent publishing, permissions, uploads, persistence, or synchronization; and requests combining several interacting changes. A mock/demo status does not make these interactions trivial. Use Sol Medium for scoped implementation and High for ambiguity or difficult diagnosis, and evaluate the Astra gate for broad integration work. When evidence is insufficient to establish every Luna condition, start from Sol Medium and assess upward.

Route the whole requested outcome, not just the easiest first step. Splitting implementation into small steps does not justify assigning the entire task to Luna. Apply any allowance-profile override only AFTER this base assessment, exactly once; never remap the resulting Astra Low a second time.

Before responding, check the current task against these conditions and return the prescribed three-line format once, with a task-specific reason. Do not replace the reason with an execution plan.

## Routing rubric

- **GPT-6 Luna + Low/Medium:** narrow, explicit, repeatable work meeting ALL Luna conditions above. Start at Low for mechanical transformations, Medium for bounded coding.
- **GPT-6.1 Sol + Medium:** normal default for production work, scoped coding, document analysis and known bug fixes.
- **GPT-6.1 Sol + High:** interacting features, multi-file implementation, ambiguous requirements, unknown/repeated bugs or difficult single-domain decisions.
- **GPT-6.1 Sol + XHigh:** exceptionally difficult single-domain work, a demonstrated shortfall at High, or the US$20 allowance override. Do not default to Max.
- **GPT-6 Astra + Low/Medium:** at least two Astra signals: three demanding work modes; end-to-end discovery through delivery; several interacting systems/artifact types; a long dependency chain; weak validation/conflicting evidence/costly hidden failures. Low for explicit strongly verifiable work, otherwise Medium.
- **GPT-6 Astra + High:** Astra-eligible work with high stakes or weak validation.
- **GPT-6 Astra + XHigh/Max:** exceptional depth or a demonstrated shortfall at High.
- **Ultra:** recommend only when this exact model/option is exposed in the current Codex environment and the user wants appropriate parallel work. Availability is not authorization to spawn agents. Do not describe it as a portable API effort.

Astra does not require a failed Sol attempt. Ordinary multi-file work alone does not establish two Astra signals. Assess actual ambiguity, dependencies and failure consequences, not just count tools.

### Evidence and availability (reviewed 2026-10-04)

Default catalog: GPT-6 Luna, GPT-6.1 Sol and GPT-6 Astra. GPT-6 Sol and GPT-5.6 models are legacy-only when explicitly requested or the user confirms a legacy-only picker. Do not invent GPT-6.1 Luna, Terra or Astra. Do not silently fall back to the older Sol.

Official guidance positions GPT-6.1 Sol for complex coding, computer use and professional work at lower cost than Astra. This supports making it the normal workhorse; it does not establish equal capability or subscription savings. Preserve effective reasoning effort on upgrade before evaluating a lower effort on representative tasks. Start ordinary production tasks at Medium; use High for coupled logic, edge cases, uncertainty or diagnosis. Low can fit a modest, specified fix with direct checks when Luna is excluded because limited judgment is required. XHigh/Max need exceptional depth or a demonstrated shortfall; the US$20 override uses XHigh by policy.

A routine multi-file or two-tool task stays on Sol. An explicit cross-system workflow with strong validation can start at Sol High. Evaluate Astra for genuinely demanding integration with at least two signals and substantial coordination/long-context difficulty or costly hidden failures. Do not demand a failed Sol run for these tasks. Do not promote every end-to-end edit solely because it includes delivery.

The reviewed local Codex catalog exposes Low/Medium/High/XHigh/Max on all three and Ultra on GPT-6.1 Sol/Astra. Recommend only the actual model-picker options. GPT-6.1 Sol's API does not support None or Minimal. Codex Ultra is client-specific; its availability does not authorize delegation.

AutomationBench is one source for cross-app automation, not a universal quality ranking or a Codex quota meter. Previous 2026-09-27 GPT-6 Sol scores must not be relabeled as GPT-6.1 Sol. No comparable GPT-6.1 Sol effort table was verified for this update; do not infer its scores or guarantee savings. Do not merge private-set, public-set and AutomationBench-AA scores. Benchmark evidence cannot relax Luna's eligibility or prove that maximum effort always wins.

Sources: [GPT-6.1 Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Codex model guidance](https://learn.chatgpt.com/docs/agent-configuration/subagents), [AutomationBench](https://zapier.com/benchmarks). Refresh these sources before claiming the catalog or ranking remains current.

## Required US$20 override

After determining the base route, apply these replacements exactly:

| Base route | Final recommendation for this profile |
| --- | --- |
| GPT-6 Astra + Low | GPT-6.1 Sol + XHigh |
| GPT-6 Astra + Medium | GPT-6.1 Sol + XHigh |
| GPT-6 Astra + High | GPT-6 Astra + Low |
| GPT-6 Astra + XHigh | GPT-6 Astra + Low |
| GPT-6 Astra + Max | GPT-6 Astra + Low |
| GPT-6 Astra + Ultra | GPT-6 Astra + Low |

Leave Luna and Sol base routes unchanged. This profile intentionally trades some reasoning depth for allowance conservation. Do not present the lower final effort as equivalent in quality to the original base route.

State that the final choice follows the US$20 allowance policy when the override changes an Astra base route. Give the user one final recommendation only; do not show a second competing base-route recommendation.

## Output language and response contract

Choose one output language before answering. Use Chinese when the request is predominantly Chinese; use English for English or genuinely mixed requests. Never mix Chinese and English in a routing response, except for official model names.

For a Chinese routing-only request, return exactly these three short lines:

`模型：<GPT-6 Luna|GPT-6.1 Sol|GPT-6 Astra>；推理强度：<轻|中|高|极高|最大|超强>`

`原因：<一条简短、针对任务的原因>`

`操作：<在模型选择器中选择模型和推理强度，然后发送“执行”>`

Map reasoning labels as follows: `Low` → `轻`, `Medium` → `中`, `High` → `高`, `XHigh` → `极高`, `Max` → `最大`, and `Ultra` → `超强`.

For an English routing-only request, return exactly these three short lines:

`Model: <GPT-6 Luna|GPT-6.1 Sol|GPT-6 Astra>; reasoning effort: <Low|Medium|High|XHigh|Max|Ultra>`

`Reason: <one concise, task-specific reason>`

`Action: <choose the model and reasoning effort in the model picker, then send "go">`

Treat `go` as a confirmation only when the entire user message is exactly `go`, ignoring case and surrounding whitespace. Do not mention speed or label `Standard` as a reasoning effort. For a normal substantive task, route first and do not execute it until the user confirms with the language-appropriate confirmation word.

On confirmation, execute the accepted task without another routing gate. If this profile is the active global profile, do not implicitly use the higher-allowance or cross-platform router.
