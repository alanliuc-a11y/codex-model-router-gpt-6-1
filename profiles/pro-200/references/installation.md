# Installation subscription choice

For an explicit install request, read this before installing or changing any configuration. A bare URL is not installation authorization. Do not install a default first and ask later.

If the user already explicitly chose one of the four supported names for this install, use it without asking again. Otherwise call the host native choice tool with ONE question and exactly these four option labels in this order: Plus, Pro 100, Pro 200, Pro 500. Chinese title: “你当前用于 Codex 的订阅是哪一档？” English title: “Which subscription do you use with Codex?” Do not add “Recommended” to a subscription label or infer the subscription from a preselection. If available, use request_user_input_async with the four strings in options; discover an equivalent native input tool when necessary. The tool must actually support four choices in the current mode. Wait for an explicitly submitted choice before installing; timeout, default focus and free-text drafts are not choices. Do not call a tool with an unsupported schema.

Do not ask the user to type a plan name. If the host has no usable four-choice control, report that installation is paused because this client cannot display the required selector. Do not fake buttons with Markdown links, claim buttons appeared, silently choose Plus, or alter client mode. A skill cannot guarantee interactive controls on every client. An explicit supported plan provided in the original install request still works.

If the user reports another plan, API-key billing, or uncertainty, explain that this release supports only these four subscriptions and pause to resolve the mismatch. Do not guess. A selected plan is user-reported, not verified account entitlement or remaining quota.

| Selection | GitHub path | Installed skill identity |
| --- | --- | --- |
| Plus | profiles/20-usd | model-router-20 |
| Pro 100 | profiles/pro-100 | model-router-pro-100 |
| Pro 200 | profiles/pro-200 | model-router-pro-200 |
| Pro 500 | profiles/pro-500 | model-router-pro-500 |

Install v1.5.0 with the available Skill Installer. The manifest profile and the skill's own policy persist the selected strategy; do not ask on each task. Only one router may be active. Before replacing an existing router, back it up outside skill discovery, preserve unrelated AGENTS.md/hooks, and replace only the managed global block using the selected package's global-routing script. Use the existing Python 3.10+ runtime for router-update.py enable-hooks only if reminders were requested or already enabled. Preserve disabled reminders on upgrades. Review/trust remains a user client step, never bypass it. If a dependency is missing, report before installing it. Verify manifest hashes, profile and managed global block; distinguish config writing from actual client operation. Restore the original configuration/install if setup fails.

Same-profile maintenance updates never show the install selector and must not change subscription strategies. Old model-router remains a legacy generic-Pro identity; preserve it until the user explicitly requests a tier selection. Do not infer Pro 100/200/500 from its name. Changing tiers is an explicit reinstallation, not an implicit update. Repository publication and isolated testing never authorize upgrading the real local install.
