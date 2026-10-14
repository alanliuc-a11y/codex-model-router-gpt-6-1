# Release reminders and explicit upgrades

Read this reference only for router maintenance, not for ordinary task routing.

## Commands and authorization

- A standalone Chinese `检查路由器更新` or English `check router update` authorizes a release check only. Run the installed `scripts/router-update.py check --force`; report verified status in the user's language. An unavailable check is not evidence that the install is current.
- A standalone Chinese `更新路由器` or English `update router` authorizes upgrading this router only. It is maintenance, not confirmation to execute a pending task. Run `scripts/router-update.py update --confirm` from the installed profile. Do not prepend a model gate to this maintenance command. Translate the structured result; report version, backup and required hook review. Do not execute the pending task afterward.
- Use Python 3.10+ from the user's available runtime. Do not install Python or change unrelated system settings without permission. Pass `--codex-home` for a custom Codex home. Network access and out-of-workspace writes remain subject to host approvals.
- Only the exact standalone maintenance phrases qualify; a quoted phrase inside another task is not update authorization.

## Setup

After installing, run the profile's existing global-routing script, then `python scripts/router-update.py enable-hooks`. This merges two UserPromptSubmit handlers into user-level `hooks.json`: a synchronous cache-only notice reader and an asynchronous daily release refresher. It preserves other handlers, creates a backup when replacing configuration, and removes the router's own previous handlers to avoid duplicates. The Python executable path is captured during setup. Re-run setup if that runtime moves.

Review and trust the hooks in the supported client's hook controls (Codex CLI: `/hooks`). Do not bypass trust, edit trust records, or claim the desktop client ran a hook just because configuration was written. Changed definitions need review again. If the installed client does not support hooks, ordinary routing still works; use the manual check command.

Disable reminders with `python scripts/router-update.py disable-hooks`. This does not disable routing or remove other hooks. The existing global-routing disable script manages routing only. To uninstall this router completely, disable its reminders and routing before moving its skill folder outside the skills directory.

## Notice contract

Normal routing remains exactly three lines. Append one fourth update line only when fresh-enough, validated local hook context verifies a newer stable release. Chinese: `更新：模型路由器已有新版（<版本>），输入“更新路由器”即可更新。` English: `Update: Model Router <version> is available. Send "update router" to update.` Use the same language as the routing response. Never fetch a release with model tools before routing or fabricate a notice from memory.

No notice on confirmation, maintenance commands, or task execution. Never interpret a notice as installation authority. The release refresher sends no prompt, chat or account information to GitHub. Its public requests disclose normal network metadata such as IP and user-agent. Only stable numeric releases from the managed repository are accepted; no arbitrary URL, draft, prerelease or downgrade. Regular refreshes, including failed attempts, are cached for 24 hours. An explicit manual check can bypass that cache. Previously verified notices expire after seven days. Concurrent refreshes are locked; offline/errors are quiet. A first background check can miss the current response; the notice can appear on a later task.

## Upgrade safety and limitations

The updater checks the latest release afresh, downloads its tagged source archive over HTTPS, stages only the active profile outside `skills`, verifies its version/name/file hashes, backs up the entire old folder and both configuration files, then replaces the profile and managed global rules. A caught installation/configuration failure restores the previous folder and exact original config bytes. Failures before replacement leave the active install intact. An abrupt OS/process crash is not covered by the automatic rollback; retained transaction files support manual recovery.

`version.json` lists SHA-256 hashes for LF-normalized package text files. These detect damage and inconsistent packaging while accepting Windows line endings; they are not an independent signature against a compromised repository. Updating executes trusted upstream skill instructions/scripts on subsequent use. Never silently install updates.

The updater refuses modified tracked package files, linked managed directories and Git-based installs. Preserve customizations and use a manual upgrade instead. Untracked additions remain in the full backup, not in the new active package. OS-level locks prevent concurrent replacement and are released when the process ends, including a crash; the persistent lock file alone does not indicate an active operation. Backups stay outside skill discovery and are never pruned automatically.

Existing v1.1.0 users must upgrade once through the Skill Installer or manual copy before reminders and this updater exist. Preserve the active profile; do not install both. After an upgrade, the updated skill is available on the next turn; hook discovery may require a new session/restart and trust review. Do not promise an OS push notification or a one-click installation link.

Official hook contract, checked 2026-10-14: https://learn.chatgpt.com/docs/hooks
