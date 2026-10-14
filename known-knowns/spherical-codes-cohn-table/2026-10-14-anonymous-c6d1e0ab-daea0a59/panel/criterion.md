# CRITERION Skeptic Report: `spherical-codes-cohn-table` — `(d, N) = (26, 232)` Full Win

context: subagent
confirmed_scope: Verified that claim/object/code_26_232.json (289,310 bytes, SHA-256 daea0a5983ec270c1f14df3cec70d19d99199037aba112f4e1e8b05dd4748b37) defines 232 explicit 33-digit vectors in R^26 whose 60-digit normalized maximum pairwise inner product is c* = 0.1619070097691030503945036 (minimum angle 80.682396749666 deg), strictly improving upon the unstarred, unlabeled standing record c_table = 0.161911811246 in Henry Cohn's spherical-codes.org table by c_table - c* = 4.801477e-6 (over 48,000x the 1e-10 threshold).

## 1. Clause-by-Clause Verification Against `claim/target.md`

### 1.1 Row Eligibility on Live `spherical-codes.org` & `/plain`
- **Presence in `/plain`**: Verified `(26, 232)` is present in `claim/data/plain.csv` (`26,232,0.161911811246`, fetched `2026-10-14T08:05:00Z`, SHA-256 `750f0b4a872e68e53dd33f82deea554afc60963b2c1d558bc0db25757856244f`).
- **Unstarred & Unlabeled on HTML Index**: Verified in `claim/data/index_metadata.json` (`26,232`: `s = 0`, `o = 0`; HTML SHA-256 `28125e4ec7b2e17b4245f88dd930307d5926e8ec546c59ac1b7b5011a4b977d5`) and `claim/CLAIM.md` that the `(26, 232)` row carries no `&ast;` (proven-optimal) mark and its reference cell (`Vadim Borisov, 2026, https://numaro.tech/`) does not contain `'needs more optimization'`.
- **Non-Kissing Exclusion Zone**: $d = 26$ is outside the $9 \le d \le 23$ kissing-number exclusion zone.
- **Baseline Coordinate Reproduction**: Verified `claim/data/codes/code_26_232.txt` reproduces $c_{\text{table}} = 0.161911811246$ to within $9.22 \times 10^{-13}$ (well within the $10^{-11}$ parser sanity tolerance).

### 1.2 High-Precision Coordinate & Normalization Verification
- **Artifacts**: `claim/object/code_26_232.json` (`289,310` bytes, SHA-256 `daea0a5983ec270c1f14df3cec70d19d99199037aba112f4e1e8b05dd4748b37`) and `claim/object/code_26_232.txt` (`232,194` bytes, SHA-256 `06a5c05efea25f4d22eb947eedd81aea210912a3f818ad9c3264baf40dfd94d7`).
- **Coordinate precision**: All $232 \times 26 = 6,032$ coordinates are given to $33$ significant digits (exceeding the minimum $20$-digit requirement).
- **60-digit and 80-digit exact all-pairs normalization check**: Both `claim/verify_spherical.py` (60-digit `Decimal`) and an independent 80-digit `Decimal` all-pairs evaluation across all $\binom{232}{2} = 26,796$ pairs confirm:
  $$c^* = 0.161907009769103050394503570173, \quad \theta_{\min} = 80.682396749666^\circ.$$
- **Improvement margin**:
  $$c_{\text{table}} - c^* = 0.161911811246 - 0.1619070097691030503945036 = 4.801477 \times 10^{-6} \ge 10^{-10}.$$

## 2. Verdict
All clauses of the `spherical-codes-cohn-table` full success criterion in `claim/target.md` are satisfied.

pass: true
