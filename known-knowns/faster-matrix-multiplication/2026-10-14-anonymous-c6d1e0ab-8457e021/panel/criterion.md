# Criterion Skeptic Report: `fmm-additive-complexity-records` — Format `(4, 5, 8)` Rank 118 in 507 Additions over `Z`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed straight-line program artifact `claim/4x5x8_m118_cr507_fv250_cn1521_ZT_reduced.json` (SHA-256 `8457e021243c258cc047506d85372ef177054c9f8473261a27b211f1f3a419ec`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_slp.py`, against every literal requirement of `fmm-additive-complexity-records` in `claim/target.md`:

1. **Explicit straight-line program for format `(n1, n2, n3)` with `max(n1, n2, n3)` at most 8 and rank `m` equal to the best rank in `fmm_sota.json`**:
   - **PASS.** `claim/4x5x8_m118_cr507_fv250_cn1521_ZT_reduced.json` is an explicit straight-line program for format `(4, 5, 8)` (`4x5x8`), satisfying `max(4, 5, 8) = 8` (at most 8), with bilinear rank `m = 118` matching the best-known rank in `fmm_sota.json` for `4x5x8`. All `m = 118` rows of expanded `U` (width `20`) and `V` (width `40`) and all `32` rows of expanded `W` (width `118`) are strictly non-zero with ternary expanded entries in `{-1, 0, 1}`.
2. **Verified symbolically to compute the full product `A*B` exactly over `Z` with ternary SLP coefficients in `{-1, 1}`**:
   - **PASS.** `claim/4x5x8_m118_cr507_fv250_cn1521_ZT_reduced.json` has `z2 = false`. Running `claim/verify_slp.py` confirms that every linear form in `u_fresh` (`45` forms), `u` (`118` forms), `v_fresh` (`74` forms), `v` (`118` forms), `w_fresh` (`131` forms), and `w` (`32` forms) uses only ternary coefficients in `{-1, 1}`, references only strictly preceding variables in an acyclic DAG without duplicate variable indices per form, and shares no variables across `U` (`A`-forms), `V` (`B`-forms), and `W` (product-forms). Symbolic expansion over `Z` confirms zero error across all `(4 * 5 * 8)^2 = 25600` bilinear monomials of `C = A * B`.
3. **Reduced addition count `cr` under Perminov's reduced convention strictly less than all live reference bounds**:
   - **PASS.** Under Perminov's reduced convention (each binary `+/-` in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` counts as `1` addition, i.e., `len(form) - 1`; multiplication by `-1` is free; no other scalar multiplications exist), `claim/verify_slp.py` recounts `cr = 507` additions (`U = 109`, `V = 162`, `W = 236`, matching `complexity.reduced = 507`, with `fv = 250` total fresh variables and `cn = 1521` naive additions). Comparing against all live reference sources recorded in `claim/CLAIM.md`:
     - Perminov `addition_reduced_ZT` minimum for `4x5x8` at rank `118`: `cr = 513` (`4x5x8_m118_cr513_fv249_cn1521_ZT_reduced.json`), beaten strictly by `-6` additions (`507` vs `513`).
     - Perminov `reduced_known.json` for `4x5x8-118`: `none` (`507` is strictly lower).
     - Perminov `README.md` and `CHANGELOG.md`: no lower reduced addition count for `4x5x8` at rank `118`.
     - `fmm.univ-lille.fr/4x5x8.html`: no complexity variant listed.
     - `solven-eu/matmulcatalog` `COVERAGE.md` `adds` column for `4x5x8`: `+1521` (`507` is strictly lower).
4. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only SLP**: Verified symbolically over `Z` (`z2 = false`), not modulo 2.
   - **Not a higher-rank SLP**: Uses the exact catalogue best rank `m = 118`.
   - **Not a rank-lowering claim**: Claims only the additive complexity reduction at fixed rank `m = 118`.
   - **Single format per claim**: This claim folder covers exclusively format `(4, 5, 8)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact integer (ring Z) ternary straight-line program in claim/4x5x8_m118_cr507_fv250_cn1521_ZT_reduced.json (sha256 8457e021243c258cc047506d85372ef177054c9f8473261a27b211f1f3a419ec) for format (4, 5, 8) at best-known rank m = 118 with reduced addition count cr = 507 (U = 109, V = 162, W = 236, fv = 250, cn = 1521), symbolically verified across all 25600 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (513 in 4x5x8_m118_cr513_fv249_cn1521_ZT_reduced.json, margin -6), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/4x5x8.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+1521).

pass: true
