# Fast Matrix Multiplication Additive Complexity: Format `(5, 5, 5)` (Rank 93) in 378 Additions over `Z`

## What

Explicit exact integer (ring Z) ternary straight-line program in claim/5x5x5_m93_cr378_fv157_cn844_ZT_reduced.json (sha256 118237670d742163d9f8caa3fd4e5c6a850fe9570fbb39ce3f32906b427c2a4a) for format (5, 5, 5) at best-known rank m = 93 with reduced addition count cr = 378 (U = 100, V = 103, W = 175, fv = 157, cn = 844), symbolically verified across all 15625 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (383 in 5x5x5_m93_cr383_fv160_cn843_ZT_reduced.json, margin -5), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/5x5x5.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+846).

In this package, the straight-line program file is stored at `object/5x5x5_m93_cr378_fv157_cn844_ZT_reduced.json` (identical bytes, SHA-256 `118237670d742163d9f8caa3fd4e5c6a850fe9570fbb39ce3f32906b427c2a4a`, 47,351 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-11823767/`), run:

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
| Perminov `addition_reduced_ZT` | `5x5x5_m93` | `93` | `383` (`5x5x5_m93_cr383_fv160_cn843_ZT_reduced.json`) | **`378`** | **`-5`** | `https://api.github.com/repos/dronperminov/FastMatrixMultiplication/contents/schemes/results/addition_reduced_ZT` | `2026-10-14T03:50:16Z` |
| Perminov `reduced_known.json` | `5x5x5-93` | `93` | `none` | **`378`** | — | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json` | `2026-10-14T03:50:15Z` |
| Sedoglavic `fmm_sota.json` | `[5, 5, 5]` | `93` | — (rank `93` verified) | **`378`** | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T03:50:16Z` |
| Lille per-format catalogue | `5x5x5` | `93` | none | **`378`** | — | `https://fmm.univ-lille.fr/5x5x5.html` | `2026-10-14T03:50:20Z` |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `5,5,5` | `93` | `+846` (naive) | **`378`** | — | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T03:50:17Z` |

## Not claimed

- This result reduces the number of straight-line program additions/subtractions (`cr = 378` vs `383`) over $\mathbb{Z}$ at the existing best-known bilinear rank `m = 93`; it does not lower the multiplicative rank `m`.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone symbolic checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* and *ternary_addition_reducer* (`https://github.com/dronperminov/FastMatrixMultiplication`, `https://github.com/dronperminov/ternary_addition_reducer`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our straight-line program builds directly on Perminov's ternary scheme for `5x5x5` (`m = 93`).
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **solven-eu**, *matmulcatalog* (`https://github.com/solven-eu/matmulcatalog`).
- Contributor credit: `anonymous-c6d1e0ab`.
