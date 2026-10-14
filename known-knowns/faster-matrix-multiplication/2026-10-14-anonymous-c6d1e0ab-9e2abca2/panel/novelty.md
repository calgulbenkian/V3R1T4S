# Novelty Panel Report — Format 4x4x6 Rank 73 SLP in 275 Reduced Additions over Z

context: subagent
context: subagent (fable)
date_utc: 2026-10-14T03:50:35Z
target_id: fmm-additive-complexity-records
claimed_object: claim/4x4x6_m73_cr275_fv101_cn534_ZT_reduced.json (SHA-256: 9e2abca2c586a6020b90ae6e020dabb4b00f47dead9e4bea48a804452a8dfff7)
claimed_bound: format (4, 4, 6) rank m = 73 ternary straight-line program with cr = 275 reduced additions (fv = 101, cn = 534) over Z

## 1. Honest Single-GET Live Fetch of Primary Scoreboards

Each primary scoreboard, directory listing, and status page was fetched once via live HTTP GET (`curl -sS -A "V3R1T4S-novelty-panel/1.0"`):

1. **Perminov `addition_reduced_ZT` Directory Listing (GitHub Contents API)**
   - URL: `https://api.github.com/repos/dronperminov/FastMatrixMultiplication/contents/schemes/results/addition_reduced_ZT`
   - Fetch Timestamp (UTC): `2026-10-14T03:50:16Z`
   - HTTP Status: `200` (256,734 bytes, 195 scheme files total, SHA-256 prefix `f57b2ae11a9f012a`)
   - Files Matching Format `4x4x6` and Rank `m = 73`: `4x4x6_m73_cr280_cn540_ZT_reduced.json`
   - Minimum Listed Reduced Addition Count (`cr`): **280** (naive additions `cn = 540`)

2. **Perminov `reduced_known.json`**
   - URL: `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json`
   - Fetch Timestamp (UTC): `2026-10-14T03:50:15Z`
   - HTTP Status: `200` (1,189 bytes, 33 format-rank keys, SHA-256 prefix `ef67c13792b0e770`)
   - Entry for `4x4x6`: `'4x4x6-74': {'Z': 467, 'Z2': 360} (higher rank 74; none at rank 73)`

3. **Perminov `README.md` and `CHANGELOG.md`**
   - `README.md` URL: `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md`
     - Fetch Timestamp (UTC): `2026-10-14T03:50:15Z`, HTTP Status: `200` (112,671 bytes, SHA-256 `7b0761ecc0fa1988cb2ef0efeca503af974eeb6ade76d30629308ebba7e78341`)
     - Lists rank `m = 73` for `4x4x6` over `ZT/Z/Q`; no lower reduced-addition count than `280` (`addition_reduced_ZT`).
   - `CHANGELOG.md` URL: `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/CHANGELOG.md`
     - Fetch Timestamp (UTC): `2026-10-14T03:50:15Z`, HTTP Status: `200` (85,319 bytes, SHA-256 prefix `07fbb3249d1213b9`)
     - No lower reduced-addition count than `280` for format `4x4x6` at rank `m = 73`.

4. **Sedoglavic Lille JSON Digest (`fmm_sota.json`)**
   - URL: `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json`
   - Fetch Timestamp (UTC): `2026-10-14T03:50:16Z`
   - HTTP Status: `200` (343,798 bytes, SHA-256 `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`, `createdAt: 2026-10-09T11:45:48`)
   - Extracted Entry for `[4, 4, 6]`: best known rank is **73** (confirming the claimed SLP has rank `m = 73` equal to the best rank in `fmm_sota.json`).

5. **Sedoglavic Lille Per-Format Page (`4x4x6.html`)**
   - URL: `https://fmm.univ-lille.fr/4x4x6.html`
   - Fetch Timestamp (UTC): `2026-10-14T03:50:21Z`
   - HTTP Status: `200` (6616 bytes, SHA-256 prefix `f30768b4561049c7`)
   - Cited Complexity Variants: none (rank 73 tensor scheme only; no reduced-addition SLP complexity variant listed)

6. **Solven `matmulcatalog` Coverage Table (`COVERAGE.md`)**
   - URL: `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md`
   - Fetch Timestamp (UTC): `2026-10-14T03:50:17Z`
   - HTTP Status: `200` (94,842 bytes, SHA-256 `c2a9bd929b477acb44d4f92aa8055a0c26eab3c33121c0734be650c5c86254b7`)
   - Extracted `adds` Column for `(4, 4, 6)`: **+565 (Dronperminov-ZT, rank 73)**

Minimum reduced addition count across all external sources for format `4x4x6` at best rank `m = 73`: **280**.

## 2. Audit of `repo/TROPHY_CASE.md` and Open Pull Requests

- **`repo/TROPHY_CASE.md`**: Audited all 53 rows of `repo/TROPHY_CASE.md` (rows 44–48 cover `fast-matrix-multiplication` rank bounds for 13x14x14, 14x14x15, 13x14x15, 14x15x15, and 15x16x16). There are **zero entries** for `fmm-additive-complexity-records` or format `4x4x6` in `repo/TROPHY_CASE.md`.
- **Open Pull Requests**: Fetched `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` at `2026-10-14T03:50:17Z` (HTTP `200`, 139,901 bytes, SHA-256 prefix `b1fd986a852cfd4d`). Exactly 8 open PRs exist (#1–#8: PR #1 control-count fix, PRs #2–#7 `fmm-catalogue-small-format-rank` rank claims on formats 13x15x15, 13x13x14, 13x14x15, 13x14x14, 14x14x15, 14x16x16, and PR #8 constant-weight code review). **No open PR** touches `fmm-additive-complexity-records` or format `4x4x6`.

## 3. Literature Search (2024–2026)

Reviewed 2024–2026 literature on straight-line program (SLP) addition reduction and common-subexpression elimination for fast matrix multiplication schemes, including:
- Perminov, *A 58-Addition, Rank-23 Scheme for General 3x3 Matrix Multiplication*, arXiv:2512.21980 (Dec 2025)
- Perminov, *Parallel Heuristic Exploration for Additive Complexity Reduction in Fast Matrix Multiplication*, arXiv:2512.13365 / arXiv:2601.05272 (2025–2026), and the `ternary_addition_reducer` corpus (`addition_reduced_ZT`)
- Dumas, Pernet, Sedoglavic, Stapleton & Tichavsky (2026) on 4x4x4 rank-48 complexity variants
- AlphaEvolve (May 2025)

No paper, preprint, or repository reports a reduced addition count below **280** for format `(4, 4, 6)` at rank `m = 73`.

## 4. Verdict

The claimed ternary straight-line program `claim/4x4x6_m73_cr275_fv101_cn534_ZT_reduced.json` (documented in `claim/CLAIM.md`, `claim/target.md`, and `claim/REPRODUCE.md`) for format `(4, 4, 6)` at best-known rank `m = 73` achieves `cr = 275` reduced additions over `Z`, which is **strictly less** than the minimum known count `280` across `addition_reduced_ZT`, `reduced_known.json`, `README.md`, `CHANGELOG.md`, `matmulcatalog` `COVERAGE.md`, `fmm.univ-lille.fr/4x4x6.html`, `repo/TROPHY_CASE.md`, open pull requests, and the 2024–2026 literature (improvement margin `-5` additions).

pass: true
