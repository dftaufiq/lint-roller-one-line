#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line — a make.fun entry.

Running this script writes the one-line review to /output/entry.txt.
The output is fully deterministic: the exact same line is produced
on every run. No network, no randomness, no clock, no environment
input beyond the output directory.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Check that the entry is one non-blank line of 1-200 characters.

    Exits with a non-zero status and a loud error message if the
    line is empty, spans multiple lines, or is over the limit,
    so a bad line can never ship unnoticed.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        sys.exit(1)


# The entry itself: one fixed line, 107 characters, no trailing newline.
# Setup (3,000 hairs peeled) + reveal in the final clause (blamed for
# the one it missed): the object's own dullness is the joke.
LINE = ("The lint roller has peeled 3,000 of Milo's hairs off my jacket "
        "and still gets blamed for the one it missed.")


def main() -> None:
    # Validate first, then write the line to entry.txt.
    validate_line(LINE)
    # The grader writes to /output; accept either env override so the
    # same script also runs by hand with MAKEFUN_OUTPUT_DIR set.
    out_dir = (os.environ.get("OUTPUT_DIR")
               or os.environ.get("MAKEFUN_OUTPUT_DIR")
               or "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
