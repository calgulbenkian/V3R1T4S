# Novelty Skeptic Report (`fmm-catalogue-small-format-rank`)

context: subagent
panel_role: novelty
target_id: fmm-catalogue-small-format-rank
format: 13x15x15
claimed_rank: 1763
claimed_ring: Q

## 1. Live Criterion Source Fetches (Single Honest GET, No Retries)

Each criterion source and the repository open pull-requests endpoint was fetched once live via `curl -sS -A "V3R1T4S-novelty-panel/1.0"`:

| Source | URL | UTC Fetch Time | HTTP Status | SHA-256 of Fetched Payload | Listed Rank for `13x15x15` |
|---|---|---|---|---|---|
| Sedoglavic `fmm_sota.json` | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T01:19:25Z` | `200` | `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1` | `1776` (`exponent: 2.812457`, `createdAt: 2026-10-09T11:45:48`) |
| Lille per-format page | `https://fmm.univ-lille.fr/13x15x15.html` | `2026-10-14T01:19:25Z` | `200` | `ce3fdb838b44413ff5b4b6d7a94ae09b6581254148141ddae788c7aa2cd68ee7` | `1797` (attributed to A. I. Perminov, Feb 2026; no lower-rank construction derivation listed) |
| Perminov `README.md` (`ZT / Z / Q`) | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md` | `2026-10-14T01:19:29Z` | `200` | `7b0761ecc0fa1988cb2ef0efeca503af974eeb6ade76d30629308ebba7e78341` | `1797 (?) / 1797 (1803) / 1776 (1803)` (minimum `1776` over `Q`) |
| `MerlijnW70/fmm-schemes` (`SHA256SUMS`) | `https://raw.githubusercontent.com/MerlijnW70/fmm-schemes/main/SHA256SUMS` | `2026-10-14T01:19:29Z` | `200` | `de848328881cf69cbe2a8d8309e04d94826cf1431b5b39e81db63f95af58a3fd` | none (`32` entries total; `13x15x15` absent) |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T01:19:30Z` | `200` | `c2a9bd929b477acb44d4f92aa8055a0c26eab3c33121c0734be650c5c86254b7` | `1797` (`F2`) / `1797` (`R/Q/Z`) |
| V3R1T4S Open Pull Requests | `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` | `2026-10-14T01:19:31Z` | `200` | `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945` | `[]` (`0` open PRs) |

### Exact Quoted Records from Primary Tables
- **`fmm_sota.json`**:
  `{"format": [13, 15, 15], "rank": 1776, "exponent": 2.812457}`
- **`13x15x15.html`**:
  Lists `13x15x15:1797` taken from `Andrew I. Perminov. FastMatrixMultiplication, GitHub, February 2026`. No composition, padding, or block-splitting construction with rank below `1797` is listed on the page.
- **Perminov `README.md`**:
  - Line 287: ``| `13x15x15` |  1803 (`Z`)   |   [1776](schemes/results/Q/13x15x15_m1776_Q.json) (`Q`)    |   2.812456688   |``
  - Line 1434: ``| `13x15x15` |  1797 (?)   | 1797 (1803)  | 1776 (1803)  |   2.812456688   |``
- **`MerlijnW70/fmm-schemes/main/SHA256SUMS`**:
  Contains 32 scheme files (`13x13x15_m1591_ZT.json`, `2x13x15_m304_ZT.json`, `7x11x15_m769_ZT.json`, etc.), none for format `13x15x15`.
- **`solven-eu/matmulcatalog` `COVERAGE.md`**:
  Line 621 lists `1797` (`Dronperminov-ZT [Z to F2]`) for `F2` and `1797` (`Dronperminov-ZT`) for `R/Q/Z`.

## 2. Repository Trophy Case & Open Pull Requests Check

- **Repository `TROPHY_CASE.md`**: Contains 53 rows total, including 5 fast matrix multiplication claims (rows 44 to 48):
  - Row 44: `(14, 15, 15)` rank `1842` over `Q`
  - Row 45: `(13, 14, 14)` rank `1558` over `Q`
  - Row 46: `(15, 16, 16)` rank `2180` over `Q`
  - Row 47: `(14, 14, 15)` rank `1716` over `Q`
  - Row 48: `(13, 14, 15)` rank `1677` over `Q`
  Format `(13, 15, 15)` is **not** present in `TROPHY_CASE.md`.
- **Open Pull Requests**: `0` open pull requests (`[]`).

## 3. Literature Search (2024–2026)

Searching the last 24 months of fast matrix multiplication literature:
1. **Perminov (2025–2026, arXiv:2603.02398, arXiv:2606.02480, and `FastMatrixMultiplication` updates through Oct 2026)**: Established the current state-of-the-art public bound of `1776` over `Q` (and `1797` over `ZT` and `Z`) for `(13, 15, 15)`.
2. **Khoruzhii, Serafin, Gelß, Pokutta (LITA, Oct 2026, arXiv:2610.03558)** and **Khoruzhii, Gelß, Pokutta (2025/2026)**: Reported improved square matrix multiplication schemes (including `15x15x15` at rank `1933` over `Q`), without publishing a `(13, 15, 15)` scheme. Moreover, naive row-peeling of `(14, 15, 15)` rank `1842` leaves at best `1842 - 78 = 1764`, whereas `claim/13x15x15_r1763_Q.json` achieves rank `1763` via an additional rank-1 nullspace absorption.
3. **Kauers & Wood (Oct 2025, arXiv:2510.19787)**, **Kauers & Moosbauer (arXiv:2502.04514)**, **Novikov et al. / AlphaEvolve (May 2025)**: Focus on smaller formats or do not report any `(13, 15, 15)` bound below `1776`.

## 4. Verdict

- **Claimed artifact**: `claim/13x15x15_r1763_Q.json` (SHA-256 `710c8ff6593f7c6e578a9ae83b4d7083ed5381db72fd734e614a3108d7c87465`, documented in `claim/CLAIM.md`, `claim/target.md`, and `claim/table_record.md`)
- **Claimed rank**: `1763` over `Q`
- **Best known rank across all criterion sources, literature, open PRs, and `TROPHY_CASE.md`**: `1776`
- **Strict improvement margin**: `1763 - 1776 = -13` multiplications (`1763` is strictly less than `1776`).

pass: true
