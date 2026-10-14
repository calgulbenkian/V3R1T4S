# CRITERION Skeptic Report: `spherical-codes-cohn-table` — `(d, N) = (28, 70)` Full Win

context: subagent
confirmed_scope: Verified that claim/object/code_28_70.json (93,832 bytes, SHA-256 cd7c56d206970b5e9b3b44ef5f31395908b4e84acf22f807c46a543556f05263) defines 70 explicit 33-digit vectors in R^28 whose 60-digit normalized maximum pairwise inner product is c* = 0.0517863124041101353861329 (minimum angle 87.031535037277 deg), strictly improving upon the unstarred, unlabeled standing record c_table = 0.051797462893 in Henry Cohn's spherical-codes.org table by c_table - c* = 1.115049e-5 (over 111,000x the 1e-10 threshold).

## 1. Clause-by-Clause Verification Against `claim/target.md`

### 1.1 Row Eligibility on Live `spherical-codes.org` & `/plain`
- **Presence in `/plain`**: Verified `(28, 70)` is present in `claim/data/plain.csv` (`28,70,0.051797462893`, fetched `2026-10-14T08:05:00Z`, SHA-256 `750f0b4a872e68e53dd33f82deea554afc60963b2c1d558bc0db25757856244f`).
- **Unstarred & Unlabeled on HTML Index**: Verified in `claim/data/index_metadata.json` (`28,70`: `s = 0`, `o = 0`; HTML SHA-256 `28125e4ec7b2e17b4245f88dd930307d5926e8ec546c59ac1b7b5011a4b977d5`) and `claim/CLAIM.md` that the `(28, 70)` row carries no `&ast;` (proven-optimal) mark and its reference cell (`Orthogonal union of 66 points in 26 dimensions and 4 points in 2 dimensions`) does not contain `'needs more optimization'`.
- **Non-Kissing Exclusion Zone**: $d = 28$ is outside the $9 \le d \le 23$ kissing-number exclusion zone.
- **Baseline Coordinate Reproduction**: Verified `claim/data/codes/code_28_70.txt` reproduces $c_{\text{table}} = 0.051797462893$ to within $6.13 \times 10^{-13}$ (well within the $10^{-11}$ parser sanity tolerance).

### 1.2 High-Precision Coordinate & Normalization Verification
- **Artifacts**: `claim/object/code_28_70.json` (`93,832` bytes, SHA-256 `cd7c56d206970b5e9b3b44ef5f31395908b4e84acf22f807c46a543556f05263`) and `claim/object/code_28_70.txt` (`75,309` bytes, SHA-256 `f6f1082ef27f21b7b885dcde6dec1daf4ed06c879a547b5732a011839779cc15`).
- **Coordinate precision**: All $70 \times 28 = 1,960$ coordinates are given to $33$ significant digits (exceeding the minimum $20$-digit requirement).
- **60-digit and 80-digit exact all-pairs normalization check**: Both `claim/verify_spherical.py` (60-digit `Decimal`) and an independent 80-digit `Decimal` all-pairs evaluation across all $\binom{70}{2} = 2,415$ pairs confirm:
  $$c^* = 0.051786312404110135386132937185, \quad \theta_{\min} = 87.031535037277^\circ.$$
- **Improvement margin**:
  $$c_{\text{table}} - c^* = 0.051797462893 - 0.0517863124041101353861329 = 1.115049 \times 10^{-5} \ge 10^{-10}.$$

## 2. Verdict
All clauses of the `spherical-codes-cohn-table` full success criterion in `claim/target.md` are satisfied.

pass: true
