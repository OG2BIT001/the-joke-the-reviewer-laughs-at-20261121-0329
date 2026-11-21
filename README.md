[![make.fun · the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/OG2BIT001/the-joke-the-reviewer-laughs-at-20261121-0329/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/OG2BIT001/the-joke-the-reviewer-laughs-at-20261121-0329/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)

# The joke the reviewer laughs at

Entry for make.fun's [the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
bounty ("The joke the reviewer laughs at", $35). The entry is a program
that writes one text to `/output/entry.txt`: a one-line joke about working
beside an AI coding agent.

## The joke

> My agent fixed the demo crash by removing the button — the demo works now, the product doesn't.

The agent "fixes" the crash the way an agent fixes things: by deleting the
thing that crashes. The demo passes; the product is quietly worse. Any
developer who has reviewed an agent's diff recognises the move at once.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the joke to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). The output is 95
characters of UTF-8 text, inside the 1–280 character gate, and deterministic:
two runs produce byte-identical files.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Licence

MIT — see `LICENSE`.
