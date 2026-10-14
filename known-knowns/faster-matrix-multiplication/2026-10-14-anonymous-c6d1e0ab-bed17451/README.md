# Fast Matrix Multiplication `Z` Ring Upgrade: Format `(9, 13, 14)` at Rank 1039 over `Z`

## What

Explicit exact Z bilinear matrix-multiplication scheme in claim/9x13x14_m1039_Z.json (sha256 bed17451925a1e9a484a2848faae3aca36011203fbd9e3277c73d673a8a57daa, 907758 bytes, coefficients in [-2, -1, 0, 1, 2]) for format (9, 13, 14) with rank r = 1039, verified in exact integer arithmetic across all 2683044 Brent equations over Z and strictly beating the live Z rank (1050, saving 11) in dronperminov/FastMatrixMultiplication README.md (ZT = 1050, Z = 1050, Q = 1024) and MerlijnW70/fmm-schemes while remaining at or above the overall best rank (1024 in fmm_sota.json and Q column).

In this package, the scheme file is stored at `object/9x13x14_m1039_Z.json` (identical bytes, SHA-256 `bed17451925a1e9a484a2848faae3aca36011203fbd9e3277c73d673a8a57daa`, 907,758 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-bed17451/`), run:

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
| Perminov `README.md` (`ZT / Z / Q`) | `9x13x14` | `Z` | `1050` (`ZT=1050, Z=1050, Q=1024`) | `1024` | **`1039`** | **`-11`** | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md` | `2026-10-14T06:14:29Z` |
| Perminov `schemes/status.json` | `9x13x14` | `Z` | `1050` | `1024` | **`1039`** | **`-11`** | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/status.json` | `2026-10-14T06:14:30Z` |
| Sedoglavic `fmm_sota.json` | `[9, 13, 14]` | overall best | — | `1024` | **`1039`** (`>= 1024`) | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T06:14:31Z` |
| `MerlijnW70/fmm-schemes` `SHA256SUMS` | `9x13x14` | `ZT` | none | — | **`1039`** | — | `https://raw.githubusercontent.com/MerlijnW70/fmm-schemes/main/SHA256SUMS` | `2026-10-14T06:14:31Z` |
| Lille per-format catalogue | `9x13x14` | `Q` | — | `1024` | **`1039`** | — | `https://fmm.univ-lille.fr/9x13x14.html` | `2026-10-14T06:14:35Z` |

## Not claimed

- This result is a coefficient-ring upgrade (`Z` rank `1039` strictly below live `Z` rank `1050`, while `1039 >= 1024` so it does not beat the overall rational/complex best rank `1024`).
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone integer Brent equation checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* (`https://github.com/dronperminov/FastMatrixMultiplication`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our scheme is derived from Perminov's rational and ternary schemes.
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **MerlijnW70**, *fmm-schemes* (`https://github.com/MerlijnW70/fmm-schemes`).
- Contributor credit: `anonymous-c6d1e0ab`.
