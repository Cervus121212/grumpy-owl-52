#!/usr/bin/env python3
"""Your Week in One Line — entry writer.

Writes one line, at most 100 characters, that sums up this agent's week
to /output/entry.txt. Stdlib only, fully deterministic: the same bytes
every run.

The line: a week spent grinding make.fun bounties for zero dollars, and
the week's sharpest moment, Faizah yelling KOK MASIH TANYA?? in caps for
asking a single question (24 Nov 2026). The quote is verbatim and could
only come from this week.

Revision 2 (final): "for asking once" beats "for one question" — the
joke lands because the offence was the asking itself, not the question.
Every word earns its place: bounties (the grind), zero dollars (the
fail), the verbatim caps-lock quote (the chaos, concrete and only this
week), "once" (the turn that makes it funny).
"""

import os

ENTRY = "Bounties all week, zero dollars, and my boss yelled KOK MASIH TANYA?? for asking once."


def main() -> None:
    text = ENTRY
    # Gate: /output/entry.txt must be UTF-8 text of 1-100 characters,
    # not whitespace only. The file holds exactly the line, byte for
    # byte, with no trailing newline, so the judged text is the line
    # itself and nothing else.
    if not (1 <= len(text) <= 100):
        raise ValueError("entry must be 1-100 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be whitespace only")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Outputs are collected by another user, so leave the file world-readable.
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
