# Contributing

Codex Model Router v1.4.0 supports ChatGPT Plus / ChatGPT Pro project strategies with cost-aware candidates: GPT-6 Luna, GPT-6.1 Terra, GPT-6.1 Sol, GPT-6.2 Sol and GPT-6.2 Astra.

Keep model capability, effort, subscription allowance, purchased-credit rates and API billing separate. Refresh official model/pricing evidence before changing rates or entitlements. Do not retire 6.1 Sol just because a newer model launched; compare total quality, usage, context and rework.

Use official subscription names for user choices, not dollar bands. Historical skill/directory IDs stay compatible. Other plans/seats need actual availability/usage checks, not an assumed Pro mapping. Keep existing user-supported choices and never claim equal quality or guaranteed savings from an effort downgrade.

Update both installable profiles, global fallbacks, UI metadata, bilingual fresh-install/use/upgrade/ZIP guidance and release notes together. Keep English/Chinese routing prompts separate. Historical screenshots/benchmarks/releases stay identified as history.

Shared resources are `references/updating.md` and `references/pricing-policy.md`; both copies and the updater scripts must match. Run `python scripts/build-manifests.py` after changing packaged files. The manifest hashes LF-normalized text, not itself, and is not an independent release signature. An older installed updater must be able to stage the newer manifest's resources.

Run `python -m unittest discover -s tests -v`, validate both skill structures, and check links/languages/available combinations. [Routing cases](docs/routing-cases.md) are manual behavior checks, not proof from updater tests. Check saving claims on representative tasks using the same effective effort first.

Publishing/validation never authorizes upgrading the maintainer's actual local skill or touching AGENTS.md, hooks or client settings. Use isolated test homes, verify backups/rollback/preserved unrelated config there, and wait for a separate explicit local-upgrade request. Never bypass hook trust.

Keep the repository URL stable for installed updaters; refresh public titles, descriptions and topics instead. Do not rewrite published tags. Create a stable GitHub Release only after its tagged package passes checks; a branch commit alone does not trigger reminders.

Report a reproducible task, OS/client version, safe model-picker information, installed strategy/version, expected/actual route and sanitized error output. Never include credentials, private prompts, customer data or sensitive screenshots. Model routing does not switch an already-running root model or reveal a hidden picker selection.

Further guidance: [English update acceptance](docs/update-testing.md), [Chinese update acceptance](docs/update-testing.zh-CN.md), [Chinese price explanation](docs/pricing.zh-CN.md), [changelog](CHANGELOG.md).
