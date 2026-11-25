"""The Moon Finally Answers Back.

Writes a single line, in the Moon's own voice, to /output/entry.txt.
The line answers four billion years of wishes, howls and late-night
promises with one tired comeback.
"""

import os

LINE = (
    "I move whole oceans for a living, and after four billion years "
    "of wishes, howls, and 2 a.m. promises, you still want me "
    "to make him text you back?"
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 240, f"entry is {len(text)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
