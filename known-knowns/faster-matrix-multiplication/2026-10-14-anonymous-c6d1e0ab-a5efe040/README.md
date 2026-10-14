# Fast Matrix Multiplication `ZT` Ring Upgrade: Format `(9, 10, 14)` at Rank 816 over `Z`

## What

Explicit exact ZT bilinear matrix-multiplication scheme in claim/9x10x14_m816_ZT.json (sha256 a5efe04017632a0da87598ba3b2509ca66bb6fea965bb71a2faebb2aef582ab1, 594899 bytes, coefficients in [-1, 0, 1]) for format (9, 10, 14) with rank r = 816, verified in exact integer arithmetic across all 1587600 Brent equations over Z and strictly beating the live ZT rank (820, saving 4) in dronperminov/FastMatrixMultiplication README.md (ZT = 820, Z = 820, Q = 808) and MerlijnW70/fmm-schemes while remaining at or above the overall best rank (808 in fmm_sota.json and Q column).

In this package, the scheme file is stored at `object/9x10x14_m816_ZT.json` (identical bytes, SHA-256 `a5efe04017632a0da87598ba3b2509ca66bb6fea965bb71a2faebb2aef582ab1`, 594,899 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-a5efe040/`), run:

```sh
sh verify-it-yourself/run_checks.sh
```

- **Requirements**: `python3` (3.8+, standard library only).
- **Rough laptop time**: 1-3 seconds.
- **Expected last line**: `ALL CHECKS PASS`

## Compared to

All criterion sources were fetched live on `2026-10-14` (`06:14:29Z`-`06:14:44Z`, one honest GET per source, no retries; see `the-record-we-beat/README.md` and `the-record-we-beat/sources_2026-10-14T06-14-29Z.json`):

| Source | Cell | Coefficient Class | Listed `ZT` Rank | Live `Q` / SOTA Rank | Our `ZT` Rank | Margin vs `ZT` | URL | UTC Fetch Time |
|---|---|---|---|---|---|---|---|---|
| Perminov `README.md` (`ZT / Z / Q`) | `9x10x14` | `ZT` | `820` (`ZT=820, Z=820, Q=808`) | `808` | **`816`** | **`-4`** | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md` | `2026-10-14T06:14:29Z` |
| Perminov `schemes/status.json` | `9x10x14` | `ZT` | `820` | `808` | **`816`** | **`-4`** | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/status.json` | `2026-10-14T06:14:30Z` |
| Sedoglavic `fmm_sota.json` | `[9, 10, 14]` | overall best | — | `808` | **`816`** (`>= 808`) | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T06:14:31Z` |
| `MerlijnW70/fmm-schemes` `SHA256SUMS` | `9x10x14` | `ZT` | none | — | **`816`** | — | `https://raw.githubusercontent.com/MerlijnW70/fmm-schemes/main/SHA256SUMS` | `2026-10-14T06:14:31Z` |
| Lille per-format catalogue | `9x10x14` | `Q` | — | `808` | **`816`** | — | `https://fmm.univ-lille.fr/9x10x14.html` | `2026-10-14T06:14:35Z` |

## Not claimed

- This result is a coefficient-ring upgrade (`ZT` rank `816` strictly below live `ZT` rank `820`, while `816 >= 808` so it does not beat the overall rational/complex best rank `808`).
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone integer Brent equation checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* (`https://github.com/dronperminov/FastMatrixMultiplication`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our scheme is derived from Perminov's rational and ternary schemes.
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **MerlijnW70**, *fmm-schemes* (`https://github.com/MerlijnW70/fmm-schemes`).
- Contributor credit: `anonymous-c6d1e0ab`.
