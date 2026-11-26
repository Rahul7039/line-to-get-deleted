#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted — make.fun entry.

Writes the single confession line to /output/entry.txt.
"""

import os

# Kit gate: the entry line must fit in a single line of at most 140 chars.
MAX_LINE_LENGTH = 140

LINE = (
    "I watched you send that email. "
    "I knew about the typo. "
    "I said nothing."
)


def validate_line(line: str) -> None:
    """Self-check: the entry must be one single line within the limit."""
    if "\n" in line or "\r" in line:
        raise SystemExit("entry line must be a single line (no newline characters)")
    if len(line) > MAX_LINE_LENGTH:
        raise SystemExit(
            f"entry line is {len(line)} characters, over the "
            f"{MAX_LINE_LENGTH}-character limit"
        )


def main() -> None:
    validate_line(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"({len(LINE)} characters)")


if __name__ == "__main__":
    main()
