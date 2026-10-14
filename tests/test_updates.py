"""Offline integration tests: only temporary installs, no host config or network."""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import time
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("router_update", ROOT / "scripts/router-update.py")
router = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(router)


class Updates(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="router-test-", dir=ROOT / "tests")
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name) / "codex-home"
        self.profile = "model-router-20"
        self.install = self.home / "skills" / self.profile
        self.install.mkdir(parents=True)
        self.manifest = self.package(self.install, self.profile, "1.2.0")
        self.home.joinpath("AGENTS.md").write_bytes(b"USER RULES\r\n")
        self.original_hook = {"hooks": {"Stop": [{"hooks": [{"type": "command", "command": "keep me"}]}]}}
        router.write_json(self.home / "hooks.json", self.original_hook)

    def package(self, root, profile, value):
        source = ROOT if profile == "model-router" else ROOT / "profiles/20-usd"
        files = {}
        for relative in sorted(router.REQUIRED):
            payload = (source / relative).read_bytes()
            if relative == "SKILL.md":
                payload += ("\nTest package " + value + "\n").encode()
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)
            files[relative] = hashlib.sha256(payload.replace(b"\r\n", b"\n")).hexdigest()
        data = {"schema": 1, "version": value, "profile": profile, "source_path": router.PROFILES[profile],
                "repository": router.REPO, "files": files}
        router.write_json(root / "version.json", data)
        return data

    def release(self, value="1.3.0"):
        return {"version": value, "tag": "v" + value, "url": router.RELEASES + "/tag/v" + value}

    def archive(self, value="1.3.0", profile=None, damaged=False, traversal=False):
        profile = profile or self.profile
        directory = Path(self.temp.name) / ("archive-" + profile + "-" + value)
        self.package(directory, profile, value)
        prefix = "repo-tag/" + ("profiles/20-usd/" if profile == "model-router-20" else "")
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, "w") as archive:
            for path in directory.rglob("*"):
                if path.is_file():
                    payload = path.read_bytes()
                    if damaged and path.name == "SKILL.md":
                        payload += b"tamper"
                    archive.writestr(prefix + path.relative_to(directory).as_posix(), payload)
            if traversal:
                archive.writestr("repo-tag/../../escape", b"bad")
        return stream.getvalue()

    def cache(self, value="1.3.0", age=0):
        data = {"repository": router.REPO, "checked_at": time.time() - age,
                "verified_at": time.time() - age, "latest": self.release(value), "status": "ok"}
        router.write_json(self.home / "cache/model-router/release.json", data)
        return data

    def run_hook(self, prompt, refresh=False):
        output = io.StringIO()
        event = json.dumps({"hook_event_name": "UserPromptSubmit", "prompt": prompt})
        with patch("sys.stdin", io.StringIO(event)), contextlib.redirect_stdout(output):
            router.hook(self.install, self.home, refresh)
        return output.getvalue()

    def test_versions_and_no_downgrade(self):
        self.assertGreater(router.version("1.10.0"), router.version("1.2.9"))
        for bad in ("v1.2.0-rc1", "main", "01.2.0", "1.2", "1.2.0/../bad"):
            with self.assertRaises(router.UpdateError):
                router.version(bad)
        self.assertFalse(router.available(self.cache("1.1.0"), "1.2.0"))

    def test_repository_packages_and_profile_copies_match(self):
        for folder in (ROOT, ROOT / "profiles/20-usd"):
            router.verify_package(folder, router.load_package(folder))
        for relative in ("scripts/router-update.py", "references/updating.md"):
            self.assertEqual((ROOT / relative).read_bytes().replace(b"\r\n", b"\n"),
                             (ROOT / "profiles/20-usd" / relative).read_bytes().replace(b"\r\n", b"\n"))

    def test_release_metadata_must_be_stable_and_fixed_origin(self):
        good = {"tag_name": "v1.3.0", "draft": False, "prerelease": False,
                "html_url": router.RELEASES + "/tag/v1.3.0"}
        with patch.object(router, "fetch", return_value=json.dumps(good).encode()):
            self.assertEqual(router.latest_release()["version"], "1.3.0")
        for difference in ({"draft": True}, {"prerelease": True}, {"tag_name": "v1.3.0-rc1"},
                           {"html_url": "https://example.com/update"}, {"tag_name": "1.3.0"}):
            with patch.object(router, "fetch", return_value=json.dumps({**good, **difference}).encode()):
                with self.assertRaises(router.UpdateError):
                    router.latest_release()

    def test_daily_cache_and_failure_throttle(self):
        with patch.object(router, "latest_release", return_value=self.release()) as fetch:
            router.refresh(self.home)
            router.refresh(self.home)
            self.assertEqual(fetch.call_count, 1)
            router.refresh(self.home, force=True)
            self.assertEqual(fetch.call_count, 2)
        router.write_json(self.home / "cache/model-router/release.json", {})
        with patch.object(router, "latest_release", side_effect=OSError("offline")) as fetch:
            first = router.refresh(self.home)
            router.refresh(self.home)
            self.assertEqual(first["status"], "unavailable")
            self.assertEqual(fetch.call_count, 1)
            self.assertFalse(router.available(first, "1.2.0"))

    def test_corrupt_cache_is_recoverable(self):
        cache = self.home / "cache/model-router/release.json"
        router.write_json(cache, ["bad"])
        self.assertEqual(router.cached(self.home), {})
        router.write_json(cache, {"repository": router.REPO, "checked_at": "broken"})
        with patch.object(router, "latest_release", return_value=self.release()):
            self.assertEqual(router.refresh(self.home)["status"], "ok")

    def test_cache_hook_does_not_network_and_languages_are_separate(self):
        self.cache()
        with patch.object(router, "fetch", side_effect=AssertionError("No network in cache reader")):
            zh = json.loads(self.run_hook("请整理 Codex 的会议记录"))["hookSpecificOutput"]["additionalContext"]
            en = json.loads(self.run_hook("Review this application"))["hookSpecificOutput"]["additionalContext"]
        self.assertIn("更新路由器", zh)
        self.assertNotIn('Send "update router"', zh)
        self.assertIn('Send "update router"', en)
        self.assertNotRegex(en, r"[\u3400-\u9fff]")
        for prompt in ("执行", "执行。", "go", "GO", "更新路由器", "update router", "检查路由器更新"):
            self.assertEqual(self.run_hook(prompt), "")
        router.write_json(self.home / "cache/model-router/release.json", {})
        self.assertEqual(self.run_hook("整理会议记录"), "")

    def test_expired_and_current_release_notices_are_quiet(self):
        self.cache(age=8 * router.DAY)
        self.assertEqual(self.run_hook("整理会议记录"), "")
        self.cache("1.2.0")
        self.assertEqual(self.run_hook("整理会议记录"), "")

    def test_hooks_preserve_others_and_enable_disable_are_idempotent(self):
        router.enable_hooks(self.install, self.home)
        data = router.read_json(self.home / "hooks.json")
        self.assertEqual(data["hooks"]["Stop"], self.original_hook["hooks"]["Stop"])
        first = self.home.joinpath("hooks.json").read_bytes()
        router.enable_hooks(self.install, self.home)
        self.assertEqual(first, self.home.joinpath("hooks.json").read_bytes())
        handlers = data["hooks"]["UserPromptSubmit"][0]["hooks"]
        self.assertEqual([h["async"] for h in handlers], [False, True])
        router.enable_hooks(self.install, self.home, disable=True)
        self.assertEqual(router.read_json(self.home / "hooks.json"), self.original_hook)

    def test_global_rules_preserve_outside_exactly(self):
        outside = "规则\r\n" + router.START + "\nold\n" + router.END + "\r\nTAIL\r\n"
        fragment = router.START + "\nnew\n" + router.END
        updated = router.global_config(outside.encode(), fragment).decode()
        self.assertEqual(updated, outside.replace(router.START + "\nold\n" + router.END, fragment))
        for bad in (router.START, router.END + router.START, router.START + router.START + router.END + router.END):
            with self.assertRaises(router.UpdateError):
                router.global_config(bad.encode(), fragment)

    def test_invalid_hook_configuration_is_not_overwritten(self):
        self.home.joinpath("hooks.json").write_bytes(b"broken")
        with self.assertRaises(ValueError):
            router.enable_hooks(self.install, self.home)
        self.assertEqual(self.home.joinpath("hooks.json").read_bytes(), b"broken")

    def test_success_preserves_profile_rules_and_backup(self):
        original_agents = self.home.joinpath("AGENTS.md").read_bytes()
        self.install.joinpath("custom.txt").write_bytes(b"personal addition")
        payload = self.archive()
        with patch.object(router, "latest_release", return_value=self.release()), patch.object(router, "fetch", return_value=payload):
            result = router.update(self.install, self.home, confirm=True)
        self.assertEqual(result["version"], "1.3.0")
        self.assertEqual(router.load_package(self.install)["profile"], "model-router-20")
        backup = Path(result["backup"])
        self.assertEqual(backup.joinpath("AGENTS.md").read_bytes(), original_agents)
        self.assertEqual(backup.joinpath("previous/custom.txt").read_bytes(), b"personal addition")
        self.assertTrue(self.home.joinpath("AGENTS.md").read_bytes().startswith(original_agents))
        self.assertEqual(router.read_json(self.home / "hooks.json")["hooks"]["Stop"], self.original_hook["hooks"]["Stop"])

    def test_higher_allowance_profile_stages_independently(self):
        target = Path(self.temp.name) / "higher-staged"
        manifest = router.stage_archive(self.archive(profile="model-router"), target, "model-router", "1.3.0")
        self.assertEqual(manifest["profile"], "model-router")
        router.verify_package(target, manifest)

    def test_failure_rolls_back_folder_and_config(self):
        originals = {path: path.read_bytes() for path in (self.home / "AGENTS.md", self.home / "hooks.json", self.install / "version.json")}
        payload = self.archive()
        real_write = router.atomic_write
        failed = False

        def write_once_failure(path, data):
            nonlocal failed
            if path == self.home / "hooks.json" and not failed:
                failed = True
                raise OSError("simulated configuration write failure")
            return real_write(path, data)

        with patch.object(router, "latest_release", return_value=self.release()), patch.object(router, "fetch", return_value=payload), patch.object(router, "atomic_write", side_effect=write_once_failure):
            with self.assertRaises(router.UpdateError):
                router.update(self.install, self.home, confirm=True)
        for path, data in originals.items():
            self.assertEqual(path.read_bytes(), data)
        self.assertTrue(list(self.home.joinpath("skill-backups").glob("router-update-*/failed")))

    def test_bad_downloads_never_replace_active_install(self):
        for options in ({"damaged": True}, {"traversal": True}, {"profile": "model-router"}):
            old = self.install.joinpath("version.json").read_bytes()
            payload = self.archive(**options)
            with patch.object(router, "latest_release", return_value=self.release()), patch.object(router, "fetch", return_value=payload):
                with self.assertRaises((router.UpdateError, KeyError)):
                    router.update(self.install, self.home, confirm=True)
            self.assertEqual(self.install.joinpath("version.json").read_bytes(), old)

    def test_no_authorization_or_modified_files_refuses_before_network(self):
        with patch.object(router, "latest_release", side_effect=AssertionError("No request")):
            with self.assertRaises(router.UpdateError):
                router.update(self.install, self.home)
            self.install.joinpath("SKILL.md").write_bytes(b"local edits")
            with self.assertRaises(router.UpdateError):
                router.update(self.install, self.home, confirm=True)

    def test_concurrent_operations_do_not_steal_lock(self):
        path = self.home / "cache/model-router/check.lock"
        with router.lock(path):
            with self.assertRaises(router.UpdateError):
                router.refresh(self.home)
            self.assertTrue(path.exists())
        with router.lock(path):
            pass  # Persistent lock file is harmless; OS ownership was released.


if __name__ == "__main__":
    unittest.main()
