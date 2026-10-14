# Spherical Code Record: `(d=28, N=70)` (`c* = 0.0517863124041101353861329` vs `0.051797462893`)

## What

Verified that claim/object/code_28_70.json (93,832 bytes, SHA-256 cd7c56d206970b5e9b3b44ef5f31395908b4e84acf22f807c46a543556f05263) defines 70 explicit 33-digit vectors in R^28 whose 60-digit normalized maximum pairwise inner product is c* = 0.0517863124041101353861329 (minimum angle 87.031535037277 deg), strictly improving upon the unstarred, unlabeled standing record c_table = 0.051797462893 in Henry Cohn's spherical-codes.org table by c_table - c* = 1.115049e-5 (over 111,000x the 1e-10 threshold).

In this package, the explicit 32-digit coordinate set is stored at `object/code_28_70.json` (and `object/code_28_70.txt`, SHA-256 `cd7c56d206970b5e9b3b44ef5f31395908b4e84acf22f807c46a543556f05263`, 93,832 bytes).

## Check It Yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-cd7c56d2/`), run:

```sh
sh verify-it-yourself/run_checks.sh
```

- **Requirements**: `python3` (3.8+, standard library `decimal` at 60-digit precision).
- **Rough laptop time**: < 2 seconds.
- **Expected last line**: `ALL CHECKS PASS`

## Compared To

All criterion sources were fetched live on `2026-10-14` (`08:38:00Z`, one honest GET per source, no retries; see `the-record-we-beat/README.md` and `the-record-we-beat/sources_2026-10-14T08-38-00Z.json`):

| Source | `(d, N)` | Listed Cosine `c_table` | Our Verified `c*` | Gain (`c_table - c*`) | Starred (`*`)? | `needs more optimization`? | URL |
|---|---|---|---|---|---|---|---|
| `spherical-codes.org` (HTML + `/plain`) | `(28, 70)` | `0.051797462893` | **`0.0517863124041101353861329`** | **`1.115049e-5`** | `no` | `no` | `https://spherical-codes.org/` |
| `TROPHY_CASE.md` | `(28, 70)` | unlisted | **`0.0517863124041101353861329`** | — | — | — | `TROPHY_CASE.md` |

## Not Claimed

- Scope: Constructive upper bound on minimal-angle cosine `c*` for `N = 70` unit vectors in `R^28` (equivalently lower bound on minimal angle). Does not claim proof of global optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone 60-digit checker shipped here; not peer reviewed.

## Credits

- **H. Cohn**, *Table of Spherical Codes* (`https://spherical-codes.org/`).
- Contributor credit: `anonymous-c6d1e0ab`.
