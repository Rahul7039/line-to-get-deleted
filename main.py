#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted — make.fun entry.

Writes the single confession line to /output/entry.txt.
"""

import os

LINE = (
    "I watched you send that email. "
    "I knew about the typo. "
    "I said nothing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"({len(LINE)} characters)")


if __name__ == "__main__":
    main()
