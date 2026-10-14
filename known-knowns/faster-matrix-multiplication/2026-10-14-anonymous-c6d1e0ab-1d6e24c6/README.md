# Fast Matrix Multiplication Additive Complexity: Format `(5, 5, 7)` (Rank 127) in 525 Additions over `Z`

## What

Explicit exact integer (ring Z) ternary straight-line program in claim/5x5x7_m127_cr525_fv245_cn1602_ZT_reduced.json (sha256 1d6e24c6edebc809e6d6cfa7a3ecfec0f9b00550ebcf92c3289d510eb1f091fd) for format (5, 5, 7) at best-known rank m = 127 with reduced addition count cr = 525 (U = 127, V = 150, W = 248, fv = 245, cn = 1602), symbolically verified across all 30625 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (531 in 5x5x7_m127_cr531_fv245_cn1607_ZT_reduced.json, margin -6), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/5x5x7.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+1606).

In this package, the straight-line program file is stored at `object/5x5x7_m127_cr525_fv245_cn1602_ZT_reduced.json` (identical bytes, SHA-256 `1d6e24c6edebc809e6d6cfa7a3ecfec0f9b00550ebcf92c3289d510eb1f091fd`, 67,448 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-1d6e24c6/`), run:

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
| Perminov `addition_reduced_ZT` | `5x5x7_m127` | `127` | `531` (`5x5x7_m127_cr531_fv245_cn1607_ZT_reduced.json`) | **`525`** | **`-6`** | `https://api.github.com/repos/dronperminov/FastMatrixMultiplication/contents/schemes/results/addition_reduced_ZT` | `2026-10-14T03:50:16Z` |
| Perminov `reduced_known.json` | `5x5x7-127` | `127` | `none` | **`525`** | — | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json` | `2026-10-14T03:50:15Z` |
| Sedoglavic `fmm_sota.json` | `[5, 5, 7]` | `127` | — (rank `127` verified) | **`525`** | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T03:50:16Z` |
| Lille per-format catalogue | `5x5x7` | `127` | none | **`525`** | — | `https://fmm.univ-lille.fr/5x5x7.html` | `2026-10-14T03:50:20Z` |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `5,5,7` | `127` | `+1606` (naive) | **`525`** | — | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T03:50:17Z` |

## Not claimed

- This result reduces the number of straight-line program additions/subtractions (`cr = 525` vs `531`) over $\mathbb{Z}$ at the existing best-known bilinear rank `m = 127`; it does not lower the multiplicative rank `m`.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone symbolic checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* and *ternary_addition_reducer* (`https://github.com/dronperminov/FastMatrixMultiplication`, `https://github.com/dronperminov/ternary_addition_reducer`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our straight-line program builds directly on Perminov's ternary scheme for `5x5x7` (`m = 127`).
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **solven-eu**, *matmulcatalog* (`https://github.com/solven-eu/matmulcatalog`).
- Contributor credit: `anonymous-c6d1e0ab`.
