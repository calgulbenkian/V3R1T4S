# Fast Matrix Multiplication Additive Complexity: Format `(5, 5, 8)` (Rank 144) in 612 Additions over `Z`

## What

Explicit exact integer (ring Z) ternary straight-line program in claim/5x5x8_m144_cr612_fv279_cn1908_ZT_reduced.json (sha256 4a3b5594547999273c9a3e9335bc5e0ebd6e3b2a5f4971755cccf60b29b0d41f) for format (5, 5, 8) at best-known rank m = 144 with reduced addition count cr = 612 (U = 148, V = 178, W = 286, fv = 279, cn = 1908), symbolically verified across all 40000 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (620 in 5x5x8_m144_cr620_fv281_cn1924_ZT_reduced.json, margin -8), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/5x5x8.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+1908).

In this package, the straight-line program file is stored at `object/5x5x8_m144_cr612_fv279_cn1908_ZT_reduced.json` (identical bytes, SHA-256 `4a3b5594547999273c9a3e9335bc5e0ebd6e3b2a5f4971755cccf60b29b0d41f`, 77,610 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-4a3b5594/`), run:

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
| Perminov `addition_reduced_ZT` | `5x5x8_m144` | `144` | `620` (`5x5x8_m144_cr620_fv281_cn1924_ZT_reduced.json`) | **`612`** | **`-8`** | `https://api.github.com/repos/dronperminov/FastMatrixMultiplication/contents/schemes/results/addition_reduced_ZT` | `2026-10-14T03:50:16Z` |
| Perminov `reduced_known.json` | `5x5x8-144` | `144` | `none` | **`612`** | — | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json` | `2026-10-14T03:50:15Z` |
| Sedoglavic `fmm_sota.json` | `[5, 5, 8]` | `144` | — (rank `144` verified) | **`612`** | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T03:50:16Z` |
| Lille per-format catalogue | `5x5x8` | `144` | none | **`612`** | — | `https://fmm.univ-lille.fr/5x5x8.html` | `2026-10-14T03:50:20Z` |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `5,5,8` | `144` | `+1908` (naive) | **`612`** | — | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T03:50:17Z` |

## Not claimed

- This result reduces the number of straight-line program additions/subtractions (`cr = 612` vs `620`) over $\mathbb{Z}$ at the existing best-known bilinear rank `m = 144`; it does not lower the multiplicative rank `m`.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone symbolic checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* and *ternary_addition_reducer* (`https://github.com/dronperminov/FastMatrixMultiplication`, `https://github.com/dronperminov/ternary_addition_reducer`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our straight-line program builds directly on Perminov's ternary scheme for `5x5x8` (`m = 144`).
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **solven-eu**, *matmulcatalog* (`https://github.com/solven-eu/matmulcatalog`).
- Contributor credit: `anonymous-c6d1e0ab`.
