# Fast Matrix Multiplication Additive Complexity: Format `(4, 5, 7)` (Rank 104) in 395 Additions over `Z`

## What

Explicit exact integer (ring Z) ternary straight-line program in claim/4x5x7_m104_cr395_fv161_cn931_ZT_reduced.json (sha256 4448c119d128c8be762c29223b43d7486bd9bb7acc9633d9d6fd23110445aa72) for format (4, 5, 7) at best-known rank m = 104 with reduced addition count cr = 395 (U = 96, V = 116, W = 183, fv = 161, cn = 931), symbolically verified across all 19600 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (400 in 4x5x7_m104_cr400_fv163_cn931_ZT_reduced.json, margin -5), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/4x5x7.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+927).

In this package, the straight-line program file is stored at `object/4x5x7_m104_cr395_fv161_cn931_ZT_reduced.json` (identical bytes, SHA-256 `4448c119d128c8be762c29223b43d7486bd9bb7acc9633d9d6fd23110445aa72`, 50,377 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-4448c119/`), run:

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
| Perminov `addition_reduced_ZT` | `4x5x7_m104` | `104` | `400` (`4x5x7_m104_cr400_fv163_cn931_ZT_reduced.json`) | **`395`** | **`-5`** | `https://api.github.com/repos/dronperminov/FastMatrixMultiplication/contents/schemes/results/addition_reduced_ZT` | `2026-10-14T03:50:16Z` |
| Perminov `reduced_known.json` | `4x5x7-104` | `104` | `none` | **`395`** | — | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json` | `2026-10-14T03:50:15Z` |
| Sedoglavic `fmm_sota.json` | `[4, 5, 7]` | `104` | — (rank `104` verified) | **`395`** | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T03:50:16Z` |
| Lille per-format catalogue | `4x5x7` | `104` | none | **`395`** | — | `https://fmm.univ-lille.fr/4x5x7.html` | `2026-10-14T03:50:20Z` |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `4,5,7` | `104` | `+927` (naive) | **`395`** | — | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T03:50:17Z` |

## Not claimed

- This result reduces the number of straight-line program additions/subtractions (`cr = 395` vs `400`) over $\mathbb{Z}$ at the existing best-known bilinear rank `m = 104`; it does not lower the multiplicative rank `m`.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone symbolic checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* and *ternary_addition_reducer* (`https://github.com/dronperminov/FastMatrixMultiplication`, `https://github.com/dronperminov/ternary_addition_reducer`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our straight-line program builds directly on Perminov's ternary scheme for `4x5x7` (`m = 104`).
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **solven-eu**, *matmulcatalog* (`https://github.com/solven-eu/matmulcatalog`).
- Contributor credit: `anonymous-c6d1e0ab`.
