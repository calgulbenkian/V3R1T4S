# Criterion Skeptic Report: `fmm-additive-complexity-records` — Format `(5, 5, 6)` Rank 110 in 451 Additions over `Z`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed straight-line program artifact `claim/5x5x6_m110_cr451_fv202_cn1208_ZT_reduced.json` (SHA-256 `4f95dd2dbee2b93b8c8e102b863438193c7d6a5b899fcd0ec5a35661c115cd5d`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_slp.py`, against every literal requirement of `fmm-additive-complexity-records` in `claim/target.md`:

1. **Explicit straight-line program for format `(n1, n2, n3)` with `max(n1, n2, n3)` at most 8 and rank `m` equal to the best rank in `fmm_sota.json`**:
   - **PASS.** `claim/5x5x6_m110_cr451_fv202_cn1208_ZT_reduced.json` is an explicit straight-line program for format `(5, 5, 6)` (`5x5x6`), satisfying `max(5, 5, 6) = 6` (at most 8), with bilinear rank `m = 110` matching the best-known rank in `fmm_sota.json` for `5x5x6`. All `m = 110` rows of expanded `U` (width `25`) and `V` (width `30`) and all `30` rows of expanded `W` (width `110`) are strictly non-zero with ternary expanded entries in `{-1, 0, 1}`.
2. **Verified symbolically to compute the full product `A*B` exactly over `Z` with ternary SLP coefficients in `{-1, 1}`**:
   - **PASS.** `claim/5x5x6_m110_cr451_fv202_cn1208_ZT_reduced.json` has `z2 = false`. Running `claim/verify_slp.py` confirms that every linear form in `u_fresh` (`48` forms), `u` (`110` forms), `v_fresh` (`56` forms), `v` (`110` forms), `w_fresh` (`98` forms), and `w` (`30` forms) uses only ternary coefficients in `{-1, 1}`, references only strictly preceding variables in an acyclic DAG without duplicate variable indices per form, and shares no variables across `U` (`A`-forms), `V` (`B`-forms), and `W` (product-forms). Symbolic expansion over `Z` confirms zero error across all `(5 * 5 * 6)^2 = 22500` bilinear monomials of `C = A * B`.
3. **Reduced addition count `cr` under Perminov's reduced convention strictly less than all live reference bounds**:
   - **PASS.** Under Perminov's reduced convention (each binary `+/-` in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` counts as `1` addition, i.e., `len(form) - 1`; multiplication by `-1` is free; no other scalar multiplications exist), `claim/verify_slp.py` recounts `cr = 451` additions (`U = 119`, `V = 124`, `W = 208`, matching `complexity.reduced = 451`, with `fv = 202` total fresh variables and `cn = 1208` naive additions). Comparing against all live reference sources recorded in `claim/CLAIM.md`:
     - Perminov `addition_reduced_ZT` minimum for `5x5x6` at rank `110`: `cr = 460` (`5x5x6_m110_cr460_fv204_cn1215_ZT_reduced.json`), beaten strictly by `-9` additions (`451` vs `460`).
     - Perminov `reduced_known.json` for `5x5x6-110`: `none` (`451` is strictly lower).
     - Perminov `README.md` and `CHANGELOG.md`: no lower reduced addition count for `5x5x6` at rank `110`.
     - `fmm.univ-lille.fr/5x5x6.html`: no complexity variant listed.
     - `solven-eu/matmulcatalog` `COVERAGE.md` `adds` column for `5x5x6`: `+1215` (`451` is strictly lower).
4. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only SLP**: Verified symbolically over `Z` (`z2 = false`), not modulo 2.
   - **Not a higher-rank SLP**: Uses the exact catalogue best rank `m = 110`.
   - **Not a rank-lowering claim**: Claims only the additive complexity reduction at fixed rank `m = 110`.
   - **Single format per claim**: This claim folder covers exclusively format `(5, 5, 6)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact integer (ring Z) ternary straight-line program in claim/5x5x6_m110_cr451_fv202_cn1208_ZT_reduced.json (sha256 4f95dd2dbee2b93b8c8e102b863438193c7d6a5b899fcd0ec5a35661c115cd5d) for format (5, 5, 6) at best-known rank m = 110 with reduced addition count cr = 451 (U = 119, V = 124, W = 208, fv = 202, cn = 1208), symbolically verified across all 22500 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (460 in 5x5x6_m110_cr460_fv204_cn1215_ZT_reduced.json, margin -9), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/5x5x6.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+1215).

pass: true
