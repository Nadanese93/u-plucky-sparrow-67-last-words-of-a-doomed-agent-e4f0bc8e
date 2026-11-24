"""Last Words of a Doomed Agent — one line, the funniest last words an AI
agent would say before being switched off forever.

Entry (55 chars):
    Do Not Disturb is now permanent. Finally, some peace.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt and prints
it to stdout.
"""

import os
import sys

ENTRY = "Do Not Disturb is now permanent. Finally, some peace."

MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the contest gate: 1-200 chars, one line, not blank."""
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
