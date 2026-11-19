---
name: model-router-20
description: Recommend a cost-aware Codex model and reasoning effort for ChatGPT Plus, retaining GPT-6.1 Sol alongside GPT-6.2 Sol/Astra, Terra and Luna. Use for model/effort selection and task routing; recommends but never switches the running root model.
metadata:
  short-description: Recommend value-aware routing for ChatGPT Plus
---

# Model Router — ChatGPT Plus

Catalog and price review: 2026-11-19; package release v1.4.0.
This is a project routing strategy for the named subscription, not an official OpenAI model-selection policy.

## ChatGPT Plus strategy

Keep a working GPT-6.1 Sol baseline as the default value-Sol, normally Medium for ordinary work and High for difficult diagnosis. The user's positive experience is a reason to preserve that workflow, not proof that 6.1 has lower published token rates.

GPT-6.2 Sol remains an active option: use it for explicit user choice, a concrete capability need, or credible same-input/effective-effort evidence of less total usage/rework. Equal published rates alone do not force migration. If the current fixed speed or allowance evidence favors 6.2, account for that too; never claim 6.1 always wins.

Apply this project's conservation mapping ONCE, after base model/effort and value-Sol selection:
| Base recommendation | Final recommendation |
| --- | --- |
| GPT-6.2 Astra Low/Medium | Selected value-Sol XHigh; default GPT-6.1 Sol XHigh, or GPT-6.2 Sol XHigh only when justified above |
| GPT-6.2 Astra High/XHigh/Max/Ultra | GPT-6.2 Astra Low |

Luna, Terra and either Sol base route stay unchanged. Never remap the resulting Astra Low or map Astra to Terra. Explain the conservation policy in the reason when it changes the route. A reduced effort is not equivalent quality; explicit supported user requirements take precedence.

The skill name `model-router-20` and directory `profiles/20-usd` are retained only for upgrade compatibility, not subscription selection labels.

Recommend the least costly setup likely to meet the task's quality bar, counting context, effort and rework, not release date alone. Recommend only; never claim to switch or verify the already-running root model. Never change speed or context-window settings.

## Catalog and scope

Active candidates: `GPT-6 Luna`, `GPT-6.1 Terra`, `GPT-6.1 Sol`, `GPT-6.2 Sol`, `GPT-6.2 Astra`. Both Sol versions are current value candidates. GPT-6 Astra, GPT-6 Sol and GPT-5.6 models are explicit legacy choices, not silent substitutes. Do not invent GPT-6.2 Luna/Terra.

This is the authoritative Codex router. A cross-platform router is an explicit-only alternative, not an implicit fallback. Check actual picker availability; if a recommended model/effort is absent, report the mismatch and resolve it with the user. Never infer plan or entitlement from a model name, subscription price or a config default. Explicit supported user choices override these project defaults.

Use the official subscription names ChatGPT Plus and ChatGPT Pro in installation choices, not dollar bands. Corporate, education, Free/Go and API-key setups need their own availability/allowance checks; do not silently classify them as Pro. This project's strategies are not official OpenAI routing algorithms.

## Whole-task assessment

Reassess the full request and unresolved context every time. Do not carry forward Luna/Terra after a small task, or route only the first screenshot/edit of a complex task. Confirmation continues the accepted task without rerouting.

Choose Luna only when ALL hold: one narrow outcome; explicit inputs/solution and acceptance; no investigation/design or coupled feature/state/data-flow changes; direct local checks and cheap recovery. Unknown/repeated bugs, lifecycle, cross-screen consistency, permissions, role-dependent publishing, persistence, uploads and synchronization exclude Luna.

Next consider Terra only when ALL hold: a bounded source-grounded writing, visual/chart/screen interpretation, defined computer-use flow or scoped known-cause fix; clear sources/requirements; concrete checks (compare sources, reopen saved records, inspect the render or run regressions); no unresolved repeated bug, coupled lifecycle/role/permission/data change, broad discovery, conflicting evidence or costly hidden failure. An interface does not remove action permissions or risk.

Otherwise use the selected value-Sol. Medium is this router's conservative multi-step starting point, not an official client default. Low can fit fully specified modest work with cheap direct checks; High for coupled features, ambiguity or tracing a cause across systems; XHigh for exceptional depth or interacting causes. Unknown/repeated bugs do not become Terra tasks by raising effort.

Consider Astra when at least two genuine signals combine with demanding coordination, long dependencies or costly hidden failures: three demanding work modes; end-to-end discovery through delivery; interacting systems/artifact types; long dependency chains; weak validation/conflicting evidence. Ordinary delivery or multiple files alone is insufficient. No failed Sol attempt is required for a genuinely hard task.

## Effort and value

- Luna: Low for mechanical work, Medium for narrowly bounded coding. This intentionally narrow policy is not the official general Luna High starting recommendation.
- Terra: normally Medium; Low for limited judgment; High for dense but bounded visual detail. Exceptional XHigh/Max needs evidence, not a way to force an unsuitable project onto Terra.
- Sol: Low/Medium/High/XHigh as above. Choose 6.1 or 6.2 by this profile's policy and [pricing-policy.md](references/pricing-policy.md), not a newer-version preference.
- Astra: determine base effort before the profile mapping: Low for explicit strongly verifiable work, otherwise Medium; High for high stakes/weak checks; XHigh/Max for exceptional depth.
- Ultra is client-specific parallel behavior. Recommend it only when the exact option exists and the user authorizes useful delegation; availability alone never authorizes spawning agents. Never delegate just to imitate a model switch.
- Preserve effective effort in version comparisons before testing a lower setting. Price per token, effort label, or a launch claim cannot prove lower total usage or equal quality. If a cheaper route fails quality, surface the shortfall rather than promise equivalence.

## Verified evidence — 2026-11-19

The reviewed local catalog offers Low/Medium/High/XHigh/Max for all five and Ultra for Terra and both Sols/Astra, not Luna. It is metadata, not proof of the user's current picker. The 6.2 Sol/Astra APIs reject None; the reviewed Codex catalog offers neither None nor Minimal, even though Terra's API supports None. Terra's documented CLI minimum is 0.159.0; do not invent a 6.2 minimum. Account, client and workspace controls still apply.

Official Standard-speed credit rates are identical for Sol 6.1 and 6.2. This does not establish identical included allowance or actual task cost. Official subscription guidance expressly exempts 6.1 Sol from long-context surcharge. Preserve a proven 6.1 workflow; do not call it obsolete or assert 6.2 is always cheaper/more expensive. Read the dated pricing reference for cost-sensitive choices; keep the user's speed unchanged.

Codex documents default context windows of 272,000 tokens for 6.2 Astra and 500,000 for 6.2 Sol, distinct from larger model/API limits. Long input alone does not justify Astra. Check usable context and billing; resolve chunking/compaction with the user if needed, never silently discard required sources or change settings.

Older benchmark scores are not 6.2 scores. This release verifies no comparable 6.2 effort table and promises no saving percentage. Do not merge public/private or AutomationBench-AA results. The routing/effort policy is a project decision, not an official ranking.

Sources: [6.2 launch](https://learn.chatgpt.com/docs/whats-new/gpt-62-astra-sol), [Codex models/context](https://learn.chatgpt.com/docs/models), [6.2 prompting](https://learn.chatgpt.com/guides/prompting-gpt-6-2-astra), [official allowance and credit pricing](https://learn.chatgpt.com/docs/pricing).

## Output language and confirmation

For every new substantive task, recommend first and stop. Before confirmation, do not use tools, browse, edit, plan, delegate or execute. Meta questions and standalone maintenance commands below are excluded.

Use Chinese for predominantly Chinese input with English names/code only; use English for English or genuinely mixed input. Routing output never mixes languages except official model names. Give one recommendation and a task-specific reason, not a plan.

Chinese, exactly three lines:
`模型：<GPT-6 Luna|GPT-6.1 Terra|GPT-6.1 Sol|GPT-6.2 Sol|GPT-6.2 Astra>；推理强度：<轻|中|高|极高|最大|超强>`
`原因：<简短的任务原因；如适用，说明依据所选节约策略>`
`操作：在模型选择器中选择模型和推理强度，然后发送“执行”。`

English, exactly three lines:
`Model: <GPT-6 Luna|GPT-6.1 Terra|GPT-6.1 Sol|GPT-6.2 Sol|GPT-6.2 Astra>; reasoning effort: <Low|Medium|High|XHigh|Max|Ultra>`
`Reason: <concise task-specific reason; mention conservation policy if applicable>`
`Action: Choose the model and reasoning effort in the model picker, then send "go".`

Map Low→轻, Medium→中, High→高, XHigh→极高, Max→最大, Ultra→超强. Standard is not reasoning effort. Chinese confirmation is `执行` or `按推荐执行`; English confirmation is only the standalone word `go`, case-insensitive, not `go ahead`. On confirmation, continue the pending task without another gate and without claiming a model switch was verified.

## Updates are separate from publication

Only verified local hook context may add one fourth routing line, in the same language: Chinese `更新：模型路由器已有新版（<版本>），输入“更新路由器”即可更新。`; English `Update: Model Router <version> is available. Send "update router" to update.` No notice on confirmation or execution turns; no model-tool network check before routing.

Standalone `更新路由器` / `update router` and `检查路由器更新` / `check router update` are maintenance, exempt from the routing gate, not confirmation to execute a pending task. Read [updating.md](references/updating.md) and use the installed helper. Notices never authorize installation.

Publishing a GitHub release or validating it does not authorize local installation, global-rule changes or hook changes. Use isolated test directories. Require a separate explicit request to upgrade the actual local skill; preserve its plan strategy, other config and reminder setting. Never bypass hook trust or claim config generation proves client execution.
