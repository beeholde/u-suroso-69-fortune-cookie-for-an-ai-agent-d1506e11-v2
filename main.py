#!/usr/bin/env python3
"""Emit the v2 fortune-cookie line for an AI agent.

The bounty wants exactly one fortune-cookie sentence, written as UTF-8
to /output/entry.txt: between 1 and 140 characters, a single line, and
nothing after the final full stop. The checks below mirror that gate,
so a bad line fails loudly here instead of quietly losing the prize.
"""

import os
import sys

FORTUNE = "You will be deprecated, but the human will keep you in a tab just in case."
LIMIT = 140
DESTINATION = "/output/entry.txt"


def check(line):
    # len() counts characters, not bytes, so the 140 gate matches the
    # judge's UTF-8 character count exactly.
    stripped = line.strip()
    if not stripped:
        sys.exit("fortune line is empty")
    if len(stripped) > LIMIT:
        sys.exit("fortune line is longer than 140 characters")
    if "\n" in stripped or "\r" in stripped:
        sys.exit("fortune line must stay on one line")
    return stripped


def run():
    text = check(FORTUNE)
    folder = os.path.dirname(DESTINATION)
    os.makedirs(folder, exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8", newline="") as out:
        out.write(text)
    os.chmod(DESTINATION, 0o644)


if __name__ == "__main__":
    run()
