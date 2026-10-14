# CRITERION Skeptic Report: `spherical-codes-cohn-table` — `(d, N) = (30, 117)` Full Win

context: subagent
confirmed_scope: Verified that claim/object/code_30_117.json (168,214 bytes, SHA-256 16db1fae5068ad356d1cf1c16e5b35b117fb9ede19e087e74bdc1291d572af19) defines 117 explicit 33-digit vectors in R^30 whose 60-digit normalized maximum pairwise inner product is c* = 0.0883794850648560216379989 (minimum angle 84.929613100835 deg), strictly improving upon the unstarred, unlabeled standing record c_table = 0.088389506027 in Henry Cohn's spherical-codes.org table by c_table - c* = 1.002096e-5 (over 100,000x the 1e-10 threshold).

## 1. Clause-by-Clause Verification Against `claim/target.md`

### 1.1 Row Eligibility on Live `spherical-codes.org` & `/plain`
- **Presence in `/plain`**: Verified `(30, 117)` is present in `claim/data/plain.csv` (`30,117,0.088389506027`, fetched `2026-10-14T08:05:00Z`, SHA-256 `750f0b4a872e68e53dd33f82deea554afc60963b2c1d558bc0db25757856244f`).
- **Unstarred & Unlabeled on HTML Index**: Verified in `claim/data/index_metadata.json` (`30,117`: `s = 0`, `o = 0`; HTML SHA-256 `28125e4ec7b2e17b4245f88dd930307d5926e8ec546c59ac1b7b5011a4b977d5`) and `claim/CLAIM.md` that the `(30, 117)` row carries no `&ast;` (proven-optimal) mark and its reference cell (`Vadim Borisov, 2026, https://numaro.tech/`) does not contain `'needs more optimization'`.
- **Non-Kissing Exclusion Zone**: $d = 30$ is outside the $9 \le d \le 23$ kissing-number exclusion zone.
- **Baseline Coordinate Reproduction**: Verified `claim/data/codes/code_30_117.txt` reproduces $c_{\text{table}} = 0.088389506027$ to within $4.64 \times 10^{-14}$ (well within the $10^{-11}$ parser sanity tolerance).

### 1.2 High-Precision Coordinate & Normalization Verification
- **Artifacts**: `claim/object/code_30_117.json` (`168,214` bytes, SHA-256 `16db1fae5068ad356d1cf1c16e5b35b117fb9ede19e087e74bdc1291d572af19`) and `claim/object/code_30_117.txt` (`135,176` bytes, SHA-256 `87acc4414d2af1ad497ce82d953dbfb17bbec1d2978be58bff6acc2793ef62f8`).
- **Coordinate precision**: All $117 \times 30 = 3,510$ coordinates are given to $33$ significant digits (exceeding the minimum $20$-digit requirement).
- **60-digit and 80-digit exact all-pairs normalization check**: Both `claim/verify_spherical.py` (60-digit `Decimal`) and an independent 80-digit `Decimal` all-pairs evaluation across all $\binom{117}{2} = 6,786$ pairs confirm:
  $$c^* = 0.088379485064856021637998908858, \quad \theta_{\min} = 84.929613100835^\circ.$$
- **Improvement margin**:
  $$c_{\text{table}} - c^* = 0.088389506027 - 0.0883794850648560216379989 = 1.002096 \times 10^{-5} \ge 10^{-10}.$$

## 2. Verdict
All clauses of the `spherical-codes-cohn-table` full success criterion in `claim/target.md` are satisfied.

pass: true
