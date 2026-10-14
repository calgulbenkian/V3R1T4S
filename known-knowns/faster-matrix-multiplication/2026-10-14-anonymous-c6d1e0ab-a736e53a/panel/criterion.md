# Criterion Skeptic Report: `fmm-ternary-integer-ring-upgrade` — Format `(4, 14, 15)` Class `Z` at Rank 569

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed bilinear scheme artifact `claim/4x14x15_m569_Z.json` (`379650` bytes, SHA-256 `a736e53a74f68425c0211816e0972faf8c027d4845885509b530644e9f64c52b`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_z_brent.py`, against every literal requirement of `fmm-ternary-integer-ring-upgrade` in `claim/target.md`:

1. **Explicit bilinear scheme for format `(n, m, p)` with `max(n, m, p)` at most 16 and `sorted(n, m, p) != (4, 4, 4)`**:
   - **PASS.** `claim/4x14x15_m569_Z.json` stores explicit bilinear factor matrices `u` (`569 x 56`), `v` (`569 x 210`), and `w` (`569 x 60`) in Perminov JSON format (`n = [4, 14, 15]`, `m = 569`, file size `379650` bytes, strictly under the `1,000,000`-byte cap). The sorted format `(4, 14, 15)` satisfies `max(4, 14, 15) = 15` (at most 16) and `(4, 14, 15) != (4, 4, 4)`. All `569` rank-one factor triples are strictly non-zero.
2. **Coefficient class (`ZT` in `{-1, 0, 1}` or `Z` in integers)**:
   - **PASS.** Every coefficient across `u`, `v`, `w` in `claim/4x14x15_m569_Z.json` is an exact integer in `[-2, -1, 0, 1, 2]` with `max_abs = 2`, matching the claimed integer (Z, coefficients in {-2, -1, 0, 1, 2}) class `Z`.
3. **Condition (1): Rank `r` strictly less than the live `Z` rank in `dronperminov/FastMatrixMultiplication/master/README.md`**:
   - **PASS.** Here `r = 569`, which is strictly less than the live `Z` column rank `572` for `4x14x15` in `dronperminov/FastMatrixMultiplication/master/README.md` (saving `3` multiplications, `569` vs `572`).
4. **Condition (2): Rank `r` at least `min(ZT, Z, Q)` and at least the live `fmm_sota.json` rank (does NOT beat the overall best rank)**:
   - **PASS.** For `4x14x15`, the live `dronperminov/FastMatrixMultiplication` `README.md` columns are `ZT = 572`, `Z = 572`, `Q = 557` (`min(ZT, Z, Q) = 557`), and the live `fmm_sota.json` best rank is `557`. Since `r = 569` is at least `557`, the scheme is a genuine ring upgrade and does not beat the overall best rank.
5. **Condition (3): No scheme of rank at most `r` in coefficient class `Z` exists in live `schemes/results/Z` or `MerlijnW70/fmm-schemes`**:
   - **PASS.** Neither `dronperminov/FastMatrixMultiplication` (`schemes/results/ZT` and `schemes/results/Z`) nor `MerlijnW70/fmm-schemes` contains a `Z` scheme for `4x14x15` of rank at most `569` (live best `Z` rank is `572`).
6. **Condition (4): Brent equations verified in exact integer arithmetic over `Z`**:
   - **PASS.** Running `claim/verify_z_brent.py` on `claim/4x14x15_m569_Z.json` verifies all `56 * 210 * 60 = 705600` Brent equations in exact Python integer arithmetic over `Z` with zero error (not merely modulo 2).
7. **Non-Subsumption & Scope Check**:
   - **PASS.** Only claim for format (4, 14, 15) in this run.

## 2. Confirmed Scope

confirmed_scope: Explicit exact Z bilinear matrix-multiplication scheme in claim/4x14x15_m569_Z.json (sha256 a736e53a74f68425c0211816e0972faf8c027d4845885509b530644e9f64c52b, 379650 bytes, coefficients in [-2, -1, 0, 1, 2]) for format (4, 14, 15) with rank r = 569, verified in exact integer arithmetic across all 705600 Brent equations over Z and strictly beating the live Z rank (572, saving 3) in dronperminov/FastMatrixMultiplication README.md (ZT = 572, Z = 572, Q = 557) and MerlijnW70/fmm-schemes while remaining at or above the overall best rank (557 in fmm_sota.json and Q column).

pass: true
