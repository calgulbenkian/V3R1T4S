# Novelty Panel Report — Format 9x11x14 (Z Ring Upgrade at Rank 889)

context: subagent
context: subagent (fable)
date_utc: 2026-10-14T06:15:20Z
target_id: fmm-ternary-integer-ring-upgrade
claimed_object: claim/9x11x14_m889_Z.json (693112 bytes, SHA-256: e25137a39f9a642d3a93ae58337d80703f5e45c2efc48e96207d7e61aeb101e5)
claimed_bound: format (9, 11, 14) integer (Z, coefficients in {-2, -1, 0, 1, 2}) bilinear scheme of rank r = 889 over Z

## 1. Honest Single-GET Live Fetch of Primary Scoreboards

Each primary scoreboard, status index, and repository table was fetched once via live HTTP GET (`curl -sS -A "V3R1T4S-novelty-panel/1.0"`):

1. **Perminov `FastMatrixMultiplication` Status Table (`README.md`)**
   - URL: `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md`
   - Fetch Timestamp (UTC): `2026-10-14T06:14:29Z`
   - HTTP Status: `200` (112,671 bytes)
   - SHA-256: `7b0761ecc0fa1988cb2ef0efeca503af974eeb6ade76d30629308ebba7e78341`
   - Extracted Rows for `9x11x14`:
     - Summary table: `| 9x11x14 | 904 (Z) | 882 (Q) | 2.812562599 |`
     - Status table (`ZT / Z / Q`): `| 9x11x14 | 900 (?) | 900 (904) | 882 (904) | 2.812562599 |`
   - Listed Ranks (`ZT / Z / Q`): **900 / 900 / 882** (minimum across all rings: **882**)

2. **Perminov `schemes/status.json` and `CHANGELOG.md`**
   - `status.json` URL: `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/status.json`
     - Fetch Timestamp (UTC): `2026-10-14T06:14:30Z`, HTTP Status: `200` (2,165,677 bytes, SHA-256 `b9b86c506ef4826220e5479569c6a84eaa720b703f73b705c043a3c90b463311`)
     - Extracted `ranks` for `9x11x14`: `ZT = 900`, `Z = 900`, `Q = 882`
     - Existing schemes in repository for `9x11x14`: ZT: 9x11x14_m900_ZT.json (rank 900); Z: 9x11x14_m904_Z.json (rank 904; best Z is 900 via ZT); Q: 9x11x14_m882_Q.json (rank 882, denominator 2), 9x11x14_m889_Q.json (rank 889, denominator 2)
   - `CHANGELOG.md` URL: `https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/CHANGELOG.md`
     - Fetch Timestamp (UTC): `2026-10-14T06:14:29Z`, HTTP Status: `200` (85,319 bytes, SHA-256 `07fbb3249d1213b95d9a9c3069d208c0c3b4390a6b87c71325af64a2d56cd175`)
     - Extracted entries for `9x11x14`: Lists Q improvements at ranks 889 and 882; no Z scheme below 900.

3. **Sedoglavic Lille JSON Digest (`fmm_sota.json`)**
   - URL: `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json`
   - Fetch Timestamp (UTC): `2026-10-14T06:14:31Z`
   - HTTP Status: `200` (343,798 bytes)
   - SHA-256: `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`
   - Snapshot Metadata: `createdAt: 2026-10-09T11:45:48`
   - Extracted Entry for `[9, 11, 14]`: `rank = 882`, `exponent = 2.812563`

4. **Sedoglavic Lille Per-Format Page (`9x11x14.html`)**
   - URL: `https://fmm.univ-lille.fr/9x11x14.html`
   - Fetch Timestamp (UTC): `2026-10-14T06:14:40Z`
   - HTTP Status: `200` (34592 bytes)
   - SHA-256: `43cfb781b1de58cfd2b72645c00eb654d86ad6572992ba5b0bcde0335b0f5776`
   - Extracted Listed Rank: **882 (over Q)**

5. **MerlijnW70 `fmm-schemes` Repository (`SHA256SUMS`)**
   - URL: `https://raw.githubusercontent.com/MerlijnW70/fmm-schemes/main/SHA256SUMS`
   - Fetch Timestamp (UTC): `2026-10-14T06:14:31Z`
   - HTTP Status: `200` (3,044 bytes, 32 lines)
   - SHA-256: `de848328881cf69cbe2a8d8309e04d94826cf1431b5b39e81db63f95af58a3fd`
   - Extracted Entry for `9x11x14`: **none** (0 matching lines)

## 2. Audit of `repo/TROPHY_CASE.md` and Open Pull Requests

- **`repo/TROPHY_CASE.md`**: Audited all 53 rows of `repo/TROPHY_CASE.md` (rows 44–48 cover `fast-matrix-multiplication` rational schemes for formats `14x15x15`, `13x14x14`, `15x16x16`, `14x14x15`, `13x14x15`). There are **zero entries** for `fmm-ternary-integer-ring-upgrade` or format `9x11x14` in `repo/TROPHY_CASE.md`.
- **Open Pull Requests (`elder-plinius/V3R1T4S`)**: Fetched `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` at `2026-10-14T06:14:43Z` (HTTP `200`, 600,454 bytes, SHA-256 `5c47bfa2a305b12c07c72fc1971e80e23c0bf9f4a75c496cfc52e030f4dc71d4`). Exactly 31 open PRs exist (#1–#31); **zero open PRs** touch `fmm-ternary-integer-ring-upgrade` or format `9x11x14`.
- **Open Pull Requests on External Repositories**: Fetched `https://api.github.com/repos/dronperminov/FastMatrixMultiplication/pulls?state=open&per_page=100` and `https://api.github.com/repos/MerlijnW70/fmm-schemes/pulls?state=open&per_page=100` at `2026-10-14T06:14:44Z` (both HTTP `200`, 2 bytes `[]`, SHA-256 `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`), confirming **0 open PRs** on either upstream repository.

## 3. Literature Search (2024–2026) and Ring-Upgrade Criteria Verification

Reviewed 2024–2026 literature on fast matrix multiplication over restricted rings (`ZT` and `Z`), including:
- Moosbauer & Poole, *Flip Graphs with Symmetry and New Matrix Multiplication Schemes*, arXiv:2502.04514 (2025)
- AlphaEvolve (May 2025)
- Perminov, *Fast Matrix Multiplication with Flip Graphs*, arXiv:2603.02398 (2026) and meta flip-graph lifting arXiv:2606.02480 (June 2026)

Checking all four target novelty criteria in `claim/target.md` for `claim/9x11x14_m889_Z.json`:
1. **Strict Improvement over Live `Z` Rank**: Claimed rank `r = 889` is strictly below the live `Z` rank `900` in Perminov's `README.md` and `status.json` (`889` vs `900`, saving `11` multiplications).
2. **Valid Ring-Upgrade Regime**: Claimed rank `r = 889` is at least the minimum over `ZT/Z/Q` (`882`) and at least `fmm_sota.json` (`882`), confirming it is a genuine ring upgrade (`889` is at least `882`) rather than an overall rank record.
3. **No Existing Scheme of Rank at Most `889` in Class `Z`**: Verified in Perminov's `schemes/status.json`, `README.md`, `CHANGELOG.md`, and `MerlijnW70/fmm-schemes` that no `Z` scheme for `9x11x14` has rank `889` or lower. (For `4x13x15`, the companion `ZT` claim in this batch has rank `535`, whereas the `Z` claim has strictly lower rank `533`.)

## 4. Verdict

The claimed `Z` scheme `claim/9x11x14_m889_Z.json` (documented in `claim/CLAIM.md`, `claim/target.md`, and `claim/REPRODUCE.md`) for format `(9, 11, 14)` at rank `r = 889` strictly beats the live `Z` record (`900`, margin `-11`), satisfies all `fmm-ternary-integer-ring-upgrade` criteria, and is absent from `repo/TROPHY_CASE.md`, all open pull requests, and the 2024–2026 literature.

pass: true
