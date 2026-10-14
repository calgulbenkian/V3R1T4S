# Novelty Panel Report — Binary Constant-Weight Code A(35, 6, 6) at Least 2218

context: subagent
context: subagent (fable)
date_utc: 2026-10-14T07:29:30Z
target_id: constant-weight-codes
claimed_object: claim/A35_6_6_2218.txt (79848 bytes, SHA-256: dd2eb057e40bc19bbd7f6a2838681200d6d55b4018e9b01a62082c35822e413e)
claimed_bound: explicit binary constant-weight code showing A(35, 6, 6) is at least 2218

## 1. Honest Single-GET Live Fetch of Primary Scoreboards

Each primary scoreboard, arXiv preprint, and repository pull-request listing was fetched once via live HTTP GET (`curl -sS -A "V3R1T4S-novelty-panel/1.0"`):

1. **Brouwer's Table of Constant-Weight Binary Codes (`Andw.html`)**
   - Primary URL: `https://aeb.win.tue.nl/codes/Andw.html`
   - Fetch Timestamp (UTC): `2026-10-14T07:29:12Z`
   - HTTP Status: `200` (127,021 bytes)
   - SHA-256: `0f1b51bf71c0ca91aef82eef740cb0dd9f6be6c4014983213d0eefe0eb631cee`
   - Legacy Mirror (`https://www.win.tue.nl/~aeb/codes/Andw.html`): fetched `2026-10-14T07:29:14Z`, HTTP `301` redirect (`311` bytes, SHA-256 `aca59c7c09c7db90e2ec17fd775eb95643ee842ee0deb1c960ed212b5b1cdc45`) pointing to `https://aeb.win.tue.nl/codes/Andw.html`.
   - Extracted Lower Bound for `(35, 6, 6)`: **2209** (Jordan Boisclair [Bo], archive code a35.6.6.2209H)
   - Extracted Lower Bound for Complement `(35, 6, 29)`: **not tabulated** (`w = 29` exceeds `n/2`, outside Brouwer's `w` up to `14` columns)

2. **Recent 2026 Preprints Cited on Brouwer's Table**
   - **Lysenstoen (`arXiv:2607.19550`)**:
     - URL: `https://arxiv.org/abs/2607.19550`
     - Fetch Timestamp (UTC): `2026-10-14T07:29:14Z`, HTTP Status: `200` (43,887 bytes, SHA-256 `6aa83d5b31b4443688dc57e54e000d5272f744fd918b6b115f6636d5291344f1`)
     - Scope: Covers `d = 6, 8` for `n` up to `34`; no bound for `A(35, 6, 6)` exceeding `2209`.
   - **Echols (`arXiv:2608.13906`)**:
     - URL: `https://arxiv.org/abs/2608.13906`
     - Fetch Timestamp (UTC): `2026-10-14T07:29:14Z`, HTTP Status: `200` (39,274 bytes, SHA-256 `cc9f1406799ec21ab93ca205599958f354524ca478d2a87e1d38921088027dd9`)
     - Scope: Seeded bit-swap tabu search for `n` up to `28`; no bound for `A(35, 6, 6)` exceeding `2209`.
   - **Yang et al. (`arXiv:2609.35051`)**:
     - URL: `https://arxiv.org/abs/2609.35051`
     - Fetch Timestamp (UTC): `2026-10-14T07:29:15Z`, HTTP Status: `200` (45,098 bytes, SHA-256 `d4458556ab8b83608bcea941a33a7b410f6054550dfe61adc0b423102cb5832c`)
     - Scope: Kissing number and `w = 8` codes for `n = 33, 34`; no bound for `A(35, 6, 6)`.

## 2. Audit of `repo/TROPHY_CASE.md` and Open Pull Requests

- **`repo/TROPHY_CASE.md`**: Audited all 53 rows of `repo/TROPHY_CASE.md` (rows 8–42 cover `constant-weight-codes`). Row 28 records `A(35,6,6)` at **2217** (`codes/A35_6_6_2217.txt`, which beat `Andw.html` `2209`). There is no entry for the complement `(35, 6, 29)`. Our claimed code `claim/A35_6_6_2218.txt` has **2218** codewords, strictly exceeding `repo/TROPHY_CASE.md` Row 28 (`2217`) by `+1` codewords and `Andw.html` (`2209`) by `+9` codewords.
- **Open Pull Requests (`elder-plinius/V3R1T4S`)**: Fetched `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` at `2026-10-14T07:29:15Z` (HTTP `200`, 988,530 bytes, SHA-256 `403eacc2e18607237486a74b0ed29a69ca2eed7639eb673c202f1f20809a991e`). Exactly 51 open PRs exist (#1–#51); only PR #8 (`A(34,8,7)` at `603`) and PR #28 (`A(27,6,10)` at `13026`) touch `constant-weight-codes`. **Zero open PRs** claim a bound for `(35, 6, 6)` or `(35, 6, 29)`.

## 3. Literature Search (2024–2026) and Composite Bar Comparison

Reviewed 2024–2026 literature on constant-weight binary codes (`A(n, d, w)`), including:
- Lysenstoen, *New lower bounds for binary constant-weight codes*, arXiv:2607.19550 (July 2026)
- Echols, *New lower bounds for constant-weight codes via seeded bit-swap tabu search*, arXiv:2608.13906 (Aug 2026)
- Boisclair, August 2026 submissions to Brouwer's `Andw.html` archive (`[Bo]`)
- Yang et al., arXiv:2609.35051 (Sep 2026)
- Gippini, Zenodo 10.5281/zenodo.23075336 (Oct 2026) and Gangl (Oct 2026)

Summary of known bounds for `A(35, 6, 6)` and complement `A(35, 6, 29)`:
- `Andw.html(35, 6, 6)`: `2209`
- `Andw.html(35, 6, 29)`: not tabulated (`0`)
- `arXiv:2607.19550`, `arXiv:2608.13906`, `arXiv:2609.35051`: none (`0`)
- `repo/TROPHY_CASE.md` (Row 28): `2217`
- Open PRs on `elder-plinius/V3R1T4S`: none (`0`)
- **Composite Known Maximum**: `max(2209, 2217) = 2217`
- **Claimed Code Size**: `2218` (strictly exceeds `2217` by `+1` codewords, and exceeds `Andw.html` `2209` by `+9` codewords)

## 4. Verdict

The claimed binary constant-weight code `claim/A35_6_6_2218.txt` (documented in `claim/CLAIM.md` and `claim/REPRODUCE.md`) with **2218** codewords for `A(35, 6, 6)` strictly beats Brouwer's live `Andw.html` table (`2209`, margin `+9`), its complement cell `(35, 6, 29)`, `repo/TROPHY_CASE.md` Row 28 (`2217`, margin `+1`), all open pull requests, and all 2024–2026 literature.

pass: true
