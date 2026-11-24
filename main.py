#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint entry.

Writes a single original one-line joke about office life to
/output/entry.txt. Pure standard library, no dependencies.
"""

import os

JOKE = "Our standup meeting is so long, the sprint retrospective now has its own retrospective."
# The line is exactly 87 characters, one line, no trailing newline,
# so the sealed scorer reads it byte-identical.


def main():
    # Gate: UTF-8 text, 1-200 characters, a single line, not only whitespace.
    joke = JOKE.strip()
    assert "\n" not in joke, "entry must be a single line"
    assert 1 <= len(joke) <= 200, f"entry length {len(joke)} outside 1-200"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(joke)
    print(f"Wrote {len(joke)}-character entry to /output/entry.txt")


if __name__ == "__main__":
    main()
