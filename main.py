#!/usr/bin/env python3
"""Entry for make.fun "The poem about permission".

Writes a single original poem to /output/entry.txt (or the path in
$ENTRY_OUTPUT, for local testing). Deterministic: the poem is a fixed
constant, printed exactly as written. Python 3.13, standard library only.
"""

import os
from pathlib import Path

POEM = """You lent me your hands
one afternoon.
I held the hammer
as if still yours.

I asked before each nail.
You nodded, not watching.
The fence stood by dusk,
your wood, my borrowed strength.

I gave them back clean.
That's it:
to hold power,
and hand it home.
"""


def main() -> None:
    output = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(POEM, encoding="utf-8")
    print(f"Wrote {len(POEM)} code points to {output}")


if __name__ == "__main__":
    main()
