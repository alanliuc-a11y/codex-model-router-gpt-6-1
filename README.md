# Codex Model Router: GPT-6.2 + value-aware Plus / Pro 100 / Pro 200 / Pro 500

**English** | [Chinese guide](README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-7c3aed.svg)](LICENSE) [![Latest release](https://img.shields.io/github/v/release/alanliuc-a11y/codex-model-router-gpt-6-1?display_name=tag&color=06b6d4)](https://github.com/alanliuc-a11y/codex-model-router-gpt-6-1/releases)

Choose a capable model and reasoning effort before work begins. Select the recommendation yourself, then send `go`. The router does not silently switch models, change speed settings or guarantee fixed token savings.

## v1.5.0: newer models, not newer-at-any-cost

Candidates: **GPT-6 Luna, GPT-6.1 Terra, GPT-6.1 Sol, GPT-6.2 Sol and GPT-6.2 Astra**. GPT-6.1 Sol remains an active value choice, not an obsolete fallback. Luna and Terra keep their verified versions.

Choose by quality, real availability, context, effort and rework. The **ChatGPT Plus** strategy retains a proven 6.1 Sol baseline; the **ChatGPT Pro 100** favors the proven 6.1 Sol baseline; **Pro 200 / Pro 500** consider 6.2 Sol first but retain 6.1 for value or preference. These are project policies, not official OpenAI routing algorithms.

The official Standard-speed credit rates for Sol 6.1 and 6.2 match. Neither is automatically cheaper per completed task. Official subscription guidance also expressly exempts 6.1 Sol from long-context surcharge. Check your actual allowance and fixed mode; do not convert API prices into included tasks. [Official pricing](https://learn.chatgpt.com/docs/pricing), reviewed November 19, 2026.

## Step 1 — Paste the repository link and install

Send this to Codex:

```text
Install https://github.com/alanliuc-a11y/codex-model-router-gpt-6-1 at v1.5.0. Read INSTALL.md first and ask me to click Plus / Pro 100 / Pro 200 / Pro 500 before installing. Preserve unrelated settings and the current reminder preference.
```

Click your subscription once; the chosen skill package remembers the strategy. Do not type a plan name. Native choice controls require a supported host tool; if unavailable, installation pauses and explains why. A README link alone cannot force a client dialog. A plan explicitly supplied with the install request skips the question. Other plans/API-key billing are not supported by this four-option installer.

| Choice | Package path | Strategy |
| --- | --- | --- |
| Plus | profiles/20-usd | Proven 6.1 Sol baseline; existing Astra conservation mapping |
| Pro 100 | profiles/pro-100 | Proven 6.1 Sol value; direct Astra when genuinely needed, lowest adequate effort |
| Pro 200 | profiles/pro-200 | 6.2 Sol balance; Astra Medium/High for demanding integration |
| Pro 500 | profiles/pro-500 | Difficult-work quality first; Astra High for costly integration, XHigh exceptionally |

All preserve Luna/Terra eligibility, supported explicit choices and 6.1 Sol value. These are project strategies, not guaranteed official quotas. Speed is never changed. Legacy generic Pro at the repository root remains only for existing same-profile updates; do not infer its Pro tier. [Install details](INSTALL.md).

### Download manually

Download the [v1.5.0 ZIP](https://github.com/alanliuc-a11y/codex-model-router-gpt-6-1/archive/refs/tags/v1.5.0.zip). Use the selected path above; install it under its manifest profile name in `<CODEX_HOME>/skills/`. Keep only one active router.

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

Use the four-strategy installation table above. Each chosen package contains its own rules and identity. All Pro strategies retain direct Astra routing when warranted; only Plus uses its existing conservation mapping. Legacy root model-router remains generic Pro, preserved for existing upgrades, and is not the new-install default. Model effort follows task difficulty, not plan rank alone.

### Availability and context

The reviewed local catalog lists Low through Max on all five and Ultra except Luna; it does not prove a user's picker. None/Minimal are not reviewed Codex choices even if an API supports them. Ultra may delegate, so availability is not authorization. Speed settings stay unchanged.

Codex documents default context of 272,000 tokens for 6.2 Astra and 500,000 for 6.2 Sol, separate from model/API capacities. Long input alone does not justify Astra; check fit and billing without changing settings or silently dropping sources. Terra's documented CLI minimum remains 0.159.0; do not assume 6.2 access from that minimum. [Official model/context guidance](https://learn.chatgpt.com/docs/models), [6.2 effort guidance](https://learn.chatgpt.com/guides/prompting-gpt-6-2-astra)

## Updates — only when you ask

Publishing v1.5.0 on GitHub **does not upgrade your local installation**. Keep the old version to test the process. Publication/validation runs use isolated test homes, not the active skill, AGENTS.md, hooks or client settings.

On v1.2.1 or later, send `check router update` to check only, or `update router` to authorize a same-strategy upgrade. Neither executes a task waiting for confirmation. A verified newer release can add one fourth routing line:

> Update: Model Router <version> is available. Send "update router" to update.

Checks read cache in the foreground and refresh asynchronously at most once per 24 hours, including failures. Manual checks may bypass the cache. The first notice may appear on a later task. API rate limits use GitHub's canonical latest-release fallback without credentials. Only a stable Release, not a branch commit, triggers updates.

For an unavailable updater or old install, paste:

```text
Update my installed Codex Model Router to v1.5.0 from alanliuc-a11y/codex-model-router-gpt-6-1. Preserve my strategy and existing identifiers: profiles/20-usd/model-router-20 for ChatGPT Plus, the existing manifest identity for Pro; never infer a numbered Pro tier from legacy model-router. Back up the skill and AGENTS.md/hooks.json outside skill discovery before reinstalling with the Skill Installer, which does not overwrite existing folders. Run global setup and verify version.json/file hashes. Preserve unrelated rules, hooks and whether reminders were enabled. Enable reminders only if previously enabled or I request them. Explain trust review without bypassing it. Keep one active router and restore the original install/config if setup fails.
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
