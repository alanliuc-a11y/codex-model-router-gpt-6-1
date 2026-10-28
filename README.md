# GPT-6.1 Terra + Sol Codex Model Router — save tokens, choose the right model

**English** | [Chinese guide](README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-7c3aed.svg)](LICENSE) [![Latest release](https://img.shields.io/github/v/release/alanliuc-a11y/codex-model-router-gpt-6-1?display_name=tag&color=06b6d4)](https://github.com/alanliuc-a11y/codex-model-router-gpt-6-1/releases)

Model Router recommends a Codex model and reasoning effort before work begins. Select the recommendation yourself, then send `go` to continue. It does not silently switch your model, change speed settings or guarantee a fixed token saving.

## New in v1.3.0 — GPT-6.1 Terra

The router now chooses among **GPT-6 Luna, GPT-6.1 Terra, GPT-6.1 Sol and GPT-6 Astra**. Terra fills the gap between mechanical tasks and complex projects: source-based writing, interpreting charts/screens, defined computer-use tasks and scoped known-cause code fixes with clear checks.

This follows the [official Terra specifications](https://developers.openai.com/api/docs/models/gpt-6.1-terra) and [model-selection guidance](https://learn.chatgpt.com/docs/model-selection), reviewed October 28, 2026. Terra does not replace every Sol route, and a screenshot does not make a complex workflow simple.

The repository URL and skill names are unchanged, so existing installations can still find updates. Current package version: **v1.3.0**. GPT-6.1 is the model family, not the package version.

## Step 1 — Install

### Easiest: ask Codex to install it

Choose **one** allowance profile and paste the matching complete message into Codex. A bare repository URL is not an installation request.

**US$20 allowance profile**

```text
Use the Skill Installer to install v1.3.0 from GitHub repository alanliuc-a11y/codex-model-router-gpt-6-1, path profiles/20-usd, named model-router-20. Run the installed global-routing script, then use an available Python 3.10+ runtime to run scripts/router-update.py enable-hooks. Preserve my other AGENTS.md rules and hooks. Explain how to review and trust the new hooks; do not bypass trust or install a runtime without asking. Report which steps are verified.
```

**Higher-allowance profile, such as 5× or 20×**

```text
Use the Skill Installer to install v1.3.0 from GitHub repository alanliuc-a11y/codex-model-router-gpt-6-1, path ., named model-router. Run the installed global-routing script, then use an available Python 3.10+ runtime to run scripts/router-update.py enable-hooks. Preserve my other AGENTS.md rules and hooks. Explain how to review and trust the new hooks; do not bypass trust or install a runtime without asking. Report which steps are verified.
```

These are this project's allowance strategies, not official OpenAI plan names or usage guarantees. Both use the same four-model rubric. The US$20 profile applies one additional rule **after** the base route:

| Original Astra route | US$20 final recommendation |
| --- | --- |
| Astra Low or Medium | GPT-6.1 Sol XHigh |
| Astra High, XHigh, Max or Ultra | GPT-6 Astra Low |

Luna, Terra and Sol routes remain unchanged. Never remap the resulting Astra Low again or substitute Terra for the Astra override. These choices trade reasoning depth for allowance conservation; they are not quality equivalences. The higher-allowance profile keeps the base route unchanged.

### Download and install manually

Download the [v1.3.0 ZIP](https://github.com/alanliuc-a11y/codex-model-router-gpt-6-1/archive/refs/tags/v1.3.0.zip). For the US$20 profile, copy `profiles/20-usd` to `<CODEX_HOME>/skills/model-router-20`. For the higher-allowance profile, copy the root package files to `<CODEX_HOME>/skills/model-router`.

Keep these together: `SKILL.md`, `GLOBAL-ROUTING.md`, `version.json`, `agents/`, `references/` and `scripts/`. Back up an existing installation outside the skills directory before replacing it. Install only one profile.

Default Codex home is `%USERPROFILE%\.codex` on Windows and `~/.codex` on macOS/Linux. From the installed profile folder, run:

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

Use a working Python 3.10+ executable, substituting its full path when needed. The first command enables prefix-free routing by updating only the marked section in your user-level `AGENTS.md`, preserving other rules and creating a backup. The second merges reminder hooks while preserving unrelated handlers.

Review and trust the new hooks in your client's supported hook controls; Codex CLI uses `/hooks`. Start a new session or restart if needed. Writing configuration does not prove the client executed it. Without a supported client/runtime or hook trust, routing still works but automatic reminders do not. [Official hook documentation](https://learn.chatgpt.com/docs/hooks)

Terra requires Codex CLI **0.159.0 or newer**. Model access still depends on your plan, client, workspace and rollout; verify the actual picker rather than silently selecting a different model. [Codex model availability](https://learn.chatgpt.com/docs/models)

## Step 2 — Use it

Once installation and global setup are complete, **type tasks normally**. No prefix is needed for each message or conversation. Mentioning `$model-router` once is not a permanent switch; the setup above is what makes routing global.

1. Describe your task.
2. Read the recommended model and reasoning effort.
3. Select that combination in Codex.
4. Send `go` as a standalone message. Codex continues the original task.

The normal recommendation has three lines:

```text
Model: GPT-6.1 Terra; reasoning effort: Medium
Reason: The supplied source and clear checks make this a bounded writing task.
Action: Choose the model and reasoning effort in the model picker, then send "go".
```

Use `$model-router-20` or `$model-router`, matching your installed profile, only when you want to force a routing-only response. `go ahead` or a sentence containing `go` is not the confirmation token. A follow-up inherits the unresolved task's full scope; the router must not keep recommending Luna or Terra merely because a previous task used it.

## Which model should appear?

| Task | Base model | Typical starting effort |
| --- | --- | --- |
| Mechanical extraction, a specified table or exact text/CSS replacement | GPT-6 Luna | Low or Medium |
| Draft from supplied facts; interpret charts/screens; a defined app task; a scoped known-cause fix with regression checks | GPT-6.1 Terra | Medium; Low for limited judgment |
| Dense but still bounded visual detail or interpretation | GPT-6.1 Terra | High |
| Broader production work, multi-source synthesis, or a task not meeting the bounded Terra conditions | GPT-6.1 Sol | Medium |
| Coupled features, unknown/repeated bugs, lifecycle, permissions or uncertain diagnosis | GPT-6.1 Sol | High |
| Exceptional single-domain depth | GPT-6.1 Sol | XHigh |
| Demanding coordination, long dependencies or costly hidden failures meeting the Astra gate | GPT-6 Astra | Low/Medium; High for weak validation or high stakes |

These effort starting points are our routing policy, not measured model equivalences. Terra is not the default for ambiguous projects, coupled state/data-flow changes, repeated failures or costly hard-to-detect errors. Do not keep such work on Terra merely by raising effort to Max.

Luna still needs one narrow explicit outcome, no investigation/design or coupled changes, and cheap direct verification. Astra needs at least two genuine complexity signals plus demanding coordination, long-context difficulty or costly hidden failures; ordinary delivery or multiple files alone are insufficient. The US$20 mapping above is applied once, after this assessment.

The reviewed local Codex catalog lists Low through Max on all four models and Ultra on Terra, Sol and Astra. Options vary. Terra's API supports None, but this local Codex catalog does not expose it: **API support is not proof of a picker option**. Ultra is client-specific, and availability does not authorize delegation. Speed settings remain untouched.

## Updating an existing installation

On v1.2.1 or later, send `check router update` to check immediately, or `update router` to authorize a same-profile upgrade. An update command does not execute a task waiting for confirmation.

For an old install, an unavailable updater or a manual bootstrap, paste:

```text
Update my installed Codex Model Router to v1.3.0 from alanliuc-a11y/codex-model-router-gpt-6-1. Preserve my profile: profiles/20-usd for model-router-20, or . for model-router. Back up the existing skill and AGENTS.md/hooks.json outside skill discovery before using the Skill Installer, which does not overwrite existing folders. Install the same profile, run its global-routing script and verify version.json/file hashes. Preserve other rules and hooks, and keep only one active router. Preserve whether reminders were enabled; reconfigure them with scripts/router-update.py enable-hooks only if previously enabled or I request them. Explain any required trust review without bypassing it. Restore the old folder and configuration if setup fails.
```

When a newer stable release is verified, the recommendation can add one fourth line:

> Update: Model Router <version> is available. Send "update router" to update.

The foreground hook reads cache only. The asynchronous refresher checks at most once per 24 hours, including failed attempts; explicit manual checks can bypass the cache. Anonymous API rate limits fall back to GitHub's canonical latest-release link without credentials. The first notice can arrive on a later task. Offline checks do not block routing; an unavailable check is not proof you are current.

Only a newer stable **GitHub Release** triggers reminders, not a branch commit. No prompts, chat content or credentials are sent to GitHub; normal network metadata remains visible. Updates stage and verify the active profile, back up the full install/configuration, and roll back caught replacement failures. Backups are retained, and disabled reminders stay disabled. Hashes detect damage, not a compromised repository.

This is not an OS push notification or a one-click installation link. Modified package files and Git checkouts require a manual upgrade. A crash or failed restoration can need manual recovery. See [testing and recovery](docs/update-testing.md).

Disable reminders with `python scripts/router-update.py disable-hooks`. Disable routing separately with the global script's `-Disable` or `--disable`; use `-Preview` or `--preview` to preview routing changes. Disable both before uninstalling.

## Authentic workflow screenshots

These older screenshots show the interaction, **not current model choices**. They have not been relabeled as Terra screenshots.

![Historical Luna selection](docs/screenshots/en-01-switch-luna-light.png)
![Historical confirmation step](docs/screenshots/en-02-confirm-go.png)
![Historical Sol confirmation](docs/screenshots/en-03-sol-confirm-go.png)
![Historical Astra selection](docs/screenshots/en-04-astra-switch.png)
![Historical Astra confirmation](docs/screenshots/en-05-astra-confirm-go.png)

## Does it save 60% of tokens?

We do not claim a fixed percentage. Compare representative tasks using the same sources, inputs and effort; then vary effort separately. Record correctness, total usage, time to a usable result and rework. A smaller model is only more efficient when it still meets the acceptance criteria.

API token prices do not measure Codex subscription allowance. Old GPT-6 Sol benchmark scores are not GPT-6.1 Terra or Sol scores, and this release does not claim a comparable AutomationBench effort ranking. [Official comparison guidance](https://learn.chatgpt.com/docs/model-selection)

## Project files and contributing

- `SKILL.md`, `GLOBAL-ROUTING.md`, `agents/openai.yaml`: routing instructions, global fallback and UI metadata.
- `profiles/20-usd/`: independently installable US$20 profile.
- `scripts/router-update.py`, `version.json`, `references/updating.md`: reminders, package verification and explicit upgrades.
- `scripts/build-manifests.py`, `tests/test_updates.py`: release packaging and offline updater tests.
- [Routing acceptance cases](docs/routing-cases.md), [update acceptance tests](docs/update-testing.md), [changelog](CHANGELOG.md) and [contribution guide](CONTRIBUTING.md).

Run `python -m unittest discover -s tests -v` for offline integration checks. The Skill Creator's `quick_validate.py <skill-folder>` checks skill structure, not routing quality. Test actual recommendations on representative tasks before relying on them. Code and these skills are [MIT licensed](LICENSE).

Search terms: save Codex tokens · reduce token usage · Codex model routing · GPT-6.1 Terra · GPT-6.1 Sol · GPT-6 Astra · GPT-6 Luna · reasoning effort · skill update reminders.
