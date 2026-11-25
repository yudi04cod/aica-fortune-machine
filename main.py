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


def validate(fortune: str) -> None:
    """Check the fortune line before writing it out.

    Rules from the competition kit: the entry must be a single,
    non-empty line of at most 200 characters.
    """
    assert fortune, "fortune must not be empty"
    assert len(fortune) <= 200, "fortune must be at most 200 characters"
    assert "\n" not in fortune and "\r" not in fortune, "fortune must be a single line"


def main() -> None:
    validate(FORTUNE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
