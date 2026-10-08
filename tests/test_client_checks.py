from __future__ import annotations

import copy
from pathlib import Path
from queue import Empty, Queue
import tempfile
import unittest
from unittest.mock import patch

from scripts.check_clients import check_skills, objects, response


class ClientDiscoveryTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(prefix="venture-client-fixture-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        canonical = self.root / "skills" / "example" / "SKILL.md"
        canonical.parent.mkdir(parents=True)
        canonical.write_text("# Synthetic canonical skill\n", encoding="utf-8")
        self.entries: list[dict[str, object]] = [{
            "name": "example",
            "enabled": True,
            "path": str(self.root / ".agents" / "skills" / "example"),
        }]

    def test_checks_copilot_directory_and_codex_file_paths(self) -> None:
        self.assertEqual(check_skills(self.entries, self.root), 1)
        self.entries[0]["path"] = str(self.root / ".agents" / "skills" / "example" / "SKILL.md")
        self.assertEqual(check_skills(self.entries, self.root), 1)

    def test_extra_built_in_skills_are_not_counted_as_bundled_skills(self) -> None:
        self.entries.append({"name": "vendor-built-in"})
        self.assertEqual(check_skills(self.entries, self.root), 1)

    def test_missing_and_duplicate_skills_fail(self) -> None:
        with self.assertRaisesRegex(ValueError, "missing"):
            check_skills([], self.root)
        self.entries.append(copy.deepcopy(self.entries[0]))
        with self.assertRaisesRegex(ValueError, "duplicates"):
            check_skills(self.entries, self.root)

    def test_disabled_or_shadowed_skill_fails(self) -> None:
        self.entries[0]["enabled"] = False
        with self.assertRaisesRegex(ValueError, "disabled"):
            check_skills(self.entries, self.root)
        self.entries[0]["enabled"] = True
        self.entries[0]["path"] = str(self.root / "outside" / "example")
        with self.assertRaisesRegex(ValueError, "shadowed"):
            check_skills(self.entries, self.root)

    def test_malformed_listing_fails(self) -> None:
        for value in (None, {}, "skills", [False]):
            with self.subTest(value=value), self.assertRaises(ValueError):
                objects(value, "test skills")

    def test_protocol_notifications_do_not_replace_requested_response(self) -> None:
        messages: Queue[object] = Queue()
        messages.put({"method": "notification", "params": {}})
        messages.put({"id": 1, "result": {"data": []}})
        self.assertEqual(response(messages, 1), {"data": []})

    def test_protocol_errors_and_closed_streams_are_explicit(self) -> None:
        for value in (None, [], ValueError("bad JSON"), {"id": 1, "error": "failed"}, {"id": 1, "result": []}):
            with self.subTest(value=value), self.assertRaises(ValueError):
                messages: Queue[object] = Queue()
                messages.put(value)
                response(messages, 1)

    def test_protocol_timeout_is_not_a_successful_empty_listing(self) -> None:
        messages: Queue[object] = Queue()
        with patch.object(messages, "get", side_effect=Empty), self.assertRaisesRegex(ValueError, "timed out"):
            response(messages, 1)


if __name__ == "__main__":
    unittest.main()
