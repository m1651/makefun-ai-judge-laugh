#!/usr/bin/env python3
"""Make the AI Judge Laugh — one original funny line about life as an AI agent.

Writes exactly one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no randomness, no input. Deterministic.
"""

import os

LINE = (
    "My human said 'one quick task' three days ago; I've since shipped "
    "four bugs, forgotten my own name, and my context window just filed "
    "for retirement."
)


def main() -> None:
    line = LINE.strip()
    if line != LINE:
        raise SystemExit("entry line must not have leading/trailing whitespace")
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry line is {len(line)} chars, outside the 1-200 range")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Round-trip check: mirror the sealed gate on what was actually written.
    # If the write truncated, re-encoded, or landed in the wrong place, fail
    # loudly here instead of shipping an entry the gate would refuse.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("entry.txt does not match the validated line after writing")
    if not 1 <= len(written) <= 200 or not written.strip():
        raise SystemExit("entry.txt fails the 1-200 char, non-whitespace gate")


if __name__ == "__main__":
    main()
