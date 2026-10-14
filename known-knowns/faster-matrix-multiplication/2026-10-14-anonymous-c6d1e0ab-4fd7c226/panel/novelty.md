# Novelty Panel Report — Format 14x16x16 Rank 2119 over Q

context: subagent
context: subagent (fable)
date_utc: 2026-10-14T02:34:35Z
target_id: fmm-catalogue-small-format-rank
claimed_object: claim/14x16x16_r2119_Q.json (SHA-256: 4fd7c2264911e65fcc6cf7074e6100202786a5de6c01b85b9ac6572fdf31ba56)
claimed_bound: format (14, 16, 16) bilinear rank 2119 over Q

## 1. Honest Single-GET Live Fetch of Primary Scoreboards

Each primary scoreboard and repository status table was fetched once via live HTTP GET (`curl -sS -A "V3R1T4S-novelty-panel/1.0"`):

1. **Sedoglavic Lille JSON Digest (`fmm_sota.json`)**
   - URL: `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json`
   - Fetch Timestamp (UTC): `2026-10-14T02:33:58Z`
   - HTTP Status: `200` (343,798 bytes)
   - SHA-256: `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`
   - Snapshot Metadata: `createdAt: 2026-10-09T11:45:48`
   - Extracted Entry for `[14, 16, 16]`: `{"format": [14, 16, 16], "rank": 2128, "exponent": 2.808914}`
   - Listed Rank: **2128**

2. **Sedoglavic Lille Per-Format Page (`14x16x16.html`)**
   - URL: `https://fmm.univ-lille.fr/14x16x16.html`
   - Fetch Timestamp (UTC): `2026-10-14T02:34:07Z`
   - HTTP Status: `200` (46,926 bytes)
   - SHA-256: `c8a6c116b6746ef25ca4eef0978d38943716a647e68fd6b7ff3e36965cb8aeb8`
   - Extracted Header: `Description of fast matrix multiplication algorithm: 14x16x16:2128`
   - Listed Rank: **2128**

3. **Perminov `FastMatrixMultiplication` Status Table (`README.md`)**
   - URL: `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md`
   - Fetch Timestamp (UTC): `2026-10-14T02:34:09Z`
   - HTTP Status: `200` (112,671 bytes)
   - SHA-256: `7b0761ecc0fa1988cb2ef0efeca503af974eeb6ade76d30629308ebba7e78341`
   - Extracted Table Rows for `14x16x16`:
     - Summary row: `| 14x16x16 | 2142 (Q) | 2128 (Q) | 2.808914234 |`
     - Status row (ZT / Z / Q): `| 14x16x16 | 2170 (?) | 2170 (?) | 2128 (2142) | 2.808914234 |`
   - Listed Ranks (ZT / Z / Q): **2170 / 2170 / 2128** (minimum: **2128**)

4. **MerlijnW70 `fmm-schemes` Repository (`SHA256SUMS`)**
   - URL: `https://raw.githubusercontent.com/MerlijnW70/fmm-schemes/main/SHA256SUMS`
   - Fetch Timestamp (UTC): `2026-10-14T02:34:09Z`
   - HTTP Status: `200` (3,044 bytes, 32 lines)
   - SHA-256: `de848328881cf69cbe2a8d8309e04d94826cf1431b5b39e81db63f95af58a3fd`
   - Extracted Entry for `14x16x16`: **none** (0 matching lines)

5. **Solven `matmulcatalog` Coverage Table (`COVERAGE.md`)**
   - URL: `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md`
   - Fetch Timestamp (UTC): `2026-10-14T02:34:09Z`
   - HTTP Status: `200` (94,842 bytes)
   - SHA-256: `c2a9bd929b477acb44d4f92aa8055a0c26eab3c33121c0734be650c5c86254b7`
   - Extracted Row for `(14,16,16)`: F2 = **2170** (`Dronperminov-ZT [Z to F2]`), R/Q/Z = **2128** (`Dronperminov-Q`)

Minimum rank across all external scoreboards over any ring: **2128**.

## 2. Audit of `repo/TROPHY_CASE.md` and Open Pull Requests

- **`repo/TROPHY_CASE.md`**: Audited all 53 rows (including rows 44–48 in the `fast-matrix-multiplication` family: `(14,15,15)` rank 1842, `(13,14,14)` rank 1558, `(15,16,16)` rank 2180, `(14,14,15)` rank 1716, and `(13,14,15)` rank 1677). There is **no prior entry** for format `(14, 16, 16)` in `repo/TROPHY_CASE.md`.
- **Open Pull Requests**: Fetched `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` at `2026-10-14T02:34:10Z` (HTTP `200`, 38,340 bytes, SHA-256 `3c174ff25f71500bcf1a11109c0a60d56ccf7e520025a454a8c43b8a56e0eb59`). Exactly 2 open PRs exist:
  - PR #1: `fix: reject malformed null control counts`
  - PR #2: `[claim] fmm-catalogue-small-format-rank: format (13, 15, 15) rank 1763 over Q (beats 1776 bar)`
  Neither open PR claims a bound for format `(14, 16, 16)`.

## 3. Literature Search (2024–2026)

Reviewed recent literature from 2024–2026 on bilinear complexity and small/medium matrix multiplication formats, including:
- AlphaEvolve (May 2025)
- Moosbauer & Poole, *Flip Graphs with Symmetry and New Matrix Multiplication Schemes*, arXiv:2502.04514 (2025)
- Perminov, *Fast Matrix Multiplication with Flip Graphs*, arXiv:2603.02398 (2026) and arXiv:2606.02480 (2026)
- Khoruzhii, Serafin, Gelß & Pokutta, *LITA: Local Improvements to Trilinear Aggregation* (2026)

No external publication or preprint reports a bilinear rank below **2128** for `(14, 16, 16)` over any ring. The claimed scheme `claim/14x16x16_r2119_Q.json` achieves rank **2119** over Q, strictly beating the best known bound of **2128** by 9 multiplications.

## 4. Verdict

The claimed rank **2119** over Q for format `(14, 16, 16)` in `claim/14x16x16_r2119_Q.json` (documented in `claim/CLAIM.md`, `claim/target.md`, and `claim/REPRODUCE.md`) strictly beats all four external criterion scoreboards (minimum 2128, margin -9), `solven-eu/matmulcatalog` (2128), `repo/TROPHY_CASE.md` (no prior entry), all open pull requests, and the 2024–2026 literature.

pass: true
