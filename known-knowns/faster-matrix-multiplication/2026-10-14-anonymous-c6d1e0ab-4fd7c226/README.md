# Fast Matrix Multiplication: Format `(14, 16, 16)` in Rank 2119 over `Q`

## What

Explicit exact rational (ring Q) bilinear matrix-multiplication scheme in claim/14x16x16_r2119_Q.json (sha256 4fd7c2264911e65fcc6cf7074e6100202786a5de6c01b85b9ac6572fdf31ba56) for format (14, 16, 16) with rank r = 2119, verified across all 12845056 Brent equations over Q and strictly beating fmm_sota.json (2128), fmm.univ-lille.fr (2128), Perminov FastMatrixMultiplication min over ZT/Z/Q (2128), MerlijnW70/fmm-schemes (unlisted), matmulcatalog F2/RQZ (2180), and TROPHY_CASE.md (unlisted).

In this package, the scheme file is stored at `object/14x16x16_r2119_Q.json` (identical bytes, SHA-256 `4fd7c2264911e65fcc6cf7074e6100202786a5de6c01b85b9ac6572fdf31ba56`, 905,718 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-4fd7c226/`), run:

```sh
sh verify-it-yourself/run_checks.sh
```

- **Requirements**: `python3` (3.8+, standard library only) and a C compiler (`cc` / `clang` / `gcc`).
- **Rough laptop time**: ~2-4 seconds.
- **Expected last line**: `ALL CHECKS PASS`

## Compared to

All criterion sources were fetched live on `2026-10-14` (`02:33:58Z`-`02:34:10Z`, one honest GET per source, no retries; see `the-record-we-beat/README.md` and `the-record-we-beat/sources_2026-10-14T02-33-58Z.json`):

| Source | Cell | Listed Rank | Our Rank (`Q`) | Margin | URL | UTC Fetch Time |
|---|---|---|---|---|---|---|
| Sedoglavic `fmm_sota.json` | `[14, 16, 16]` | `2128` | **`2119`** | **`-9`** | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T02:33:58Z` |
| Lille per-format catalogue | `14x16x16` | `2128` | **`2119`** | **`-9`** | `https://fmm.univ-lille.fr/14x16x16.html` | `2026-10-14T02:34:05Z` |
| Perminov `README.md` (`ZT / Z / Q`) | `14x16x16` | `2170 / 2170 / 2128` (min `2128`) | **`2119`** | **`-9`** | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md` | `2026-10-14T02:34:09Z` |
| `MerlijnW70/fmm-schemes` | `14x16x16` | none (`-`) | **`2119`** | - | `https://raw.githubusercontent.com/MerlijnW70/fmm-schemes/main/SHA256SUMS` | `2026-10-14T02:34:09Z` |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `14,16,16` | `2170` (`F2`) / `2128` (`R/Q/Z`) | **`2119`** | **`-9`** | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T02:34:09Z` |

## Not claimed

- This bound is over the rational numbers $\mathbb{Q}$ (`ring: "Q"`), with denominators dividing $L = 29,030,400 = 2^{11} \cdot 3^4 \cdot 5^2 \cdot 7$. Nothing is claimed for the ternary (`ZT`), integer (`Z`), or characteristic-2 (`GF(2)`) ranks of format `(14, 16, 16)`.
- This is a finite-format rank bound for `(14, 16, 16)` and does not improve the asymptotic exponent $\omega$ of matrix multiplication.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone checker shipped here; not peer reviewed.

## Credits

- **K. Khoruzhii, L. Serafin, P. Gelß, and S. Pokutta**, *Local Improvements to Trilinear Aggregation* (`https://github.com/khoruzhii/lita`, 2026): our `(14, 16, 16)` rank `2119` scheme descends from LITA's `(16, 16, 16)` rank `2236` square scheme via the V3R1T4S `(15, 16, 16)` rank `2180` scheme (`known-knowns/faster-matrix-multiplication/schemes/15x16x16_r2180_Q.json`). Please cite LITA when using this derived scheme.
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **A. I. Perminov**, *FastMatrixMultiplication* (`https://github.com/dronperminov/FastMatrixMultiplication`, arXiv:2606.02480).
- **MerlijnW70**, *fmm-schemes* (`https://github.com/MerlijnW70/fmm-schemes`).
- **solven-eu**, *matmulcatalog* (`https://github.com/solven-eu/matmulcatalog`).
- **M. Kauers and J. Wood**, arXiv:2510.19787 (slice restrictions), and **R. P. Brent**, STAN-CS-70-157 (1970) (the Brent equations).
- Contributor credit: `anonymous-c6d1e0ab`.
