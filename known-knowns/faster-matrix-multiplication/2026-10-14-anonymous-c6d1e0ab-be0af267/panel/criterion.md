# Criterion Skeptic Report: `fmm-additive-complexity-records` — Format `(4, 6, 6)` Rank 105 in 425 Additions over `Z`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed straight-line program artifact `claim/4x6x6_m105_cr425_fv245_cn894_ZT_reduced.json` (SHA-256 `be0af267aac940936b561873f40efc50339eebfb7005fc248a578433ced2cdc4`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_slp.py`, against every literal requirement of `fmm-additive-complexity-records` in `claim/target.md`:

1. **Explicit straight-line program for format `(n1, n2, n3)` with `max(n1, n2, n3)` at most 8 and rank `m` equal to the best rank in `fmm_sota.json`**:
   - **PASS.** `claim/4x6x6_m105_cr425_fv245_cn894_ZT_reduced.json` is an explicit straight-line program for format `(4, 6, 6)` (`4x6x6`), satisfying `max(4, 6, 6) = 6` (at most 8), with bilinear rank `m = 105` matching the best-known rank in `fmm_sota.json` for `4x6x6`. All `m = 105` rows of expanded `U` (width `24`) and `V` (width `36`) and all `24` rows of expanded `W` (width `105`) are strictly non-zero with ternary expanded entries in `{-1, 0, 1}`.
2. **Verified symbolically to compute the full product `A*B` exactly over `Z` with ternary SLP coefficients in `{-1, 1}`**:
   - **PASS.** `claim/4x6x6_m105_cr425_fv245_cn894_ZT_reduced.json` has `z2 = false`. Running `claim/verify_slp.py` confirms that every linear form in `u_fresh` (`63` forms), `u` (`105` forms), `v_fresh` (`72` forms), `v` (`105` forms), `w_fresh` (`110` forms), and `w` (`24` forms) uses only ternary coefficients in `{-1, 1}`, references only strictly preceding variables in an acyclic DAG without duplicate variable indices per form, and shares no variables across `U` (`A`-forms), `V` (`B`-forms), and `W` (product-forms). Symbolic expansion over `Z` confirms zero error across all `(4 * 6 * 6)^2 = 20736` bilinear monomials of `C = A * B`.
3. **Reduced addition count `cr` under Perminov's reduced convention strictly less than all live reference bounds**:
   - **PASS.** Under Perminov's reduced convention (each binary `+/-` in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` counts as `1` addition, i.e., `len(form) - 1`; multiplication by `-1` is free; no other scalar multiplications exist), `claim/verify_slp.py` recounts `cr = 425` additions (`U = 108`, `V = 131`, `W = 186`, matching `complexity.reduced = 425`, with `fv = 245` total fresh variables and `cn = 894` naive additions). Comparing against all live reference sources recorded in `claim/CLAIM.md`:
     - Perminov `addition_reduced_ZT` minimum for `4x6x6` at rank `105`: `cr = 430` (`4x6x6_m105_cr430_fv243_cn894_ZT_reduced.json`), beaten strictly by `-5` additions (`425` vs `430`).
     - Perminov `reduced_known.json` for `4x6x6-105`: `none` (`425` is strictly lower).
     - Perminov `README.md` and `CHANGELOG.md`: no lower reduced addition count for `4x6x6` at rank `105`.
     - `fmm.univ-lille.fr/4x6x6.html`: no complexity variant listed.
     - `solven-eu/matmulcatalog` `COVERAGE.md` `adds` column for `4x6x6`: `+965` (`425` is strictly lower).
4. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only SLP**: Verified symbolically over `Z` (`z2 = false`), not modulo 2.
   - **Not a higher-rank SLP**: Uses the exact catalogue best rank `m = 105`.
   - **Not a rank-lowering claim**: Claims only the additive complexity reduction at fixed rank `m = 105`.
   - **Single format per claim**: This claim folder covers exclusively format `(4, 6, 6)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact integer (ring Z) ternary straight-line program in claim/4x6x6_m105_cr425_fv245_cn894_ZT_reduced.json (sha256 be0af267aac940936b561873f40efc50339eebfb7005fc248a578433ced2cdc4) for format (4, 6, 6) at best-known rank m = 105 with reduced addition count cr = 425 (U = 108, V = 131, W = 186, fv = 245, cn = 894), symbolically verified across all 20736 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (430 in 4x6x6_m105_cr430_fv243_cn894_ZT_reduced.json, margin -5), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/4x6x6.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+965).

pass: true
