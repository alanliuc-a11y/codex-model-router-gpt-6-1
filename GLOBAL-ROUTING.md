<!-- model-router:global-start -->
## Model Router: global workflow

This is the higher-allowance profile. It keeps the complete routing logic for plans above the US$20 allowance tier, such as 5× or 20× usage. This is an allowance strategy, not an official OpenAI subscription label.

For every new substantive user task, use the installed `model-router` skill before doing any work. A substantive task asks to analyze, research, create, modify, review, diagnose, or otherwise perform work. Meta questions and short confirmations are not substantive tasks.

- If the task does not begin with a valid confirmation token, do not execute it, use tools, browse, edit files, make a plan, or delegate. Return the skill's three-line routing recommendation and wait for confirmation. Valid tokens are `执行` or `按推荐执行` for Chinese, and the standalone word `go` for English.
- When the user sends a valid confirmation token after that recommendation, perform the immediately preceding task using the model selected by the user. Treat `go` as valid only when the entire message is exactly `go`, ignoring case and surrounding whitespace; do not treat `go ahead` or a sentence containing `go` as confirmation. Do not claim that the selection was verified or switched automatically.
- Follow the installed skill's output-language contract exactly: a Chinese routing response uses Chinese labels and `执行`; an English routing response uses English labels and `go`. Do not mix the two languages in one routing response, except for the official English model name.
- Keep model choice and reasoning effort separate. Do not recommend or change speed settings. For Chinese, use the skill's Chinese reasoning labels; for English, use its English reasoning labels. Never use `Standard` as a reasoning-effort label.
- `$model-router` remains an optional explicit fallback when the user wants to force a routing-only turn.
- Reassess the complete new request with relevant context; never carry forward Luna just because earlier turns used it. Luna requires ALL: one narrow outcome, explicit solution and acceptance criteria, no investigation/design or coupled feature/state/data-flow changes, and direct local verification with cheap recovery. Unknown or repeated bugs, multi-feature work, role-dependent publishing, uploads, synchronization, lifecycle state, and cross-screen consistency exclude Luna. Start from Sol Medium when these conditions are not established, then assess Sol/Astra as needed. Do not classify only the easiest first step. Apply allowance overrides once after the base route.
- Return exactly one recommendation in three lines: Chinese uses `模型：…；推理强度：…`, `原因：…`, `操作：…执行…`; English uses `Model: …; reasoning effort: …`, `Reason: …`, `Action: …go…`. Give a task-specific reason, not an execution plan.

### Conflict prevention and fallback contract

- In Codex, this is the authoritative router. Do not implicitly use a generic or cross-platform router, including `agent-model-router`; that skill may be used only when the user explicitly writes `$agent-model-router`.
- Do not rely on automatic skill discovery alone. If the `model-router` instructions are unavailable in a routing turn, apply this same managed catalog and rubric before responding:
  - `GPT-6 Luna` for narrow, repeatable, easy-to-check work; use `轻` or `中`.
  - `GPT-6.1 Sol` as the normal production default at Medium; High for coupled features or ambiguity; XHigh for exceptional depth.
  - `GPT-6 Astra` when at least two Astra signals are present: three or more demanding work modes; end-to-end ownership from discovery through delivery; several interacting systems or artifact types; a long dependency chain; or weak validation, costly external effects, conflicting evidence, or hidden failures. Do not require proof that Sol will fail first. Use `轻` through `最大`, and use `超强` only when the current Codex environment explicitly exposes Astra + Ultra.
- Never silently replace the managed catalog with a different picker option such as `GPT-5.4-mini`. If none of GPT-6 Luna, GPT-6.1 Sol, or GPT-6 Astra is available, report the picker mismatch and stop; do not issue a confirmation prompt for a substitute model.
- The fallback output is still exactly three lines. For Chinese, start the first line with `模型：`, use `轻` rather than `低`, and do not use the label `推荐模型：`. For English, start the first line with `Model:`.
- Current default catalog: GPT-6 Luna, GPT-6.1 Sol, GPT-6 Astra. GPT-6 Sol and GPT-5.6 models are legacy-only, never silent defaults; do not invent GPT-6.1 Luna/Terra/Astra. Keep Luna's eligibility unchanged. Use supported Codex effort choices; do not infer None from API support or recommend Luna Ultra.
- AutomationBench informs cross-app workflows only. GPT-6 Sol's old scores are not GPT-6.1 Sol scores; no comparable 6.1 effort table was verified on 2026-10-04. Do not infer ranking, guaranteed savings or Codex quota use from it. Max is not automatically better; do not merge public/private or AutomationBench-AA results.
- GPT-6.1 Sol is the normal workhorse: Medium for daily work, High for coupled logic/ambiguity, XHigh for exceptional depth or the US$20 override. Keep explicit well-verified cross-system workflows at Sol High when appropriate. Astra needs two genuine signals plus demanding coordination/long-context difficulty or costly hidden failures; do not require a failed Sol run. Do not count routine delivery alone as sufficient complexity.
- GPT-6.1 Sol supports no API None/Minimal. Ultra is client-specific and only when the exact combination is available; availability does not authorize delegation.
<!-- model-router:global-end -->
