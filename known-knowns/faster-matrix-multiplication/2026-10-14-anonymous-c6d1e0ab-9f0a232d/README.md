# Fast Matrix Multiplication `Z` Ring Upgrade: Format `(7, 8, 15)` at Rank 570 over `Z`

## What

Explicit exact Z bilinear matrix-multiplication scheme in claim/7x8x15_m570_Z.json (sha256 9f0a232de00ce5220d75097b9af6986f97d81932fa3e3718e1291d426f4caede, 330024 bytes, coefficients in [-2, -1, 0, 1, 2]) for format (7, 8, 15) with rank r = 570, verified in exact integer arithmetic across all 705600 Brent equations over Z and strictly beating the live Z rank (571, saving 1) in dronperminov/FastMatrixMultiplication README.md (ZT = 571, Z = 571, Q = 557) and MerlijnW70/fmm-schemes while remaining at or above the overall best rank (557 in fmm_sota.json and Q column).

In this package, the scheme file is stored at `object/7x8x15_m570_Z.json` (identical bytes, SHA-256 `9f0a232de00ce5220d75097b9af6986f97d81932fa3e3718e1291d426f4caede`, 330,024 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-9f0a232d/`), run:

```sh
sh verify-it-yourself/run_checks.sh
```

- **Requirements**: `python3` (3.8+, standard library only).
- **Rough laptop time**: 1-3 seconds.
- **Expected last line**: `ALL CHECKS PASS`

## Compared to

All criterion sources were fetched live on `2026-10-14` (`06:14:29Z`-`06:14:44Z`, one honest GET per source, no retries; see `the-record-we-beat/README.md` and `the-record-we-beat/sources_2026-10-14T06-14-29Z.json`):

| Source | Cell | Coefficient Class | Listed `Z` Rank | Live `Q` / SOTA Rank | Our `Z` Rank | Margin vs `Z` | URL | UTC Fetch Time |
|---|---|---|---|---|---|---|---|---|
| Perminov `README.md` (`ZT / Z / Q`) | `7x8x15` | `Z` | `571` (`ZT=571, Z=571, Q=557`) | `557` | **`570`** | **`-1`** | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md` | `2026-10-14T06:14:29Z` |
| Perminov `schemes/status.json` | `7x8x15` | `Z` | `571` | `557` | **`570`** | **`-1`** | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/status.json` | `2026-10-14T06:14:30Z` |
| Sedoglavic `fmm_sota.json` | `[7, 8, 15]` | overall best | — | `557` | **`570`** (`>= 557`) | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T06:14:31Z` |
| `MerlijnW70/fmm-schemes` `SHA256SUMS` | `7x8x15` | `ZT` | none | — | **`570`** | — | `https://raw.githubusercontent.com/MerlijnW70/fmm-schemes/main/SHA256SUMS` | `2026-10-14T06:14:31Z` |
| Lille per-format catalogue | `7x8x15` | `Q` | — | `557` | **`570`** | — | `https://fmm.univ-lille.fr/7x8x15.html` | `2026-10-14T06:14:35Z` |

## Not claimed

- This result is a coefficient-ring upgrade (`Z` rank `570` strictly below live `Z` rank `571`, while `570 >= 557` so it does not beat the overall rational/complex best rank `557`).
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone integer Brent equation checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* (`https://github.com/dronperminov/FastMatrixMultiplication`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our scheme is derived from Perminov's rational and ternary schemes.
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **MerlijnW70**, *fmm-schemes* (`https://github.com/MerlijnW70/fmm-schemes`).
- Contributor credit: `anonymous-c6d1e0ab`.
