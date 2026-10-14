# Contributing

Thank you for helping improve GPT-6.1 Sol Codex Model Router (package v1.2.1).

The default catalog is GPT-6 Luna, GPT-6.1 Sol and GPT-6 Astra. Recheck official documentation and the client catalog before changing it; do not relabel older benchmark scores as a newer model's results. Installation changes must update fresh-install, ZIP-download and existing-install upgrade instructions in both languages.

Useful contributions include:

- a reproducible installation or global-routing issue;
- a routing case where the recommendation was clearly too weak or too costly;
- a documentation or translation correction;
- a tested improvement that keeps the managed Codex catalog intact.

Before opening an issue, check that the task began in a new Codex turn and include the Codex version, operating system, available model-picker options, task type, expected route, actual route, and any safe-to-share error output. Never include API keys, private prompts, customer data, or screenshots containing sensitive information.

For pull requests, keep the change focused, explain the user-visible effect, and update both English and Chinese documentation when the workflow changes.

This project recommends model and reasoning choices. It must not claim automatic model switching, fixed token savings, or access to a user's current picker selection.

For updater changes, run `python -m unittest discover -s tests -v`; update both installable copies of `scripts/router-update.py` and `references/updating.md`, then run `python scripts/build-manifests.py`. The manifests hash LF-normalized package text, excluding the manifest itself. A release-version change must update the builder, both skill headers, bilingual fresh-install/ZIP/upgrade instructions, release notes and changelog. Never rewrite published tags. Create a new stable GitHub Release only after its tagged package passes verification; a branch push alone does not notify users.

Test offline checks, authorization, language separation, both profiles, preserved unrelated config, broken downloads and rollback. Do not bypass hook trust in client acceptance tests. CI checks scripts and package integrity; it does not prove desktop hook execution or model-routing quality. Manual acceptance: [English](docs/update-testing.md), [Chinese](docs/update-testing.zh-CN.md).
