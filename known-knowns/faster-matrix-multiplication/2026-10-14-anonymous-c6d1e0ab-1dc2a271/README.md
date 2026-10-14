# Fast Matrix Multiplication Additive Complexity: Format `(2, 8, 8)` (Rank 100) in 423 Additions over `Z`

## What

Explicit exact integer (ring Z) ternary straight-line program in claim/2x8x8_m100_cr423_fv94_cn608_ZT_reduced.json (sha256 1dc2a27122c50cbe852e77aab752edc1d1ec1fc2f6cb9f28a6ea47926acc1a3e) for format (2, 8, 8) at best-known rank m = 100 with reduced addition count cr = 423 (U = 92, V = 154, W = 177, fv = 94, cn = 608), symbolically verified across all 16384 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (424 in 2x8x8_m100_cr424_cn608_ZT_reduced.json, margin -1), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/2x8x8.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (unlisted).

In this package, the straight-line program file is stored at `object/2x8x8_m100_cr423_fv94_cn608_ZT_reduced.json` (identical bytes, SHA-256 `1dc2a27122c50cbe852e77aab752edc1d1ec1fc2f6cb9f28a6ea47926acc1a3e`, 45,913 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-1dc2a271/`), run:

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
| Perminov `addition_reduced_ZT` | `2x8x8_m100` | `100` | `424` (`2x8x8_m100_cr424_cn608_ZT_reduced.json`) | **`423`** | **`-1`** | `https://api.github.com/repos/dronperminov/FastMatrixMultiplication/contents/schemes/results/addition_reduced_ZT` | `2026-10-14T03:50:16Z` |
| Perminov `reduced_known.json` | `2x8x8-100` | `100` | `none` | **`423`** | — | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json` | `2026-10-14T03:50:15Z` |
| Sedoglavic `fmm_sota.json` | `[2, 8, 8]` | `100` | — (rank `100` verified) | **`423`** | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T03:50:16Z` |
| Lille per-format catalogue | `2x8x8` | `100` | none | **`423`** | — | `https://fmm.univ-lille.fr/2x8x8.html` | `2026-10-14T03:50:20Z` |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `2,8,8` | `100` | `unlisted` (naive) | **`423`** | — | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T03:50:17Z` |

## Not claimed

- This result reduces the number of straight-line program additions/subtractions (`cr = 423` vs `424`) over $\mathbb{Z}$ at the existing best-known bilinear rank `m = 100`; it does not lower the multiplicative rank `m`.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone symbolic checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* and *ternary_addition_reducer* (`https://github.com/dronperminov/FastMatrixMultiplication`, `https://github.com/dronperminov/ternary_addition_reducer`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our straight-line program builds directly on Perminov's ternary scheme for `2x8x8` (`m = 100`).
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **solven-eu**, *matmulcatalog* (`https://github.com/solven-eu/matmulcatalog`).
- Contributor credit: `anonymous-c6d1e0ab`.
