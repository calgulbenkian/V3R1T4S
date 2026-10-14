# Fast Matrix Multiplication Catalogue Rank Record: Format `(16, 18, 18)` at Rank 2900 over `Q`

## What

Partial Win p1 on fmm-catalogue-small-format-rank is verified by the explicit exact rational (ring Q) bilinear scheme in claim/16x18x18_r2900_Q.json (sha256 0975cd66f4a942c0d5fd289c59c7d5a0703e86dee33b40911924de746c679de3, 241556 bytes) for format (16, 18, 18) with max dimension 18 in 17..32 and rank r = 2900, deterministically verified across all 26873856 Brent equations over Q and strictly beating fmm_sota.json (2916, margin -16) and fmm.univ-lille.fr/16x18x18.html (2916, margin -16).

In this package, the bilinear scheme is stored at `object/16x18x18_r2900_Q.json` (identical bytes, SHA-256 `0975cd66f4a942c0d5fd289c59c7d5a0703e86dee33b40911924de746c679de3`, 241,556 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-0975cd66/`), run:

```sh
sh verify-it-yourself/run_checks.sh
```

- **Requirements**: `python3` (3.8+, standard library only).
- **Rough laptop time**: 2-6 seconds.
- **Expected last line**: `ALL CHECKS PASS`

## Compared to

All criterion sources were fetched live on `2026-10-14` (`06:19:43Z`-`06:20:15Z`, one honest GET per source, no retries; see `the-record-we-beat/README.md` and `the-record-we-beat/sources_2026-10-14T06-19-43Z.json`):

| Source | Cell | Listed Rank | Our Rank over `Q` | Margin | URL | UTC Fetch Time |
|---|---|---|---|---|---|---|
| Sedoglavic `fmm_sota.json` | `[16, 18, 18]` | `2916` | **`2900`** | **`-16`** | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T06:19:43Z` |
| Lille per-format catalogue | `16x18x18` | `2916` | **`2900`** | **`-16`** | `https://fmm.univ-lille.fr/16x18x18.html` | `2026-10-14T06:19:50Z` |
| Perminov `README.md` (`ZT / Z / Q`) | `16x18x18` | `unlisted (max<=16)` | **`2900`** | — | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md` | `2026-10-14T06:19:43Z` |
| `MerlijnW70/fmm-schemes` `SHA256SUMS` | `16x18x18` | none | **`2900`** | — | `https://raw.githubusercontent.com/MerlijnW70/fmm-schemes/main/SHA256SUMS` | `2026-10-14T06:19:44Z` |
| `TROPHY_CASE.md` | `16x18x18` | `none` | **`2900`** | **`-16`** | `TROPHY_CASE.md` | `2026-10-14T06:19:44Z` |

## Not claimed

- Scope: Partial Win `p1` (`17 <= max(n, m, p) <= 32`) for format `(16, 18, 18)` over $\mathbb{Q}$ at rank `2900`.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exact Brent equation checker shipped here; not peer reviewed.

## Credits

- **K. Khoruzhii, P. Gelß, S. Pokutta**, *LITA: Learning Iterative Tensor Algorithms for Fast Matrix Multiplication* (`https://github.com/khoruzhii/lita`, arXiv:2602.12686, Feb 2026): our hyperplane peeling + Rado-Edmonds matroid absorption cascade starts from the `17x17x17` (`r=2723`) and `18x18x18` (`r=3031`) anchors.
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **A. I. Perminov**, *FastMatrixMultiplication* (`https://github.com/dronperminov/FastMatrixMultiplication`).
- Contributor credit: `anonymous-c6d1e0ab`.
