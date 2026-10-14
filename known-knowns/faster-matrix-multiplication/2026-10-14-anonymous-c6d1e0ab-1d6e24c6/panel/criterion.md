# Criterion Skeptic Report: `fmm-additive-complexity-records` — Format `(5, 5, 7)` Rank 127 in 525 Additions over `Z`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed straight-line program artifact `claim/5x5x7_m127_cr525_fv245_cn1602_ZT_reduced.json` (SHA-256 `1d6e24c6edebc809e6d6cfa7a3ecfec0f9b00550ebcf92c3289d510eb1f091fd`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_slp.py`, against every literal requirement of `fmm-additive-complexity-records` in `claim/target.md`:

1. **Explicit straight-line program for format `(n1, n2, n3)` with `max(n1, n2, n3)` at most 8 and rank `m` equal to the best rank in `fmm_sota.json`**:
   - **PASS.** `claim/5x5x7_m127_cr525_fv245_cn1602_ZT_reduced.json` is an explicit straight-line program for format `(5, 5, 7)` (`5x5x7`), satisfying `max(5, 5, 7) = 7` (at most 8), with bilinear rank `m = 127` matching the best-known rank in `fmm_sota.json` for `5x5x7`. All `m = 127` rows of expanded `U` (width `25`) and `V` (width `35`) and all `35` rows of expanded `W` (width `127`) are strictly non-zero with ternary expanded entries in `{-1, 0, 1}`.
2. **Verified symbolically to compute the full product `A*B` exactly over `Z` with ternary SLP coefficients in `{-1, 1}`**:
   - **PASS.** `claim/5x5x7_m127_cr525_fv245_cn1602_ZT_reduced.json` has `z2 = false`. Running `claim/verify_slp.py` confirms that every linear form in `u_fresh` (`60` forms), `u` (`127` forms), `v_fresh` (`65` forms), `v` (`127` forms), `w_fresh` (`120` forms), and `w` (`35` forms) uses only ternary coefficients in `{-1, 1}`, references only strictly preceding variables in an acyclic DAG without duplicate variable indices per form, and shares no variables across `U` (`A`-forms), `V` (`B`-forms), and `W` (product-forms). Symbolic expansion over `Z` confirms zero error across all `(5 * 5 * 7)^2 = 30625` bilinear monomials of `C = A * B`.
3. **Reduced addition count `cr` under Perminov's reduced convention strictly less than all live reference bounds**:
   - **PASS.** Under Perminov's reduced convention (each binary `+/-` in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` counts as `1` addition, i.e., `len(form) - 1`; multiplication by `-1` is free; no other scalar multiplications exist), `claim/verify_slp.py` recounts `cr = 525` additions (`U = 127`, `V = 150`, `W = 248`, matching `complexity.reduced = 525`, with `fv = 245` total fresh variables and `cn = 1602` naive additions). Comparing against all live reference sources recorded in `claim/CLAIM.md`:
     - Perminov `addition_reduced_ZT` minimum for `5x5x7` at rank `127`: `cr = 531` (`5x5x7_m127_cr531_fv245_cn1607_ZT_reduced.json`), beaten strictly by `-6` additions (`525` vs `531`).
     - Perminov `reduced_known.json` for `5x5x7-127`: `none` (`525` is strictly lower).
     - Perminov `README.md` and `CHANGELOG.md`: no lower reduced addition count for `5x5x7` at rank `127`.
     - `fmm.univ-lille.fr/5x5x7.html`: no complexity variant listed.
     - `solven-eu/matmulcatalog` `COVERAGE.md` `adds` column for `5x5x7`: `+1606` (`525` is strictly lower).
4. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only SLP**: Verified symbolically over `Z` (`z2 = false`), not modulo 2.
   - **Not a higher-rank SLP**: Uses the exact catalogue best rank `m = 127`.
   - **Not a rank-lowering claim**: Claims only the additive complexity reduction at fixed rank `m = 127`.
   - **Single format per claim**: This claim folder covers exclusively format `(5, 5, 7)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact integer (ring Z) ternary straight-line program in claim/5x5x7_m127_cr525_fv245_cn1602_ZT_reduced.json (sha256 1d6e24c6edebc809e6d6cfa7a3ecfec0f9b00550ebcf92c3289d510eb1f091fd) for format (5, 5, 7) at best-known rank m = 127 with reduced addition count cr = 525 (U = 127, V = 150, W = 248, fv = 245, cn = 1602), symbolically verified across all 30625 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (531 in 5x5x7_m127_cr531_fv245_cn1607_ZT_reduced.json, margin -6), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/5x5x7.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+1606).

pass: true
