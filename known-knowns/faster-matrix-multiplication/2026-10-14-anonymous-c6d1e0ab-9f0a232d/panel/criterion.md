# Criterion Skeptic Report: `fmm-ternary-integer-ring-upgrade` — Format `(7, 8, 15)` Class `Z` at Rank 570

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed bilinear scheme artifact `claim/7x8x15_m570_Z.json` (`330024` bytes, SHA-256 `9f0a232de00ce5220d75097b9af6986f97d81932fa3e3718e1291d426f4caede`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_z_brent.py`, against every literal requirement of `fmm-ternary-integer-ring-upgrade` in `claim/target.md`:

1. **Explicit bilinear scheme for format `(n, m, p)` with `max(n, m, p)` at most 16 and `sorted(n, m, p) != (4, 4, 4)`**:
   - **PASS.** `claim/7x8x15_m570_Z.json` stores explicit bilinear factor matrices `u` (`570 x 56`), `v` (`570 x 120`), and `w` (`570 x 105`) in Perminov JSON format (`n = [7, 8, 15]`, `m = 570`, file size `330024` bytes, strictly under the `1,000,000`-byte cap). The sorted format `(7, 8, 15)` satisfies `max(7, 8, 15) = 15` (at most 16) and `(7, 8, 15) != (4, 4, 4)`. All `570` rank-one factor triples are strictly non-zero.
2. **Coefficient class (`ZT` in `{-1, 0, 1}` or `Z` in integers)**:
   - **PASS.** Every coefficient across `u`, `v`, `w` in `claim/7x8x15_m570_Z.json` is an exact integer in `[-2, -1, 0, 1, 2]` with `max_abs = 2`, matching the claimed integer (Z, coefficients in {-2, -1, 0, 1, 2}) class `Z`.
3. **Condition (1): Rank `r` strictly less than the live `Z` rank in `dronperminov/FastMatrixMultiplication/master/README.md`**:
   - **PASS.** Here `r = 570`, which is strictly less than the live `Z` column rank `571` for `7x8x15` in `dronperminov/FastMatrixMultiplication/master/README.md` (saving `1` multiplications, `570` vs `571`).
4. **Condition (2): Rank `r` at least `min(ZT, Z, Q)` and at least the live `fmm_sota.json` rank (does NOT beat the overall best rank)**:
   - **PASS.** For `7x8x15`, the live `dronperminov/FastMatrixMultiplication` `README.md` columns are `ZT = 571`, `Z = 571`, `Q = 557` (`min(ZT, Z, Q) = 557`), and the live `fmm_sota.json` best rank is `557`. Since `r = 570` is at least `557`, the scheme is a genuine ring upgrade and does not beat the overall best rank.
5. **Condition (3): No scheme of rank at most `r` in coefficient class `Z` exists in live `schemes/results/Z` or `MerlijnW70/fmm-schemes`**:
   - **PASS.** Neither `dronperminov/FastMatrixMultiplication` (`schemes/results/ZT` and `schemes/results/Z`) nor `MerlijnW70/fmm-schemes` contains a `Z` scheme for `7x8x15` of rank at most `570` (live best `Z` rank is `571`).
6. **Condition (4): Brent equations verified in exact integer arithmetic over `Z`**:
   - **PASS.** Running `claim/verify_z_brent.py` on `claim/7x8x15_m570_Z.json` verifies all `56 * 120 * 105 = 705600` Brent equations in exact Python integer arithmetic over `Z` with zero error (not merely modulo 2).
7. **Non-Subsumption & Scope Check**:
   - **PASS.** Only claim for format (7, 8, 15) in this run.

## 2. Confirmed Scope

confirmed_scope: Explicit exact Z bilinear matrix-multiplication scheme in claim/7x8x15_m570_Z.json (sha256 9f0a232de00ce5220d75097b9af6986f97d81932fa3e3718e1291d426f4caede, 330024 bytes, coefficients in [-2, -1, 0, 1, 2]) for format (7, 8, 15) with rank r = 570, verified in exact integer arithmetic across all 705600 Brent equations over Z and strictly beating the live Z rank (571, saving 1) in dronperminov/FastMatrixMultiplication README.md (ZT = 571, Z = 571, Q = 557) and MerlijnW70/fmm-schemes while remaining at or above the overall best rank (557 in fmm_sota.json and Q column).

pass: true
