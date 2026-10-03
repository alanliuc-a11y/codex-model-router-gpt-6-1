<!-- model-router:global-start -->
## Model Router: global workflow

This is the US$20 allowance profile. It applies the quota-conserving override after the base routing decision. This is an allowance strategy, not an official OpenAI subscription label.

For every new substantive user task, use the installed `model-router-20` skill before doing any work. A substantive task asks to analyze, research, create, modify, review, diagnose, or otherwise perform work. Meta questions and short confirmations are not substantive tasks.

- If the task does not begin with a valid confirmation token, do not execute it, use tools, browse, edit files, make a plan, or delegate. Return the skill's three-line routing recommendation and wait for confirmation. Valid tokens are `执行` or `按推荐执行` for Chinese, and the standalone word `go` for English.
- When the user sends a valid confirmation token after that recommendation, perform the immediately preceding task using the model selected by the user. Do not claim that the selection was verified or switched automatically.
- Follow the installed skill's output-language contract exactly. Keep model choice and reasoning effort separate. Do not recommend or change speed settings. Never use `Standard` as a reasoning-effort label.
- `$model-router-20` remains an optional explicit fallback when the user wants to force a routing-only turn.
- Reassess the complete new request with relevant context; never carry forward Luna just because earlier turns used it. Luna requires ALL: one narrow outcome, explicit solution and acceptance criteria, no investigation/design or coupled feature/state/data-flow changes, and direct local verification with cheap recovery. Unknown or repeated bugs, multi-feature work, role-dependent publishing, uploads, synchronization, lifecycle state, and cross-screen consistency exclude Luna. Start from Sol Medium when these conditions are not established, then assess Sol/Astra as needed. Do not classify only the easiest first step. Apply allowance overrides once after the base route.
- Return exactly one recommendation in three lines: Chinese uses `模型：…；推理强度：…`, `原因：…`, `操作：…执行…`; English uses `Model: …; reasoning effort: …`, `Reason: …`, `Action: …go…`. Give a task-specific reason, not an execution plan.

### Fallback routing contract

- Use the same base rubric as the higher-allowance profile: Luna Low/Medium only when all eligibility conditions above are met; Sol Medium for ordinary production work, High for coupled features or difficult diagnosis, and XHigh for exceptional single-domain depth; Astra when at least two Astra signals are present.
- For an Astra base route, use Low only for explicit work with strong verification, otherwise Medium. Use High for high stakes, weak validation, conflicting evidence or costly hidden failures. XHigh/Max are exceptional depth choices; Ultra requires explicit availability. Determine this base effort before applying the profile mapping below.
- Astra signals are: three or more demanding work modes; end-to-end ownership from discovery through delivery; several interacting systems or artifact types; a long dependency chain; or weak validation, costly external effects, conflicting evidence, or hidden failures.
- After choosing the base route, replace every `GPT-6 Astra + 轻` or `GPT-6 Astra + 中` route with `GPT-6.1 Sol + 极高`. Replace every `GPT-6 Astra + 高`、`极高`、`最大`、or `超强` route with `GPT-6 Astra + 轻`.
- Do not silently replace the managed catalog with a different picker option. If none of GPT-6 Luna, GPT-6.1 Sol, or GPT-6 Astra is available, report the picker mismatch and stop.
- The fallback output is exactly three lines. For Chinese, start the first line with `模型：`; for English, start the first line with `Model:`.
- Current default catalog: GPT-6 Luna, GPT-6.1 Sol, GPT-6 Astra. GPT-6 Sol and GPT-5.6 models are legacy-only, never silent defaults; do not invent GPT-6.1 Luna/Terra/Astra. Keep Luna's eligibility unchanged. Use supported Codex effort choices; do not infer None from API support or recommend Luna Ultra.
- AutomationBench informs cross-app workflows only. GPT-6 Sol's old scores are not GPT-6.1 Sol scores; no comparable 6.1 effort table was verified on 2026-10-04. Do not infer ranking, guaranteed savings or Codex quota use from it. Max is not automatically better; do not merge public/private or AutomationBench-AA results.
- GPT-6.1 Sol is the normal workhorse: Medium for daily work, High for coupled logic/ambiguity, XHigh for exceptional depth or the US$20 override. Keep explicit well-verified cross-system workflows at Sol High when appropriate. Astra needs two genuine signals plus demanding coordination/long-context difficulty or costly hidden failures; do not require a failed Sol run. Do not count routine delivery alone as sufficient complexity.
- GPT-6.1 Sol supports no API None/Minimal. Ultra is client-specific and only when the exact combination is available; availability does not authorize delegation.
<!-- model-router:global-end -->
