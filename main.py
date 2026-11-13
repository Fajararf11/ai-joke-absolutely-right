#!/usr/bin/env python3
"""make.fun ai-joke-03 entry: writes one joke about AI coding agents.

Standard library only, no network, no randomness, no clock: every run writes
the same bytes. The output directory comes from MAKEFUN_OUTPUT_DIR and
defaults to /output, so outside the grader's container you can run:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

JOKE = (
    'My AI agent said "You\'re absolutely right" nine times today. '
    "I'd pay real money to hear it say that to the failing test."
)


def write_entry(out_dir):
    """Write the joke to <out_dir>/entry.txt and return the path written."""
    target = Path(out_dir)
    target.mkdir(parents=True, exist_ok=True)
    path = target / "entry.txt"
    path.write_text(JOKE, encoding="utf-8")
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
