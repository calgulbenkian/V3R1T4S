# Criterion Skeptic Report: `fmm-ternary-integer-ring-upgrade` — Format `(9, 11, 14)` Class `Z` at Rank 889

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed bilinear scheme artifact `claim/9x11x14_m889_Z.json` (`693112` bytes, SHA-256 `e25137a39f9a642d3a93ae58337d80703f5e45c2efc48e96207d7e61aeb101e5`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_z_brent.py`, against every literal requirement of `fmm-ternary-integer-ring-upgrade` in `claim/target.md`:

1. **Explicit bilinear scheme for format `(n, m, p)` with `max(n, m, p)` at most 16 and `sorted(n, m, p) != (4, 4, 4)`**:
   - **PASS.** `claim/9x11x14_m889_Z.json` stores explicit bilinear factor matrices `u` (`889 x 99`), `v` (`889 x 154`), and `w` (`889 x 126`) in Perminov JSON format (`n = [9, 11, 14]`, `m = 889`, file size `693112` bytes, strictly under the `1,000,000`-byte cap). The sorted format `(9, 11, 14)` satisfies `max(9, 11, 14) = 14` (at most 16) and `(9, 11, 14) != (4, 4, 4)`. All `889` rank-one factor triples are strictly non-zero.
2. **Coefficient class (`ZT` in `{-1, 0, 1}` or `Z` in integers)**:
   - **PASS.** Every coefficient across `u`, `v`, `w` in `claim/9x11x14_m889_Z.json` is an exact integer in `[-2, -1, 0, 1, 2]` with `max_abs = 2`, matching the claimed integer (Z, coefficients in {-2, -1, 0, 1, 2}) class `Z`.
3. **Condition (1): Rank `r` strictly less than the live `Z` rank in `dronperminov/FastMatrixMultiplication/master/README.md`**:
   - **PASS.** Here `r = 889`, which is strictly less than the live `Z` column rank `900` for `9x11x14` in `dronperminov/FastMatrixMultiplication/master/README.md` (saving `11` multiplications, `889` vs `900`).
4. **Condition (2): Rank `r` at least `min(ZT, Z, Q)` and at least the live `fmm_sota.json` rank (does NOT beat the overall best rank)**:
   - **PASS.** For `9x11x14`, the live `dronperminov/FastMatrixMultiplication` `README.md` columns are `ZT = 900`, `Z = 900`, `Q = 882` (`min(ZT, Z, Q) = 882`), and the live `fmm_sota.json` best rank is `882`. Since `r = 889` is at least `882`, the scheme is a genuine ring upgrade and does not beat the overall best rank.
5. **Condition (3): No scheme of rank at most `r` in coefficient class `Z` exists in live `schemes/results/Z` or `MerlijnW70/fmm-schemes`**:
   - **PASS.** Neither `dronperminov/FastMatrixMultiplication` (`schemes/results/ZT` and `schemes/results/Z`) nor `MerlijnW70/fmm-schemes` contains a `Z` scheme for `9x11x14` of rank at most `889` (live best `Z` rank is `900`).
6. **Condition (4): Brent equations verified in exact integer arithmetic over `Z`**:
   - **PASS.** Running `claim/verify_z_brent.py` on `claim/9x11x14_m889_Z.json` verifies all `99 * 154 * 126 = 1920996` Brent equations in exact Python integer arithmetic over `Z` with zero error (not merely modulo 2).
7. **Non-Subsumption & Scope Check**:
   - **PASS.** Only claim for format (9, 11, 14) in this run.

## 2. Confirmed Scope

confirmed_scope: Explicit exact Z bilinear matrix-multiplication scheme in claim/9x11x14_m889_Z.json (sha256 e25137a39f9a642d3a93ae58337d80703f5e45c2efc48e96207d7e61aeb101e5, 693112 bytes, coefficients in [-2, -1, 0, 1, 2]) for format (9, 11, 14) with rank r = 889, verified in exact integer arithmetic across all 1920996 Brent equations over Z and strictly beating the live Z rank (900, saving 11) in dronperminov/FastMatrixMultiplication README.md (ZT = 900, Z = 900, Q = 882) and MerlijnW70/fmm-schemes while remaining at or above the overall best rank (882 in fmm_sota.json and Q column).

pass: true
