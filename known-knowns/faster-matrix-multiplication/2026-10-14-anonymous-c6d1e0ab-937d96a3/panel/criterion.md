# Criterion Skeptic Report: `fmm-ternary-integer-ring-upgrade` — Format `(4, 13, 15)` Class `ZT` at Rank 535

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed bilinear scheme artifact `claim/4x13x15_m535_ZT.json` (`338479` bytes, SHA-256 `937d96a3adc5b64e84e86d8a0d9bc0b7e160f22f00f3ca4af7239abb76a281f2`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_z_brent.py`, against every literal requirement of `fmm-ternary-integer-ring-upgrade` in `claim/target.md`:

1. **Explicit bilinear scheme for format `(n, m, p)` with `max(n, m, p)` at most 16 and `sorted(n, m, p) != (4, 4, 4)`**:
   - **PASS.** `claim/4x13x15_m535_ZT.json` stores explicit bilinear factor matrices `u` (`535 x 52`), `v` (`535 x 195`), and `w` (`535 x 60`) in Perminov JSON format (`n = [4, 13, 15]`, `m = 535`, file size `338479` bytes, strictly under the `1,000,000`-byte cap). The sorted format `(4, 13, 15)` satisfies `max(4, 13, 15) = 15` (at most 16) and `(4, 13, 15) != (4, 4, 4)`. All `535` rank-one factor triples are strictly non-zero.
2. **Coefficient class (`ZT` in `{-1, 0, 1}` or `Z` in integers)**:
   - **PASS.** Every coefficient across `u`, `v`, `w` in `claim/4x13x15_m535_ZT.json` is an exact integer in `[-1, 0, 1]` with `max_abs = 1`, matching the claimed ternary (ZT, coefficients in {-1, 0, 1}) class `ZT`.
3. **Condition (1): Rank `r` strictly less than the live `ZT` rank in `dronperminov/FastMatrixMultiplication/master/README.md`**:
   - **PASS.** Here `r = 535`, which is strictly less than the live `ZT` column rank `536` for `4x13x15` in `dronperminov/FastMatrixMultiplication/master/README.md` (saving `1` multiplications, `535` vs `536`).
4. **Condition (2): Rank `r` at least `min(ZT, Z, Q)` and at least the live `fmm_sota.json` rank (does NOT beat the overall best rank)**:
   - **PASS.** For `4x13x15`, the live `dronperminov/FastMatrixMultiplication` `README.md` columns are `ZT = 536`, `Z = 536`, `Q = 520` (`min(ZT, Z, Q) = 520`), and the live `fmm_sota.json` best rank is `520`. Since `r = 535` is at least `520`, the scheme is a genuine ring upgrade and does not beat the overall best rank.
5. **Condition (3): No scheme of rank at most `r` in coefficient class `ZT` exists in live `schemes/results/ZT` or `MerlijnW70/fmm-schemes`**:
   - **PASS.** Neither `dronperminov/FastMatrixMultiplication` (`schemes/results/ZT` and `schemes/results/Z`) nor `MerlijnW70/fmm-schemes` contains a `ZT` scheme for `4x13x15` of rank at most `535` (live best `ZT` rank is `536`).
6. **Condition (4): Brent equations verified in exact integer arithmetic over `Z`**:
   - **PASS.** Running `claim/verify_z_brent.py` on `claim/4x13x15_m535_ZT.json` verifies all `52 * 195 * 60 = 608400` Brent equations in exact Python integer arithmetic over `Z` with zero error (not merely modulo 2).
7. **Non-Subsumption & Scope Check**:
   - **PASS.** Distinct from the integer (class Z) rank-533 claim for (4, 13, 15) because class ZT restricts coefficients to {-1, 0, 1} whereas the rank-533 scheme uses coefficient -2.

## 2. Confirmed Scope

confirmed_scope: Explicit exact ZT bilinear matrix-multiplication scheme in claim/4x13x15_m535_ZT.json (sha256 937d96a3adc5b64e84e86d8a0d9bc0b7e160f22f00f3ca4af7239abb76a281f2, 338479 bytes, coefficients in [-1, 0, 1]) for format (4, 13, 15) with rank r = 535, verified in exact integer arithmetic across all 608400 Brent equations over Z and strictly beating the live ZT rank (536, saving 1) in dronperminov/FastMatrixMultiplication README.md (ZT = 536, Z = 536, Q = 520) and MerlijnW70/fmm-schemes while remaining at or above the overall best rank (520 in fmm_sota.json and Q column).

pass: true
