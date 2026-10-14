# Criterion Skeptic Report: `fmm-additive-complexity-records` — Format `(3, 4, 5)` Rank 47 in 159 Additions over `Z`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed straight-line program artifact `claim/3x4x5_m47_cr159_fv60_cn277_ZT_reduced.json` (SHA-256 `197ffad82f4cdd3ea6899fe41fc93c1b7c16917cfa5dba26199fe8143c06292d`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_slp.py`, against every literal requirement of `fmm-additive-complexity-records` in `claim/target.md`:

1. **Explicit straight-line program for format `(n1, n2, n3)` with `max(n1, n2, n3)` at most 8 and rank `m` equal to the best rank in `fmm_sota.json`**:
   - **PASS.** `claim/3x4x5_m47_cr159_fv60_cn277_ZT_reduced.json` is an explicit straight-line program for format `(3, 4, 5)` (`3x4x5`), satisfying `max(3, 4, 5) = 5` (at most 8), with bilinear rank `m = 47` matching the best-known rank in `fmm_sota.json` for `3x4x5`. All `m = 47` rows of expanded `U` (width `12`) and `V` (width `20`) and all `15` rows of expanded `W` (width `47`) are strictly non-zero with ternary expanded entries in `{-1, 0, 1}`.
2. **Verified symbolically to compute the full product `A*B` exactly over `Z` with ternary SLP coefficients in `{-1, 1}`**:
   - **PASS.** `claim/3x4x5_m47_cr159_fv60_cn277_ZT_reduced.json` has `z2 = false`. Running `claim/verify_slp.py` confirms that every linear form in `u_fresh` (`20` forms), `u` (`47` forms), `v_fresh` (`17` forms), `v` (`47` forms), `w_fresh` (`23` forms), and `w` (`15` forms) uses only ternary coefficients in `{-1, 1}`, references only strictly preceding variables in an acyclic DAG without duplicate variable indices per form, and shares no variables across `U` (`A`-forms), `V` (`B`-forms), and `W` (product-forms). Symbolic expansion over `Z` confirms zero error across all `(3 * 4 * 5)^2 = 3600` bilinear monomials of `C = A * B`.
3. **Reduced addition count `cr` under Perminov's reduced convention strictly less than all live reference bounds**:
   - **PASS.** Under Perminov's reduced convention (each binary `+/-` in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` counts as `1` addition, i.e., `len(form) - 1`; multiplication by `-1` is free; no other scalar multiplications exist), `claim/verify_slp.py` recounts `cr = 159` additions (`U = 39`, `V = 46`, `W = 74`, matching `complexity.reduced = 159`, with `fv = 60` total fresh variables and `cn = 277` naive additions). Comparing against all live reference sources recorded in `claim/CLAIM.md`:
     - Perminov `addition_reduced_ZT` minimum for `3x4x5` at rank `47`: `cr = 161` (`3x4x5_m47_cr161_cn277_ZT_reduced.json`), beaten strictly by `-2` additions (`159` vs `161`).
     - Perminov `reduced_known.json` for `3x4x5-47`: `276 (Z) / 242 (Z2)` (`159` is strictly lower).
     - Perminov `README.md` and `CHANGELOG.md`: no lower reduced addition count for `3x4x5` at rank `47`.
     - `fmm.univ-lille.fr/3x4x5.html`: no complexity variant listed.
     - `solven-eu/matmulcatalog` `COVERAGE.md` `adds` column for `3x4x5`: `+287` (`159` is strictly lower).
4. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only SLP**: Verified symbolically over `Z` (`z2 = false`), not modulo 2.
   - **Not a higher-rank SLP**: Uses the exact catalogue best rank `m = 47`.
   - **Not a rank-lowering claim**: Claims only the additive complexity reduction at fixed rank `m = 47`.
   - **Single format per claim**: This claim folder covers exclusively format `(3, 4, 5)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact integer (ring Z) ternary straight-line program in claim/3x4x5_m47_cr159_fv60_cn277_ZT_reduced.json (sha256 197ffad82f4cdd3ea6899fe41fc93c1b7c16917cfa5dba26199fe8143c06292d) for format (3, 4, 5) at best-known rank m = 47 with reduced addition count cr = 159 (U = 39, V = 46, W = 74, fv = 60, cn = 277), symbolically verified across all 3600 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (161 in 3x4x5_m47_cr161_cn277_ZT_reduced.json, margin -2), reduced_known.json (276 (Z) / 242 (Z2)), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/3x4x5.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+287).

pass: true
