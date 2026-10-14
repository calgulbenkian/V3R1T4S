# Criterion Skeptic Report: `fmm-additive-complexity-records` — Format `(4, 4, 7)` Rank 85 in 317 Additions over `Z`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed straight-line program artifact `claim/4x4x7_m85_cr317_fv119_cn631_ZT_reduced.json` (SHA-256 `ec055cb50ec26544703661a163796d145b57c732a2fa1586abb9d7dadfcb56dc`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_slp.py`, against every literal requirement of `fmm-additive-complexity-records` in `claim/target.md`:

1. **Explicit straight-line program for format `(n1, n2, n3)` with `max(n1, n2, n3)` at most 8 and rank `m` equal to the best rank in `fmm_sota.json`**:
   - **PASS.** `claim/4x4x7_m85_cr317_fv119_cn631_ZT_reduced.json` is an explicit straight-line program for format `(4, 4, 7)` (`4x4x7`), satisfying `max(4, 4, 7) = 7` (at most 8), with bilinear rank `m = 85` matching the best-known rank in `fmm_sota.json` for `4x4x7`. All `m = 85` rows of expanded `U` (width `16`) and `V` (width `28`) and all `28` rows of expanded `W` (width `85`) are strictly non-zero with ternary expanded entries in `{-1, 0, 1}`.
2. **Verified symbolically to compute the full product `A*B` exactly over `Z` with ternary SLP coefficients in `{-1, 1}`**:
   - **PASS.** `claim/4x4x7_m85_cr317_fv119_cn631_ZT_reduced.json` has `z2 = false`. Running `claim/verify_slp.py` confirms that every linear form in `u_fresh` (`23` forms), `u` (`85` forms), `v_fresh` (`42` forms), `v` (`85` forms), `w_fresh` (`54` forms), and `w` (`28` forms) uses only ternary coefficients in `{-1, 1}`, references only strictly preceding variables in an acyclic DAG without duplicate variable indices per form, and shares no variables across `U` (`A`-forms), `V` (`B`-forms), and `W` (product-forms). Symbolic expansion over `Z` confirms zero error across all `(4 * 4 * 7)^2 = 12544` bilinear monomials of `C = A * B`.
3. **Reduced addition count `cr` under Perminov's reduced convention strictly less than all live reference bounds**:
   - **PASS.** Under Perminov's reduced convention (each binary `+/-` in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` counts as `1` addition, i.e., `len(form) - 1`; multiplication by `-1` is free; no other scalar multiplications exist), `claim/verify_slp.py` recounts `cr = 317` additions (`U = 80`, `V = 92`, `W = 145`, matching `complexity.reduced = 317`, with `fv = 119` total fresh variables and `cn = 631` naive additions). Comparing against all live reference sources recorded in `claim/CLAIM.md`:
     - Perminov `addition_reduced_ZT` minimum for `4x4x7` at rank `85`: `cr = 319` (`4x4x7_m85_cr319_fv119_cn631_ZT_reduced.json`), beaten strictly by `-2` additions (`317` vs `319`).
     - Perminov `reduced_known.json` for `4x4x7-85`: `none` (`317` is strictly lower).
     - Perminov `README.md` and `CHANGELOG.md`: no lower reduced addition count for `4x4x7` at rank `85`.
     - `fmm.univ-lille.fr/4x4x7.html`: no complexity variant listed.
     - `solven-eu/matmulcatalog` `COVERAGE.md` `adds` column for `4x4x7`: `+631` (`317` is strictly lower).
4. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only SLP**: Verified symbolically over `Z` (`z2 = false`), not modulo 2.
   - **Not a higher-rank SLP**: Uses the exact catalogue best rank `m = 85`.
   - **Not a rank-lowering claim**: Claims only the additive complexity reduction at fixed rank `m = 85`.
   - **Single format per claim**: This claim folder covers exclusively format `(4, 4, 7)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact integer (ring Z) ternary straight-line program in claim/4x4x7_m85_cr317_fv119_cn631_ZT_reduced.json (sha256 ec055cb50ec26544703661a163796d145b57c732a2fa1586abb9d7dadfcb56dc) for format (4, 4, 7) at best-known rank m = 85 with reduced addition count cr = 317 (U = 80, V = 92, W = 145, fv = 119, cn = 631), symbolically verified across all 12544 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (319 in 4x4x7_m85_cr319_fv119_cn631_ZT_reduced.json, margin -2), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/4x4x7.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+631).

pass: true
