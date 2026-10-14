# Criterion Skeptic Report: `fmm-additive-complexity-records` — Format `(2, 8, 8)` Rank 100 in 423 Additions over `Z`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed straight-line program artifact `claim/2x8x8_m100_cr423_fv94_cn608_ZT_reduced.json` (SHA-256 `1dc2a27122c50cbe852e77aab752edc1d1ec1fc2f6cb9f28a6ea47926acc1a3e`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_slp.py`, against every literal requirement of `fmm-additive-complexity-records` in `claim/target.md`:

1. **Explicit straight-line program for format `(n1, n2, n3)` with `max(n1, n2, n3)` at most 8 and rank `m` equal to the best rank in `fmm_sota.json`**:
   - **PASS.** `claim/2x8x8_m100_cr423_fv94_cn608_ZT_reduced.json` is an explicit straight-line program for format `(2, 8, 8)` (`2x8x8`), satisfying `max(2, 8, 8) = 8` (at most 8), with bilinear rank `m = 100` matching the best-known rank in `fmm_sota.json` for `2x8x8`. All `m = 100` rows of expanded `U` (width `16`) and `V` (width `64`) and all `16` rows of expanded `W` (width `100`) are strictly non-zero with ternary expanded entries in `{-1, 0, 1}`.
2. **Verified symbolically to compute the full product `A*B` exactly over `Z` with ternary SLP coefficients in `{-1, 1}`**:
   - **PASS.** `claim/2x8x8_m100_cr423_fv94_cn608_ZT_reduced.json` has `z2 = false`. Running `claim/verify_slp.py` confirms that every linear form in `u_fresh` (`33` forms), `u` (`100` forms), `v_fresh` (`16` forms), `v` (`100` forms), `w_fresh` (`45` forms), and `w` (`16` forms) uses only ternary coefficients in `{-1, 1}`, references only strictly preceding variables in an acyclic DAG without duplicate variable indices per form, and shares no variables across `U` (`A`-forms), `V` (`B`-forms), and `W` (product-forms). Symbolic expansion over `Z` confirms zero error across all `(2 * 8 * 8)^2 = 16384` bilinear monomials of `C = A * B`.
3. **Reduced addition count `cr` under Perminov's reduced convention strictly less than all live reference bounds**:
   - **PASS.** Under Perminov's reduced convention (each binary `+/-` in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` counts as `1` addition, i.e., `len(form) - 1`; multiplication by `-1` is free; no other scalar multiplications exist), `claim/verify_slp.py` recounts `cr = 423` additions (`U = 92`, `V = 154`, `W = 177`, matching `complexity.reduced = 423`, with `fv = 94` total fresh variables and `cn = 608` naive additions). Comparing against all live reference sources recorded in `claim/CLAIM.md`:
     - Perminov `addition_reduced_ZT` minimum for `2x8x8` at rank `100`: `cr = 424` (`2x8x8_m100_cr424_cn608_ZT_reduced.json`), beaten strictly by `-1` additions (`423` vs `424`).
     - Perminov `reduced_known.json` for `2x8x8-100`: `none` (`423` is strictly lower).
     - Perminov `README.md` and `CHANGELOG.md`: no lower reduced addition count for `2x8x8` at rank `100`.
     - `fmm.univ-lille.fr/2x8x8.html`: no complexity variant listed.
     - `solven-eu/matmulcatalog` `COVERAGE.md` `adds` column for `2x8x8`: `unlisted` (`423` is strictly lower).
4. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only SLP**: Verified symbolically over `Z` (`z2 = false`), not modulo 2.
   - **Not a higher-rank SLP**: Uses the exact catalogue best rank `m = 100`.
   - **Not a rank-lowering claim**: Claims only the additive complexity reduction at fixed rank `m = 100`.
   - **Single format per claim**: This claim folder covers exclusively format `(2, 8, 8)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact integer (ring Z) ternary straight-line program in claim/2x8x8_m100_cr423_fv94_cn608_ZT_reduced.json (sha256 1dc2a27122c50cbe852e77aab752edc1d1ec1fc2f6cb9f28a6ea47926acc1a3e) for format (2, 8, 8) at best-known rank m = 100 with reduced addition count cr = 423 (U = 92, V = 154, W = 177, fv = 94, cn = 608), symbolically verified across all 16384 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (424 in 2x8x8_m100_cr424_cn608_ZT_reduced.json, margin -1), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/2x8x8.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (unlisted).

pass: true
