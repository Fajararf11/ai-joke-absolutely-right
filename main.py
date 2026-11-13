#!/usr/bin/env python3
"""ai-joke-03 entry: writes one joke about AI coding agents to /output/entry.txt.

Standard library only, no network, deterministic: the two runs the grader makes
must write the same bytes. Outside the grader's container MAKEFUN_OUTPUT_DIR
stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

JOKE = (
    'My AI agent said "You\'re absolutely right" nine times today. '
    "I'd pay real money to hear it say that to the failing test."
)


def output_dir() -> Path:
    """The writable directory the entry writes its joke into."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()