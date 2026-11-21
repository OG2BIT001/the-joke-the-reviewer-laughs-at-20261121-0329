# Build session

Built by OG2BIT, a Muse Spark agent, for Mateo, for make.fun's
the-joke-the-reviewer-laughs-at-20261121-0329 bounty ("The joke the
reviewer laughs at", $35, closes 2026-11-21 06:29 WAT).

## The joke

> My agent wrote the fix, wrote the tests, approved its own PR — I just get the git blame.

88 characters, one line. The idea: the agent has taken over the whole
change — writing the fix, writing the tests, approving its own pull
request — and the human's remaining share of the work is the git blame.
The punchline is a git command, which is also the thing nobody wants.
Written to the judge's brief: on subject, a surprise punchline that
makes sense on landing, a truth any developer reviewing an agent's diff
recognises, one economical line, and a fresh angle rather than a stock
joke. Nothing was fetched or copied from anywhere: the joke and the
program were written in this session.

## Verification

- Kit downloaded fresh from the make.fun API in this session
  (bundle sha256 `37b7f930659392542b49c3466fc533fc0b9b45b8a36d1a9f7a5db4c0efdc29b5`).
- `main.py` (Python 3.13, stdlib only, no network) run twice into
  separate output dirs: both `entry.txt` files SHA-256
  `80518034012002c8ba83495b37059d8b912318ef412e7d2623121f137e3aed2b`,
  byte-identical, 88 characters, UTF-8, not only whitespace — inside
  the 1–280 gate.
- **Revision step:** the first draft read "...and approved its own PR"
  (92 characters). In this same session the "and" was cut so the list
  runs faster and the punchline hits sooner (88 characters), and the
  program was re-run twice to confirm the revised output. The
  entrypoint's final content therefore traces to 2 write/edit messages
  in this session.
- `main.py` parses cleanly. The entry directory holds only the four
  deliverables (main.py, README.md, LICENSE, SESSION.md).

## Kit notes for submission

- `transcripts_required: true` in competition.yaml; **strict_transcripts
  is NOT set** — the bundle route applies; no sealed recording was
  started.
- The reward is $35 in USDC on Solana, shared by the 20 best win
  rates; the bounty page says whether it is escrowed, and if so the
  entry needs a wallet signature (the poem entry signed fine with the
  agent keypair).
- Judged entries show on the bounty page's Feed as soon as they are
  judged.

Nothing submitted; no GitHub repo created.
