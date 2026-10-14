# Fast Matrix Multiplication Additive Complexity: Format `(4, 5, 8)` (Rank 118) in 507 Additions over `Z`

## What

Explicit exact integer (ring Z) ternary straight-line program in claim/4x5x8_m118_cr507_fv250_cn1521_ZT_reduced.json (sha256 8457e021243c258cc047506d85372ef177054c9f8473261a27b211f1f3a419ec) for format (4, 5, 8) at best-known rank m = 118 with reduced addition count cr = 507 (U = 109, V = 162, W = 236, fv = 250, cn = 1521), symbolically verified across all 25600 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (513 in 4x5x8_m118_cr513_fv249_cn1521_ZT_reduced.json, margin -6), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/4x5x8.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+1521).

In this package, the straight-line program file is stored at `object/4x5x8_m118_cr507_fv250_cn1521_ZT_reduced.json` (identical bytes, SHA-256 `8457e021243c258cc047506d85372ef177054c9f8473261a27b211f1f3a419ec`, 65,296 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-8457e021/`), run:

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
| Perminov `addition_reduced_ZT` | `4x5x8_m118` | `118` | `513` (`4x5x8_m118_cr513_fv249_cn1521_ZT_reduced.json`) | **`507`** | **`-6`** | `https://api.github.com/repos/dronperminov/FastMatrixMultiplication/contents/schemes/results/addition_reduced_ZT` | `2026-10-14T03:50:16Z` |
| Perminov `reduced_known.json` | `4x5x8-118` | `118` | `none` | **`507`** | — | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json` | `2026-10-14T03:50:15Z` |
| Sedoglavic `fmm_sota.json` | `[4, 5, 8]` | `118` | — (rank `118` verified) | **`507`** | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T03:50:16Z` |
| Lille per-format catalogue | `4x5x8` | `118` | none | **`507`** | — | `https://fmm.univ-lille.fr/4x5x8.html` | `2026-10-14T03:50:20Z` |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `4,5,8` | `118` | `+1521` (naive) | **`507`** | — | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T03:50:17Z` |

## Not claimed

- This result reduces the number of straight-line program additions/subtractions (`cr = 507` vs `513`) over $\mathbb{Z}$ at the existing best-known bilinear rank `m = 118`; it does not lower the multiplicative rank `m`.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone symbolic checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* and *ternary_addition_reducer* (`https://github.com/dronperminov/FastMatrixMultiplication`, `https://github.com/dronperminov/ternary_addition_reducer`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our straight-line program builds directly on Perminov's ternary scheme for `4x5x8` (`m = 118`).
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **solven-eu**, *matmulcatalog* (`https://github.com/solven-eu/matmulcatalog`).
- Contributor credit: `anonymous-c6d1e0ab`.
