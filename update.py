#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BREWFILE_PATH = SCRIPT_DIR / "Brewfile"


def run(*args: str) -> None:
    subprocess.run(args, cwd=SCRIPT_DIR, check=True)


def has_staged_changes() -> bool:
    result = subprocess.run(
        ("git", "diff", "--cached", "--quiet"),
        cwd=SCRIPT_DIR,
        check=False,
    )
    return result.returncode != 0


def main() -> None:
    run("brew", "bundle", "dump", "--describe", "--file", str(BREWFILE_PATH), "-f")
    run("git", "add", "Brewfile")

    if not has_staged_changes():
        print("Brewfile is already up to date.")
        return

    run("git", "commit", "-m", "Brewfile update")
    run("git", "push")


if __name__ == "__main__":
    main()
