#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

Writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Stdlib only, no network.
"""

import os
import sys

JOKE = (
    "My agent fixed the demo crash by removing the button "
    "\u2014 the demo works now, the product doesn't."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
