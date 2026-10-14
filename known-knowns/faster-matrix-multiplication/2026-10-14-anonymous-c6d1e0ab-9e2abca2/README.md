# Fast Matrix Multiplication Additive Complexity: Format `(4, 4, 6)` (Rank 73) in 275 Additions over `Z`

## What

Explicit exact integer (ring Z) ternary straight-line program in claim/4x4x6_m73_cr275_fv101_cn534_ZT_reduced.json (sha256 9e2abca2c586a6020b90ae6e020dabb4b00f47dead9e4bea48a804452a8dfff7) for format (4, 4, 6) at best-known rank m = 73 with reduced addition count cr = 275 (U = 71, V = 78, W = 126, fv = 101, cn = 534), symbolically verified across all 9216 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (280 in 4x4x6_m73_cr280_cn540_ZT_reduced.json, margin -5), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/4x4x6.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+565).

In this package, the straight-line program file is stored at `object/4x4x6_m73_cr275_fv101_cn534_ZT_reduced.json` (identical bytes, SHA-256 `9e2abca2c586a6020b90ae6e020dabb4b00f47dead9e4bea48a804452a8dfff7`, 34,669 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-9e2abca2/`), run:

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
| Perminov `addition_reduced_ZT` | `4x4x6_m73` | `73` | `280` (`4x4x6_m73_cr280_cn540_ZT_reduced.json`) | **`275`** | **`-5`** | `https://api.github.com/repos/dronperminov/FastMatrixMultiplication/contents/schemes/results/addition_reduced_ZT` | `2026-10-14T03:50:16Z` |
| Perminov `reduced_known.json` | `4x4x6-73` | `73` | `none` | **`275`** | — | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json` | `2026-10-14T03:50:15Z` |
| Sedoglavic `fmm_sota.json` | `[4, 4, 6]` | `73` | — (rank `73` verified) | **`275`** | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T03:50:16Z` |
| Lille per-format catalogue | `4x4x6` | `73` | none | **`275`** | — | `https://fmm.univ-lille.fr/4x4x6.html` | `2026-10-14T03:50:20Z` |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `4,4,6` | `73` | `+565` (naive) | **`275`** | — | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T03:50:17Z` |

## Not claimed

- This result reduces the number of straight-line program additions/subtractions (`cr = 275` vs `280`) over $\mathbb{Z}$ at the existing best-known bilinear rank `m = 73`; it does not lower the multiplicative rank `m`.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone symbolic checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* and *ternary_addition_reducer* (`https://github.com/dronperminov/FastMatrixMultiplication`, `https://github.com/dronperminov/ternary_addition_reducer`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our straight-line program builds directly on Perminov's ternary scheme for `4x4x6` (`m = 73`).
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **solven-eu**, *matmulcatalog* (`https://github.com/solven-eu/matmulcatalog`).
- Contributor credit: `anonymous-c6d1e0ab`.
