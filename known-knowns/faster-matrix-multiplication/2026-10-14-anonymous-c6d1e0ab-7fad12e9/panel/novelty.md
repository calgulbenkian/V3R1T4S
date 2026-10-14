# Novelty Panel Report — Format 15x16x16 Rank 2177 over Q

context: subagent
context: subagent (fable)
date_utc: 2026-10-14T06:20:30Z
target_id: fmm-catalogue-small-format-rank
claimed_object: claim/15x16x16_r2177_Q.json (745817 bytes, SHA-256: 7fad12e946debb23b15ffe57e5fc3f15a8f05c1859510e5aaccb9af5907618aa)
claimed_bound: Full Win (max(n,m,p) = 16) — format (15, 16, 16) bilinear scheme of rank r = 2177 over Q

## 1. Honest Single-GET Live Fetch of Primary Scoreboards

Each primary scoreboard and repository status table was fetched once via live HTTP GET (`curl -sS -A "V3R1T4S-novelty-panel/1.0"`):

1. **Sedoglavic Lille JSON Digest (`fmm_sota.json`)**
   - URL: `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json`
   - Fetch Timestamp (UTC): `2026-10-14T06:19:43Z`
   - HTTP Status: `200` (343,798 bytes)
   - SHA-256: `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`
   - Snapshot Metadata: `createdAt: 2026-10-09T11:45:48`
   - Extracted Entry for `[15, 16, 16]`: `{"format": [15, 16, 16], "rank": 2223, "exponent": 2.801309}`
   - Listed Rank: **2223** (our rank `2177` beats `fmm_sota.json` by `-46` multiplications)

2. **Sedoglavic Lille Per-Format Page (`15x16x16.html`)**
   - URL: `https://fmm.univ-lille.fr/15x16x16.html`
   - Fetch Timestamp (UTC): `2026-10-14T06:19:46Z`
   - HTTP Status: `200` (105530 bytes)
   - SHA-256: `ec9909c16f784fb8dd22e470b9bb2770603927f85c83c5be118acbedb139f0b2`
   - Extracted Header: `Description of fast matrix multiplication algorithm: 15x16x16:2262`
   - Listed Rank: **2262** (our rank `2177` beats `15x16x16.html` by `-85` multiplications)

3. **Perminov `FastMatrixMultiplication` Status Table (`README.md`)**
   - URL: `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md`
   - Fetch Timestamp (UTC): `2026-10-14T06:19:43Z`
   - HTTP Status: `200` (112,671 bytes)
   - SHA-256: `7b0761ecc0fa1988cb2ef0efeca503af974eeb6ade76d30629308ebba7e78341`
   - Extracted Entry for `15x16x16`: **ZT = 2302 (?), Z = 2302 (?), Q = 2223 (2262) (minimum: 2223)**

4. **MerlijnW70 `fmm-schemes` Repository (`SHA256SUMS`)**
   - URL: `https://raw.githubusercontent.com/MerlijnW70/fmm-schemes/main/SHA256SUMS`
   - Fetch Timestamp (UTC): `2026-10-14T06:19:44Z`
   - HTTP Status: `200` (3,044 bytes, 32 lines)
   - SHA-256: `de848328881cf69cbe2a8d8309e04d94826cf1431b5b39e81db63f95af58a3fd`
   - Extracted Entry for `15x16x16`: **none** (0 matching lines)

5. **Solven `matmulcatalog` Coverage Table (`COVERAGE.md`)**
   - URL: `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md`
   - Fetch Timestamp (UTC): `2026-10-14T06:19:44Z`
   - HTTP Status: `200` (94,842 bytes)
   - SHA-256: `c2a9bd929b477acb44d4f92aa8055a0c26eab3c33121c0734be650c5c86254b7`
   - Extracted Entry for `15x16x16`: **F2 = 2302 (Dronperminov-ZT), R/Q/Z = 2302 (Dronperminov-ZT)**

## 2. Audit of `repo/TROPHY_CASE.md` and Open Pull Requests

- **`repo/TROPHY_CASE.md`**: Audited all 53 rows of `repo/TROPHY_CASE.md` (rows 44–48 cover `fast-matrix-multiplication` rational schemes). Entry for `15x16x16`: **Row 46 records format (15, 16, 16) at rank 2180 over Q (schemes/15x16x16_r2180_Q.json); our claimed rank 2177 strictly beats Row 46 by 3 multiplications (margin -3) and beats the external minimum 2223 by 46 multiplications (margin -46)**.
- **Open Pull Requests (`elder-plinius/V3R1T4S`)**: Fetched `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` at `2026-10-14T06:19:44Z` (HTTP `200`, 600,454 bytes, SHA-256 `0185f4e69ea7c57d9f7064c978dacde78af1837eafa4e0bf1dfff02f32441b76`). Exactly 31 open PRs exist (#1–#31); **zero open PRs** claim a bound for format `15x16x16`.

## 3. Literature Search (2024–2026)

Reviewed 2024–2026 literature on fast matrix multiplication and bilinear tensor rank for medium rectangular formats, including:
- AlphaEvolve (May 2025)
- Moosbauer & Poole, *Flip Graphs with Symmetry and New Matrix Multiplication Schemes*, arXiv:2502.04514 (2025)
- Perminov, *Fast Matrix Multiplication with Flip Graphs*, arXiv:2603.02398 (2026) and arXiv:2606.02480 (2026)
- Khoruzhii, Serafin, Gelß & Pokutta, *LITA: Local Improvements to Trilinear Aggregation* (2026)

No published paper, preprint, or public repository reports a bilinear rank as low as **2177** for format `(15, 16, 16)` over any ring. The lowest previously known rank across all external and internal sources is **2180**, which `claim/15x16x16_r2177_Q.json` strictly beats by `-3` multiplications.

## 4. Verdict

The claimed rank **2177** over Q for format `(15, 16, 16)` in `claim/15x16x16_r2177_Q.json` (documented in `claim/CLAIM.md`, `claim/table_record.md`, `claim/target.md`, and `claim/REPRODUCE.md`) strictly beats all external scoreboards (`fmm_sota.json = 2223`, `fmm.univ-lille.fr/15x16x16.html = 2262`, Perminov, MerlijnW70, `matmulcatalog`), `repo/TROPHY_CASE.md` (best overall prior bound `2180`, margin `-3`), all open pull requests, and the 2024–2026 literature.

pass: true
