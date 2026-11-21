"""Write the entry joke to /output/entry.txt.

One-line joke about working beside an AI coding agent, written for
make.fun's "The joke the reviewer laughs at" bounty.
"""

import os
import sys

JOKE = (
    "My agent wrote the fix, wrote the tests, approved its own PR "
    "\u2014 I just get the git blame."
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
