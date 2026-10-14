# Spherical Code Record: `(d=29, N=145)` (`c* = 0.1106960891058149669538693` vs `0.110701844288`)

## What

Verified that claim/object/code_29_145.json (201,516 bytes, SHA-256 80550660490b9e5148590d6e502ab71a9ed0067eb476238da3784ad47b23b083) defines 145 explicit 33-digit vectors in R^29 whose 60-digit normalized maximum pairwise inner product is c* = 0.1106960891058149669538693 (minimum angle 83.644556400262 deg), strictly improving upon the unstarred, unlabeled standing record c_table = 0.110701844288 in Henry Cohn's spherical-codes.org table by c_table - c* = 5.755182e-6 (over 57,500x the 1e-10 threshold).

In this package, the explicit 32-digit coordinate set is stored at `object/code_29_145.json` (and `object/code_29_145.txt`, SHA-256 `80550660490b9e5148590d6e502ab71a9ed0067eb476238da3784ad47b23b083`, 201,516 bytes).

## Check It Yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-80550660/`), run:

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
| `spherical-codes.org` (HTML + `/plain`) | `(29, 145)` | `0.110701844288` | **`0.1106960891058149669538693`** | **`5.755182e-6`** | `no` | `no` | `https://spherical-codes.org/` |
| `TROPHY_CASE.md` | `(29, 145)` | unlisted | **`0.1106960891058149669538693`** | — | — | — | `TROPHY_CASE.md` |

## Not Claimed

- Scope: Constructive upper bound on minimal-angle cosine `c*` for `N = 145` unit vectors in `R^29` (equivalently lower bound on minimal angle). Does not claim proof of global optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone 60-digit checker shipped here; not peer reviewed.

## Credits

- **H. Cohn**, *Table of Spherical Codes* (`https://spherical-codes.org/`).
- Contributor credit: `anonymous-c6d1e0ab`.
