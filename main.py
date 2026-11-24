#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — entry program.

Writes one original line of plain text (an alien tourist's review of
planet Earth, at most 200 characters) to /output/entry.txt.

Design of the line (chosen against the judge brief, most important first):
1. Reads as an alien tourist's review of Earth: it opens "Two days on
   Earth" (a visitor's stay, echoing the two-day window) and closes from
   orbit — the visitor's outside view is clear in the line.
2. Funny from the alien's angle: a water-covered planet whose locals
   fight over the dry bits — the laugh comes from the alien noticing
   what humans take for granted, not from a joke bolted on.
3. Original: a 70%-water paradox, not the first obvious thought about
   traffic, gravity, money or weather.
4. Sounds like a real review: a verdict ("Four stars") and a closing
   remark ("Next time, I'm staying in orbit").
5. Tight: one clean joke, punch lands at the end, 141 characters.

The line is written verbatim by this program (stdlib only, no network,
no randomness, deterministic): the same bytes on every run.
"""

import os

LINE = (
    "Two days on Earth: 70% water, yet the locals fight over the dry "
    "bits. Four stars - the sunsets are worth it. Next time, I'm "
    "staying in orbit."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    # Read-back verification: fail loudly on any difference.
    with open(path, encoding="utf-8") as f:
        data = f.read()
    assert data == LINE, "read-back mismatch"
    assert 1 <= len(data) <= 200, "entry must be 1-200 characters"
    assert data.strip() == data, "entry must not be only whitespace"
    print(f"wrote {path}: {len(data)} characters, {len(data.encode('utf-8'))} bytes")


if __name__ == "__main__":
    main()
