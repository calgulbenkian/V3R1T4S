# Fast Matrix Multiplication `ZT` Ring Upgrade: Format `(4, 13, 15)` at Rank 535 over `Z`

## What

Explicit exact ZT bilinear matrix-multiplication scheme in claim/4x13x15_m535_ZT.json (sha256 937d96a3adc5b64e84e86d8a0d9bc0b7e160f22f00f3ca4af7239abb76a281f2, 338479 bytes, coefficients in [-1, 0, 1]) for format (4, 13, 15) with rank r = 535, verified in exact integer arithmetic across all 608400 Brent equations over Z and strictly beating the live ZT rank (536, saving 1) in dronperminov/FastMatrixMultiplication README.md (ZT = 536, Z = 536, Q = 520) and MerlijnW70/fmm-schemes while remaining at or above the overall best rank (520 in fmm_sota.json and Q column).

In this package, the scheme file is stored at `object/4x13x15_m535_ZT.json` (identical bytes, SHA-256 `937d96a3adc5b64e84e86d8a0d9bc0b7e160f22f00f3ca4af7239abb76a281f2`, 338,479 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-937d96a3/`), run:

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
| Perminov `README.md` (`ZT / Z / Q`) | `4x13x15` | `ZT` | `536` (`ZT=536, Z=536, Q=520`) | `520` | **`535`** | **`-1`** | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md` | `2026-10-14T06:14:29Z` |
| Perminov `schemes/status.json` | `4x13x15` | `ZT` | `536` | `520` | **`535`** | **`-1`** | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/status.json` | `2026-10-14T06:14:30Z` |
| Sedoglavic `fmm_sota.json` | `[4, 13, 15]` | overall best | — | `520` | **`535`** (`>= 520`) | — | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T06:14:31Z` |
| `MerlijnW70/fmm-schemes` `SHA256SUMS` | `4x13x15` | `ZT` | none | — | **`535`** | — | `https://raw.githubusercontent.com/MerlijnW70/fmm-schemes/main/SHA256SUMS` | `2026-10-14T06:14:31Z` |
| Lille per-format catalogue | `4x13x15` | `Q` | — | `520` | **`535`** | — | `https://fmm.univ-lille.fr/4x13x15.html` | `2026-10-14T06:14:35Z` |

## Not claimed

- This result is a coefficient-ring upgrade (`ZT` rank `535` strictly below live `ZT` rank `536`, while `535 >= 520` so it does not beat the overall rational/complex best rank `520`).
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone integer Brent equation checker shipped here; not peer reviewed.

## Credits

- **A. I. Perminov**, *FastMatrixMultiplication* (`https://github.com/dronperminov/FastMatrixMultiplication`, arXiv:2512.13365, arXiv:2512.21980, arXiv:2606.02480): our scheme is derived from Perminov's rational and ternary schemes.
- **A. Sedoglavic**, *Catalogue of Fast Matrix Multiplication Algorithms* (`https://fmm.univ-lille.fr/` and `https://github.com/sedoglavic/fmm_digest`).
- **MerlijnW70**, *fmm-schemes* (`https://github.com/MerlijnW70/fmm-schemes`).
- Contributor credit: `anonymous-c6d1e0ab`.
