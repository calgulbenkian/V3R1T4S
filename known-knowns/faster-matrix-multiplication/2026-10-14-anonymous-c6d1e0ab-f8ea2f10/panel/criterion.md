# Criterion Skeptic Report: `fmm-additive-complexity-records` — Format `(4, 6, 7)` Rank 123 in 505 Additions over `Z`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed straight-line program artifact `claim/4x6x7_m123_cr505_fv237_cn1573_ZT_reduced.json` (SHA-256 `f8ea2f1002c2100a61df1ee19be3bf1335a80c1990b2a3d4f3217feebcc52869`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_slp.py`, against every literal requirement of `fmm-additive-complexity-records` in `claim/target.md`:

1. **Explicit straight-line program for format `(n1, n2, n3)` with `max(n1, n2, n3)` at most 8 and rank `m` equal to the best rank in `fmm_sota.json`**:
   - **PASS.** `claim/4x6x7_m123_cr505_fv237_cn1573_ZT_reduced.json` is an explicit straight-line program for format `(4, 6, 7)` (`4x6x7`), satisfying `max(4, 6, 7) = 7` (at most 8), with bilinear rank `m = 123` matching the best-known rank in `fmm_sota.json` for `4x6x7`. All `m = 123` rows of expanded `U` (width `24`) and `V` (width `42`) and all `28` rows of expanded `W` (width `123`) are strictly non-zero with ternary expanded entries in `{-1, 0, 1}`.
2. **Verified symbolically to compute the full product `A*B` exactly over `Z` with ternary SLP coefficients in `{-1, 1}`**:
   - **PASS.** `claim/4x6x7_m123_cr505_fv237_cn1573_ZT_reduced.json` has `z2 = false`. Running `claim/verify_slp.py` confirms that every linear form in `u_fresh` (`47` forms), `u` (`123` forms), `v_fresh` (`71` forms), `v` (`123` forms), `w_fresh` (`119` forms), and `w` (`28` forms) uses only ternary coefficients in `{-1, 1}`, references only strictly preceding variables in an acyclic DAG without duplicate variable indices per form, and shares no variables across `U` (`A`-forms), `V` (`B`-forms), and `W` (product-forms). Symbolic expansion over `Z` confirms zero error across all `(4 * 6 * 7)^2 = 28224` bilinear monomials of `C = A * B`.
3. **Reduced addition count `cr` under Perminov's reduced convention strictly less than all live reference bounds**:
   - **PASS.** Under Perminov's reduced convention (each binary `+/-` in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` counts as `1` addition, i.e., `len(form) - 1`; multiplication by `-1` is free; no other scalar multiplications exist), `claim/verify_slp.py` recounts `cr = 505` additions (`U = 121`, `V = 159`, `W = 225`, matching `complexity.reduced = 505`, with `fv = 237` total fresh variables and `cn = 1573` naive additions). Comparing against all live reference sources recorded in `claim/CLAIM.md`:
     - Perminov `addition_reduced_ZT` minimum for `4x6x7` at rank `123`: `cr = 517` (`4x6x7_m123_cr517_cn1586_ZT_reduced.json`), beaten strictly by `-12` additions (`505` vs `517`).
     - Perminov `reduced_known.json` for `4x6x7-123`: `none` (`505` is strictly lower).
     - Perminov `README.md` and `CHANGELOG.md`: no lower reduced addition count for `4x6x7` at rank `123`.
     - `fmm.univ-lille.fr/4x6x7.html`: no complexity variant listed.
     - `solven-eu/matmulcatalog` `COVERAGE.md` `adds` column for `4x6x7`: `+1586` (`505` is strictly lower).
4. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only SLP**: Verified symbolically over `Z` (`z2 = false`), not modulo 2.
   - **Not a higher-rank SLP**: Uses the exact catalogue best rank `m = 123`.
   - **Not a rank-lowering claim**: Claims only the additive complexity reduction at fixed rank `m = 123`.
   - **Single format per claim**: This claim folder covers exclusively format `(4, 6, 7)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact integer (ring Z) ternary straight-line program in claim/4x6x7_m123_cr505_fv237_cn1573_ZT_reduced.json (sha256 f8ea2f1002c2100a61df1ee19be3bf1335a80c1990b2a3d4f3217feebcc52869) for format (4, 6, 7) at best-known rank m = 123 with reduced addition count cr = 505 (U = 121, V = 159, W = 225, fv = 237, cn = 1573), symbolically verified across all 28224 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (517 in 4x6x7_m123_cr517_cn1586_ZT_reduced.json, margin -12), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/4x6x7.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+1586).

pass: true
