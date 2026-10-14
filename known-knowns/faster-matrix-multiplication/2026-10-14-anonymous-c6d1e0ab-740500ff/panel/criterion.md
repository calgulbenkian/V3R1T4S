# Criterion Skeptic Report: `fmm-additive-complexity-records` — Format `(4, 6, 8)` Rank 140 in 546 Additions over `Z`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed straight-line program artifact `claim/4x6x8_m140_cr546_fv288_cn1248_ZT_reduced.json` (SHA-256 `740500ff5c86434ddbb45c0e60d65af983dd457fbe6f1084e64e74480d7f53db`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_slp.py`, against every literal requirement of `fmm-additive-complexity-records` in `claim/target.md`:

1. **Explicit straight-line program for format `(n1, n2, n3)` with `max(n1, n2, n3)` at most 8 and rank `m` equal to the best rank in `fmm_sota.json`**:
   - **PASS.** `claim/4x6x8_m140_cr546_fv288_cn1248_ZT_reduced.json` is an explicit straight-line program for format `(4, 6, 8)` (`4x6x8`), satisfying `max(4, 6, 8) = 8` (at most 8), with bilinear rank `m = 140` matching the best-known rank in `fmm_sota.json` for `4x6x8`. All `m = 140` rows of expanded `U` (width `24`) and `V` (width `48`) and all `32` rows of expanded `W` (width `140`) are strictly non-zero with ternary expanded entries in `{-1, 0, 1}`.
2. **Verified symbolically to compute the full product `A*B` exactly over `Z` with ternary SLP coefficients in `{-1, 1}`**:
   - **PASS.** `claim/4x6x8_m140_cr546_fv288_cn1248_ZT_reduced.json` has `z2 = false`. Running `claim/verify_slp.py` confirms that every linear form in `u_fresh` (`73` forms), `u` (`140` forms), `v_fresh` (`75` forms), `v` (`140` forms), `w_fresh` (`140` forms), and `w` (`32` forms) uses only ternary coefficients in `{-1, 1}`, references only strictly preceding variables in an acyclic DAG without duplicate variable indices per form, and shares no variables across `U` (`A`-forms), `V` (`B`-forms), and `W` (product-forms). Symbolic expansion over `Z` confirms zero error across all `(4 * 6 * 8)^2 = 36864` bilinear monomials of `C = A * B`.
3. **Reduced addition count `cr` under Perminov's reduced convention strictly less than all live reference bounds**:
   - **PASS.** Under Perminov's reduced convention (each binary `+/-` in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` counts as `1` addition, i.e., `len(form) - 1`; multiplication by `-1` is free; no other scalar multiplications exist), `claim/verify_slp.py` recounts `cr = 546` additions (`U = 115`, `V = 171`, `W = 260`, matching `complexity.reduced = 546`, with `fv = 288` total fresh variables and `cn = 1248` naive additions). Comparing against all live reference sources recorded in `claim/CLAIM.md`:
     - Perminov `addition_reduced_ZT` minimum for `4x6x8` at rank `140`: `cr = 551` (`4x6x8_m140_cr551_cn1248_ZT_reduced.json`), beaten strictly by `-5` additions (`546` vs `551`).
     - Perminov `reduced_known.json` for `4x6x8-140`: `none` (`546` is strictly lower).
     - Perminov `README.md` and `CHANGELOG.md`: no lower reduced addition count for `4x6x8` at rank `140`.
     - `fmm.univ-lille.fr/4x6x8.html`: no complexity variant listed.
     - `solven-eu/matmulcatalog` `COVERAGE.md` `adds` column for `4x6x8`: `unlisted` (`546` is strictly lower).
4. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only SLP**: Verified symbolically over `Z` (`z2 = false`), not modulo 2.
   - **Not a higher-rank SLP**: Uses the exact catalogue best rank `m = 140`.
   - **Not a rank-lowering claim**: Claims only the additive complexity reduction at fixed rank `m = 140`.
   - **Single format per claim**: This claim folder covers exclusively format `(4, 6, 8)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact integer (ring Z) ternary straight-line program in claim/4x6x8_m140_cr546_fv288_cn1248_ZT_reduced.json (sha256 740500ff5c86434ddbb45c0e60d65af983dd457fbe6f1084e64e74480d7f53db) for format (4, 6, 8) at best-known rank m = 140 with reduced addition count cr = 546 (U = 115, V = 171, W = 260, fv = 288, cn = 1248), symbolically verified across all 36864 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (551 in 4x6x8_m140_cr551_cn1248_ZT_reduced.json, margin -5), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/4x6x8.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (unlisted).

pass: true
