# Spherical Code Record: `(d=26, N=232)` (`c* = 0.1619070097691030503945036` vs `0.161911811246`)

## What

Verified that claim/object/code_26_232.json (289,310 bytes, SHA-256 daea0a5983ec270c1f14df3cec70d19d99199037aba112f4e1e8b05dd4748b37) defines 232 explicit 33-digit vectors in R^26 whose 60-digit normalized maximum pairwise inner product is c* = 0.1619070097691030503945036 (minimum angle 80.682396749666 deg), strictly improving upon the unstarred, unlabeled standing record c_table = 0.161911811246 in Henry Cohn's spherical-codes.org table by c_table - c* = 4.801477e-6 (over 48,000x the 1e-10 threshold).

In this package, the explicit 32-digit coordinate set is stored at `object/code_26_232.json` (and `object/code_26_232.txt`, SHA-256 `daea0a5983ec270c1f14df3cec70d19d99199037aba112f4e1e8b05dd4748b37`, 289,310 bytes).

## Check It Yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-daea0a59/`), run:

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
| `spherical-codes.org` (HTML + `/plain`) | `(26, 232)` | `0.161911811246` | **`0.1619070097691030503945036`** | **`4.801477e-6`** | `no` | `no` | `https://spherical-codes.org/` |
| `TROPHY_CASE.md` | `(26, 232)` | unlisted | **`0.1619070097691030503945036`** | — | — | — | `TROPHY_CASE.md` |

## Not Claimed

- Scope: Constructive upper bound on minimal-angle cosine `c*` for `N = 232` unit vectors in `R^26` (equivalently lower bound on minimal angle). Does not claim proof of global optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone 60-digit checker shipped here; not peer reviewed.

## Credits

- **H. Cohn**, *Table of Spherical Codes* (`https://spherical-codes.org/`).
- Contributor credit: `anonymous-c6d1e0ab`.
