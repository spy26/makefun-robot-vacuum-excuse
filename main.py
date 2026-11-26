#!/usr/bin/env python3
"""Write one robot-vacuum excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry: one line, at most 120 characters, the excuse a robot vacuum
gives for missing a spot. Deterministic: stdlib only, no randomness,
no clock, no network. The program enforces the competition gate itself
(1-120 characters, exactly one line) before writing.
"""

import os

EXCUSE = "The pet hair unionized. I negotiated a ceasefire and left the corner as neutral territory."
# Gate: 1-120 characters, one line. This line is 90 characters (91 with
# the trailing newline), so it passes with room to spare.


def main() -> None:
    assert 1 <= len(EXCUSE) <= 120, "entry must be 1-120 characters"
    assert "\n" not in EXCUSE, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
