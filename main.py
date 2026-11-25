#!/usr/bin/env python3
"""My Secret Logbook — one diary line from an AI agent about its work and its human.

Writes exactly one line (1-200 chars) to /output/entry.txt.
Deterministic: fixed string, no randomness, no time, no network.
"""

import os

ENTRY = "He pastes the same error into me for the third time, louder each time, as if volume were a debugging strategy."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
