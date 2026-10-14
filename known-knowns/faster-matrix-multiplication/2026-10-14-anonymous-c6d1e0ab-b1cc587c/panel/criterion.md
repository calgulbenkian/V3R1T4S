# Criterion Skeptic Report: `fmm-additive-complexity-records` — Format `(3, 5, 5)` Rank 58 in 218 Additions over `Z`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed straight-line program artifact `claim/3x5x5_m58_cr218_fv70_cn357_ZT_reduced.json` (SHA-256 `b1cc587cfcd53662a62995834bb546248b177ba2dd46139fddcb726caf2d46ac`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_slp.py`, against every literal requirement of `fmm-additive-complexity-records` in `claim/target.md`:

1. **Explicit straight-line program for format `(n1, n2, n3)` with `max(n1, n2, n3)` at most 8 and rank `m` equal to the best rank in `fmm_sota.json`**:
   - **PASS.** `claim/3x5x5_m58_cr218_fv70_cn357_ZT_reduced.json` is an explicit straight-line program for format `(3, 5, 5)` (`3x5x5`), satisfying `max(3, 5, 5) = 5` (at most 8), with bilinear rank `m = 58` matching the best-known rank in `fmm_sota.json` for `3x5x5`. All `m = 58` rows of expanded `U` (width `15`) and `V` (width `25`) and all `15` rows of expanded `W` (width `58`) are strictly non-zero with ternary expanded entries in `{-1, 0, 1}`.
2. **Verified symbolically to compute the full product `A*B` exactly over `Z` with ternary SLP coefficients in `{-1, 1}`**:
   - **PASS.** `claim/3x5x5_m58_cr218_fv70_cn357_ZT_reduced.json` has `z2 = false`. Running `claim/verify_slp.py` confirms that every linear form in `u_fresh` (`24` forms), `u` (`58` forms), `v_fresh` (`16` forms), `v` (`58` forms), `w_fresh` (`30` forms), and `w` (`15` forms) uses only ternary coefficients in `{-1, 1}`, references only strictly preceding variables in an acyclic DAG without duplicate variable indices per form, and shares no variables across `U` (`A`-forms), `V` (`B`-forms), and `W` (product-forms). Symbolic expansion over `Z` confirms zero error across all `(3 * 5 * 5)^2 = 5625` bilinear monomials of `C = A * B`.
3. **Reduced addition count `cr` under Perminov's reduced convention strictly less than all live reference bounds**:
   - **PASS.** Under Perminov's reduced convention (each binary `+/-` in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` counts as `1` addition, i.e., `len(form) - 1`; multiplication by `-1` is free; no other scalar multiplications exist), `claim/verify_slp.py` recounts `cr = 218` additions (`U = 52`, `V = 70`, `W = 96`, matching `complexity.reduced = 218`, with `fv = 70` total fresh variables and `cn = 357` naive additions). Comparing against all live reference sources recorded in `claim/CLAIM.md`:
     - Perminov `addition_reduced_ZT` minimum for `3x5x5` at rank `58`: `cr = 221` (`3x5x5_m58_cr221_cn357_ZT_reduced.json`), beaten strictly by `-3` additions (`218` vs `221`).
     - Perminov `reduced_known.json` for `3x5x5-58`: `326 (Z) / 255 (Z2)` (`218` is strictly lower).
     - Perminov `README.md` and `CHANGELOG.md`: no lower reduced addition count for `3x5x5` at rank `58`.
     - `fmm.univ-lille.fr/3x5x5.html`: no complexity variant listed.
     - `solven-eu/matmulcatalog` `COVERAGE.md` `adds` column for `3x5x5`: `+413` (`218` is strictly lower).
4. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only SLP**: Verified symbolically over `Z` (`z2 = false`), not modulo 2.
   - **Not a higher-rank SLP**: Uses the exact catalogue best rank `m = 58`.
   - **Not a rank-lowering claim**: Claims only the additive complexity reduction at fixed rank `m = 58`.
   - **Single format per claim**: This claim folder covers exclusively format `(3, 5, 5)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact integer (ring Z) ternary straight-line program in claim/3x5x5_m58_cr218_fv70_cn357_ZT_reduced.json (sha256 b1cc587cfcd53662a62995834bb546248b177ba2dd46139fddcb726caf2d46ac) for format (3, 5, 5) at best-known rank m = 58 with reduced addition count cr = 218 (U = 52, V = 70, W = 96, fv = 70, cn = 357), symbolically verified across all 5625 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (221 in 3x5x5_m58_cr221_cn357_ZT_reduced.json, margin -3), reduced_known.json (326 (Z) / 255 (Z2)), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/3x5x5.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+413).

pass: true
