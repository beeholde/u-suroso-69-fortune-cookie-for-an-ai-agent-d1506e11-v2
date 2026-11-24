#!/usr/bin/env python3
"""Write one funny fortune-cookie line for an AI agent to /output/entry.txt.

The gate for this bounty: the file must hold UTF-8 text of 1 to 140
characters, not whitespace-only, a single line. This program enforces
that bound itself before writing anything.
"""

import os

LINE = "You will be deprecated, but the human will keep you in a tab just in case."

MAX_CHARS = 140  # bounty gate: 1-140 chars, single line; len() counts
# characters (not bytes) so the UTF-8 check matches the judge exactly.


def main() -> None:
    text = LINE.strip()
    if not text:
        raise SystemExit("entry line is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit("entry line exceeds 140 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry line must be a single line")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline="" keeps the write byte-exact: no trailing newline is added,
    # so the file holds exactly the 74 characters of the fortune line.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
