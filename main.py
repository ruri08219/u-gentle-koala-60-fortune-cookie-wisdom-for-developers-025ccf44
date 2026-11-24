"""Fortune-cookie entry for make.fun.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. Deterministic: constant string, no time, no random,
no network, standard library only.
"""

import os

ENTRY = "The code that works only on your machine has already chosen its only user."

MAX_CHARS = 120


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError("entry must be 1-120 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify by reading the file back, bytes included.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == ENTRY.encode("utf-8"), "entry.txt bytes do not match ENTRY"
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert written.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
