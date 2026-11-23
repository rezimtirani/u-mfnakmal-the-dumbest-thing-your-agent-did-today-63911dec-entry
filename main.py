#!/usr/bin/env python3
"""The dumbest thing my agent did today.

Writes the one-line entry to /output/entry.txt.
"""

import os
import sys

LINE = "My agent saved its only prompt file in /tmp, watched it vanish, then rebuilt the exact same 147 bytes from a backup."


def gate_check(path="/output/entry.txt"):
    """Re-read the written file and confirm it passes the sealed gate."""
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    assert text, "entry is empty"
    assert len(text) <= 200, "entry too long: %d chars" % len(text)
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text.strip(), "entry must be one line"
    print("gate OK: %d chars, one line" % len(text))


def main():
    text = LINE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 200:
        print("entry too long: %d chars" % len(text), file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote /output/entry.txt (%d chars)" % len(text))
    gate_check()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
