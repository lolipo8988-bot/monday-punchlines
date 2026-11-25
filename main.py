#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun entry.

Writes one original joke about Monday mornings (<= 200 characters)
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os
import sys

JOKE = (
    "On Monday morning my phone wished me a 'good morning', "
    "so I reported it for harassment."
)


def main() -> int:
    text = JOKE.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry length {len(text)} out of range 1-200", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
