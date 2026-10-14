# The Record We Beat: Format `(13, 14, 14)` (`fmm-catalogue-small-format-rank`)

All four criterion sources (plus `solven-eu/matmulcatalog` and the repository open pull requests endpoint) were fetched live with a single honest GET (`curl -sS`) on `2026-10-14` (`02:33:58Z`-`02:34:10Z`) by the independent `NOVELTY` panelist.

| Source | URL | UTC Fetch Time | HTTP Status | SHA-256 of Fetched Page | Extracted Cell for `(13, 14, 14)` |
|---|---|---|---|---|---|
| Sedoglavic `fmm_sota.json` | `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` | `2026-10-14T02:33:58Z` | `200` | `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1` | `{"format": [13, 14, 14], "rank": 1582, "exponent": 2.796678}` (`createdAt: 2026-10-09T11:45:48`) |
| Lille per-format catalogue page | `https://fmm.univ-lille.fr/13x14x14.html` | `2026-10-14T02:34:05Z` | `200` | `f4f5d1067f4dea0882d6c15b04fa4399609c5cd695777824ce1a96c6d22330cd` | `13x14x14:1614` |
| Perminov `README.md` (`ZT / Z / Q`) | `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md` | `2026-10-14T02:34:09Z` | `200` | `7b0761ecc0fa1988cb2ef0efeca503af974eeb6ade76d30629308ebba7e78341` | `1614 (?) / 1614 (1614) / 1582 (1614)` (minimum `1582`) |
| `MerlijnW70/fmm-schemes` (`SHA256SUMS`) | `https://raw.githubusercontent.com/MerlijnW70/fmm-schemes/main/SHA256SUMS` | `2026-10-14T02:34:09Z` | `200` | `de848328881cf69cbe2a8d8309e04d94826cf1431b5b39e81db63f95af58a3fd` | none (`32` entries; `13x14x14` absent) |
| `solven-eu/matmulcatalog` `COVERAGE.md` | `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` | `2026-10-14T02:34:09Z` | `200` | `c2a9bd929b477acb44d4f92aa8055a0c26eab3c33121c0734be650c5c86254b7` | `1614` (`F2`) / `1614` (`R/Q/Z`) |
| V3R1T4S Open Pull Requests | `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` | `2026-10-14T02:34:10Z` | `200` | `3c174ff25f71500bcf1a11109c0a60d56ccf7e520025a454a8c43b8a56e0eb59` | `2` open PRs (`#1`, `#2`; none for `13x14x14`) |

- **Minimum across all 4 criterion sources**: `1582`
- **Our verified rank over `Q` (`object/13x14x14_r1541_Q.json`)**: `1541` (`margin = -41`).
