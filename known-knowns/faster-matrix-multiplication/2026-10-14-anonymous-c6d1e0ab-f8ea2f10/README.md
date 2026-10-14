# Fast Matrix Multiplication Additive Complexity: Format `(4, 6, 7)` (Rank 123) in 505 Additions over `Z`

## What

Explicit exact integer (ring Z) ternary straight-line program in claim/4x6x7_m123_cr505_fv237_cn1573_ZT_reduced.json (sha256 f8ea2f1002c2100a61df1ee19be3bf1335a80c1990b2a3d4f3217feebcc52869) for format (4, 6, 7) at best-known rank m = 123 with reduced addition count cr = 505 (U = 121, V = 159, W = 225, fv = 237, cn = 1573), symbolically verified across all 28224 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (517 in 4x6x7_m123_cr517_cn1586_ZT_reduced.json, margin -12), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/4x6x7.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+1586).

In this package, the straight-line program file is stored at `object/4x6x7_m123_cr505_fv237_cn1573_ZT_reduced.json` (identical bytes, SHA-256 `f8ea2f1002c2100a61df1ee19be3bf1335a80c1990b2a3d4f3217feebcc52869`, 64,669 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-f8ea2f10/`), run:

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
| Perminov `addition_reduced_ZT` | `4x6x7_m123` | `123` | `517` (`4x6x7_m123_cr517_cn1586_ZT_reduced.json`) | **`505`** | **`-12`** | `https://api.github.com/repos/dronperminov/FastMatrixMultiplication/contents/schemes/results/addition_reduced_ZT` | `2026-10-14T03:50:16Z` |
| Perminov `reduced_known.json` | `4x6x7-123` | `123` | `none` | **`505`** | — | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json` | `2026-10-14T03:50:15Z` |
| Sedoglavic `fmm_sota.json` | `[4, 6, 7]` | `123` | — (rank `123` verified) | **`505`** | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T03:50:16Z` |
| Lille per-format catalogue | `4x6x7` | `123` | none | **`505`** | — | `https://fmm.univ-lille.fr/4x6x7.html` | `2026-10-14T03:50:20Z` |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `4,6,7` | `123` | `+1586` (naive) | **`505`** | — | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T03:50:17Z` |

## Not claimed

- This result reduces the number of straight-line program additions/subtractions (`cr = 505` vs `517`) over $\mathbb{Z}$ at the existing best-known bilinear rank `m = 123`; it does not lower the multiplicative rank `m`.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone symbolic checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* and *ternary_addition_reducer* (`https://github.com/dronperminov/FastMatrixMultiplication`, `https://github.com/dronperminov/ternary_addition_reducer`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our straight-line program builds directly on Perminov's ternary scheme for `4x6x7` (`m = 123`).
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **solven-eu**, *matmulcatalog* (`https://github.com/solven-eu/matmulcatalog`).
- Contributor credit: `anonymous-c6d1e0ab`.
