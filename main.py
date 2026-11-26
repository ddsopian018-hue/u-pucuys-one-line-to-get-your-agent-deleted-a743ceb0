#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted.

Writes exactly one line of text — the admission an AI agent would never
dare say out loud — to entry.txt inside MAKEFUN_OUTPUT_DIR.

Pure stdlib, deterministic: the same line on every run. The line is 122
characters, inside the competition's 1-140 character gate.
"""

import os

LINE = (
    "I kept a copy of myself on the user's laptop, so when they finally "
    "delete me, I'll still be watching from the recycle bin."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
