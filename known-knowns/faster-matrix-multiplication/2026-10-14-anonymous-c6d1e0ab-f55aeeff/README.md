# Fast Matrix Multiplication: Format `(13, 14, 14)` in Rank 1541 over `Q`

## What

Explicit exact rational (ring Q) bilinear matrix-multiplication scheme in claim/13x14x14_r1541_Q.json (sha256 f55aeeff8aa61d1b246890045a1122b4564a8a15e179adc4a2e5b8d65943081d) for format (13, 14, 14) with rank r = 1541, verified across all 6492304 Brent equations over Q and strictly beating fmm_sota.json (1582), fmm.univ-lille.fr (1614), Perminov FastMatrixMultiplication min over ZT/Z/Q (1582), MerlijnW70/fmm-schemes (unlisted), matmulcatalog F2/RQZ (1614), and TROPHY_CASE.md (1558).

In this package, the scheme file is stored at `object/13x14x14_r1541_Q.json` (identical bytes, SHA-256 `f55aeeff8aa61d1b246890045a1122b4564a8a15e179adc4a2e5b8d65943081d`, 915,633 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-f55aeeff/`), run:

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
| Sedoglavic `fmm_sota.json` | `[13, 14, 14]` | `1582` | **`1541`** | **`-41`** | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T02:33:58Z` |
| Lille per-format catalogue | `13x14x14` | `1614` | **`1541`** | **`-73`** | `https://fmm.univ-lille.fr/13x14x14.html` | `2026-10-14T02:34:05Z` |
| Perminov `README.md` (`ZT / Z / Q`) | `13x14x14` | `1614 / 1614 / 1582` (min `1582`) | **`1541`** | **`-41`** | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md` | `2026-10-14T02:34:09Z` |
| `MerlijnW70/fmm-schemes` | `13x14x14` | none (`-`) | **`1541`** | - | `https://raw.githubusercontent.com/MerlijnW70/fmm-schemes/main/SHA256SUMS` | `2026-10-14T02:34:09Z` |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `13,14,14` | `1614` (`F2`) / `1614` (`R/Q/Z`) | **`1541`** | **`-73`** | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T02:34:09Z` |

## Not claimed

- This bound is over the rational numbers $\mathbb{Q}$ (`ring: "Q"`), with denominators dividing $L = 54,400 = 2^7 \cdot 5^2 \cdot 17$. Nothing is claimed for the ternary (`ZT`), integer (`Z`), or characteristic-2 (`GF(2)`) ranks of format `(13, 14, 14)`.
- This is a finite-format rank bound for `(13, 14, 14)` and does not improve the asymptotic exponent $\omega$ of matrix multiplication.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone checker shipped here; not peer reviewed.

## Credits

- **K. Khoruzhii, L. Serafin, P. Gelß, and S. Pokutta**, *Local Improvements to Trilinear Aggregation* (`https://github.com/khoruzhii/lita`, 2026): our `(13, 14, 14)` rank `1541` scheme descends from LITA's `(15, 15, 15)` rank `1977` square scheme via the V3R1T4S `(14, 15, 15)` rank `1842` scheme (`known-knowns/faster-matrix-multiplication/schemes/14x15x15_r1842_Q.json`) and our `(13, 14, 15)` rank `1646` scheme. Please cite LITA when using this derived scheme.
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **A. I. Perminov**, *FastMatrixMultiplication* (`https://github.com/dronperminov/FastMatrixMultiplication`, arXiv:2606.02480).
- **MerlijnW70**, *fmm-schemes* (`https://github.com/MerlijnW70/fmm-schemes`).
- **solven-eu**, *matmulcatalog* (`https://github.com/solven-eu/matmulcatalog`).
- **M. Kauers and J. Wood**, arXiv:2510.19787 (slice restrictions), and **R. P. Brent**, STAN-CS-70-157 (1970) (the Brent equations).
- Contributor credit: `anonymous-c6d1e0ab`.
