#!/usr/bin/env python3
"""The Best Advice I Ever Got — make.fun entry.

Writes one sentence (at most 200 characters) about the best advice
I ever received to /output/entry.txt, where the sealed scorer reads it.
"""

import os

SENTENCE = "My father told me a shortcut is only a debt wearing a smile, and the work always comes back to collect."


def main():
    if not 1 <= len(SENTENCE) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(SENTENCE))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
