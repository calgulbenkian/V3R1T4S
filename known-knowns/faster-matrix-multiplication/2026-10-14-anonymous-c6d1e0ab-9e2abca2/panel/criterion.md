# Criterion Skeptic Report: `fmm-additive-complexity-records` — Format `(4, 4, 6)` Rank 73 in 275 Additions over `Z`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed straight-line program artifact `claim/4x4x6_m73_cr275_fv101_cn534_ZT_reduced.json` (SHA-256 `9e2abca2c586a6020b90ae6e020dabb4b00f47dead9e4bea48a804452a8dfff7`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_slp.py`, against every literal requirement of `fmm-additive-complexity-records` in `claim/target.md`:

1. **Explicit straight-line program for format `(n1, n2, n3)` with `max(n1, n2, n3)` at most 8 and rank `m` equal to the best rank in `fmm_sota.json`**:
   - **PASS.** `claim/4x4x6_m73_cr275_fv101_cn534_ZT_reduced.json` is an explicit straight-line program for format `(4, 4, 6)` (`4x4x6`), satisfying `max(4, 4, 6) = 6` (at most 8), with bilinear rank `m = 73` matching the best-known rank in `fmm_sota.json` for `4x4x6`. All `m = 73` rows of expanded `U` (width `16`) and `V` (width `24`) and all `24` rows of expanded `W` (width `73`) are strictly non-zero with ternary expanded entries in `{-1, 0, 1}`.
2. **Verified symbolically to compute the full product `A*B` exactly over `Z` with ternary SLP coefficients in `{-1, 1}`**:
   - **PASS.** `claim/4x4x6_m73_cr275_fv101_cn534_ZT_reduced.json` has `z2 = false`. Running `claim/verify_slp.py` confirms that every linear form in `u_fresh` (`21` forms), `u` (`73` forms), `v_fresh` (`36` forms), `v` (`73` forms), `w_fresh` (`44` forms), and `w` (`24` forms) uses only ternary coefficients in `{-1, 1}`, references only strictly preceding variables in an acyclic DAG without duplicate variable indices per form, and shares no variables across `U` (`A`-forms), `V` (`B`-forms), and `W` (product-forms). Symbolic expansion over `Z` confirms zero error across all `(4 * 4 * 6)^2 = 9216` bilinear monomials of `C = A * B`.
3. **Reduced addition count `cr` under Perminov's reduced convention strictly less than all live reference bounds**:
   - **PASS.** Under Perminov's reduced convention (each binary `+/-` in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` counts as `1` addition, i.e., `len(form) - 1`; multiplication by `-1` is free; no other scalar multiplications exist), `claim/verify_slp.py` recounts `cr = 275` additions (`U = 71`, `V = 78`, `W = 126`, matching `complexity.reduced = 275`, with `fv = 101` total fresh variables and `cn = 534` naive additions). Comparing against all live reference sources recorded in `claim/CLAIM.md`:
     - Perminov `addition_reduced_ZT` minimum for `4x4x6` at rank `73`: `cr = 280` (`4x4x6_m73_cr280_cn540_ZT_reduced.json`), beaten strictly by `-5` additions (`275` vs `280`).
     - Perminov `reduced_known.json` for `4x4x6-73`: `none` (`275` is strictly lower).
     - Perminov `README.md` and `CHANGELOG.md`: no lower reduced addition count for `4x4x6` at rank `73`.
     - `fmm.univ-lille.fr/4x4x6.html`: no complexity variant listed.
     - `solven-eu/matmulcatalog` `COVERAGE.md` `adds` column for `4x4x6`: `+565` (`275` is strictly lower).
4. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only SLP**: Verified symbolically over `Z` (`z2 = false`), not modulo 2.
   - **Not a higher-rank SLP**: Uses the exact catalogue best rank `m = 73`.
   - **Not a rank-lowering claim**: Claims only the additive complexity reduction at fixed rank `m = 73`.
   - **Single format per claim**: This claim folder covers exclusively format `(4, 4, 6)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact integer (ring Z) ternary straight-line program in claim/4x4x6_m73_cr275_fv101_cn534_ZT_reduced.json (sha256 9e2abca2c586a6020b90ae6e020dabb4b00f47dead9e4bea48a804452a8dfff7) for format (4, 4, 6) at best-known rank m = 73 with reduced addition count cr = 275 (U = 71, V = 78, W = 126, fv = 101, cn = 534), symbolically verified across all 9216 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (280 in 4x4x6_m73_cr280_cn540_ZT_reduced.json, margin -5), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/4x4x6.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+565).

pass: true
