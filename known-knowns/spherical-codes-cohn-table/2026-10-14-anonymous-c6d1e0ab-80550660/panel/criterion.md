# CRITERION Skeptic Report: `spherical-codes-cohn-table` — `(d, N) = (29, 145)` Full Win

context: subagent
confirmed_scope: Verified that claim/object/code_29_145.json (201,516 bytes, SHA-256 80550660490b9e5148590d6e502ab71a9ed0067eb476238da3784ad47b23b083) defines 145 explicit 33-digit vectors in R^29 whose 60-digit normalized maximum pairwise inner product is c* = 0.1106960891058149669538693 (minimum angle 83.644556400262 deg), strictly improving upon the unstarred, unlabeled standing record c_table = 0.110701844288 in Henry Cohn's spherical-codes.org table by c_table - c* = 5.755182e-6 (over 57,500x the 1e-10 threshold).

## 1. Clause-by-Clause Verification Against `claim/target.md`

### 1.1 Row Eligibility on Live `spherical-codes.org` & `/plain`
- **Presence in `/plain`**: Verified `(29, 145)` is present in `claim/data/plain.csv` (`29,145,0.110701844288`, fetched `2026-10-14T08:05:00Z`, SHA-256 `750f0b4a872e68e53dd33f82deea554afc60963b2c1d558bc0db25757856244f`).
- **Unstarred & Unlabeled on HTML Index**: Verified in `claim/data/index_metadata.json` (`29,145`: `s = 0`, `o = 0`; HTML SHA-256 `28125e4ec7b2e17b4245f88dd930307d5926e8ec546c59ac1b7b5011a4b977d5`) and `claim/CLAIM.md` that the `(29, 145)` row carries no `&ast;` (proven-optimal) mark and its reference cell (`Vadim Borisov, 2026, https://numaro.tech/`) does not contain `'needs more optimization'`.
- **Non-Kissing Exclusion Zone**: $d = 29$ is outside the $9 \le d \le 23$ kissing-number exclusion zone.
- **Baseline Coordinate Reproduction**: Verified `claim/data/codes/code_29_145.txt` reproduces $c_{\text{table}} = 0.110701844288$ to within $7.58 \times 10^{-13}$ (well within the $10^{-11}$ parser sanity tolerance).

### 1.2 High-Precision Coordinate & Normalization Verification
- **Artifacts**: `claim/object/code_29_145.json` (`201,516` bytes, SHA-256 `80550660490b9e5148590d6e502ab71a9ed0067eb476238da3784ad47b23b083`) and `claim/object/code_29_145.txt` (`161,887` bytes, SHA-256 `4e4787fc145320dad4cc5361b10833df8c845a054ec69ee1562623bd728ffa8b`).
- **Coordinate precision**: All $145 \times 29 = 4,205$ coordinates are given to $33$ significant digits (exceeding the minimum $20$-digit requirement).
- **60-digit and 80-digit exact all-pairs normalization check**: Both `claim/verify_spherical.py` (60-digit `Decimal`) and an independent 80-digit `Decimal` all-pairs evaluation across all $\binom{145}{2} = 10,440$ pairs confirm:
  $$c^* = 0.110696089105814966953869301689, \quad \theta_{\min} = 83.644556400262^\circ.$$
- **Improvement margin**:
  $$c_{\text{table}} - c^* = 0.110701844288 - 0.1106960891058149669538693 = 5.755182 \times 10^{-6} \ge 10^{-10}.$$

## 2. Verdict
All clauses of the `spherical-codes-cohn-table` full success criterion in `claim/target.md` are satisfied.

pass: true
