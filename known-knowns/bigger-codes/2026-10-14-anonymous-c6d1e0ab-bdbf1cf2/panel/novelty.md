# Novelty Panel Report — Binary Constant-Weight Code A(27, 8, 10) at Least 1740

context: subagent
context: subagent (fable)
date_utc: 2026-10-14T07:29:30Z
target_id: constant-weight-codes
claimed_object: claim/A27_8_10_1740.txt (48720 bytes, SHA-256: bdbf1cf2b34d5a2771172cea5d11fe6abcff25a0de03cc60808796fbe6e0acbe)
claimed_bound: explicit binary constant-weight code showing A(27, 8, 10) is at least 1740

## 1. Honest Single-GET Live Fetch of Primary Scoreboards

Each primary scoreboard, arXiv preprint, and repository pull-request listing was fetched once via live HTTP GET (`curl -sS -A "V3R1T4S-novelty-panel/1.0"`):

1. **Brouwer's Table of Constant-Weight Binary Codes (`Andw.html`)**
   - Primary URL: `https://aeb.win.tue.nl/codes/Andw.html`
   - Fetch Timestamp (UTC): `2026-10-14T07:29:12Z`
   - HTTP Status: `200` (127,021 bytes)
   - SHA-256: `0f1b51bf71c0ca91aef82eef740cb0dd9f6be6c4014983213d0eefe0eb631cee`
   - Legacy Mirror (`https://www.win.tue.nl/~aeb/codes/Andw.html`): fetched `2026-10-14T07:29:14Z`, HTTP `301` redirect (`311` bytes, SHA-256 `aca59c7c09c7db90e2ec17fd775eb95643ee842ee0deb1c960ed212b5b1cdc45`) pointing to `https://aeb.win.tue.nl/codes/Andw.html`.
   - Extracted Lower Bound for `(27, 8, 10)`: **1728** (Jordan Boisclair [Bo], archive code a27.8.10.1728H)
   - Extracted Lower Bound for Complement `(27, 8, 17)`: **not tabulated** (`w = 17` exceeds `n/2`, outside Brouwer's `w` up to `14` columns)

2. **Recent 2026 Preprints Cited on Brouwer's Table**
   - **Lysenstoen (`arXiv:2607.19550`)**:
     - URL: `https://arxiv.org/abs/2607.19550`
     - Fetch Timestamp (UTC): `2026-10-14T07:29:14Z`, HTTP Status: `200` (43,887 bytes, SHA-256 `6aa83d5b31b4443688dc57e54e000d5272f744fd918b6b115f6636d5291344f1`)
     - Scope: Covers `d = 6, 8` for `n` up to `34`; no bound for `A(27, 8, 10)` exceeding `1728`.
   - **Echols (`arXiv:2608.13906`)**:
     - URL: `https://arxiv.org/abs/2608.13906`
     - Fetch Timestamp (UTC): `2026-10-14T07:29:14Z`, HTTP Status: `200` (39,274 bytes, SHA-256 `cc9f1406799ec21ab93ca205599958f354524ca478d2a87e1d38921088027dd9`)
     - Scope: Seeded bit-swap tabu search for `n` up to `28`; no bound for `A(27, 8, 10)` exceeding `1728`.
   - **Yang et al. (`arXiv:2609.35051`)**:
     - URL: `https://arxiv.org/abs/2609.35051`
     - Fetch Timestamp (UTC): `2026-10-14T07:29:15Z`, HTTP Status: `200` (45,098 bytes, SHA-256 `d4458556ab8b83608bcea941a33a7b410f6054550dfe61adc0b423102cb5832c`)
     - Scope: Kissing number and `w = 8` codes for `n = 33, 34`; no bound for `A(27, 8, 10)`.

## 2. Audit of `repo/TROPHY_CASE.md` and Open Pull Requests

- **`repo/TROPHY_CASE.md`**: Audited all 53 rows of `repo/TROPHY_CASE.md` (rows 8–42 cover `constant-weight-codes`). Row 15 records `A(27,8,10)` at **1737** (`codes/A27_8_10_1737.txt`, which beat `Andw.html` `1728`). There is no entry for the complement `(27, 8, 17)`. Our claimed code `claim/A27_8_10_1740.txt` has **1740** codewords, strictly exceeding `repo/TROPHY_CASE.md` Row 15 (`1737`) by `+3` codewords and `Andw.html` (`1728`) by `+12` codewords.
- **Open Pull Requests (`elder-plinius/V3R1T4S`)**: Fetched `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` at `2026-10-14T07:29:15Z` (HTTP `200`, 988,530 bytes, SHA-256 `403eacc2e18607237486a74b0ed29a69ca2eed7639eb673c202f1f20809a991e`). Exactly 51 open PRs exist (#1–#51); only PR #8 (`A(34,8,7)` at `603`) and PR #28 (`A(27,6,10)` at `13026`) touch `constant-weight-codes`. **Zero open PRs** claim a bound for `(27, 8, 10)` or `(27, 8, 17)`.

## 3. Literature Search (2024–2026) and Composite Bar Comparison

Reviewed 2024–2026 literature on constant-weight binary codes (`A(n, d, w)`), including:
- Lysenstoen, *New lower bounds for binary constant-weight codes*, arXiv:2607.19550 (July 2026)
- Echols, *New lower bounds for constant-weight codes via seeded bit-swap tabu search*, arXiv:2608.13906 (Aug 2026)
- Boisclair, August 2026 submissions to Brouwer's `Andw.html` archive (`[Bo]`)
- Yang et al., arXiv:2609.35051 (Sep 2026)
- Gippini, Zenodo 10.5281/zenodo.23075336 (Oct 2026) and Gangl (Oct 2026)

Summary of known bounds for `A(27, 8, 10)` and complement `A(27, 8, 17)`:
- `Andw.html(27, 8, 10)`: `1728`
- `Andw.html(27, 8, 17)`: not tabulated (`0`)
- `arXiv:2607.19550`, `arXiv:2608.13906`, `arXiv:2609.35051`: none (`0`)
- `repo/TROPHY_CASE.md` (Row 15): `1737`
- Open PRs on `elder-plinius/V3R1T4S`: none (`0`)
- **Composite Known Maximum**: `max(1728, 1737) = 1737`
- **Claimed Code Size**: `1740` (strictly exceeds `1737` by `+3` codewords, and exceeds `Andw.html` `1728` by `+12` codewords)

## 4. Verdict

The claimed binary constant-weight code `claim/A27_8_10_1740.txt` (documented in `claim/CLAIM.md` and `claim/REPRODUCE.md`) with **1740** codewords for `A(27, 8, 10)` strictly beats Brouwer's live `Andw.html` table (`1728`, margin `+12`), its complement cell `(27, 8, 17)`, `repo/TROPHY_CASE.md` Row 15 (`1737`, margin `+3`), all open pull requests, and all 2024–2026 literature.

pass: true
