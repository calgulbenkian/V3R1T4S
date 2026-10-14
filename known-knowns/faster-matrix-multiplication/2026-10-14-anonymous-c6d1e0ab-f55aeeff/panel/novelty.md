# Novelty Panel Report — Format 13x14x14 Rank 1541 over Q

context: subagent
context: subagent (fable)
date_utc: 2026-10-14T02:34:35Z
target_id: fmm-catalogue-small-format-rank
claimed_object: claim/13x14x14_r1541_Q.json (SHA-256: f55aeeff8aa61d1b246890045a1122b4564a8a15e179adc4a2e5b8d65943081d)
claimed_bound: format (13, 14, 14) bilinear rank 1541 over Q

## 1. Honest Single-GET Live Fetch of Primary Scoreboards

Each primary scoreboard and repository status table was fetched once via live HTTP GET (`curl -sS -A "V3R1T4S-novelty-panel/1.0"`):

1. **Sedoglavic Lille JSON Digest (`fmm_sota.json`)**
   - URL: `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json`
   - Fetch Timestamp (UTC): `2026-10-14T02:33:58Z`
   - HTTP Status: `200` (343,798 bytes)
   - SHA-256: `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`
   - Snapshot Metadata: `createdAt: 2026-10-09T11:45:48`
   - Extracted Entry for `[13, 14, 14]`: `{"format": [13, 14, 14], "rank": 1582, "exponent": 2.817692}`
   - Listed Rank: **1582**

2. **Sedoglavic Lille Per-Format Page (`13x14x14.html`)**
   - URL: `https://fmm.univ-lille.fr/13x14x14.html`
   - Fetch Timestamp (UTC): `2026-10-14T02:34:03Z`
   - HTTP Status: `200` (19,336 bytes)
   - SHA-256: `f4f5d1067f4dea0882d6c15b04fa4399609c5cd695777824ce1a96c6d22330cd`
   - Extracted Header: `Description of fast matrix multiplication algorithm: 13x14x14:1614`
   - Listed Rank: **1614**

3. **Perminov `FastMatrixMultiplication` Status Table (`README.md`)**
   - URL: `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md`
   - Fetch Timestamp (UTC): `2026-10-14T02:34:09Z`
   - HTTP Status: `200` (112,671 bytes)
   - SHA-256: `7b0761ecc0fa1988cb2ef0efeca503af974eeb6ade76d30629308ebba7e78341`
   - Extracted Table Rows for `13x14x14`:
     - Summary row: `| 13x14x14 | 1625 (Z) | 1582 (Q) | 2.817691580 |`
     - Status row (ZT / Z / Q): `| 13x14x14 | 1614 (?) | 1614 (1625) | 1582 (1625) | 2.817691580 |`
   - Listed Ranks (ZT / Z / Q): **1614 / 1614 / 1582** (minimum: **1582**)

4. **MerlijnW70 `fmm-schemes` Repository (`SHA256SUMS`)**
   - URL: `https://raw.githubusercontent.com/MerlijnW70/fmm-schemes/main/SHA256SUMS`
   - Fetch Timestamp (UTC): `2026-10-14T02:34:09Z`
   - HTTP Status: `200` (3,044 bytes, 32 lines)
   - SHA-256: `de848328881cf69cbe2a8d8309e04d94826cf1431b5b39e81db63f95af58a3fd`
   - Extracted Entry for `13x14x14`: **none** (0 matching lines)

5. **Solven `matmulcatalog` Coverage Table (`COVERAGE.md`)**
   - URL: `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md`
   - Fetch Timestamp (UTC): `2026-10-14T02:34:09Z`
   - HTTP Status: `200` (94,842 bytes)
   - SHA-256: `c2a9bd929b477acb44d4f92aa8055a0c26eab3c33121c0734be650c5c86254b7`
   - Extracted Row for `(13,14,14)`: F2 = **1614** (`Dronperminov-ZT [Z to F2]`), R/Q/Z = **1614** (`Dronperminov-ZT`)

Minimum rank across all external scoreboards over any ring: **1582**.

## 2. Audit of `repo/TROPHY_CASE.md` and Open Pull Requests

- **`repo/TROPHY_CASE.md`**: Row 45 records format `(13, 14, 14)` at rank **1558** over Q (`schemes/13x14x14_r1558_Q.json`, obtained by restriction of LITA square `14x14x14`). Our claimed rank **1541** strictly beats `repo/TROPHY_CASE.md` row 45 (1541 vs 1558, margin -17 multiplications).
- **Open Pull Requests**: Fetched `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` at `2026-10-14T02:34:10Z` (HTTP `200`, 38,340 bytes, SHA-256 `3c174ff25f71500bcf1a11109c0a60d56ccf7e520025a454a8c43b8a56e0eb59`). Exactly 2 open PRs exist:
  - PR #1: `fix: reject malformed null control counts`
  - PR #2: `[claim] fmm-catalogue-small-format-rank: format (13, 15, 15) rank 1763 over Q (beats 1776 bar)`
  Neither open PR claims a bound for format `(13, 14, 14)`.

## 3. Literature Search (2024–2026)

Reviewed recent literature from 2024–2026 on bilinear complexity and small/medium matrix multiplication formats, including:
- AlphaEvolve (May 2025)
- Moosbauer & Poole, *Flip Graphs with Symmetry and New Matrix Multiplication Schemes*, arXiv:2502.04514 (2025)
- Perminov, *Fast Matrix Multiplication with Flip Graphs*, arXiv:2603.02398 (2026) and arXiv:2606.02480 (2026)
- Khoruzhii, Serafin, Gelß & Pokutta, *LITA: Local Improvements to Trilinear Aggregation* (2026)

No external publication or preprint reports a bilinear rank below **1582** for `(13, 14, 14)` over any ring, and the prior internal record in `repo/TROPHY_CASE.md` is **1558**. The claimed scheme `claim/13x14x14_r1541_Q.json` achieves rank **1541** over Q, strictly beating the external minimum (1582) by 41 multiplications and `repo/TROPHY_CASE.md` (1558) by 17 multiplications.

## 4. Verdict

The claimed rank **1541** over Q for format `(13, 14, 14)` in `claim/13x14x14_r1541_Q.json` (documented in `claim/CLAIM.md`, `claim/target.md`, and `claim/REPRODUCE.md`) strictly beats all four external criterion scoreboards (minimum 1582, margin -41), `solven-eu/matmulcatalog` (1614), `repo/TROPHY_CASE.md` (1558, margin -17), all open pull requests, and the 2024–2026 literature.

pass: true
