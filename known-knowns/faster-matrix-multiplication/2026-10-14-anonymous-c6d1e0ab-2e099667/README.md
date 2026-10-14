# Fast Matrix Multiplication Additive Complexity: Format `(4, 5, 5)` (Rank 76) in 295 Additions over `Z`

## What

Explicit exact integer (ring Z) ternary straight-line program in claim/4x5x5_m76_cr295_fv113_cn530_ZT_reduced.json (sha256 2e09966726d94ad6ade2c53de92b73c0e2f78a2d39d2a4a52f50a0e61eef085d) for format (4, 5, 5) at best-known rank m = 76 with reduced addition count cr = 295 (U = 76, V = 89, W = 130, fv = 113, cn = 530), symbolically verified across all 10000 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (299 in 4x5x5_m76_cr299_fv112_cn530_ZT_reduced.json, margin -4), reduced_known.json (451 (Z) / 372 (Z2)), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/4x5x5.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+549).

In this package, the straight-line program file is stored at `object/4x5x5_m76_cr295_fv113_cn530_ZT_reduced.json` (identical bytes, SHA-256 `2e09966726d94ad6ade2c53de92b73c0e2f78a2d39d2a4a52f50a0e61eef085d`, 36,780 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-2e099667/`), run:

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
| Perminov `addition_reduced_ZT` | `4x5x5_m76` | `76` | `299` (`4x5x5_m76_cr299_fv112_cn530_ZT_reduced.json`) | **`295`** | **`-4`** | `https://api.github.com/repos/dronperminov/FastMatrixMultiplication/contents/schemes/results/addition_reduced_ZT` | `2026-10-14T03:50:16Z` |
| Perminov `reduced_known.json` | `4x5x5-76` | `76` | `Z:451 / Z2:372` | **`295`** | — | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json` | `2026-10-14T03:50:15Z` |
| Sedoglavic `fmm_sota.json` | `[4, 5, 5]` | `76` | — (rank `76` verified) | **`295`** | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T03:50:16Z` |
| Lille per-format catalogue | `4x5x5` | `76` | none | **`295`** | — | `https://fmm.univ-lille.fr/4x5x5.html` | `2026-10-14T03:50:20Z` |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `4,5,5` | `76` | `+549` (naive) | **`295`** | — | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T03:50:17Z` |

## Not claimed

- This result reduces the number of straight-line program additions/subtractions (`cr = 295` vs `299`) over $\mathbb{Z}$ at the existing best-known bilinear rank `m = 76`; it does not lower the multiplicative rank `m`.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone symbolic checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* and *ternary_addition_reducer* (`https://github.com/dronperminov/FastMatrixMultiplication`, `https://github.com/dronperminov/ternary_addition_reducer`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our straight-line program builds directly on Perminov's ternary scheme for `4x5x5` (`m = 76`).
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **solven-eu**, *matmulcatalog* (`https://github.com/solven-eu/matmulcatalog`).
- Contributor credit: `anonymous-c6d1e0ab`.
