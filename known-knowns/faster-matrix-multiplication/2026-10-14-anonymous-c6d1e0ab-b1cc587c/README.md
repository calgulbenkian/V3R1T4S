# Fast Matrix Multiplication Additive Complexity: Format `(3, 5, 5)` (Rank 58) in 218 Additions over `Z`

## What

Explicit exact integer (ring Z) ternary straight-line program in claim/3x5x5_m58_cr218_fv70_cn357_ZT_reduced.json (sha256 b1cc587cfcd53662a62995834bb546248b177ba2dd46139fddcb726caf2d46ac) for format (3, 5, 5) at best-known rank m = 58 with reduced addition count cr = 218 (U = 52, V = 70, W = 96, fv = 70, cn = 357), symbolically verified across all 5625 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (221 in 3x5x5_m58_cr221_cn357_ZT_reduced.json, margin -3), reduced_known.json (326 (Z) / 255 (Z2)), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/3x5x5.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+413).

In this package, the straight-line program file is stored at `object/3x5x5_m58_cr218_fv70_cn357_ZT_reduced.json` (identical bytes, SHA-256 `b1cc587cfcd53662a62995834bb546248b177ba2dd46139fddcb726caf2d46ac`, 26,510 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-b1cc587c/`), run:

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
| Perminov `addition_reduced_ZT` | `3x5x5_m58` | `58` | `221` (`3x5x5_m58_cr221_cn357_ZT_reduced.json`) | **`218`** | **`-3`** | `https://api.github.com/repos/dronperminov/FastMatrixMultiplication/contents/schemes/results/addition_reduced_ZT` | `2026-10-14T03:50:16Z` |
| Perminov `reduced_known.json` | `3x5x5-58` | `58` | `Z:326 / Z2:255` | **`218`** | — | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json` | `2026-10-14T03:50:15Z` |
| Sedoglavic `fmm_sota.json` | `[3, 5, 5]` | `58` | — (rank `58` verified) | **`218`** | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T03:50:16Z` |
| Lille per-format catalogue | `3x5x5` | `58` | none | **`218`** | — | `https://fmm.univ-lille.fr/3x5x5.html` | `2026-10-14T03:50:20Z` |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `3,5,5` | `58` | `+413` (naive) | **`218`** | — | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T03:50:17Z` |

## Not claimed

- This result reduces the number of straight-line program additions/subtractions (`cr = 218` vs `221`) over $\mathbb{Z}$ at the existing best-known bilinear rank `m = 58`; it does not lower the multiplicative rank `m`.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone symbolic checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* and *ternary_addition_reducer* (`https://github.com/dronperminov/FastMatrixMultiplication`, `https://github.com/dronperminov/ternary_addition_reducer`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our straight-line program builds directly on Perminov's ternary scheme for `3x5x5` (`m = 58`).
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **solven-eu**, *matmulcatalog* (`https://github.com/solven-eu/matmulcatalog`).
- Contributor credit: `anonymous-c6d1e0ab`.
