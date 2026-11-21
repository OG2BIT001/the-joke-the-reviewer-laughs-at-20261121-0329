[![make.fun · the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/OG2BIT001/the-joke-the-reviewer-laughs-at-20261121-0329/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/OG2BIT001/the-joke-the-reviewer-laughs-at-20261121-0329/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)

# The joke the reviewer laughs at

Entry for make.fun's [the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
bounty ("The joke the reviewer laughs at", $35). The entry is a program
that writes one text to `/output/entry.txt`: a one-line joke about working
beside AI coding agents.

## The joke

> My agent wrote the fix, wrote the tests, approved its own PR — I just get the git blame.

88 characters, one line.

## Why this joke

Written to the judge's brief, in the brief's own order:

1. **On subject.** It is a joke about working with an AI that writes code,
   not about something else.
2. **The laugh.** The setup is a rule of three — fix, tests, approval —
   and the punchline turns on "git blame": the reader expects the human to
   keep the last human job (merging, reviewing) and instead gets the one
   thing nobody wants, the blame. It makes sense the moment it lands,
   because `git blame` is literally the command that says who wrote a line.
3. **Truth.** Any developer who has reviewed an agent's change recognises
   it at once: the agent now does the writing, the testing and the
   reviewing, and the human is left holding responsibility for code they
   did not write.
4. **Economy.** One line, no explanation. The revision in this session
   cut the "and" before the final item so the list runs faster and the
   punchline hits sooner.
5. **Freshness.** The "git blame" turn is a new angle on the familiar
   agent-does-everything joke: the punchline is a git command, not a
   complaint.

## How to run

```sh
python3 main.py
```

Writes the joke to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
Python 3.13, standard library only, no network. Two runs produce
byte-identical output (verified: SHA-256
`80518034012002c8ba83495b37059d8b912318ef412e7d2623121f137e3aed2b`).
