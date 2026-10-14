# Criterion Skeptic Report: `fmm-ternary-integer-ring-upgrade` — Format `(9, 13, 14)` Class `Z` at Rank 1039

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed bilinear scheme artifact `claim/9x13x14_m1039_Z.json` (`907758` bytes, SHA-256 `bed17451925a1e9a484a2848faae3aca36011203fbd9e3277c73d673a8a57daa`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_z_brent.py`, against every literal requirement of `fmm-ternary-integer-ring-upgrade` in `claim/target.md`:

1. **Explicit bilinear scheme for format `(n, m, p)` with `max(n, m, p)` at most 16 and `sorted(n, m, p) != (4, 4, 4)`**:
   - **PASS.** `claim/9x13x14_m1039_Z.json` stores explicit bilinear factor matrices `u` (`1039 x 117`), `v` (`1039 x 182`), and `w` (`1039 x 126`) in Perminov JSON format (`n = [9, 13, 14]`, `m = 1039`, file size `907758` bytes, strictly under the `1,000,000`-byte cap). The sorted format `(9, 13, 14)` satisfies `max(9, 13, 14) = 14` (at most 16) and `(9, 13, 14) != (4, 4, 4)`. All `1039` rank-one factor triples are strictly non-zero.
2. **Coefficient class (`ZT` in `{-1, 0, 1}` or `Z` in integers)**:
   - **PASS.** Every coefficient across `u`, `v`, `w` in `claim/9x13x14_m1039_Z.json` is an exact integer in `[-2, -1, 0, 1, 2]` with `max_abs = 2`, matching the claimed integer (Z, coefficients in {-2, -1, 0, 1, 2}) class `Z`.
3. **Condition (1): Rank `r` strictly less than the live `Z` rank in `dronperminov/FastMatrixMultiplication/master/README.md`**:
   - **PASS.** Here `r = 1039`, which is strictly less than the live `Z` column rank `1050` for `9x13x14` in `dronperminov/FastMatrixMultiplication/master/README.md` (saving `11` multiplications, `1039` vs `1050`).
4. **Condition (2): Rank `r` at least `min(ZT, Z, Q)` and at least the live `fmm_sota.json` rank (does NOT beat the overall best rank)**:
   - **PASS.** For `9x13x14`, the live `dronperminov/FastMatrixMultiplication` `README.md` columns are `ZT = 1050`, `Z = 1050`, `Q = 1024` (`min(ZT, Z, Q) = 1024`), and the live `fmm_sota.json` best rank is `1024`. Since `r = 1039` is at least `1024`, the scheme is a genuine ring upgrade and does not beat the overall best rank.
5. **Condition (3): No scheme of rank at most `r` in coefficient class `Z` exists in live `schemes/results/Z` or `MerlijnW70/fmm-schemes`**:
   - **PASS.** Neither `dronperminov/FastMatrixMultiplication` (`schemes/results/ZT` and `schemes/results/Z`) nor `MerlijnW70/fmm-schemes` contains a `Z` scheme for `9x13x14` of rank at most `1039` (live best `Z` rank is `1050`).
6. **Condition (4): Brent equations verified in exact integer arithmetic over `Z`**:
   - **PASS.** Running `claim/verify_z_brent.py` on `claim/9x13x14_m1039_Z.json` verifies all `117 * 182 * 126 = 2683044` Brent equations in exact Python integer arithmetic over `Z` with zero error (not merely modulo 2).
7. **Non-Subsumption & Scope Check**:
   - **PASS.** Only claim for format (9, 13, 14) in this run.

## 2. Confirmed Scope

confirmed_scope: Explicit exact Z bilinear matrix-multiplication scheme in claim/9x13x14_m1039_Z.json (sha256 bed17451925a1e9a484a2848faae3aca36011203fbd9e3277c73d673a8a57daa, 907758 bytes, coefficients in [-2, -1, 0, 1, 2]) for format (9, 13, 14) with rank r = 1039, verified in exact integer arithmetic across all 2683044 Brent equations over Z and strictly beating the live Z rank (1050, saving 11) in dronperminov/FastMatrixMultiplication README.md (ZT = 1050, Z = 1050, Q = 1024) and MerlijnW70/fmm-schemes while remaining at or above the overall best rank (1024 in fmm_sota.json and Q column).

pass: true
