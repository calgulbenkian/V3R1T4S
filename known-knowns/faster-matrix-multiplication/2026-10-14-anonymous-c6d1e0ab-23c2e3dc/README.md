# Fast Matrix Multiplication Catalogue Rank Record: Format `(15, 15, 16)` at Rank 2129 over `Q`

## What

Full Win on fmm-catalogue-small-format-rank is verified by the explicit exact rational (ring Q) bilinear scheme in claim/15x15x16_r2129_Q.json (sha256 23c2e3dca666f4b9e60a3f05f27534f98baba50c924b973bdc59a703f723450e, 717505 bytes) for format (15, 15, 16) with rank r = 2129, deterministically verified across all 12960000 Brent equations over Q and strictly beating fmm_sota.json (2132, margin -3), fmm.univ-lille.fr/15x15x16.html (2132, margin -3), Perminov FastMatrixMultiplication min over ZT/Z/Q (2132), MerlijnW70/fmm-schemes (unlisted), and TROPHY_CASE.md (unlisted).

In this package, the bilinear scheme is stored at `object/15x15x16_r2129_Q.json` (identical bytes, SHA-256 `23c2e3dca666f4b9e60a3f05f27534f98baba50c924b973bdc59a703f723450e`, 717,505 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-23c2e3dc/`), run:

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
| Sedoglavic `fmm_sota.json` | `[15, 15, 16]` | `2132` | **`2129`** | **`-3`** | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T06:19:43Z` |
| Lille per-format catalogue | `15x15x16` | `2132` | **`2129`** | **`-3`** | `https://fmm.univ-lille.fr/15x15x16.html` | `2026-10-14T06:19:50Z` |
| Perminov `README.md` (`ZT / Z / Q`) | `15x15x16` | `2132 / 2132 / 2132` | **`2129`** | — | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md` | `2026-10-14T06:19:43Z` |
| `MerlijnW70/fmm-schemes` `SHA256SUMS` | `15x15x16` | none | **`2129`** | — | `https://raw.githubusercontent.com/MerlijnW70/fmm-schemes/main/SHA256SUMS` | `2026-10-14T06:19:44Z` |
| `TROPHY_CASE.md` | `15x15x16` | `none` | **`2129`** | **`-3`** | `TROPHY_CASE.md` | `2026-10-14T06:19:44Z` |

## Not claimed

- Scope: Full Win (`max(n, m, p) <= 16`) for format `(15, 15, 16)` over $\mathbb{Q}$ at rank `2129`.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exact Brent equation checker shipped here; not peer reviewed.

## Credits

- **K. Khoruzhii, P. Gelß, S. Pokutta**, *LITA: Learning Iterative Tensor Algorithms for Fast Matrix Multiplication* (`https://github.com/khoruzhii/lita`, arXiv:2602.12686, Feb 2026): our hyperplane peeling + Rado-Edmonds matroid absorption cascade starts from the `17x17x17` (`r=2723`) and `18x18x18` (`r=3031`) anchors.
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **A. I. Perminov**, *FastMatrixMultiplication* (`https://github.com/dronperminov/FastMatrixMultiplication`).
- Contributor credit: `anonymous-c6d1e0ab`.
