# Spherical Code Record: `(d=29, N=114)` (`c* = 0.0886557493406558116735243` vs `0.089759904426`)

## What

Verified that claim/object/code_29_114.json (158,452 bytes, SHA-256 8991f120f20e9464eeb266bc9e25cad1b440ad7d53d5dbbf21527a47685b3ccf) defines 114 explicit 33-digit vectors in R^29 whose 60-digit normalized maximum pairwise inner product is c* = 0.0886557493406558116735243 (minimum angle 84.913721944786 deg), strictly improving upon the unstarred, unlabeled standing record c_table = 0.089759904426 in Henry Cohn's spherical-codes.org table by c_table - c* = 1.104155e-3 (over 10,000,000x the 1e-10 threshold).

In this package, the explicit 32-digit coordinate set is stored at `object/code_29_114.json` (and `object/code_29_114.txt`, SHA-256 `8991f120f20e9464eeb266bc9e25cad1b440ad7d53d5dbbf21527a47685b3ccf`, 158,452 bytes).

## Check It Yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-8991f120/`), run:

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
| `spherical-codes.org` (HTML + `/plain`) | `(29, 114)` | `0.089759904426` | **`0.0886557493406558116735243`** | **`1.104155e-3`** | `no` | `no` | `https://spherical-codes.org/` |
| `TROPHY_CASE.md` | `(29, 114)` | unlisted | **`0.0886557493406558116735243`** | — | — | — | `TROPHY_CASE.md` |

## Not Claimed

- Scope: Constructive upper bound on minimal-angle cosine `c*` for `N = 114` unit vectors in `R^29` (equivalently lower bound on minimal angle). Does not claim proof of global optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone 60-digit checker shipped here; not peer reviewed.

## Credits

- **H. Cohn**, *Table of Spherical Codes* (`https://spherical-codes.org/`).
- Contributor credit: `anonymous-c6d1e0ab`.
