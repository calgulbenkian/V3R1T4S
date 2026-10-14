# Fast Matrix Multiplication Additive Complexity: Format `(5, 5, 6)` (Rank 110) in 451 Additions over `Z`

## What

Explicit exact integer (ring Z) ternary straight-line program in claim/5x5x6_m110_cr451_fv202_cn1208_ZT_reduced.json (sha256 4f95dd2dbee2b93b8c8e102b863438193c7d6a5b899fcd0ec5a35661c115cd5d) for format (5, 5, 6) at best-known rank m = 110 with reduced addition count cr = 451 (U = 119, V = 124, W = 208, fv = 202, cn = 1208), symbolically verified across all 22500 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (460 in 5x5x6_m110_cr460_fv204_cn1215_ZT_reduced.json, margin -9), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/5x5x6.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+1215).

In this package, the straight-line program file is stored at `object/5x5x6_m110_cr451_fv202_cn1208_ZT_reduced.json` (identical bytes, SHA-256 `4f95dd2dbee2b93b8c8e102b863438193c7d6a5b899fcd0ec5a35661c115cd5d`, 57,458 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-4f95dd2d/`), run:

```sh
sh verify-it-yourself/run_checks.sh
```

- **Requirements**: `python3` (3.8+, standard library only).
- **Rough laptop time**: < 1 second.
- **Expected last line**: `ALL CHECKS PASS`

## Compared to

All criterion sources were fetched live on `2026-10-14` (`03:50:15Z`-`03:50:28Z`, one honest GET per source, no retries; see `the-record-we-beat/README.md` and `the-record-we-beat/sources_2026-10-14T03-50-16Z.json`):

| Source | Cell | Rank `m` | Listed Additions (`cr`) | Our Additions (`cr`) | Margin | URL | UTC Fetch Time |
|---|---|---|---|---|---|---|---|
| Perminov `addition_reduced_ZT` | `5x5x6_m110` | `110` | `460` (`5x5x6_m110_cr460_fv204_cn1215_ZT_reduced.json`) | **`451`** | **`-9`** | `https://api.github.com/repos/dronperminov/FastMatrixMultiplication/contents/schemes/results/addition_reduced_ZT` | `2026-10-14T03:50:16Z` |
| Perminov `reduced_known.json` | `5x5x6-110` | `110` | `none` | **`451`** | — | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json` | `2026-10-14T03:50:15Z` |
| Sedoglavic `fmm_sota.json` | `[5, 5, 6]` | `110` | — (rank `110` verified) | **`451`** | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T03:50:16Z` |
| Lille per-format catalogue | `5x5x6` | `110` | none | **`451`** | — | `https://fmm.univ-lille.fr/5x5x6.html` | `2026-10-14T03:50:20Z` |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `5,5,6` | `110` | `+1215` (naive) | **`451`** | — | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T03:50:17Z` |

## Not claimed

- This result reduces the number of straight-line program additions/subtractions (`cr = 451` vs `460`) over $\mathbb{Z}$ at the existing best-known bilinear rank `m = 110`; it does not lower the multiplicative rank `m`.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone symbolic checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* and *ternary_addition_reducer* (`https://github.com/dronperminov/FastMatrixMultiplication`, `https://github.com/dronperminov/ternary_addition_reducer`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our straight-line program builds directly on Perminov's ternary scheme for `5x5x6` (`m = 110`).
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **solven-eu**, *matmulcatalog* (`https://github.com/solven-eu/matmulcatalog`).
- Contributor credit: `anonymous-c6d1e0ab`.
