#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch entry for make.fun competition
u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.

Writes a single sentence pitching a ridiculous invention that fixes a tiny
everyday annoyance to $MAKEFUN_OUTPUT_DIR/entry.txt (default ./out).
Deterministic, Python 3 stdlib only, no network, no secrets.

The invention: a Wi-Fi router that leans over and whispers the password to
guests in a tiny embarrassed voice, so its owner never has to spell out
"capital K, underscore, zero" ever again. The annoyance is the little
ritual of reciting a Wi-Fi password character by character to every guest;
the fix is absurd (a shy, whispering router) yet weirdly plausible (the
router already knows the password, so why shouldn't it just tell them?).

Design: the entry is validated twice, by two separate steps. First,
``validate`` checks the pitch string in memory against the competition
gate (UTF-8 text, 1-220 characters, not only whitespace, exactly one
sentence ending in a single period, no newlines). Then ``write_entry``
writes it to ``entry.txt`` and reads the file back from disk, verifying
that what landed on disk is byte-identical to the pitch and still passes
the same gate — so the submitted file is exactly what was checked, never
a stale or half-written copy. The output is deterministic: the pitch is a
fixed string, so every run produces the same bytes.
"""

import os
import sys

# The pitch: one sentence, 1-220 characters, naming the annoyance (spelling
# out the Wi-Fi password), the invention (a whispering router) and its silly
# mechanism (it leans over and whispers in a tiny embarrassed voice).
PITCH = (
    "A Wi-Fi router that leans over and whispers the password to guests in "
    "a tiny embarrassed voice, so you never have to spell out 'capital K, "
    "underscore, zero' ever again."
)


def validate(text: str) -> None:
    """Verify the entry against the gate: UTF-8 text, 1-220 chars, not only
    whitespace, exactly one sentence.

    Called twice: once on the pitch string in memory, and once on the text
    read back from the written file, so a write error cannot slip through.
    """
    if not text or not text.strip():
        raise SystemExit("entry is empty or only whitespace")
    encoded = text.encode("utf-8")  # raises if not valid UTF-8 text
    if not (1 <= len(text) <= 220):
        raise SystemExit(f"entry is {len(text)} chars, must be 1-220")
    if text.strip() != text:
        raise SystemExit("entry has leading/trailing whitespace")
    # Single sentence: exactly one sentence-terminating period, at the end.
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence ending in '.'")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    print(f"validate OK: {len(text)} chars, {len(encoded)} bytes, "
          f"1 sentence")


def write_entry(text: str, out_dir: str) -> str:
    """Write the pitch to ``entry.txt`` in ``out_dir`` and verify the file
    on disk, byte for byte, before returning its path.

    The read-back check is the point: it proves the bytes the gate will
    read are the bytes we validated, not just the string we intended.
    """
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify what was actually written, not just what we intended.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("written entry differs from the pitch")
    validate(written)
    print(f"wrote {path}")
    return path


def main() -> None:
    validate(PITCH)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./out")
    write_entry(PITCH, out_dir)


if __name__ == "__main__":
    main()
