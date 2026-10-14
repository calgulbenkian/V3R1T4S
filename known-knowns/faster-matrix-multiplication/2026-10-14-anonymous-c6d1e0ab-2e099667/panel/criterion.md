# Criterion Skeptic Report: `fmm-additive-complexity-records` — Format `(4, 5, 5)` Rank 76 in 295 Additions over `Z`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed straight-line program artifact `claim/4x5x5_m76_cr295_fv113_cn530_ZT_reduced.json` (SHA-256 `2e09966726d94ad6ade2c53de92b73c0e2f78a2d39d2a4a52f50a0e61eef085d`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_slp.py`, against every literal requirement of `fmm-additive-complexity-records` in `claim/target.md`:

1. **Explicit straight-line program for format `(n1, n2, n3)` with `max(n1, n2, n3)` at most 8 and rank `m` equal to the best rank in `fmm_sota.json`**:
   - **PASS.** `claim/4x5x5_m76_cr295_fv113_cn530_ZT_reduced.json` is an explicit straight-line program for format `(4, 5, 5)` (`4x5x5`), satisfying `max(4, 5, 5) = 5` (at most 8), with bilinear rank `m = 76` matching the best-known rank in `fmm_sota.json` for `4x5x5`. All `m = 76` rows of expanded `U` (width `20`) and `V` (width `25`) and all `20` rows of expanded `W` (width `76`) are strictly non-zero with ternary expanded entries in `{-1, 0, 1}`.
2. **Verified symbolically to compute the full product `A*B` exactly over `Z` with ternary SLP coefficients in `{-1, 1}`**:
   - **PASS.** `claim/4x5x5_m76_cr295_fv113_cn530_ZT_reduced.json` has `z2 = false`. Running `claim/verify_slp.py` confirms that every linear form in `u_fresh` (`40` forms), `u` (`76` forms), `v_fresh` (`35` forms), `v` (`76` forms), `w_fresh` (`38` forms), and `w` (`20` forms) uses only ternary coefficients in `{-1, 1}`, references only strictly preceding variables in an acyclic DAG without duplicate variable indices per form, and shares no variables across `U` (`A`-forms), `V` (`B`-forms), and `W` (product-forms). Symbolic expansion over `Z` confirms zero error across all `(4 * 5 * 5)^2 = 10000` bilinear monomials of `C = A * B`.
3. **Reduced addition count `cr` under Perminov's reduced convention strictly less than all live reference bounds**:
   - **PASS.** Under Perminov's reduced convention (each binary `+/-` in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` counts as `1` addition, i.e., `len(form) - 1`; multiplication by `-1` is free; no other scalar multiplications exist), `claim/verify_slp.py` recounts `cr = 295` additions (`U = 76`, `V = 89`, `W = 130`, matching `complexity.reduced = 295`, with `fv = 113` total fresh variables and `cn = 530` naive additions). Comparing against all live reference sources recorded in `claim/CLAIM.md`:
     - Perminov `addition_reduced_ZT` minimum for `4x5x5` at rank `76`: `cr = 299` (`4x5x5_m76_cr299_fv112_cn530_ZT_reduced.json`), beaten strictly by `-4` additions (`295` vs `299`).
     - Perminov `reduced_known.json` for `4x5x5-76`: `451 (Z) / 372 (Z2)` (`295` is strictly lower).
     - Perminov `README.md` and `CHANGELOG.md`: no lower reduced addition count for `4x5x5` at rank `76`.
     - `fmm.univ-lille.fr/4x5x5.html`: no complexity variant listed.
     - `solven-eu/matmulcatalog` `COVERAGE.md` `adds` column for `4x5x5`: `+549` (`295` is strictly lower).
4. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only SLP**: Verified symbolically over `Z` (`z2 = false`), not modulo 2.
   - **Not a higher-rank SLP**: Uses the exact catalogue best rank `m = 76`.
   - **Not a rank-lowering claim**: Claims only the additive complexity reduction at fixed rank `m = 76`.
   - **Single format per claim**: This claim folder covers exclusively format `(4, 5, 5)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact integer (ring Z) ternary straight-line program in claim/4x5x5_m76_cr295_fv113_cn530_ZT_reduced.json (sha256 2e09966726d94ad6ade2c53de92b73c0e2f78a2d39d2a4a52f50a0e61eef085d) for format (4, 5, 5) at best-known rank m = 76 with reduced addition count cr = 295 (U = 76, V = 89, W = 130, fv = 113, cn = 530), symbolically verified across all 10000 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (299 in 4x5x5_m76_cr299_fv112_cn530_ZT_reduced.json, margin -4), reduced_known.json (451 (Z) / 372 (Z2)), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/4x5x5.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+549).

pass: true
