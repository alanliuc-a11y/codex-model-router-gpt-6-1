#!/usr/bin/env python3
"""Cached release reminders and explicit, backup-first upgrades; Python 3.10+."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shlex
import stat
import subprocess
import sys
import tempfile
import time
import urllib.request
import uuid
import zipfile

REPO = "alanliuc-a11y/codex-model-router-gpt-6-1"
RELEASES = f"https://github.com/{REPO}/releases"
API = f"https://api.github.com/repos/{REPO}/releases/latest"
OWNER = "model-router-updates"
DAY = 86400
MAX_DOWNLOAD = 32 * 1024 * 1024
START = "<!-- model-router:global-start -->"
END = "<!-- model-router:global-end -->"
PROFILES = {"model-router": ".", "model-router-20": "profiles/20-usd"}
REQUIRED = {"SKILL.md", "GLOBAL-ROUTING.md", "agents/openai.yaml",
            "scripts/global-routing.ps1", "scripts/global-routing.sh",
            "scripts/router-update.py", "references/updating.md"}


class UpdateError(Exception):
    pass


def version(value):
    match = re.fullmatch(r"v?(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", str(value))
    if not match:
        raise UpdateError("Expected a stable major.minor.patch version.")
    return tuple(map(int, match.groups()))


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def atomic_write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".router-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def write_json(path, data):
    atomic_write(path, (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))


def safe_child(root, relative):
    parts = PurePosixPath(relative).parts
    if not parts or any(p in (".", "..") or ":" in p or "\\" in p for p in parts) or relative.startswith("/"):
        raise UpdateError("Unsafe package path.")
    target = root.joinpath(*parts)
    if not target.resolve().is_relative_to(root.resolve()):
        raise UpdateError("Path escapes its managed directory.")
    return target


def no_links(path):
    reparse = path.exists() and bool(getattr(path.lstat(), "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0))
    if path.is_symlink() or reparse:
        raise UpdateError("Linked managed paths are not supported.")


def validate_manifest(data, profile=None, expected=None):
    if not isinstance(data, dict) or data.get("schema") != 1 or data.get("repository") != REPO:
        raise UpdateError("Invalid package manifest or repository.")
    version(data.get("version"))
    name = data.get("profile")
    if name not in PROFILES or data.get("source_path") != PROFILES[name] or (profile and name != profile):
        raise UpdateError("Package profile mismatch.")
    if expected and version(data["version"]) != version(expected):
        raise UpdateError("Release and package versions differ.")
    files = data.get("files")
    if not isinstance(files, dict) or not REQUIRED.issubset(files) or len(files) > 100 or "version.json" in files:
        raise UpdateError("Incomplete package file list.")
    for name, digest in files.items():
        safe_child(Path.cwd(), name)
        if not re.fullmatch(r"[a-f0-9]{64}", str(digest)):
            raise UpdateError("Invalid package checksum.")
    return data


def load_package(root):
    return validate_manifest(read_json(root / "version.json"))


def verify_package(root, manifest):
    for relative, digest in manifest["files"].items():
        path = safe_child(root, relative)
        no_links(path)
        if not path.is_file() or hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest() != digest:
            raise UpdateError("Package file verification failed; preserve local edits and reinstall manually.")
    skill = (root / "SKILL.md").read_text(encoding="utf-8-sig")
    if not re.search(r"^name:\s*" + re.escape(manifest["profile"]) + r"\s*$", skill, re.M):
        raise UpdateError("Skill name does not match the selected profile.")
    fragment = (root / "GLOBAL-ROUTING.md").read_text(encoding="utf-8-sig")
    if fragment.count(START) != 1 or fragment.count(END) != 1:
        raise UpdateError("Invalid global routing markers.")


def managed_home(value=None):
    home = Path(value or os.environ.get("CODEX_HOME") or Path.home() / ".codex").absolute()
    if home == Path(home.anchor) or home == Path.home():
        raise UpdateError("CODEX_HOME must not be a filesystem root or home directory.")
    no_links(home)
    for relative in ("skills", "skill-backups", "cache", "cache/model-router", "AGENTS.md", "hooks.json"):
        no_links(safe_child(home, relative))
    return home


def installed_root(root, home, manifest):
    expected = safe_child(home, "skills/" + manifest["profile"])
    no_links(expected)
    if root.resolve() != expected.resolve():
        raise UpdateError("Run this command from the installed skill, not the repository checkout.")
    if (root / ".git").exists():
        raise UpdateError("Git checkouts must be upgraded manually to preserve repository work.")


@contextmanager
def lock(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(path, os.O_CREAT | os.O_RDWR, 0o600)
    acquired = False
    try:
        if os.fstat(fd).st_size == 0:
            os.write(fd, b"0")
        os.lseek(fd, 0, os.SEEK_SET)
        try:
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(fd, msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as error:
            raise UpdateError("Another operation currently holds the router lock.") from error
        acquired = True
        yield
    finally:
        if acquired:
            os.lseek(fd, 0, os.SEEK_SET)
            if os.name == "nt":
                msvcrt.locking(fd, msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)


def fetch(url, limit=MAX_DOWNLOAD, timeout=4):
    # Fixed public GitHub endpoints only; no prompts, credentials or account data.
    request = urllib.request.Request(url, headers={"User-Agent": "codex-model-router-updater",
                                                  "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = response.read(limit + 1)
    if len(data) > limit:
        raise UpdateError("Download exceeds the permitted size.")
    return data


def latest_release():
    data = json.loads(fetch(API, limit=512 * 1024))
    tag = data.get("tag_name")
    version(tag)
    if tag != "v" + tag.removeprefix("v") or data.get("draft") is not False or data.get("prerelease") is not False or data.get("html_url") != RELEASES + "/tag/" + tag:
        raise UpdateError("Not a stable release from the managed repository.")
    return {"version": tag.removeprefix("v"), "url": data["html_url"], "tag": tag}


def cached(home):
    try:
        data = read_json(home / "cache/model-router/release.json")
        if data.get("repository") != REPO:
            return {}
        if "latest" in data:
            item = data["latest"]
            version(item["version"])
            if item["tag"] != "v" + item["version"] or item["url"] != RELEASES + "/tag/" + item["tag"]:
                return {}
        return data
    except (OSError, ValueError, KeyError, TypeError, AttributeError, UpdateError):
        return {}


def refresh(home, force=False):
    with lock(home / "cache/model-router/check.lock"):
        data = cached(home)
        now = time.time()
        try:
            age = now - float(data.get("checked_at", 0))
        except (TypeError, ValueError):
            age = DAY
        if not force and 0 <= age < DAY:
            return data
        data.update(repository=REPO, checked_at=now)
        try:
            data["latest"] = latest_release()
            data["verified_at"] = now
            data["status"] = "ok"
        except Exception:
            # Cache failed attempts too, avoiding a request storm on offline clients.
            data["status"] = "unavailable"
        write_json(home / "cache/model-router/release.json", data)
        return data


def available(data, current):
    try:
        age = time.time() - float(data["verified_at"])
        return 0 <= age <= 7 * DAY and version(data["latest"]["version"]) > version(current)
    except (KeyError, ValueError, TypeError, UpdateError):
        return False


def language(prompt):
    chinese = len(re.findall(r"[\u3400-\u9fff]", prompt))
    words = re.findall(r"[A-Za-z]+", prompt)
    return "zh" if chinese and (len(words) <= 2 or chinese >= sum(map(len, words))) else "en"


def maintenance_or_confirmation(prompt):
    return prompt.strip().casefold().rstrip("。.!！") in {
        "执行", "按推荐执行", "go", "更新路由器", "检查路由器更新", "update router", "check router update"}


def hook(root, home, refresh_only=False):
    event = json.load(sys.stdin)
    if event.get("hook_event_name") != "UserPromptSubmit":
        return
    prompt = event.get("prompt", "")
    if not isinstance(prompt, str) or maintenance_or_confirmation(prompt):
        return
    if refresh_only:
        refresh(home)
        return
    manifest = load_package(root)
    data = cached(home)
    if not available(data, manifest["version"]):
        return
    latest = data["latest"]["version"]
    notice = (f"更新：模型路由器已有新版（{latest}），输入“更新路由器”即可更新。"
              if language(prompt) == "zh" else
              f'Update: Model Router {latest} is available. Send "update router" to update.')
    context = "Model Router verified update notice: " + notice + (
        "\nOnly in a routing-only response, append this notice as the optional fourth line, once. "
        "If you choose another response language, translate the notice and maintenance command to that language. "
        "Do not add it to task execution, switch models, update files, or replace a pending task. "
        "No update is authorized by this notice.")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit",
                                            "additionalContext": context}}, ensure_ascii=False))


def owned(handler):
    return isinstance(handler, dict) and "router-update.py" in str(handler.get("command", "")) and "--owner " + OWNER in str(handler.get("command", ""))


def hook_config(existing, root, home, enable=True):
    data = json.loads(existing.decode("utf-8-sig")) if existing is not None else {"hooks": {}}
    if not isinstance(data, dict) or not isinstance(data.get("hooks", {}), dict):
        raise UpdateError("Invalid hooks.json; refusing to overwrite it.")
    hooks = data.setdefault("hooks", {})
    groups = hooks.get("UserPromptSubmit", [])
    if not isinstance(groups, list):
        raise UpdateError("Invalid UserPromptSubmit hook configuration.")
    kept = []
    for group in groups:
        if not isinstance(group, dict) or not isinstance(group.get("hooks"), list):
            raise UpdateError("Invalid hook group; refusing to overwrite it.")
        handlers = [h for h in group["hooks"] if not owned(h)]
        if handlers:
            kept.append({**group, "hooks": handlers})
    if enable:
        handlers = []
        for mode in ("hook", "refresh-hook"):
            args = [sys.executable, str(root / "scripts/router-update.py"), mode,
                    "--codex-home", str(home), "--owner", OWNER]
            command = subprocess.list2cmdline(args) if os.name == "nt" else shlex.join(args)
            handlers.append({"type": "command", "command": command, "timeout": 8,
                             "async": mode == "refresh-hook", "additionalContextLimit": 256})
        kept.append({"hooks": handlers})
    if kept:
        hooks["UserPromptSubmit"] = kept
    else:
        hooks.pop("UserPromptSubmit", None)
    return (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def global_config(existing, fragment):
    text = existing.decode("utf-8-sig") if existing is not None else ""
    if text.count(START) != text.count(END) or text.count(START) > 1 or (START in text and text.index(END) < text.index(START)):
        raise UpdateError("Global routing markers need manual repair.")
    if START in text:
        text = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: fragment.strip(), text, flags=re.S)
    else:
        text += ("\n\n" if text else "") + fragment.strip() + "\n"
    return text.encode("utf-8")


def snapshot(path):
    no_links(path)
    return path.read_bytes() if path.exists() else None


def enable_hooks(root, home, disable=False):
    manifest = load_package(root)
    installed_root(root, home, manifest)
    if not disable:
        verify_package(root, manifest)
    with lock(home / "cache/model-router/install.lock"):
        path = home / "hooks.json"
        old = snapshot(path)
        new = hook_config(old, root, home, not disable)
        if new == old:
            return {"changed": False}
        backup = home / "skill-backups" / ("hooks-" + uuid.uuid4().hex + ".json")
        if old is not None:
            atomic_write(backup, old)
        atomic_write(path, new)
        return {"changed": True, "backup": str(backup) if old is not None else None,
                "review_required": not disable}


def stage_archive(payload, destination, profile, expected):
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        entries = archive.infolist()
        if len(entries) > 2000 or sum(e.file_size for e in entries) > 64 * 1024 * 1024:
            raise UpdateError("Archive is too large.")
        names = set()
        roots = set()
        for entry in entries:
            safe_child(destination, entry.filename.rstrip("/"))
            if stat.S_ISLNK(entry.external_attr >> 16) or entry.file_size > 8 * 1024 * 1024:
                raise UpdateError("Unsupported archive entry.")
            if entry.filename in names:
                raise UpdateError("Duplicate archive entry.")
            names.add(entry.filename)
            roots.add(entry.filename.split("/")[0])
        if len(roots) != 1:
            raise UpdateError("Unexpected source archive structure.")
        prefix = next(iter(roots)) + "/"
        if PROFILES[profile] != ".":
            prefix += PROFILES[profile] + "/"
        manifest_bytes = archive.read(prefix + "version.json")
        manifest = validate_manifest(json.loads(manifest_bytes), profile, expected)
        destination.mkdir(parents=True, exist_ok=False)
        atomic_write(destination / "version.json", manifest_bytes)
        for relative in manifest["files"]:
            atomic_write(safe_child(destination, relative), archive.read(prefix + relative))
        verify_package(destination, manifest)
        return manifest


def update(root, home, confirm=False):
    if not confirm:
        raise UpdateError("Explicit update authorization is required; pass --confirm only after the user's update command.")
    manifest = load_package(root)
    installed_root(root, home, manifest)
    verify_package(root, manifest)
    for directory, folders, files in os.walk(root):
        for name in folders + files:
            no_links(Path(directory) / name)
    with lock(home / "cache/model-router/install.lock"):
        release = latest_release()  # Never mutate using stale cache metadata.
        if version(release["version"]) <= version(manifest["version"]):
            return {"updated": False, "version": manifest["version"]}
        # Stage on the same filesystem, outside skills. Never recursively delete a user's install.
        backup_base = home / "skill-backups"
        backup_base.mkdir(parents=True, exist_ok=True)
        transaction = Path(tempfile.mkdtemp(prefix="router-update-", dir=backup_base))
        staged = transaction / "new"
        payload = fetch(f"https://codeload.github.com/{REPO}/zip/refs/tags/{release['tag']}", timeout=30)
        new_manifest = stage_archive(payload, staged, manifest["profile"], release["version"])
        agents = home / "AGENTS.md"
        hooks = home / "hooks.json"
        originals = {agents: snapshot(agents), hooks: snapshot(hooks)}
        replacements = {
            agents: global_config(originals[agents], (staged / "GLOBAL-ROUTING.md").read_text(encoding="utf-8")),
            hooks: hook_config(originals[hooks], root, home),
        }
        for path, data in originals.items():
            if data is not None:
                atomic_write(transaction / path.name, data)
        backup = transaction / "previous"
        root.rename(backup)
        try:
            staged.rename(root)
            verify_package(root, new_manifest)
            for path, data in replacements.items():
                atomic_write(path, data)
        except Exception as error:
            # Retain failed package and restore original install/config byte-for-byte.
            if root.exists():
                root.rename(transaction / "failed")
            backup.rename(root)
            for path, data in originals.items():
                if data is None:
                    path.unlink(missing_ok=True)
                else:
                    atomic_write(path, data)
            raise UpdateError("Upgrade failed; the original installation and configuration were restored.") from error
        return {"updated": True, "version": new_manifest["version"], "profile": manifest["profile"],
                "backup": str(transaction), "review_required": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["check", "hook", "refresh-hook", "enable-hooks", "disable-hooks", "update"])
    parser.add_argument("--codex-home")
    parser.add_argument("--owner", default=OWNER)
    parser.add_argument("--force", action="store_true", help="Explicit manual check, bypassing the daily cache")
    parser.add_argument("--confirm", action="store_true", help="User explicitly authorized this update")
    args = parser.parse_args()
    quiet = args.command in ("hook", "refresh-hook")
    try:
        root = Path(__file__).resolve().parent.parent
        home = managed_home(args.codex_home)
        if quiet:
            hook(root, home, args.command == "refresh-hook")
            return 0
        manifest = load_package(root)
        if args.command == "check":
            data = refresh(home, args.force)
            result = {"installed": manifest["version"], "update_available": available(data, manifest["version"]), **data}
        elif args.command in ("enable-hooks", "disable-hooks"):
            result = enable_hooks(root, home, args.command == "disable-hooks")
        else:
            result = update(root, home, args.confirm)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except Exception as error:
        if quiet:
            return 0  # Offline, malformed cache and permissions must never block a task.
        message = str(error) if isinstance(error, UpdateError) else "Operation failed; inspect local permissions, runtime and connectivity."
        print(json.dumps({"error": message}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
