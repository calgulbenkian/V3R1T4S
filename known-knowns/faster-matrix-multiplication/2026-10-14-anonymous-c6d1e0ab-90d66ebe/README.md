# Fast Matrix Multiplication Additive Complexity: Format `(2, 4, 8)` (Rank 51) in 187 Additions over `Z`

## What

Explicit exact integer (ring Z) ternary straight-line program in claim/2x4x8_m51_cr187_fv62_cn354_ZT_reduced.json (sha256 90d66ebee7ee850df3b63def31ba158745a7eb6c74b3a38d651aebf514bdf388) for format (2, 4, 8) at best-known rank m = 51 with reduced addition count cr = 187 (U = 38, V = 71, W = 78, fv = 62, cn = 354), symbolically verified across all 4096 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (188 in 2x4x8_m51_cr188_cn354_ZT_reduced.json, margin -1), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/2x4x8.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+354).

In this package, the straight-line program file is stored at `object/2x4x8_m51_cr187_fv62_cn354_ZT_reduced.json` (identical bytes, SHA-256 `90d66ebee7ee850df3b63def31ba158745a7eb6c74b3a38d651aebf514bdf388`, 23,291 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-90d66ebe/`), run:

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
| Perminov `addition_reduced_ZT` | `2x4x8_m51` | `51` | `188` (`2x4x8_m51_cr188_cn354_ZT_reduced.json`) | **`187`** | **`-1`** | `https://api.github.com/repos/dronperminov/FastMatrixMultiplication/contents/schemes/results/addition_reduced_ZT` | `2026-10-14T03:50:16Z` |
| Perminov `reduced_known.json` | `2x4x8-51` | `51` | `none` | **`187`** | — | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json` | `2026-10-14T03:50:15Z` |
| Sedoglavic `fmm_sota.json` | `[2, 4, 8]` | `51` | — (rank `51` verified) | **`187`** | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T03:50:16Z` |
| Lille per-format catalogue | `2x4x8` | `51` | none | **`187`** | — | `https://fmm.univ-lille.fr/2x4x8.html` | `2026-10-14T03:50:20Z` |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `2,4,8` | `51` | `+354` (naive) | **`187`** | — | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T03:50:17Z` |

## Not claimed

- This result reduces the number of straight-line program additions/subtractions (`cr = 187` vs `188`) over $\mathbb{Z}$ at the existing best-known bilinear rank `m = 51`; it does not lower the multiplicative rank `m`.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone symbolic checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* and *ternary_addition_reducer* (`https://github.com/dronperminov/FastMatrixMultiplication`, `https://github.com/dronperminov/ternary_addition_reducer`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our straight-line program builds directly on Perminov's ternary scheme for `2x4x8` (`m = 51`).
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **solven-eu**, *matmulcatalog* (`https://github.com/solven-eu/matmulcatalog`).
- Contributor credit: `anonymous-c6d1e0ab`.
