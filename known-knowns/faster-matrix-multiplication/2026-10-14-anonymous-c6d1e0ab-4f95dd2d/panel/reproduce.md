# REPRODUCE Skeptic Report — Format 5x5x6 Rank 110 SLP in 451 Reduced Additions over Z

role: reproduce
skeptic: astra
context: subagent
context: subagent (astra)

## 1. Quoted Definition and Claimed Object

From `claim/CLAIM.md`:
> # Claim: Format `(5, 5, 6)` Rank 110 Straight-Line Program in 451 Additions over `Z`
> - **Target**: `fmm-additive-complexity-records`
> - **Format**: `(5, 5, 6)` (`5x5x6`)
> - **Rank**: `m = 110` (matches the best rank in `fmm_sota.json`)
> - **Ring**: `Z` (ternary straight-line program, coefficients in `{-1, 1}`)
> - **Claimed Reduced Additions (`cr`)**: `451` (`fv = 202` fresh variables, `cn = 1208` naive additions)
> - **Previous Best (`addition_reduced_ZT`)**: `460` (`5x5x6_m110_cr460_fv204_cn1215_ZT_reduced.json`, margin `-9`)
> - **Other Sources**: `reduced_known.json` = `none`, `matmulcatalog` `adds` = `+1215`, `fmm.univ-lille.fr/5x5x6.html` = no complexity variant listed
> - **Object File**: `claim/5x5x6_m110_cr451_fv202_cn1208_ZT_reduced.json`
> ## Definition Verified
> Every linear form in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` is an acyclic sum/difference of already-computed quantities with coefficients in `{-1, 1}` (each binary `+/-` counted as 1 addition; negation is free), and the expanded bilinear forms compute the exact matrix product $C = A B$ over $\mathbb{Z}$ across all $n_1 n_2 n_3 n_1 n_2 n_3$ monomials.

From `claim/target.md` (Success Criterion):
> Success means an explicit straight-line program (list of linear forms over the inputs, r products, and linear forms producing the outputs) for a format (n,m,p) with max(n,m,p) le 8 and rank r equal to the best rank listed for that format in fmm_sota.json (re-fetched live), that (1) is verified symbolically to compute the full product A*B exactly over Z, and (2) uses a number of additions/subtractions STRICTLY LESS (direction: min) than the smallest reduced addition count for that format and rank in Perminov's live repository (the addition_reduced_ZT scheme file for the format, reduced_known.json, README and CHANGELOG) re-fetched live immediately before claiming, counted under Perminov's 'reduced' convention (each binary +/- between already-computed quantities counts one; multiplication by -1 is free; multiplication by any other scalar is not allowed in a ternary SLP), AND below any lower count published for that format and rank on the live Lille per-format page's cited complexity variant and in matmulcatalog's live COVERAGE.md 'adds' column.

Mathematical definition of the straight-line program (SLP) and Brent equations for format `(n1, n2, n3) = (5, 5, 6)` and rank `m = 110` over `Z`:
- In each section (`U` with `na = 25` inputs, `V` with `nb = 30` inputs, `W` with `m = 110` product inputs), intermediate variables in `u_fresh`, `v_fresh`, `w_fresh` and output linear forms in `u`, `v`, `w` are linear combinations `sum_t c_t * var[idx_t]` with ternary coefficients `c_t in {-1, 1}`, strictly prior indices `idx_t` (acyclic DAG), and distinct `idx_t` within each form.
- Each linear form `f` of length `len(f) ge 1` contributes `len(f) - 1` binary additions/subtractions to the reduced addition count `cr`.
- Upon expanding the DAGs to basis matrices `U in Z^{110 x 25}`, `V in Z^{110 x 30}`, `W in Z^{30 x 110}`, all `25 * 30 * 30 = 22500` Brent equations over `Z` must hold identically:
$$\sum_{k=0}^{109} U_{k, i_1 n_2 + j_1} \, V_{k, j_2 n_3 + l_2} \, W_{l_3 n_1 + i_3, k} = \delta_{i_1, i_3} \, \delta_{j_1, j_2} \, \delta_{l_2, l_3}$$

## 2. File Integrity Verification

- **Path**: `claim/5x5x6_m110_cr451_fv202_cn1208_ZT_reduced.json`
- **Byte size**: `57458` bytes
- **SHA-256**: `4f95dd2dbee2b93b8c8e102b863438193c7d6a5b899fcd0ec5a35661c115cd5d`
- **Dimensions & Rank**: `n = [5, 5, 6]`, `m = 110`, `z2 = false`
- **Declared Complexity**: `reduced = 451`, `naive = 1208`

## 3. Independent Verification Before Reading Author Code

Before inspecting `claim/verify_slp.py`, I wrote and ran an independent Python SLP verifier from the mathematical definition:

1. **DAG Acyclicity, Ternary Coefficient, and Disjointness Audit**:
   - Verified that every term in `u_fresh` (`48` forms), `u` (`110` forms), `v_fresh` (`56` forms), `v` (`110` forms), `w_fresh` (`98` forms), and `w` (`30` forms) has integer coefficient strictly in `{-1, 1}`, references only strictly earlier variable indices within its own section (`0 le idx le var_id - 1`), has no duplicate variable indices within any single linear form, and shares no variables across `U`, `V`, `W`.
2. **Independent Addition and Fresh-Variable Count**:
   - Recounted reduced additions `cr = sum(len(form) - 1)`:
     - `cr(U) = 119` (`fv(U) = 48`)
     - `cr(V) = 124` (`fv(V) = 56`)
     - `cr(W) = 208` (`fv(W) = 98`)
     - **Total reduced additions**: `cr = 119 + 124 + 208 = 451` (matches claimed `cr = 451` exactly).
     - **Total fresh variables**: `fv = 48 + 56 + 98 = 202` (matches claimed `fv = 202` exactly).
   - Recounted expanded nonzeros and naive additions `cn = sum(max(0, nnz(row) - 1))`:
     - `nnz(U) = 489` (`cn(U) = 379`), `nnz(V) = 487` (`cn(V) = 377`), `nnz(W) = 482` (`cn(W) = 452`).
     - **Total naive additions**: `cn = 379 + 377 + 452 = 1208` (matches claimed `cn = 1208` exactly).
3. **Exhaustive Symbolic Brent Equation Verification over Z**:
   - Expanded all linear forms over `Z` and checked all `25 * 30 * 30 = 22500` Brent equations over `Z`.
   - Result: `total_eq = 22500`, `bad_eq = 0` (zero error on every bilinear monomial over `Z`).
4. **Step-by-Step Integer Matrix Multiplication Check**:
   - Evaluated the straight-line program step-by-step on deterministic integer matrices `A in Z^{5 x 5}` (`A_{i,j} = 3^{i n_2 + j} + (i+1)(j+2)`) and `B in Z^{5 x 6}` (`B_{j,l} = 5^{j n_3 + l} + (j+2)(l+3)`).
   - Confirmed that the step-by-step SLP output `C_SLP` equals `A * B` entrywise over `Z` across all `30` output entries (`matmul_ok = True`).
5. **1-Entry Corruption Negative Test**:
   - Flipped a single coefficient sign in `u[0][0]` (`value -> -value`).
   - Independent verifier rejected the corrupted SLP (`bad_eq = 144` mismatched Brent equations, `matmul_ok = False`).
   - Author's `claim/verify_slp.py` also rejected the corrupted SLP (`rc = 1`, `FAIL: claim/5x5x6_m110_cr451_fv202_cn1208_ZT_reduced.json (corrupted) | Symbolic bilinear identity failed over Z (144 mismatched monomials)`).

## 4. Reproduction of Author Verification Command

Executed the command from `claim/REPRODUCE.md`:
```
python3 claim/verify_slp.py claim/5x5x6_m110_cr451_fv202_cn1208_ZT_reduced.json
```
Output (`exit 0`):
```
PASS: claim/5x5x6_m110_cr451_fv202_cn1208_ZT_reduced.json | format=5x5x6 m=110 cr=451 (U=119, V=124, W=208) fv=202 cn=1208
```
All temporary files created during verification were cleaned up.

pass: true
