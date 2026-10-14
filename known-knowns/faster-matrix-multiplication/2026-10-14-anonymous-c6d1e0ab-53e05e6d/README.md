# Fast Matrix Multiplication Catalogue Rank Record: Format `(15, 16, 17)` at Rank 2313 over `Q`

## What

Partial Win p1 on fmm-catalogue-small-format-rank is verified by the explicit exact rational (ring Q) bilinear scheme in claim/15x16x17_r2313_Q.json (sha256 53e05e6d257401e1089d7ace8d42b7cbde78f8992e90223791fea6c1df50da57, 751346 bytes) for format (15, 16, 17) with max dimension 17 in 17..32 and rank r = 2313, deterministically verified across all 16646400 Brent equations over Q and strictly beating fmm_sota.json (2448, margin -135) and fmm.univ-lille.fr/15x16x17.html (2448, margin -135).

In this package, the bilinear scheme is stored at `object/15x16x17_r2313_Q.json` (identical bytes, SHA-256 `53e05e6d257401e1089d7ace8d42b7cbde78f8992e90223791fea6c1df50da57`, 751,346 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-53e05e6d/`), run:

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
| Sedoglavic `fmm_sota.json` | `[15, 16, 17]` | `2448` | **`2313`** | **`-135`** | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T06:19:43Z` |
| Lille per-format catalogue | `15x16x17` | `2448` | **`2313`** | **`-135`** | `https://fmm.univ-lille.fr/15x16x17.html` | `2026-10-14T06:19:50Z` |
| Perminov `README.md` (`ZT / Z / Q`) | `15x16x17` | `unlisted (max<=16)` | **`2313`** | — | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md` | `2026-10-14T06:19:43Z` |
| `MerlijnW70/fmm-schemes` `SHA256SUMS` | `15x16x17` | none | **`2313`** | — | `https://raw.githubusercontent.com/MerlijnW70/fmm-schemes/main/SHA256SUMS` | `2026-10-14T06:19:44Z` |
| `TROPHY_CASE.md` | `15x16x17` | `none` | **`2313`** | **`-135`** | `TROPHY_CASE.md` | `2026-10-14T06:19:44Z` |

## Not claimed

- Scope: Partial Win `p1` (`17 <= max(n, m, p) <= 32`) for format `(15, 16, 17)` over $\mathbb{Q}$ at rank `2313`.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exact Brent equation checker shipped here; not peer reviewed.

## Credits

- **K. Khoruzhii, P. Gelß, S. Pokutta**, *LITA: Learning Iterative Tensor Algorithms for Fast Matrix Multiplication* (`https://github.com/khoruzhii/lita`, arXiv:2602.12686, Feb 2026): our hyperplane peeling + Rado-Edmonds matroid absorption cascade starts from the `17x17x17` (`r=2723`) and `18x18x18` (`r=3031`) anchors.
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **A. I. Perminov**, *FastMatrixMultiplication* (`https://github.com/dronperminov/FastMatrixMultiplication`).
- Contributor credit: `anonymous-c6d1e0ab`.
