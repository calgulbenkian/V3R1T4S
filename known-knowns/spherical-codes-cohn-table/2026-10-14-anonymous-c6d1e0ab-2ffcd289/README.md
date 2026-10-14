# Spherical Code Record: `(d=30, N=74)` (`c* = 0.0515109900801632382072426` vs `0.051797462893`)

## What

Verified that claim/object/code_30_74.json (106,243 bytes, SHA-256 2ffcd2896808bedffa1ba211a4ee8dbe30cd0e3c457da8df5d09ec3745596686) defines 74 explicit 33-digit vectors in R^30 whose 60-digit normalized maximum pairwise inner product is c* = 0.0515109900801632382072426 (minimum angle 87.047330926989 deg), strictly improving upon the unstarred, unlabeled standing record c_table = 0.051797462893 in Henry Cohn's spherical-codes.org table by c_table - c* = 2.864728e-4 (over 2,860,000x the 1e-10 threshold).

In this package, the explicit 32-digit coordinate set is stored at `object/code_30_74.json` (and `object/code_30_74.txt`, SHA-256 `2ffcd2896808bedffa1ba211a4ee8dbe30cd0e3c457da8df5d09ec3745596686`, 106,243 bytes).

## Check It Yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-2ffcd289/`), run:

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
| `spherical-codes.org` (HTML + `/plain`) | `(30, 74)` | `0.051797462893` | **`0.0515109900801632382072426`** | **`2.864728e-4`** | `no` | `no` | `https://spherical-codes.org/` |
| `TROPHY_CASE.md` | `(30, 74)` | unlisted | **`0.0515109900801632382072426`** | — | — | — | `TROPHY_CASE.md` |

## Not Claimed

- Scope: Constructive upper bound on minimal-angle cosine `c*` for `N = 74` unit vectors in `R^30` (equivalently lower bound on minimal angle). Does not claim proof of global optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone 60-digit checker shipped here; not peer reviewed.

## Credits

- **H. Cohn**, *Table of Spherical Codes* (`https://spherical-codes.org/`).
- Contributor credit: `anonymous-c6d1e0ab`.
