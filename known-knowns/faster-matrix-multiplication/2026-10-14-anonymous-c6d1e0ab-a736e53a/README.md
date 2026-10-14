# Fast Matrix Multiplication `Z` Ring Upgrade: Format `(4, 14, 15)` at Rank 569 over `Z`

## What

Explicit exact Z bilinear matrix-multiplication scheme in claim/4x14x15_m569_Z.json (sha256 a736e53a74f68425c0211816e0972faf8c027d4845885509b530644e9f64c52b, 379650 bytes, coefficients in [-2, -1, 0, 1, 2]) for format (4, 14, 15) with rank r = 569, verified in exact integer arithmetic across all 705600 Brent equations over Z and strictly beating the live Z rank (572, saving 3) in dronperminov/FastMatrixMultiplication README.md (ZT = 572, Z = 572, Q = 557) and MerlijnW70/fmm-schemes while remaining at or above the overall best rank (557 in fmm_sota.json and Q column).

In this package, the scheme file is stored at `object/4x14x15_m569_Z.json` (identical bytes, SHA-256 `a736e53a74f68425c0211816e0972faf8c027d4845885509b530644e9f64c52b`, 379,650 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-a736e53a/`), run:

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
| Perminov `README.md` (`ZT / Z / Q`) | `4x14x15` | `Z` | `572` (`ZT=572, Z=572, Q=557`) | `557` | **`569`** | **`-3`** | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md` | `2026-10-14T06:14:29Z` |
| Perminov `schemes/status.json` | `4x14x15` | `Z` | `572` | `557` | **`569`** | **`-3`** | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/status.json` | `2026-10-14T06:14:30Z` |
| Sedoglavic `fmm_sota.json` | `[4, 14, 15]` | overall best | — | `557` | **`569`** (`>= 557`) | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T06:14:31Z` |
| `MerlijnW70/fmm-schemes` `SHA256SUMS` | `4x14x15` | `ZT` | none | — | **`569`** | — | `https://raw.githubusercontent.com/MerlijnW70/fmm-schemes/main/SHA256SUMS` | `2026-10-14T06:14:31Z` |
| Lille per-format catalogue | `4x14x15` | `Q` | — | `557` | **`569`** | — | `https://fmm.univ-lille.fr/4x14x15.html` | `2026-10-14T06:14:35Z` |

## Not claimed

- This result is a coefficient-ring upgrade (`Z` rank `569` strictly below live `Z` rank `572`, while `569 >= 557` so it does not beat the overall rational/complex best rank `557`).
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone integer Brent equation checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* (`https://github.com/dronperminov/FastMatrixMultiplication`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our scheme is derived from Perminov's rational and ternary schemes.
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **MerlijnW70**, *fmm-schemes* (`https://github.com/MerlijnW70/fmm-schemes`).
- Contributor credit: `anonymous-c6d1e0ab`.
