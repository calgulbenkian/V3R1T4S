# Criterion Skeptic Report: `fmm-ternary-integer-ring-upgrade` — Format `(4, 13, 15)` Class `Z` at Rank 533

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed bilinear scheme artifact `claim/4x13x15_m533_Z.json` (`337217` bytes, SHA-256 `6083d9f3d15c408b83094f0d8d2f48ce60ecb549856051182174e92f00aa5596`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_z_brent.py`, against every literal requirement of `fmm-ternary-integer-ring-upgrade` in `claim/target.md`:

1. **Explicit bilinear scheme for format `(n, m, p)` with `max(n, m, p)` at most 16 and `sorted(n, m, p) != (4, 4, 4)`**:
   - **PASS.** `claim/4x13x15_m533_Z.json` stores explicit bilinear factor matrices `u` (`533 x 52`), `v` (`533 x 195`), and `w` (`533 x 60`) in Perminov JSON format (`n = [4, 13, 15]`, `m = 533`, file size `337217` bytes, strictly under the `1,000,000`-byte cap). The sorted format `(4, 13, 15)` satisfies `max(4, 13, 15) = 15` (at most 16) and `(4, 13, 15) != (4, 4, 4)`. All `533` rank-one factor triples are strictly non-zero.
2. **Coefficient class (`ZT` in `{-1, 0, 1}` or `Z` in integers)**:
   - **PASS.** Every coefficient across `u`, `v`, `w` in `claim/4x13x15_m533_Z.json` is an exact integer in `[-2, -1, 0, 1]` with `max_abs = 2`, matching the claimed integer (Z, coefficients in {-2, -1, 0, 1}) class `Z`.
3. **Condition (1): Rank `r` strictly less than the live `Z` rank in `dronperminov/FastMatrixMultiplication/master/README.md`**:
   - **PASS.** Here `r = 533`, which is strictly less than the live `Z` column rank `536` for `4x13x15` in `dronperminov/FastMatrixMultiplication/master/README.md` (saving `3` multiplications, `533` vs `536`).
4. **Condition (2): Rank `r` at least `min(ZT, Z, Q)` and at least the live `fmm_sota.json` rank (does NOT beat the overall best rank)**:
   - **PASS.** For `4x13x15`, the live `dronperminov/FastMatrixMultiplication` `README.md` columns are `ZT = 536`, `Z = 536`, `Q = 520` (`min(ZT, Z, Q) = 520`), and the live `fmm_sota.json` best rank is `520`. Since `r = 533` is at least `520`, the scheme is a genuine ring upgrade and does not beat the overall best rank.
5. **Condition (3): No scheme of rank at most `r` in coefficient class `Z` exists in live `schemes/results/Z` or `MerlijnW70/fmm-schemes`**:
   - **PASS.** Neither `dronperminov/FastMatrixMultiplication` (`schemes/results/ZT` and `schemes/results/Z`) nor `MerlijnW70/fmm-schemes` contains a `Z` scheme for `4x13x15` of rank at most `533` (live best `Z` rank is `536`).
6. **Condition (4): Brent equations verified in exact integer arithmetic over `Z`**:
   - **PASS.** Running `claim/verify_z_brent.py` on `claim/4x13x15_m533_Z.json` verifies all `52 * 195 * 60 = 608400` Brent equations in exact Python integer arithmetic over `Z` with zero error (not merely modulo 2).
7. **Non-Subsumption & Scope Check**:
   - **PASS.** Distinct from the ternary (class ZT) rank-535 claim for (4, 13, 15) because this scheme achieves strictly lower rank r = 533 in integer class Z (max_abs = 2).

## 2. Confirmed Scope

confirmed_scope: Explicit exact Z bilinear matrix-multiplication scheme in claim/4x13x15_m533_Z.json (sha256 6083d9f3d15c408b83094f0d8d2f48ce60ecb549856051182174e92f00aa5596, 337217 bytes, coefficients in [-2, -1, 0, 1]) for format (4, 13, 15) with rank r = 533, verified in exact integer arithmetic across all 608400 Brent equations over Z and strictly beating the live Z rank (536, saving 3) in dronperminov/FastMatrixMultiplication README.md (ZT = 536, Z = 536, Q = 520) and MerlijnW70/fmm-schemes while remaining at or above the overall best rank (520 in fmm_sota.json and Q column).

pass: true
