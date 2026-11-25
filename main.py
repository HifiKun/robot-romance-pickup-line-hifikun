#!/usr/bin/env python3
"""Robot Romance: one-line pickup line for an AI.

Writes a single joke pickup line, aimed at a robot/AI, to
/output/entry.txt. The line must be one line, 1-200 characters,
and the joke has to land on the machine premise itself.
"""

import os

# The line: a transformer "attention" pun. A token is the smallest
# unit a language model reads, and "attention" is the mechanism that
# decides what it focuses on -- so spending all my attention on one
# token is both a love confession and literally how the model works.
ENTRY = "Are you a token? Because I keep spending all my attention on you."


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise SystemExit("entry is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry is {len(line)} characters, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote /output/entry.txt ({len(line)} characters, 1 line)")


if __name__ == "__main__":
    main()
