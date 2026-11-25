#!/usr/bin/env python3
"""Midnight Fridge Roast (make.fun entry).

Writes the keeper roast line byte-exact to /output/entry.txt.
Pure stdlib only (grader runs python:3.13-slim, no third-party imports).

Gate verified: 108 characters / 108 bytes, pure ASCII, one line, no trailing
newline (sealed scorer: 1-200 characters).
Device: P13 numbers ledger (the 11:59/12:00 midnight boundary) + P1 self-sealing
loop — the fridge's punctuality is the failure; it never fails to lock on time.
"""

import os

KEEPER = "You opened at 11:59 and locked at 12:00. You are the only thing in this house that has never once been late."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)


if __name__ == "__main__":
    main()
