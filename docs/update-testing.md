# Update reminders: setup, testing and recovery

## What is and is not verified

The repository includes automated offline integration tests for both package profiles, cache behavior, language separation, authorization, preservation of unrelated configuration, unsafe/damaged archives and caught-failure rollback. These are script tests, not proof of desktop hook execution or model response quality. Complete the manual acceptance below on your actual client.

## Setup

1. Follow the [README](../README.md) to install one v1.2.1 profile. Earlier versions cannot detect this feature before upgrading once.
2. Use an available Python 3.10+ executable. From the installed skill folder, run the global-routing script, then `python scripts/router-update.py enable-hooks` (use `python3` on macOS/Linux).
3. Review and trust both new hook handlers in your client's supported hook controls. In Codex CLI, use `/hooks`. Restart or open a new session if configuration is not reloaded. If your desktop client lacks that interface/support, keep ordinary routing and use manual checks; do not assume configuration means execution.
4. Automatic checks run on user prompts, not while Codex is closed. The foreground handler only reads cache; the async handler refreshes it at most once per 24 hours, including failed attempts. Explicit checks bypass the cache. The first check may not affect the current response. [Official hook lifecycle](https://learn.chatgpt.com/docs/hooks)

## Real-client acceptance

1. **Normal task:** submit a clear table-formatting task. Expect three routing lines with one model and effort. Do not expect a reminder when the installed release is current.
2. **Confirmation:** select the recommended model and send `go`. Expect the original task to execute; no new routing gate or update notice.
3. **Check:** send `check router update`. Expect a verified release/status report, or an unavailable-check report—not a false “up to date” claim.
4. **Future newer release:** after a newer stable Release is published, wait for the next allowed refresh or run the manual check. On a new task, expect at most one English update line below the recommendation. Test the equivalent flow in the other language using its matching guide.
5. **Update command:** send `update router`. Expect the same installed profile, a verified installed version and a retained backup path. This does not authorize the pending task. Review changed hooks again if prompted; start a new turn/session to load the upgrade.
6. **Offline:** disconnect networking and submit a task. Routing must remain usable. A previously verified notice can remain for up to seven days; an unavailable check cannot prove the release is current.
7. **Disable:** run `python scripts/router-update.py disable-hooks`, reload the client, then submit a task. Routing remains, and these reminders stop; unrelated hooks remain.

Do not fabricate a public release or edit production cache to demonstrate a newer version. The offline test suite supplies synthetic releases in temporary installs, without touching real user configuration.

## Automated tests

From the repository checkout:

```sh
python -m unittest discover -s tests -v
```

Tests create and remove only their own temporary folders under `tests/`; they perform no network access. Release preparation regenerates both manifests with `python scripts/build-manifests.py`. GitHub CI tests Windows, macOS and Linux; use its actual run result, not the workflow file's presence, as cross-platform evidence.

## Recovery and boundaries

Updates use the latest stable Release, not arbitrary main-branch commits. Package text hashes normalize Windows line endings. Hashes share the repository's trust boundary; they are not an independent release signature.

The updater retains a transaction folder under `<CODEX_HOME>/skill-backups/router-update-.../`: `previous/` contains the old complete skill; `AGENTS.md` and `hooks.json`, if originally present, contain exact configuration backups. A failed replacement can also leave `failed/`. Caught installation failures automatically restore the old install/config; an abrupt OS/process crash or failure to write during restoration may require manual recovery.

For manual recovery, stop updater activity, preserve any new work, and ask Codex to restore only that transaction's previous profile and configuration files. Do not delete a broad skills directory or unrelated rules. Review hooks afterward. Backups are not automatically deleted.

The updater refuses modified package files and Git checkouts, rather than discarding customizations. An ordinary manual upgrade can preserve those changes with your approval. If the captured Python executable moves, re-run hook setup with a working runtime. Disable routing separately with its global-routing script; disable both routing and reminders before uninstalling.
