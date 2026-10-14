# CRITERION Skeptic Report: `spherical-codes-cohn-table` — `(d, N) = (29, 114)` Full Win

context: subagent
confirmed_scope: Verified that claim/object/code_29_114.json (158,452 bytes, SHA-256 8991f120f20e9464eeb266bc9e25cad1b440ad7d53d5dbbf21527a47685b3ccf) defines 114 explicit 33-digit vectors in R^29 whose 60-digit normalized maximum pairwise inner product is c* = 0.0886557493406558116735243 (minimum angle 84.913721944786 deg), strictly improving upon the unstarred, unlabeled standing record c_table = 0.089759904426 in Henry Cohn's spherical-codes.org table by c_table - c* = 1.104155e-3 (over 10,000,000x the 1e-10 threshold).

## 1. Clause-by-Clause Verification Against `claim/target.md`

### 1.1 Row Eligibility on Live `spherical-codes.org` & `/plain`
- **Presence in `/plain`**: Verified `(29, 114)` is present in `claim/data/plain.csv` (`29,114,0.089759904426`, fetched `2026-10-14T08:05:00Z`, SHA-256 `750f0b4a872e68e53dd33f82deea554afc60963b2c1d558bc0db25757856244f`).
- **Unstarred & Unlabeled on HTML Index**: Verified in `claim/data/index_metadata.json` (`29,114`: `s = 0`, `o = 0`; HTML SHA-256 `28125e4ec7b2e17b4245f88dd930307d5926e8ec546c59ac1b7b5011a4b977d5`) and `claim/CLAIM.md` that the `(29, 114)` row carries no `&ast;` (proven-optimal) mark and its reference cell (`Orthogonal union of 112 points in 28 dimensions and 2 points in 1 dimension`) does not contain `'needs more optimization'`.
- **Non-Kissing Exclusion Zone**: $d = 29$ is outside the $9 \le d \le 23$ kissing-number exclusion zone.
- **Baseline Coordinate Reproduction**: Verified `claim/data/codes/code_29_114.txt` reproduces $c_{\text{table}} = 0.089759904426$ to within $1.30 \times 10^{-14}$ (well within the $10^{-11}$ parser sanity tolerance).

### 1.2 High-Precision Coordinate & Normalization Verification
- **Artifacts**: `claim/object/code_29_114.json` (`158,452` bytes, SHA-256 `8991f120f20e9464eeb266bc9e25cad1b440ad7d53d5dbbf21527a47685b3ccf`) and `claim/object/code_29_114.txt` (`127,286` bytes, SHA-256 `fd4e17f48c826275b2a087d3765e4f46394e2e5e6925864190ff5237cafd9108`).
- **Coordinate precision**: All $114 \times 29 = 3,306$ coordinates are given to $33$ significant digits (exceeding the minimum $20$-digit requirement).
- **60-digit and 80-digit exact all-pairs normalization check**: Both `claim/verify_spherical.py` (60-digit `Decimal`) and an independent 80-digit `Decimal` all-pairs evaluation across all $\binom{114}{2} = 6,441$ pairs confirm:
  $$c^* = 0.088655749340655811673524337741, \quad \theta_{\min} = 84.913721944786^\circ.$$
- **Improvement margin**:
  $$c_{\text{table}} - c^* = 0.089759904426 - 0.0886557493406558116735243 = 1.104155 \times 10^{-3} \ge 10^{-10}.$$

## 2. Verdict
All clauses of the `spherical-codes-cohn-table` full success criterion in `claim/target.md` are satisfied.

pass: true
