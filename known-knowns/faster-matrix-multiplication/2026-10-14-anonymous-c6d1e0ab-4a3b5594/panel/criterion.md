# Criterion Skeptic Report: `fmm-additive-complexity-records` — Format `(5, 5, 8)` Rank 144 in 612 Additions over `Z`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed straight-line program artifact `claim/5x5x8_m144_cr612_fv279_cn1908_ZT_reduced.json` (SHA-256 `4a3b5594547999273c9a3e9335bc5e0ebd6e3b2a5f4971755cccf60b29b0d41f`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_slp.py`, against every literal requirement of `fmm-additive-complexity-records` in `claim/target.md`:

1. **Explicit straight-line program for format `(n1, n2, n3)` with `max(n1, n2, n3)` at most 8 and rank `m` equal to the best rank in `fmm_sota.json`**:
   - **PASS.** `claim/5x5x8_m144_cr612_fv279_cn1908_ZT_reduced.json` is an explicit straight-line program for format `(5, 5, 8)` (`5x5x8`), satisfying `max(5, 5, 8) = 8` (at most 8), with bilinear rank `m = 144` matching the best-known rank in `fmm_sota.json` for `5x5x8`. All `m = 144` rows of expanded `U` (width `25`) and `V` (width `40`) and all `40` rows of expanded `W` (width `144`) are strictly non-zero with ternary expanded entries in `{-1, 0, 1}`.
2. **Verified symbolically to compute the full product `A*B` exactly over `Z` with ternary SLP coefficients in `{-1, 1}`**:
   - **PASS.** `claim/5x5x8_m144_cr612_fv279_cn1908_ZT_reduced.json` has `z2 = false`. Running `claim/verify_slp.py` confirms that every linear form in `u_fresh` (`58` forms), `u` (`144` forms), `v_fresh` (`85` forms), `v` (`144` forms), `w_fresh` (`136` forms), and `w` (`40` forms) uses only ternary coefficients in `{-1, 1}`, references only strictly preceding variables in an acyclic DAG without duplicate variable indices per form, and shares no variables across `U` (`A`-forms), `V` (`B`-forms), and `W` (product-forms). Symbolic expansion over `Z` confirms zero error across all `(5 * 5 * 8)^2 = 40000` bilinear monomials of `C = A * B`.
3. **Reduced addition count `cr` under Perminov's reduced convention strictly less than all live reference bounds**:
   - **PASS.** Under Perminov's reduced convention (each binary `+/-` in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` counts as `1` addition, i.e., `len(form) - 1`; multiplication by `-1` is free; no other scalar multiplications exist), `claim/verify_slp.py` recounts `cr = 612` additions (`U = 148`, `V = 178`, `W = 286`, matching `complexity.reduced = 612`, with `fv = 279` total fresh variables and `cn = 1908` naive additions). Comparing against all live reference sources recorded in `claim/CLAIM.md`:
     - Perminov `addition_reduced_ZT` minimum for `5x5x8` at rank `144`: `cr = 620` (`5x5x8_m144_cr620_fv281_cn1924_ZT_reduced.json`), beaten strictly by `-8` additions (`612` vs `620`).
     - Perminov `reduced_known.json` for `5x5x8-144`: `none` (`612` is strictly lower).
     - Perminov `README.md` and `CHANGELOG.md`: no lower reduced addition count for `5x5x8` at rank `144`.
     - `fmm.univ-lille.fr/5x5x8.html`: no complexity variant listed.
     - `solven-eu/matmulcatalog` `COVERAGE.md` `adds` column for `5x5x8`: `+1908` (`612` is strictly lower).
4. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only SLP**: Verified symbolically over `Z` (`z2 = false`), not modulo 2.
   - **Not a higher-rank SLP**: Uses the exact catalogue best rank `m = 144`.
   - **Not a rank-lowering claim**: Claims only the additive complexity reduction at fixed rank `m = 144`.
   - **Single format per claim**: This claim folder covers exclusively format `(5, 5, 8)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact integer (ring Z) ternary straight-line program in claim/5x5x8_m144_cr612_fv279_cn1908_ZT_reduced.json (sha256 4a3b5594547999273c9a3e9335bc5e0ebd6e3b2a5f4971755cccf60b29b0d41f) for format (5, 5, 8) at best-known rank m = 144 with reduced addition count cr = 612 (U = 148, V = 178, W = 286, fv = 279, cn = 1908), symbolically verified across all 40000 bilinear monomials over Z and strictly beating Perminov addition_reduced_ZT (620 in 5x5x8_m144_cr620_fv281_cn1924_ZT_reduced.json, margin -8), reduced_known.json (none), README.md/CHANGELOG.md (no lower count), fmm.univ-lille.fr/5x5x8.html (no complexity variant listed), and matmulcatalog COVERAGE.md adds (+1908).

pass: true
