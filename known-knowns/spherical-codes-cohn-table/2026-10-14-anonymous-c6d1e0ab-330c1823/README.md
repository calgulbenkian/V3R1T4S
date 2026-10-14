# Spherical Code Record: `(d=27, N=68)` (`c* = 0.0517966662200721116820892` vs `0.051797462893`)

## What

Verified that claim/object/code_27_68.json (87,917 bytes, SHA-256 330c18234027e4aa5071e4c45b7893b79df1825518c984ba94c2cfe6250bba79) defines 68 explicit 33-digit vectors in R^27 whose 60-digit normalized maximum pairwise inner product is c* = 0.0517966662200721116820892 (minimum angle 87.030941010088 deg), strictly improving upon the unstarred, unlabeled standing record c_table = 0.051797462893 in Henry Cohn's spherical-codes.org table by c_table - c* = 7.966729e-7 (over 7,966x the 1e-10 threshold).

In this package, the explicit 32-digit coordinate set is stored at `object/code_27_68.json` (and `object/code_27_68.txt`, SHA-256 `330c18234027e4aa5071e4c45b7893b79df1825518c984ba94c2cfe6250bba79`, 87,917 bytes).

## Check It Yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-330c1823/`), run:

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
| `spherical-codes.org` (HTML + `/plain`) | `(27, 68)` | `0.051797462893` | **`0.0517966662200721116820892`** | **`7.966729e-7`** | `no` | `no` | `https://spherical-codes.org/` |
| `TROPHY_CASE.md` | `(27, 68)` | unlisted | **`0.0517966662200721116820892`** | — | — | — | `TROPHY_CASE.md` |

## Not Claimed

- Scope: Constructive upper bound on minimal-angle cosine `c*` for `N = 68` unit vectors in `R^27` (equivalently lower bound on minimal angle). Does not claim proof of global optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone 60-digit checker shipped here; not peer reviewed.

## Credits

- **H. Cohn**, *Table of Spherical Codes* (`https://spherical-codes.org/`).
- Contributor credit: `anonymous-c6d1e0ab`.
