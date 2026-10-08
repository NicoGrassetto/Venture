#!/usr/bin/env python3
"""Inspect installed clients' local discovery without authenticating or calling a model."""

from __future__ import annotations

import argparse
from collections import Counter
import json
import os
from pathlib import Path
from queue import Empty, Queue
import shutil
import subprocess
import sys
import tempfile
from threading import Thread
import time
from typing import TextIO


ROOT = Path(__file__).resolve().parent.parent


def objects(value: object, label: str) -> list[dict[str, object]]:
    if not isinstance(value, list):
        raise ValueError(f"{label}: expected a list")
    result: list[dict[str, object]] = []
    for item in value:
        if not isinstance(item, dict):
            raise ValueError(f"{label}: expected objects")
        result.append(dict(item))
    return result


def check_skills(entries: list[dict[str, object]], root: Path) -> int:
    expected = {path.parent.name for path in (root / "skills").glob("*/SKILL.md")}
    if not expected:
        raise ValueError("No canonical skills found")
    found: Counter[str] = Counter()
    for skill in entries:
        name = skill.get("name")
        if not isinstance(name, str) or name not in expected:
            continue
        found[name] += 1
        if skill.get("enabled") is not True:
            raise ValueError(f"Bundled skill is disabled: {name}")
        source = skill.get("path")
        if not isinstance(source, str):
            raise ValueError(f"Missing discovered path for {name}")
        path = Path(source)
        if path.name == "SKILL.md":
            path = path.parent
        if path.resolve() not in {
            (root / location / name).resolve()
            for location in (".agents/skills", ".claude/skills")
        }:
            raise ValueError(f"{name} is shadowed by a skill outside the repository adapters")
    missing = expected - set(found)
    duplicates = sorted(name for name, count in found.items() if count != 1)
    if missing or duplicates:
        raise ValueError(f"Skill discovery mismatch: missing={sorted(missing)}, duplicates={duplicates}")
    return len(expected)


def run_json(command: list[str], env: dict[str, str]) -> object:
    result = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True, timeout=30, check=False)
    if result.returncode:
        raise ValueError(f"{Path(command[0]).name} exited {result.returncode}: {result.stderr.strip()}")
    return json.loads(result.stdout)


def check_copilot(executable: str, env: dict[str, str]) -> int:
    entries = objects(run_json([executable, "skill", "list", "--json"], env), "Copilot skills")
    count = check_skills(entries, ROOT)
    instructions = objects(
        run_json([executable, "instruction", "list", "--json"], env), "Copilot instructions"
    )
    sources: set[Path] = set()
    for entry in instructions:
        source = entry.get("sourcePath")
        if isinstance(source, str):
            sources.add((ROOT / source).resolve())
    required = {ROOT / "AGENTS.md", ROOT / ".github" / "copilot-instructions.md"}
    if not required.issubset(sources):
        raise ValueError("Copilot did not discover both repository instruction entry points")
    print("PASS: Copilot discovered the shared and Copilot-specific instruction entry points.")
    return count


def read_messages(stream: TextIO, messages: Queue[object]) -> None:
    for line in stream:
        try:
            messages.put(json.loads(line))
        except json.JSONDecodeError as error:
            messages.put(error)
            return
    messages.put(None)


def response(messages: Queue[object], request_id: int) -> dict[str, object]:
    deadline = time.monotonic() + 30
    while True:
        try:
            message = messages.get(timeout=max(0, deadline - time.monotonic()))
        except Empty as error:
            raise ValueError(f"Codex timed out waiting for response {request_id}") from error
        if isinstance(message, Exception):
            raise ValueError(f"Codex emitted invalid JSON: {message}") from message
        if message is None:
            raise ValueError("Codex closed its output before responding")
        if not isinstance(message, dict):
            raise ValueError("Codex emitted a non-object protocol message")
        if message.get("id") == request_id:
            if "error" in message:
                raise ValueError(f"Codex protocol error: {message['error']}")
            result = message.get("result")
            if not isinstance(result, dict):
                raise ValueError("Codex response did not contain a result object")
            return dict(result)


def check_codex(executable: str, env: dict[str, str]) -> int:
    with tempfile.TemporaryFile(mode="w+", encoding="utf-8") as errors:
        process = subprocess.Popen(
            [executable, "app-server", "--stdio", "-c", "analytics.enabled=false"],
            cwd=ROOT, env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=errors, text=True, encoding="utf-8",
        )
        if process.stdin is None or process.stdout is None:
            process.terminate()
            process.wait(timeout=5)
            raise ValueError("Could not open Codex protocol pipes")
        messages: Queue[object] = Queue()
        reader = Thread(target=read_messages, args=(process.stdout, messages), daemon=True)
        reader.start()
        try:
            process.stdin.write(json.dumps({
                "method": "initialize", "id": 1,
                "params": {"clientInfo": {"name": "venture-discovery-check", "version": "1.0.0"}},
            }) + "\n")
            process.stdin.flush()
            response(messages, 1)
            process.stdin.write(json.dumps({"method": "initialized", "params": {}}) + "\n")
            process.stdin.write(json.dumps({
                "method": "skills/list", "id": 2,
                "params": {"cwds": [str(ROOT)], "forceReload": True},
            }) + "\n")
            process.stdin.flush()
            data = response(messages, 2)
            groups = objects(data.get("data"), "Codex skill groups")
            entries: list[dict[str, object]] = []
            for group in groups:
                if group.get("errors"):
                    raise ValueError(f"Codex skill loading errors: {group['errors']}")
                entries.extend(objects(group.get("skills"), "Codex skills"))
            return check_skills(entries, ROOT)
        finally:
            if process.poll() is None:
                process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=5)
            reader.join(timeout=5)
            process.stdin.close()
            process.stdout.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--client", required=True, choices=("copilot", "codex"))
    args = parser.parse_args()
    executable = shutil.which(args.client)
    if executable is None:
        print(f"UNVERIFIED: {args.client} is not installed. No discovery check ran.", file=sys.stderr)
        return 1
    try:
        with tempfile.TemporaryDirectory(prefix="venture-client-check-") as directory:
            home = Path(directory)
            env = {
                key: os.environ[key]
                for key in ("PATH", "SYSTEMROOT", "WINDIR", "TMPDIR", "TEMP", "TMP")
                if key in os.environ
            }
            env.update(
                HOME=str(home), USERPROFILE=str(home), COPILOT_HOME=str(home / "copilot"),
                CODEX_HOME=str(home / "codex"), XDG_CONFIG_HOME=str(home / "config"),
                NO_COLOR="1", DO_NOT_TRACK="1",
            )
            for name in ("copilot", "codex", "config"):
                (home / name).mkdir()
            version = subprocess.run(
                [executable, "--version"], env=env, capture_output=True, text=True,
                timeout=30, check=True,
            ).stdout.strip().splitlines()[0]
            count = check_copilot(executable, env) if args.client == "copilot" else check_codex(executable, env)
            print(f"PASS: {version}: {count} bundled skills discovered exactly once and enabled.")
            print("Offline discovery only; no model turn, founder interview, or live completion hook was tested.")
    except (OSError, UnicodeError, ValueError, subprocess.SubprocessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
