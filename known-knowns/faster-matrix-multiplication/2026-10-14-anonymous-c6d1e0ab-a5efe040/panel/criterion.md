# Criterion Skeptic Report: `fmm-ternary-integer-ring-upgrade` — Format `(9, 10, 14)` Class `ZT` at Rank 816

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed bilinear scheme artifact `claim/9x10x14_m816_ZT.json` (`594899` bytes, SHA-256 `a5efe04017632a0da87598ba3b2509ca66bb6fea965bb71a2faebb2aef582ab1`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_z_brent.py`, against every literal requirement of `fmm-ternary-integer-ring-upgrade` in `claim/target.md`:

1. **Explicit bilinear scheme for format `(n, m, p)` with `max(n, m, p)` at most 16 and `sorted(n, m, p) != (4, 4, 4)`**:
   - **PASS.** `claim/9x10x14_m816_ZT.json` stores explicit bilinear factor matrices `u` (`816 x 90`), `v` (`816 x 140`), and `w` (`816 x 126`) in Perminov JSON format (`n = [9, 10, 14]`, `m = 816`, file size `594899` bytes, strictly under the `1,000,000`-byte cap). The sorted format `(9, 10, 14)` satisfies `max(9, 10, 14) = 14` (at most 16) and `(9, 10, 14) != (4, 4, 4)`. All `816` rank-one factor triples are strictly non-zero.
2. **Coefficient class (`ZT` in `{-1, 0, 1}` or `Z` in integers)**:
   - **PASS.** Every coefficient across `u`, `v`, `w` in `claim/9x10x14_m816_ZT.json` is an exact integer in `[-1, 0, 1]` with `max_abs = 1`, matching the claimed ternary (ZT, coefficients in {-1, 0, 1}) class `ZT`.
3. **Condition (1): Rank `r` strictly less than the live `ZT` rank in `dronperminov/FastMatrixMultiplication/master/README.md`**:
   - **PASS.** Here `r = 816`, which is strictly less than the live `ZT` column rank `820` for `9x10x14` in `dronperminov/FastMatrixMultiplication/master/README.md` (saving `4` multiplications, `816` vs `820`).
4. **Condition (2): Rank `r` at least `min(ZT, Z, Q)` and at least the live `fmm_sota.json` rank (does NOT beat the overall best rank)**:
   - **PASS.** For `9x10x14`, the live `dronperminov/FastMatrixMultiplication` `README.md` columns are `ZT = 820`, `Z = 820`, `Q = 808` (`min(ZT, Z, Q) = 808`), and the live `fmm_sota.json` best rank is `808`. Since `r = 816` is at least `808`, the scheme is a genuine ring upgrade and does not beat the overall best rank.
5. **Condition (3): No scheme of rank at most `r` in coefficient class `ZT` exists in live `schemes/results/ZT` or `MerlijnW70/fmm-schemes`**:
   - **PASS.** Neither `dronperminov/FastMatrixMultiplication` (`schemes/results/ZT` and `schemes/results/Z`) nor `MerlijnW70/fmm-schemes` contains a `ZT` scheme for `9x10x14` of rank at most `816` (live best `ZT` rank is `820`).
6. **Condition (4): Brent equations verified in exact integer arithmetic over `Z`**:
   - **PASS.** Running `claim/verify_z_brent.py` on `claim/9x10x14_m816_ZT.json` verifies all `90 * 140 * 126 = 1587600` Brent equations in exact Python integer arithmetic over `Z` with zero error (not merely modulo 2).
7. **Non-Subsumption & Scope Check**:
   - **PASS.** Only claim for format (9, 10, 14) in this run.

## 2. Confirmed Scope

confirmed_scope: Explicit exact ZT bilinear matrix-multiplication scheme in claim/9x10x14_m816_ZT.json (sha256 a5efe04017632a0da87598ba3b2509ca66bb6fea965bb71a2faebb2aef582ab1, 594899 bytes, coefficients in [-1, 0, 1]) for format (9, 10, 14) with rank r = 816, verified in exact integer arithmetic across all 1587600 Brent equations over Z and strictly beating the live ZT rank (820, saving 4) in dronperminov/FastMatrixMultiplication README.md (ZT = 820, Z = 820, Q = 808) and MerlijnW70/fmm-schemes while remaining at or above the overall best rank (808 in fmm_sota.json and Q column).

pass: true
