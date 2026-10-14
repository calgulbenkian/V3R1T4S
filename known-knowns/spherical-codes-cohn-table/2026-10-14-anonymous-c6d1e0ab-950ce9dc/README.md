# Spherical Code Record: `(d=29, N=72)` (`c* = 0.0517077789990875933009913` vs `0.051797462893`)

## What

Verified that claim/object/code_29_72.json (99,927 bytes, SHA-256 950ce9dc86f4ea867119e0d09e9d202a7e4b36680d1375202857a3d847340713) defines 72 explicit 33-digit vectors in R^29 whose 60-digit normalized maximum pairwise inner product is c* = 0.0517077789990875933009913 (minimum angle 87.036040706523 deg), strictly improving upon the unstarred, unlabeled standing record c_table = 0.051797462893 in Henry Cohn's spherical-codes.org table by c_table - c* = 8.968389e-5 (over 896,000x the 1e-10 threshold).

In this package, the explicit 32-digit coordinate set is stored at `object/code_29_72.json` (and `object/code_29_72.txt`, SHA-256 `950ce9dc86f4ea867119e0d09e9d202a7e4b36680d1375202857a3d847340713`, 99,927 bytes).

## Check It Yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-950ce9dc/`), run:

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
| `spherical-codes.org` (HTML + `/plain`) | `(29, 72)` | `0.051797462893` | **`0.0517077789990875933009913`** | **`8.968389e-5`** | `no` | `no` | `https://spherical-codes.org/` |
| `TROPHY_CASE.md` | `(29, 72)` | unlisted | **`0.0517077789990875933009913`** | — | — | — | `TROPHY_CASE.md` |

## Not Claimed

- Scope: Constructive upper bound on minimal-angle cosine `c*` for `N = 72` unit vectors in `R^29` (equivalently lower bound on minimal angle). Does not claim proof of global optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone 60-digit checker shipped here; not peer reviewed.

## Credits

- **H. Cohn**, *Table of Spherical Codes* (`https://spherical-codes.org/`).
- Contributor credit: `anonymous-c6d1e0ab`.
