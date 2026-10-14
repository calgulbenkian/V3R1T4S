# REPRODUCE Skeptic Report — Format 4x5x5 Rank 76 SLP in 295 Reduced Additions over Z

role: reproduce
skeptic: astra
context: subagent
context: subagent (astra)

## 1. Quoted Definition and Claimed Object

From `claim/CLAIM.md`:
> # Claim: Format `(4, 5, 5)` Rank 76 Straight-Line Program in 295 Additions over `Z`
> - **Target**: `fmm-additive-complexity-records`
> - **Format**: `(4, 5, 5)` (`4x5x5`)
> - **Rank**: `m = 76` (matches the best rank in `fmm_sota.json`)
> - **Ring**: `Z` (ternary straight-line program, coefficients in `{-1, 1}`)
> - **Claimed Reduced Additions (`cr`)**: `295` (`fv = 113` fresh variables, `cn = 530` naive additions)
> - **Previous Best (`addition_reduced_ZT`)**: `299` (`4x5x5_m76_cr299_fv112_cn530_ZT_reduced.json`, margin `-4`)
> - **Other Sources**: `reduced_known.json` = `451 (Z) / 372 (Z2)`, `matmulcatalog` `adds` = `+549`, `fmm.univ-lille.fr/4x5x5.html` = no complexity variant listed
> - **Object File**: `claim/4x5x5_m76_cr295_fv113_cn530_ZT_reduced.json`
> ## Definition Verified
> Every linear form in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` is an acyclic sum/difference of already-computed quantities with coefficients in `{-1, 1}` (each binary `+/-` counted as 1 addition; negation is free), and the expanded bilinear forms compute the exact matrix product $C = A B$ over $\mathbb{Z}$ across all $n_1 n_2 n_3 n_1 n_2 n_3$ monomials.

From `claim/target.md` (Success Criterion):
> Success means an explicit straight-line program (list of linear forms over the inputs, r products, and linear forms producing the outputs) for a format (n,m,p) with max(n,m,p) le 8 and rank r equal to the best rank listed for that format in fmm_sota.json (re-fetched live), that (1) is verified symbolically to compute the full product A*B exactly over Z, and (2) uses a number of additions/subtractions STRICTLY LESS (direction: min) than the smallest reduced addition count for that format and rank in Perminov's live repository (the addition_reduced_ZT scheme file for the format, reduced_known.json, README and CHANGELOG) re-fetched live immediately before claiming, counted under Perminov's 'reduced' convention (each binary +/- between already-computed quantities counts one; multiplication by -1 is free; multiplication by any other scalar is not allowed in a ternary SLP), AND below any lower count published for that format and rank on the live Lille per-format page's cited complexity variant and in matmulcatalog's live COVERAGE.md 'adds' column.

Mathematical definition of the straight-line program (SLP) and Brent equations for format `(n1, n2, n3) = (4, 5, 5)` and rank `m = 76` over `Z`:
- In each section (`U` with `na = 20` inputs, `V` with `nb = 25` inputs, `W` with `m = 76` product inputs), intermediate variables in `u_fresh`, `v_fresh`, `w_fresh` and output linear forms in `u`, `v`, `w` are linear combinations `sum_t c_t * var[idx_t]` with ternary coefficients `c_t in {-1, 1}`, strictly prior indices `idx_t` (acyclic DAG), and distinct `idx_t` within each form.
- Each linear form `f` of length `len(f) ge 1` contributes `len(f) - 1` binary additions/subtractions to the reduced addition count `cr`.
- Upon expanding the DAGs to basis matrices `U in Z^{76 x 20}`, `V in Z^{76 x 25}`, `W in Z^{20 x 76}`, all `20 * 25 * 20 = 10000` Brent equations over `Z` must hold identically:
$$\sum_{k=0}^{75} U_{k, i_1 n_2 + j_1} \, V_{k, j_2 n_3 + l_2} \, W_{l_3 n_1 + i_3, k} = \delta_{i_1, i_3} \, \delta_{j_1, j_2} \, \delta_{l_2, l_3}$$

## 2. File Integrity Verification

- **Path**: `claim/4x5x5_m76_cr295_fv113_cn530_ZT_reduced.json`
- **Byte size**: `36780` bytes
- **SHA-256**: `2e09966726d94ad6ade2c53de92b73c0e2f78a2d39d2a4a52f50a0e61eef085d`
- **Dimensions & Rank**: `n = [4, 5, 5]`, `m = 76`, `z2 = false`
- **Declared Complexity**: `reduced = 295`, `naive = 530`

## 3. Independent Verification Before Reading Author Code

Before inspecting `claim/verify_slp.py`, I wrote and ran an independent Python SLP verifier from the mathematical definition:

1. **DAG Acyclicity, Ternary Coefficient, and Disjointness Audit**:
   - Verified that every term in `u_fresh` (`40` forms), `u` (`76` forms), `v_fresh` (`35` forms), `v` (`76` forms), `w_fresh` (`38` forms), and `w` (`20` forms) has integer coefficient strictly in `{-1, 1}`, references only strictly earlier variable indices within its own section (`0 le idx le var_id - 1`), has no duplicate variable indices within any single linear form, and shares no variables across `U`, `V`, `W`.
2. **Independent Addition and Fresh-Variable Count**:
   - Recounted reduced additions `cr = sum(len(form) - 1)`:
     - `cr(U) = 76` (`fv(U) = 40`)
     - `cr(V) = 89` (`fv(V) = 35`)
     - `cr(W) = 130` (`fv(W) = 38`)
     - **Total reduced additions**: `cr = 76 + 89 + 130 = 295` (matches claimed `cr = 295` exactly).
     - **Total fresh variables**: `fv = 40 + 35 + 38 = 113` (matches claimed `fv = 113` exactly).
   - Recounted expanded nonzeros and naive additions `cn = sum(max(0, nnz(row) - 1))`:
     - `nnz(U) = 236` (`cn(U) = 160`), `nnz(V) = 266` (`cn(V) = 190`), `nnz(W) = 200` (`cn(W) = 180`).
     - **Total naive additions**: `cn = 160 + 190 + 180 = 530` (matches claimed `cn = 530` exactly).
3. **Exhaustive Symbolic Brent Equation Verification over Z**:
   - Expanded all linear forms over `Z` and checked all `20 * 25 * 20 = 10000` Brent equations over `Z`.
   - Result: `total_eq = 10000`, `bad_eq = 0` (zero error on every bilinear monomial over `Z`).
4. **Step-by-Step Integer Matrix Multiplication Check**:
   - Evaluated the straight-line program step-by-step on deterministic integer matrices `A in Z^{4 x 5}` (`A_{i,j} = 3^{i n_2 + j} + (i+1)(j+2)`) and `B in Z^{5 x 5}` (`B_{j,l} = 5^{j n_3 + l} + (j+2)(l+3)`).
   - Confirmed that the step-by-step SLP output `C_SLP` equals `A * B` entrywise over `Z` across all `20` output entries (`matmul_ok = True`).
5. **1-Entry Corruption Negative Test**:
   - Flipped a single coefficient sign in `u[0][0]` (`value -> -value`).
   - Independent verifier rejected the corrupted SLP (`bad_eq = 3` mismatched Brent equations, `matmul_ok = False`).
   - Author's `claim/verify_slp.py` also rejected the corrupted SLP (`rc = 1`, `FAIL: claim/4x5x5_m76_cr295_fv113_cn530_ZT_reduced.json (corrupted) | Symbolic bilinear identity failed over Z (3 mismatched monomials)`).

## 4. Reproduction of Author Verification Command

Executed the command from `claim/REPRODUCE.md`:
```
python3 claim/verify_slp.py claim/4x5x5_m76_cr295_fv113_cn530_ZT_reduced.json
```
Output (`exit 0`):
```
PASS: claim/4x5x5_m76_cr295_fv113_cn530_ZT_reduced.json | format=4x5x5 m=76 cr=295 (U=76, V=89, W=130) fv=113 cn=530
```
All temporary files created during verification were cleaned up.

pass: true
