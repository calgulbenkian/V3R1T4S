# Fast Matrix Multiplication Additive Complexity: Format `(3, 4, 5)` (Rank 47) in 159 Additions over `Z`

## What

Explicit exact integer (ring Z) ternary straight-line program in claim/3x4x5_m47_cr159_fv60_cn277_ZT_reduced.json (sha256 197ffad82f4cdd3ea6899fe41fc93c1b7c16917cfa5dba26199fe8143c06292d) for format (3, 4, 5) at best-known rank m = 47 with reduced addition count cr = 159 (U = 39, V = 46, W = 74, fv = 60, cn = 277), symbolically verified across all 3600 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (161 in 3x4x5_m47_cr161_cn277_ZT_reduced.json, margin -2), reduced_known.json (276 (Z) / 242 (Z2)), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/3x4x5.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+287).

In this package, the straight-line program file is stored at `object/3x4x5_m47_cr159_fv60_cn277_ZT_reduced.json` (identical bytes, SHA-256 `197ffad82f4cdd3ea6899fe41fc93c1b7c16917cfa5dba26199fe8143c06292d`, 20,943 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-197ffad8/`), run:

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
| Perminov `addition_reduced_ZT` | `3x4x5_m47` | `47` | `161` (`3x4x5_m47_cr161_cn277_ZT_reduced.json`) | **`159`** | **`-2`** | `https://api.github.com/repos/dronperminov/FastMatrixMultiplication/contents/schemes/results/addition_reduced_ZT` | `2026-10-14T03:50:16Z` |
| Perminov `reduced_known.json` | `3x4x5-47` | `47` | `Z:276 / Z2:242` | **`159`** | — | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json` | `2026-10-14T03:50:15Z` |
| Sedoglavic `fmm_sota.json` | `[3, 4, 5]` | `47` | — (rank `47` verified) | **`159`** | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T03:50:16Z` |
| Lille per-format catalogue | `3x4x5` | `47` | none | **`159`** | — | `https://fmm.univ-lille.fr/3x4x5.html` | `2026-10-14T03:50:20Z` |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `3,4,5` | `47` | `+287` (naive) | **`159`** | — | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T03:50:17Z` |

## Not claimed

- This result reduces the number of straight-line program additions/subtractions (`cr = 159` vs `161`) over $\mathbb{Z}$ at the existing best-known bilinear rank `m = 47`; it does not lower the multiplicative rank `m`.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone symbolic checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* and *ternary_addition_reducer* (`https://github.com/dronperminov/FastMatrixMultiplication`, `https://github.com/dronperminov/ternary_addition_reducer`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our straight-line program builds directly on Perminov's ternary scheme for `3x4x5` (`m = 47`).
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **solven-eu**, *matmulcatalog* (`https://github.com/solven-eu/matmulcatalog`).
- Contributor credit: `anonymous-c6d1e0ab`.
