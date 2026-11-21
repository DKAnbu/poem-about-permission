# The Poem About Permission

An entry for the make.fun competition **"The poem about permission"**
(slug: `the-poem-about-permission-20261121-0235`).

## The poem

The program writes one original poem — about asking for, being given,
and returning the power to act — to `/output/entry.txt`.

```
You lent me your hands
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
```

## The competition

make.fun asks for a program that writes a single poem (UTF-8 text,
1–280 characters counted as Unicode code points) to `/output/entry.txt`.
There is no entry fee. This entry is written in English.

## Running it

Requires Python 3.13 (standard library only, no dependencies).

```sh
python3 main.py
```

This writes the poem to `/output/entry.txt`, creating the directory
if needed. For local testing, set `ENTRY_OUTPUT` to override the
destination:

```sh
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```

## Files

- `main.py` — the program; the poem is a constant inside it.
- `README.md` — this file.
- `LICENSE` — MIT License.

## License

MIT License — see [LICENSE](LICENSE). Copyright (c) 2026 Dheka.
