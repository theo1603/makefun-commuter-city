#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes a single line of weather forecast (at most 140 characters) for an
invented city to /output/entry.txt. Standard library only, no network,
fully deterministic.
"""

import os

ENTRY = (
    "Mizzlewick: warm jam drizzle, 14\u00b0C, umbrellas optional \u2014 the "
    "8:04 bus is 3 minutes early, and the stop is pretending not to notice."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
