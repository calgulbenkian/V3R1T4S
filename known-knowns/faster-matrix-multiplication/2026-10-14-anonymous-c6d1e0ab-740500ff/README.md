# Fast Matrix Multiplication Additive Complexity: Format `(4, 6, 8)` (Rank 140) in 546 Additions over `Z`

## What

Explicit exact integer (ring Z) ternary straight-line program in claim/4x6x8_m140_cr546_fv288_cn1248_ZT_reduced.json (sha256 740500ff5c86434ddbb45c0e60d65af983dd457fbe6f1084e64e74480d7f53db) for format (4, 6, 8) at best-known rank m = 140 with reduced addition count cr = 546 (U = 115, V = 171, W = 260, fv = 288, cn = 1248), symbolically verified across all 36864 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (551 in 4x6x8_m140_cr551_cn1248_ZT_reduced.json, margin -5), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/4x6x8.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (unlisted).

In this package, the straight-line program file is stored at `object/4x6x8_m140_cr546_fv288_cn1248_ZT_reduced.json` (identical bytes, SHA-256 `740500ff5c86434ddbb45c0e60d65af983dd457fbe6f1084e64e74480d7f53db`, 73,288 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-740500ff/`), run:

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
| Perminov `addition_reduced_ZT` | `4x6x8_m140` | `140` | `551` (`4x6x8_m140_cr551_cn1248_ZT_reduced.json`) | **`546`** | **`-5`** | `https://api.github.com/repos/dronperminov/FastMatrixMultiplication/contents/schemes/results/addition_reduced_ZT` | `2026-10-14T03:50:16Z` |
| Perminov `reduced_known.json` | `4x6x8-140` | `140` | `none` | **`546`** | — | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json` | `2026-10-14T03:50:15Z` |
| Sedoglavic `fmm_sota.json` | `[4, 6, 8]` | `140` | — (rank `140` verified) | **`546`** | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T03:50:16Z` |
| Lille per-format catalogue | `4x6x8` | `140` | none | **`546`** | — | `https://fmm.univ-lille.fr/4x6x8.html` | `2026-10-14T03:50:20Z` |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `4,6,8` | `140` | `unlisted` (naive) | **`546`** | — | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T03:50:17Z` |

## Not claimed

- This result reduces the number of straight-line program additions/subtractions (`cr = 546` vs `551`) over $\mathbb{Z}$ at the existing best-known bilinear rank `m = 140`; it does not lower the multiplicative rank `m`.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone symbolic checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* and *ternary_addition_reducer* (`https://github.com/dronperminov/FastMatrixMultiplication`, `https://github.com/dronperminov/ternary_addition_reducer`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our straight-line program builds directly on Perminov's ternary scheme for `4x6x8` (`m = 140`).
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **solven-eu**, *matmulcatalog* (`https://github.com/solven-eu/matmulcatalog`).
- Contributor credit: `anonymous-c6d1e0ab`.
