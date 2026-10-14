# Criterion Skeptic Report: `fmm-additive-complexity-records` — Format `(5, 5, 5)` Rank 93 in 378 Additions over `Z`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed straight-line program artifact `claim/5x5x5_m93_cr378_fv157_cn844_ZT_reduced.json` (SHA-256 `118237670d742163d9f8caa3fd4e5c6a850fe9570fbb39ce3f32906b427c2a4a`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_slp.py`, against every literal requirement of `fmm-additive-complexity-records` in `claim/target.md`:

1. **Explicit straight-line program for format `(n1, n2, n3)` with `max(n1, n2, n3)` at most 8 and rank `m` equal to the best rank in `fmm_sota.json`**:
   - **PASS.** `claim/5x5x5_m93_cr378_fv157_cn844_ZT_reduced.json` is an explicit straight-line program for format `(5, 5, 5)` (`5x5x5`), satisfying `max(5, 5, 5) = 5` (at most 8), with bilinear rank `m = 93` matching the best-known rank in `fmm_sota.json` for `5x5x5`. All `m = 93` rows of expanded `U` (width `25`) and `V` (width `25`) and all `25` rows of expanded `W` (width `93`) are strictly non-zero with ternary expanded entries in `{-1, 0, 1}`.
2. **Verified symbolically to compute the full product `A*B` exactly over `Z` with ternary SLP coefficients in `{-1, 1}`**:
   - **PASS.** `claim/5x5x5_m93_cr378_fv157_cn844_ZT_reduced.json` has `z2 = false`. Running `claim/verify_slp.py` confirms that every linear form in `u_fresh` (`44` forms), `u` (`93` forms), `v_fresh` (`44` forms), `v` (`93` forms), `w_fresh` (`69` forms), and `w` (`25` forms) uses only ternary coefficients in `{-1, 1}`, references only strictly preceding variables in an acyclic DAG without duplicate variable indices per form, and shares no variables across `U` (`A`-forms), `V` (`B`-forms), and `W` (product-forms). Symbolic expansion over `Z` confirms zero error across all `(5 * 5 * 5)^2 = 15625` bilinear monomials of `C = A * B`.
3. **Reduced addition count `cr` under Perminov's reduced convention strictly less than all live reference bounds**:
   - **PASS.** Under Perminov's reduced convention (each binary `+/-` in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` counts as `1` addition, i.e., `len(form) - 1`; multiplication by `-1` is free; no other scalar multiplications exist), `claim/verify_slp.py` recounts `cr = 378` additions (`U = 100`, `V = 103`, `W = 175`, matching `complexity.reduced = 378`, with `fv = 157` total fresh variables and `cn = 844` naive additions). Comparing against all live reference sources recorded in `claim/CLAIM.md`:
     - Perminov `addition_reduced_ZT` minimum for `5x5x5` at rank `93`: `cr = 383` (`5x5x5_m93_cr383_fv160_cn843_ZT_reduced.json`), beaten strictly by `-5` additions (`378` vs `383`).
     - Perminov `reduced_known.json` for `5x5x5-93`: `none` (`378` is strictly lower).
     - Perminov `README.md` and `CHANGELOG.md`: no lower reduced addition count for `5x5x5` at rank `93`.
     - `fmm.univ-lille.fr/5x5x5.html`: no complexity variant listed.
     - `solven-eu/matmulcatalog` `COVERAGE.md` `adds` column for `5x5x5`: `+846` (`378` is strictly lower).
4. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only SLP**: Verified symbolically over `Z` (`z2 = false`), not modulo 2.
   - **Not a higher-rank SLP**: Uses the exact catalogue best rank `m = 93`.
   - **Not a rank-lowering claim**: Claims only the additive complexity reduction at fixed rank `m = 93`.
   - **Single format per claim**: This claim folder covers exclusively format `(5, 5, 5)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact integer (ring Z) ternary straight-line program in claim/5x5x5_m93_cr378_fv157_cn844_ZT_reduced.json (sha256 118237670d742163d9f8caa3fd4e5c6a850fe9570fbb39ce3f32906b427c2a4a) for format (5, 5, 5) at best-known rank m = 93 with reduced addition count cr = 378 (U = 100, V = 103, W = 175, fv = 157, cn = 844), symbolically verified across all 15625 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (383 in 5x5x5_m93_cr383_fv160_cn843_ZT_reduced.json, margin -5), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/5x5x5.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+846).

pass: true
