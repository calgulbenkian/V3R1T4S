# Spherical Code Record: `(d=30, N=117)` (`c* = 0.0883794850648560216379989` vs `0.088389506027`)

## What

Verified that claim/object/code_30_117.json (168,214 bytes, SHA-256 16db1fae5068ad356d1cf1c16e5b35b117fb9ede19e087e74bdc1291d572af19) defines 117 explicit 33-digit vectors in R^30 whose 60-digit normalized maximum pairwise inner product is c* = 0.0883794850648560216379989 (minimum angle 84.929613100835 deg), strictly improving upon the unstarred, unlabeled standing record c_table = 0.088389506027 in Henry Cohn's spherical-codes.org table by c_table - c* = 1.002096e-5 (over 100,000x the 1e-10 threshold).

In this package, the explicit 32-digit coordinate set is stored at `object/code_30_117.json` (and `object/code_30_117.txt`, SHA-256 `16db1fae5068ad356d1cf1c16e5b35b117fb9ede19e087e74bdc1291d572af19`, 168,214 bytes).

## Check It Yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-16db1fae/`), run:

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
| `spherical-codes.org` (HTML + `/plain`) | `(30, 117)` | `0.088389506027` | **`0.0883794850648560216379989`** | **`1.002096e-5`** | `no` | `no` | `https://spherical-codes.org/` |
| `TROPHY_CASE.md` | `(30, 117)` | unlisted | **`0.0883794850648560216379989`** | — | — | — | `TROPHY_CASE.md` |

## Not Claimed

- Scope: Constructive upper bound on minimal-angle cosine `c*` for `N = 117` unit vectors in `R^30` (equivalently lower bound on minimal angle). Does not claim proof of global optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone 60-digit checker shipped here; not peer reviewed.

## Credits

- **H. Cohn**, *Table of Spherical Codes* (`https://spherical-codes.org/`).
- Contributor credit: `anonymous-c6d1e0ab`.
