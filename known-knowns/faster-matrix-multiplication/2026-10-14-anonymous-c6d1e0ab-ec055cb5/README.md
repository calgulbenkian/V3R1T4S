# Fast Matrix Multiplication Additive Complexity: Format `(4, 4, 7)` (Rank 85) in 317 Additions over `Z`

## What

Explicit exact integer (ring Z) ternary straight-line program in claim/4x4x7_m85_cr317_fv119_cn631_ZT_reduced.json (sha256 ec055cb50ec26544703661a163796d145b57c732a2fa1586abb9d7dadfcb56dc) for format (4, 4, 7) at best-known rank m = 85 with reduced addition count cr = 317 (U = 80, V = 92, W = 145, fv = 119, cn = 631), symbolically verified across all 12544 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (319 in 4x4x7_m85_cr319_fv119_cn631_ZT_reduced.json, margin -2), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/4x4x7.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+631).

In this package, the straight-line program file is stored at `object/4x4x7_m85_cr317_fv119_cn631_ZT_reduced.json` (identical bytes, SHA-256 `ec055cb50ec26544703661a163796d145b57c732a2fa1586abb9d7dadfcb56dc`, 40,311 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-ec055cb5/`), run:

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
| Perminov `addition_reduced_ZT` | `4x4x7_m85` | `85` | `319` (`4x4x7_m85_cr319_fv119_cn631_ZT_reduced.json`) | **`317`** | **`-2`** | `https://api.github.com/repos/dronperminov/FastMatrixMultiplication/contents/schemes/results/addition_reduced_ZT` | `2026-10-14T03:50:16Z` |
| Perminov `reduced_known.json` | `4x4x7-85` | `85` | `none` | **`317`** | — | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json` | `2026-10-14T03:50:15Z` |
| Sedoglavic `fmm_sota.json` | `[4, 4, 7]` | `85` | — (rank `85` verified) | **`317`** | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T03:50:16Z` |
| Lille per-format catalogue | `4x4x7` | `85` | none | **`317`** | — | `https://fmm.univ-lille.fr/4x4x7.html` | `2026-10-14T03:50:20Z` |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `4,4,7` | `85` | `+631` (naive) | **`317`** | — | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T03:50:17Z` |

## Not claimed

- This result reduces the number of straight-line program additions/subtractions (`cr = 317` vs `319`) over $\mathbb{Z}$ at the existing best-known bilinear rank `m = 85`; it does not lower the multiplicative rank `m`.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone symbolic checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* and *ternary_addition_reducer* (`https://github.com/dronperminov/FastMatrixMultiplication`, `https://github.com/dronperminov/ternary_addition_reducer`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our straight-line program builds directly on Perminov's ternary scheme for `4x4x7` (`m = 85`).
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **solven-eu**, *matmulcatalog* (`https://github.com/solven-eu/matmulcatalog`).
- Contributor credit: `anonymous-c6d1e0ab`.
