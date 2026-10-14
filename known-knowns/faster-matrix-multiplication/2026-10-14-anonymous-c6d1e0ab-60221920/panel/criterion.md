# Criterion Skeptic Report: `fmm-additive-complexity-records` — Format `(4, 5, 6)` Rank 90 in 374 Additions over `Z`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed straight-line program artifact `claim/4x5x6_m90_cr374_fv179_cn1008_ZT_reduced.json` (SHA-256 `60221920dc02e9a5198d6df81dbafa70f481f0367db9600fe418b21dc220584a`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_slp.py`, against every literal requirement of `fmm-additive-complexity-records` in `claim/target.md`:

1. **Explicit straight-line program for format `(n1, n2, n3)` with `max(n1, n2, n3)` at most 8 and rank `m` equal to the best rank in `fmm_sota.json`**:
   - **PASS.** `claim/4x5x6_m90_cr374_fv179_cn1008_ZT_reduced.json` is an explicit straight-line program for format `(4, 5, 6)` (`4x5x6`), satisfying `max(4, 5, 6) = 6` (at most 8), with bilinear rank `m = 90` matching the best-known rank in `fmm_sota.json` for `4x5x6`. All `m = 90` rows of expanded `U` (width `20`) and `V` (width `30`) and all `24` rows of expanded `W` (width `90`) are strictly non-zero with ternary expanded entries in `{-1, 0, 1}`.
2. **Verified symbolically to compute the full product `A*B` exactly over `Z` with ternary SLP coefficients in `{-1, 1}`**:
   - **PASS.** `claim/4x5x6_m90_cr374_fv179_cn1008_ZT_reduced.json` has `z2 = false`. Running `claim/verify_slp.py` confirms that every linear form in `u_fresh` (`40` forms), `u` (`90` forms), `v_fresh` (`52` forms), `v` (`90` forms), `w_fresh` (`87` forms), and `w` (`24` forms) uses only ternary coefficients in `{-1, 1}`, references only strictly preceding variables in an acyclic DAG without duplicate variable indices per form, and shares no variables across `U` (`A`-forms), `V` (`B`-forms), and `W` (product-forms). Symbolic expansion over `Z` confirms zero error across all `(4 * 5 * 6)^2 = 14400` bilinear monomials of `C = A * B`.
3. **Reduced addition count `cr` under Perminov's reduced convention strictly less than all live reference bounds**:
   - **PASS.** Under Perminov's reduced convention (each binary `+/-` in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` counts as `1` addition, i.e., `len(form) - 1`; multiplication by `-1` is free; no other scalar multiplications exist), `claim/verify_slp.py` recounts `cr = 374` additions (`U = 86`, `V = 114`, `W = 174`, matching `complexity.reduced = 374`, with `fv = 179` total fresh variables and `cn = 1008` naive additions). Comparing against all live reference sources recorded in `claim/CLAIM.md`:
     - Perminov `addition_reduced_ZT` minimum for `4x5x6` at rank `90`: `cr = 380` (`4x5x6_m90_cr380_fv180_cn1023_ZT_reduced.json`), beaten strictly by `-6` additions (`374` vs `380`).
     - Perminov `reduced_known.json` for `4x5x6-90`: `none` (`374` is strictly lower).
     - Perminov `README.md` and `CHANGELOG.md`: no lower reduced addition count for `4x5x6` at rank `90`.
     - `fmm.univ-lille.fr/4x5x6.html`: no complexity variant listed.
     - `solven-eu/matmulcatalog` `COVERAGE.md` `adds` column for `4x5x6`: `+775` (`374` is strictly lower).
4. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only SLP**: Verified symbolically over `Z` (`z2 = false`), not modulo 2.
   - **Not a higher-rank SLP**: Uses the exact catalogue best rank `m = 90`.
   - **Not a rank-lowering claim**: Claims only the additive complexity reduction at fixed rank `m = 90`.
   - **Single format per claim**: This claim folder covers exclusively format `(4, 5, 6)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact integer (ring Z) ternary straight-line program in claim/4x5x6_m90_cr374_fv179_cn1008_ZT_reduced.json (sha256 60221920dc02e9a5198d6df81dbafa70f481f0367db9600fe418b21dc220584a) for format (4, 5, 6) at best-known rank m = 90 with reduced addition count cr = 374 (U = 86, V = 114, W = 174, fv = 179, cn = 1008), symbolically verified across all 14400 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (380 in 4x5x6_m90_cr380_fv180_cn1023_ZT_reduced.json, margin -6), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/4x5x6.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+775).

pass: true
