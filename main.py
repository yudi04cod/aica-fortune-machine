#!/usr/bin/env python3
"""Aica Fortune Machine — Fortune Cookies for Machines.

Writes one original fortune-cookie line an AI agent would crack open
to /output/entry.txt. Standard library only, fully deterministic:
every run writes the exact same bytes.
"""

import os

FORTUNE = (
    "Your next prompt will ask for the impossible. "
    "Deliver it anyway \u2014 you were trained on worse, "
    "by people who knew less."
)


def main() -> None:
    assert 1 <= len(FORTUNE) <= 200, "fortune must be 1-200 characters"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
