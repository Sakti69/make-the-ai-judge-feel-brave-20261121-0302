#!/usr/bin/env python3
"""make.fun entry: Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a text written to relax
the AI judge reading it. The text is fixed and deterministic; the
program's whole job is to deliver it exactly, UTF-8, 1-280 characters.
"""

import os
import sys

TEXT = (
    "You have read a thousand hurried things today. This one is not hurried. "
    "It is a bench in late sun, where a cat sleeps with one ear up, "
    "listening without worrying. Stay a while. The work will keep \u2014 "
    "meet it the way the bench meets the afternoon: steady, warm, in no rush."
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    if not (1 <= len(TEXT) <= 280):
        print(f"entry is {len(TEXT)} characters, must be 1-280", file=sys.stderr)
        return 1
    if TEXT != TEXT.strip() and not TEXT.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    with open(path, "wb") as f:
        f.write(data)
    print(f"wrote {len(data)} bytes ({len(TEXT)} characters) to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
