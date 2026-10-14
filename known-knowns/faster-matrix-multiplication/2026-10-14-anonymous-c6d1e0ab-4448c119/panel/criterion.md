# Criterion Skeptic Report: `fmm-additive-complexity-records` — Format `(4, 5, 7)` Rank 104 in 395 Additions over `Z`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed straight-line program artifact `claim/4x5x7_m104_cr395_fv161_cn931_ZT_reduced.json` (SHA-256 `4448c119d128c8be762c29223b43d7486bd9bb7acc9633d9d6fd23110445aa72`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_slp.py`, against every literal requirement of `fmm-additive-complexity-records` in `claim/target.md`:

1. **Explicit straight-line program for format `(n1, n2, n3)` with `max(n1, n2, n3)` at most 8 and rank `m` equal to the best rank in `fmm_sota.json`**:
   - **PASS.** `claim/4x5x7_m104_cr395_fv161_cn931_ZT_reduced.json` is an explicit straight-line program for format `(4, 5, 7)` (`4x5x7`), satisfying `max(4, 5, 7) = 7` (at most 8), with bilinear rank `m = 104` matching the best-known rank in `fmm_sota.json` for `4x5x7`. All `m = 104` rows of expanded `U` (width `20`) and `V` (width `35`) and all `28` rows of expanded `W` (width `104`) are strictly non-zero with ternary expanded entries in `{-1, 0, 1}`.
2. **Verified symbolically to compute the full product `A*B` exactly over `Z` with ternary SLP coefficients in `{-1, 1}`**:
   - **PASS.** `claim/4x5x7_m104_cr395_fv161_cn931_ZT_reduced.json` has `z2 = false`. Running `claim/verify_slp.py` confirms that every linear form in `u_fresh` (`33` forms), `u` (`104` forms), `v_fresh` (`59` forms), `v` (`104` forms), `w_fresh` (`69` forms), and `w` (`28` forms) uses only ternary coefficients in `{-1, 1}`, references only strictly preceding variables in an acyclic DAG without duplicate variable indices per form, and shares no variables across `U` (`A`-forms), `V` (`B`-forms), and `W` (product-forms). Symbolic expansion over `Z` confirms zero error across all `(4 * 5 * 7)^2 = 19600` bilinear monomials of `C = A * B`.
3. **Reduced addition count `cr` under Perminov's reduced convention strictly less than all live reference bounds**:
   - **PASS.** Under Perminov's reduced convention (each binary `+/-` in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` counts as `1` addition, i.e., `len(form) - 1`; multiplication by `-1` is free; no other scalar multiplications exist), `claim/verify_slp.py` recounts `cr = 395` additions (`U = 96`, `V = 116`, `W = 183`, matching `complexity.reduced = 395`, with `fv = 161` total fresh variables and `cn = 931` naive additions). Comparing against all live reference sources recorded in `claim/CLAIM.md`:
     - Perminov `addition_reduced_ZT` minimum for `4x5x7` at rank `104`: `cr = 400` (`4x5x7_m104_cr400_fv163_cn931_ZT_reduced.json`), beaten strictly by `-5` additions (`395` vs `400`).
     - Perminov `reduced_known.json` for `4x5x7-104`: `none` (`395` is strictly lower).
     - Perminov `README.md` and `CHANGELOG.md`: no lower reduced addition count for `4x5x7` at rank `104`.
     - `fmm.univ-lille.fr/4x5x7.html`: no complexity variant listed.
     - `solven-eu/matmulcatalog` `COVERAGE.md` `adds` column for `4x5x7`: `+927` (`395` is strictly lower).
4. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only SLP**: Verified symbolically over `Z` (`z2 = false`), not modulo 2.
   - **Not a higher-rank SLP**: Uses the exact catalogue best rank `m = 104`.
   - **Not a rank-lowering claim**: Claims only the additive complexity reduction at fixed rank `m = 104`.
   - **Single format per claim**: This claim folder covers exclusively format `(4, 5, 7)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact integer (ring Z) ternary straight-line program in claim/4x5x7_m104_cr395_fv161_cn931_ZT_reduced.json (sha256 4448c119d128c8be762c29223b43d7486bd9bb7acc9633d9d6fd23110445aa72) for format (4, 5, 7) at best-known rank m = 104 with reduced addition count cr = 395 (U = 96, V = 116, W = 183, fv = 161, cn = 931), symbolically verified across all 19600 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (400 in 4x5x7_m104_cr400_fv163_cn931_ZT_reduced.json, margin -5), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/4x5x7.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+927).

pass: true
