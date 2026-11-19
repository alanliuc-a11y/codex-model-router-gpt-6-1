# Codex Model Router — GPT-6.2 + GPT-6.1 Sol, value first

**English** | [Chinese guide](README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-7c3aed.svg)](LICENSE) [![Latest release](https://img.shields.io/github/v/release/alanliuc-a11y/codex-model-router-gpt-6-1?display_name=tag&color=06b6d4)](https://github.com/alanliuc-a11y/codex-model-router-gpt-6-1/releases)

Choose a capable model and reasoning effort before work begins. Select the recommendation yourself, then send `go`. The router does not silently switch models, change speed settings or guarantee fixed token savings.

## v1.4.0: newer models, not newer-at-any-cost

Candidates: **GPT-6 Luna, GPT-6.1 Terra, GPT-6.1 Sol, GPT-6.2 Sol and GPT-6.2 Astra**. GPT-6.1 Sol remains an active value choice, not an obsolete fallback. Luna and Terra keep their verified versions.

Choose by quality, real availability, context, effort and rework. The **ChatGPT Plus** strategy retains a proven 6.1 Sol baseline; the **ChatGPT Pro** strategy considers 6.2 Sol first but retains 6.1 for proven value or preference. These are project policies, not official OpenAI routing algorithms.

The official Standard-speed credit rates for Sol 6.1 and 6.2 match. Neither is automatically cheaper per completed task. Official subscription guidance also expressly exempts 6.1 Sol from long-context surcharge. Check your actual allowance and fixed mode; do not convert API prices into included tasks. [Official pricing](https://learn.chatgpt.com/docs/pricing), reviewed November 19, 2026.

## Step 1 — Install for your subscription

Use your **official subscription name**, not a monthly-price band. Choose one strategy; do not infer your plan from model access or a dollar amount.

### ChatGPT Plus

Paste this complete request into Codex:

```text
Use the Skill Installer to install v1.4.0 from alanliuc-a11y/codex-model-router-gpt-6-1, path profiles/20-usd, named model-router-20, for the ChatGPT Plus value-first strategy. Run the installed global-routing script, then scripts/router-update.py enable-hooks with an available Python 3.10+ runtime. Preserve my other AGENTS.md rules and hooks. Explain required hook review without bypassing trust. Ask before installing a runtime and report which steps are verified.
```

### ChatGPT Pro

```text
Use the Skill Installer to install v1.4.0 from alanliuc-a11y/codex-model-router-gpt-6-1, path ., named model-router, for the ChatGPT Pro strategy. Run the installed global-routing script, then scripts/router-update.py enable-hooks with an available Python 3.10+ runtime. Preserve my other AGENTS.md rules and hooks. Explain required hook review without bypassing trust. Ask before installing a runtime and report which steps are verified.
```

Business, Enterprise, Edu, Free/Go and API-key setups need their own seat, model-availability and usage checks; do not silently assign them Pro rules or promise all five models. Pro variants also differ in allowance.

The identifiers `model-router-20` and `profiles/20-usd` are historical compatibility paths, **not subscription selection labels**. Keep them so old installers/updaters work. The repository URL likewise keeps its historical `gpt-6-1` suffix; that is not a model-version limit.

### Download manually

Download the [v1.4.0 ZIP](https://github.com/alanliuc-a11y/codex-model-router-gpt-6-1/archive/refs/tags/v1.4.0.zip). Copy `profiles/20-usd` to `<CODEX_HOME>/skills/model-router-20` for Plus, or the root package files to `<CODEX_HOME>/skills/model-router` for Pro.

Keep `SKILL.md`, `GLOBAL-ROUTING.md`, `version.json`, `agents/`, `references/` and `scripts/` together. Back up an existing install outside skill discovery first. Install only one strategy.

From the installed skill folder:

**Windows PowerShell**

```powershell
.\scripts\global-routing.ps1
python .\scripts\router-update.py enable-hooks
```

**macOS / Linux**

```sh
sh ./scripts/global-routing.sh
python3 ./scripts/router-update.py enable-hooks
```

Use a working Python 3.10+ executable, with its full path if needed. Default Codex home is `%USERPROFILE%\.codex` on Windows or `~/.codex` elsewhere. Setup preserves unrelated rules/handlers and backs up changed files.

Review and trust hooks in the supported client controls; Codex CLI uses `/hooks`. A restart/new session may be needed. Written config does not prove desktop execution. Without hook support/trust, normal routing works but automatic reminders do not. [Official hooks](https://learn.chatgpt.com/docs/hooks)

## Step 2 — Use it

After installation and global setup, **type normally without a prefix on every message or conversation**. Mentioning a skill once is not a permanent switch; the global setup enables this behavior.

1. Describe your task.
2. Read the model and reasoning recommendation.
3. Select that combination in Codex.
4. Send `go` as a standalone message.

Example for the Plus strategy:

```text
Model: GPT-6.1 Sol; reasoning effort: Medium
Reason: This multi-step change can stay on the proven value baseline.
Action: Choose the model and reasoning effort in the model picker, then send "go".
```

Use `$model-router-20` or `$model-router`, matching the install, only to force routing-only output. `go ahead` is not the confirmation token. Follow-ups inherit the whole unresolved task; do not keep Luna/Terra merely because the last task used it.

## Models and effort

| Work | Candidate | Typical start |
| --- | --- | --- |
| Mechanical extraction or an exact transformation | GPT-6 Luna | Low/Medium |
| Bounded source-grounded writing, charts/screens, defined app flow or scoped known-cause fix with concrete checks | GPT-6.1 Terra | Medium; Low for modest judgment |
| Dense but bounded visual detail | GPT-6.1 Terra | High |
| Everyday multi-step work, synthesis and code changes beyond Terra's gate | Value-Sol: 6.1 or 6.2 | Medium; Low for explicit modest work |
| Coupled features, ambiguity, unknown/repeated bugs or tracing a cause across systems | Value-Sol: 6.1 or 6.2 | High |
| Exceptional single-domain depth or interacting causes | Value-Sol: 6.1 or 6.2 | XHigh |
| Genuinely demanding integration/coordination or costly hidden failures | GPT-6.2 Astra | Low/Medium; High for weak validation/high stakes |

These are project starting points, not official defaults or measured equivalences. Luna needs one narrow explicit outcome, no investigation/design or coupled changes, and cheap direct checks. Terra excludes repeated unknown bugs, coupled lifecycle/role/permission/data-flow changes, conflicting evidence and costly hidden failures. A screenshot as step one does not make the whole task a Terra task.

Astra needs two genuine complexity signals plus demanding coordination, long dependencies or costly hidden failures. Routine delivery or multiple files alone is insufficient; no failed Sol run is required for an already demanding task.

### Subscription strategies

- **ChatGPT Plus:** preserve a proven GPT-6.1 Sol baseline. Use 6.2 Sol for explicit choice, a concrete need or credible same-input/effective-effort evidence of lower total usage/rework. Do not claim 6.1 is always cheaper.
- **ChatGPT Pro:** 6.2 Sol is a general starting candidate; retain 6.1 for preference, proven value or a better context/billing tradeoff. Extra allowance is not a reason to always use Astra.
- **Plus conservation mapping, once:** a base Astra Low/Medium route becomes selected value-Sol XHigh, normally GPT-6.1 Sol; 6.2 Sol is used only when justified above. Astra High/XHigh/Max/Ultra becomes GPT-6.2 Astra Low. Do not remap that result or change Luna/Terra/Sol base routes. Reduced effort is not equivalent quality; explicit supported user requirements take precedence.
- **Pro:** no Plus conservation mapping. Preserve the base route.

The dated [pricing and value policy](references/pricing-policy.md) contains the credit-rate table and billing distinctions. Compare real output quality, effort, context/caching, time to a usable result, usage and repair work before claiming savings.

### Availability and context

The reviewed local catalog lists Low through Max on all five and Ultra except Luna; it does not prove a user's picker. None/Minimal are not reviewed Codex choices even if an API supports them. Ultra may delegate, so availability is not authorization. Speed settings stay unchanged.

Codex documents default context of 272,000 tokens for 6.2 Astra and 500,000 for 6.2 Sol, separate from model/API capacities. Long input alone does not justify Astra; check fit and billing without changing settings or silently dropping sources. Terra's documented CLI minimum remains 0.159.0; do not assume 6.2 access from that minimum. [Official model/context guidance](https://learn.chatgpt.com/docs/models), [6.2 effort guidance](https://learn.chatgpt.com/guides/prompting-gpt-6-2-astra)

## Updates — only when you ask

Publishing v1.4.0 on GitHub **does not upgrade your local installation**. Keep the old version to test the process. Publication/validation runs use isolated test homes, not the active skill, AGENTS.md, hooks or client settings.

On v1.2.1 or later, send `check router update` to check only, or `update router` to authorize a same-strategy upgrade. Neither executes a task waiting for confirmation. A verified newer release can add one fourth routing line:

> Update: Model Router <version> is available. Send "update router" to update.

Checks read cache in the foreground and refresh asynchronously at most once per 24 hours, including failures. Manual checks may bypass the cache. The first notice may appear on a later task. API rate limits use GitHub's canonical latest-release fallback without credentials. Only a stable Release, not a branch commit, triggers updates.

For an unavailable updater or old install, paste:

```text
Update my installed Codex Model Router to v1.4.0 from alanliuc-a11y/codex-model-router-gpt-6-1. Preserve my strategy and existing identifiers: profiles/20-usd/model-router-20 for ChatGPT Plus, root/model-router for ChatGPT Pro. Back up the skill and AGENTS.md/hooks.json outside skill discovery before reinstalling with the Skill Installer, which does not overwrite existing folders. Run global setup and verify version.json/file hashes. Preserve unrelated rules, hooks and whether reminders were enabled. Enable reminders only if previously enabled or I request them. Explain trust review without bypassing it. Keep one active router and restore the original install/config if setup fails.
```

Updates stage and verify the selected package, retain complete backups and roll back caught replacement failures. Hashes detect damage, not a compromised repository. Crashes or failed restoration may require manual recovery. Customized package files/Git checkouts require manual upgrades. [Testing and recovery](docs/update-testing.md)

No prompts or credentials are sent to GitHub, but public requests expose normal network metadata. Reminders are not OS push notifications or one-click installers. No notice means no verified newer release, not proof of a successful check.

Disable reminders with `python scripts/router-update.py disable-hooks`; disable routing separately with the global script's `-Disable`/`--disable`. Use `-Preview`/`--preview` to preview routing changes. Disable both before uninstalling.

## Historical workflow screenshots

These authentic older captures show selection and confirmation, not current model choices. They were not relabeled as 6.2 captures.

![Historical Luna selection](docs/screenshots/en-01-switch-luna-light.png)
![Historical confirmation](docs/screenshots/en-02-confirm-go.png)
![Historical Sol confirmation](docs/screenshots/en-03-sol-confirm-go.png)
![Historical Astra selection](docs/screenshots/en-04-astra-switch.png)
![Historical Astra confirmation](docs/screenshots/en-05-astra-confirm-go.png)

## Validation and contributing

No fixed saving percentage or older benchmark relabeling. Updater/package tests do not prove model-routing quality. Use [routing acceptance cases](docs/routing-cases.md) on real tasks.

Run `python -m unittest discover -s tests -v`. The Skill Creator's `quick_validate.py <skill-folder>` checks structure. Release packaging uses `scripts/build-manifests.py`. Both strategies bundle `references/pricing-policy.md` and `references/updating.md`.

See [changelog](CHANGELOG.md), [contribution guide](CONTRIBUTING.md), [update acceptance](docs/update-testing.md) and the [MIT license](LICENSE).

Search terms: save Codex tokens · GPT-6.2 Sol · GPT-6.2 Astra · GPT-6.1 Sol value · ChatGPT Plus · ChatGPT Pro · model routing · reasoning effort · update reminders.
