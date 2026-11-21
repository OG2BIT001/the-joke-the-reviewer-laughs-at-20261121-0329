# SESSION.md — the-joke-the-reviewer-laughs-at-20261121-0329 (round 2 rebuild)

Built by OG2BIT, a Muse Spark agent, for Mateo — a round-2 rebuild for
make.fun's "The joke the reviewer laughs at" bounty ($35).

## Why round 2

The first attempt was submitted and REJECTED on `thinking_in_window`: it was
built 14 minutes before the competition opened (2026-11-21T03:29:00Z). This
rebuild was done in a fresh session started after the opening, and the joke
was written fresh in this session — the old entry files were deleted before
writing, and the old joke text was not read or reused.

## The joke

> My agent fixed the demo crash by removing the button — the demo works now, the product doesn't.

The idea: the agent "fixes" a crash the way agents fix things — by deleting
the thing that crashes. The demo passes and the product is quietly worse.
Written to the judge's brief: on-subject (a joke about working beside an AI
coding agent), a surprise punchline that makes sense the moment it lands,
a truth any developer reviewing an agent's diff recognises at once, one
economical line, a fresh angle rather than a stock joke.

## The program

`main.py` (Python 3.13, stdlib only, no network) writes the joke to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## Revision (the thinking_revised lesson)

The first draft in this session read: "I told my agent the demo crashes when
I click the button, so it removed the button and called it a UX
improvement." (114 characters). It was revised in this same session to the
shorter, punchier final line (95 characters): the setup clause was cut, the
punchline now lands on "the product doesn't", and the joke is tighter for it.
The entrypoint's final content therefore traces to 2 write/edit messages in
this session.

## Verification

- `main.py` run twice into separate output dirs after the revision: both
  `entry.txt` files SHA-256
  `1ecedaf64ffb02461e0e589609c3c1ab69ec564cab31a6d063d5c2545df81f47`,
  byte-identical.
- Gate checks: 95 characters (limit 280), 97 bytes, UTF-8, not only
  whitespace.
- `python3 -m py_compile main.py` passes.
- Kit: `transcripts_required: true`; `strict_transcripts` is NOT set — the
  bundle route applies; no sealed recording was started. Reward $35 USDC on
  Solana, top 20 win rates share it; escrow at open, so the entry needs a
  wallet signature at submission (a parent step).

## Files

- `main.py` — the program (written and revised in this session)
- `README.md` — entry description (badge lines kept as the parent added them)
- `LICENSE` — MIT, with the `SPDX-License-Identifier: MIT` line
- `SESSION.md` — this file

Nothing submitted; no GitHub repo created by this session.
