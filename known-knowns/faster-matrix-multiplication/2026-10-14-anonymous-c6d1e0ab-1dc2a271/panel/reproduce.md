# REPRODUCE Skeptic Report — Format 2x8x8 Rank 100 SLP in 423 Reduced Additions over Z

role: reproduce
skeptic: astra
context: subagent
context: subagent (astra)

## 1. Quoted Definition and Claimed Object

From `claim/CLAIM.md`:
> # Claim: Format `(2, 8, 8)` Rank 100 Straight-Line Program in 423 Additions over `Z`
> - **Target**: `fmm-additive-complexity-records`
> - **Format**: `(2, 8, 8)` (`2x8x8`)
> - **Rank**: `m = 100` (matches the best rank in `fmm_sota.json`)
> - **Ring**: `Z` (ternary straight-line program, coefficients in `{-1, 1}`)
> - **Claimed Reduced Additions (`cr`)**: `423` (`fv = 94` fresh variables, `cn = 608` naive additions)
> - **Previous Best (`addition_reduced_ZT`)**: `424` (`2x8x8_m100_cr424_cn608_ZT_reduced.json`, margin `-1`)
> - **Other Sources**: `reduced_known.json` = `none`, `matmulcatalog` `adds` = `unlisted`, `fmm.univ-lille.fr/2x8x8.html` = no complexity variant listed
> - **Object File**: `claim/2x8x8_m100_cr423_fv94_cn608_ZT_reduced.json`
> ## Definition Verified
> Every linear form in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` is an acyclic sum/difference of already-computed quantities with coefficients in `{-1, 1}` (each binary `+/-` counted as 1 addition; negation is free), and the expanded bilinear forms compute the exact matrix product $C = A B$ over $\mathbb{Z}$ across all $n_1 n_2 n_3 n_1 n_2 n_3$ monomials.

From `claim/target.md` (Success Criterion):
> Success means an explicit straight-line program (list of linear forms over the inputs, r products, and linear forms producing the outputs) for a format (n,m,p) with max(n,m,p) le 8 and rank r equal to the best rank listed for that format in fmm_sota.json (re-fetched live), that (1) is verified symbolically to compute the full product A*B exactly over Z, and (2) uses a number of additions/subtractions STRICTLY LESS (direction: min) than the smallest reduced addition count for that format and rank in Perminov's live repository (the addition_reduced_ZT scheme file for the format, reduced_known.json, README and CHANGELOG) re-fetched live immediately before claiming, counted under Perminov's 'reduced' convention (each binary +/- between already-computed quantities counts one; multiplication by -1 is free; multiplication by any other scalar is not allowed in a ternary SLP), AND below any lower count published for that format and rank on the live Lille per-format page's cited complexity variant and in matmulcatalog's live COVERAGE.md 'adds' column.

Mathematical definition of the straight-line program (SLP) and Brent equations for format `(n1, n2, n3) = (2, 8, 8)` and rank `m = 100` over `Z`:
- In each section (`U` with `na = 16` inputs, `V` with `nb = 64` inputs, `W` with `m = 100` product inputs), intermediate variables in `u_fresh`, `v_fresh`, `w_fresh` and output linear forms in `u`, `v`, `w` are linear combinations `sum_t c_t * var[idx_t]` with ternary coefficients `c_t in {-1, 1}`, strictly prior indices `idx_t` (acyclic DAG), and distinct `idx_t` within each form.
- Each linear form `f` of length `len(f) ge 1` contributes `len(f) - 1` binary additions/subtractions to the reduced addition count `cr`.
- Upon expanding the DAGs to basis matrices `U in Z^{100 x 16}`, `V in Z^{100 x 64}`, `W in Z^{16 x 100}`, all `16 * 64 * 16 = 16384` Brent equations over `Z` must hold identically:
$$\sum_{k=0}^{99} U_{k, i_1 n_2 + j_1} \, V_{k, j_2 n_3 + l_2} \, W_{l_3 n_1 + i_3, k} = \delta_{i_1, i_3} \, \delta_{j_1, j_2} \, \delta_{l_2, l_3}$$

## 2. File Integrity Verification

- **Path**: `claim/2x8x8_m100_cr423_fv94_cn608_ZT_reduced.json`
- **Byte size**: `45913` bytes
- **SHA-256**: `1dc2a27122c50cbe852e77aab752edc1d1ec1fc2f6cb9f28a6ea47926acc1a3e`
- **Dimensions & Rank**: `n = [2, 8, 8]`, `m = 100`, `z2 = false`
- **Declared Complexity**: `reduced = 423`, `naive = 608`

## 3. Independent Verification Before Reading Author Code

Before inspecting `claim/verify_slp.py`, I wrote and ran an independent Python SLP verifier from the mathematical definition:

1. **DAG Acyclicity, Ternary Coefficient, and Disjointness Audit**:
   - Verified that every term in `u_fresh` (`33` forms), `u` (`100` forms), `v_fresh` (`16` forms), `v` (`100` forms), `w_fresh` (`45` forms), and `w` (`16` forms) has integer coefficient strictly in `{-1, 1}`, references only strictly earlier variable indices within its own section (`0 le idx le var_id - 1`), has no duplicate variable indices within any single linear form, and shares no variables across `U`, `V`, `W`.
2. **Independent Addition and Fresh-Variable Count**:
   - Recounted reduced additions `cr = sum(len(form) - 1)`:
     - `cr(U) = 92` (`fv(U) = 33`)
     - `cr(V) = 154` (`fv(V) = 16`)
     - `cr(W) = 177` (`fv(W) = 45`)
     - **Total reduced additions**: `cr = 92 + 154 + 177 = 423` (matches claimed `cr = 423` exactly).
     - **Total fresh variables**: `fv = 33 + 16 + 45 = 94` (matches claimed `fv = 94` exactly).
   - Recounted expanded nonzeros and naive additions `cn = sum(max(0, nnz(row) - 1))`:
     - `nnz(U) = 264` (`cn(U) = 164`), `nnz(V) = 296` (`cn(V) = 196`), `nnz(W) = 264` (`cn(W) = 248`).
     - **Total naive additions**: `cn = 164 + 196 + 248 = 608` (matches claimed `cn = 608` exactly).
3. **Exhaustive Symbolic Brent Equation Verification over Z**:
   - Expanded all linear forms over `Z` and checked all `16 * 64 * 16 = 16384` Brent equations over `Z`.
   - Result: `total_eq = 16384`, `bad_eq = 0` (zero error on every bilinear monomial over `Z`).
4. **Step-by-Step Integer Matrix Multiplication Check**:
   - Evaluated the straight-line program step-by-step on deterministic integer matrices `A in Z^{2 x 8}` (`A_{i,j} = 3^{i n_2 + j} + (i+1)(j+2)`) and `B in Z^{8 x 8}` (`B_{j,l} = 5^{j n_3 + l} + (j+2)(l+3)`).
   - Confirmed that the step-by-step SLP output `C_SLP` equals `A * B` entrywise over `Z` across all `16` output entries (`matmul_ok = True`).
5. **1-Entry Corruption Negative Test**:
   - Flipped a single coefficient sign in `u[0][0]` (`value -> -value`).
   - Independent verifier rejected the corrupted SLP (`bad_eq = 12` mismatched Brent equations, `matmul_ok = False`).
   - Author's `claim/verify_slp.py` also rejected the corrupted SLP (`rc = 1`, `FAIL: claim/2x8x8_m100_cr423_fv94_cn608_ZT_reduced.json (corrupted) | Symbolic bilinear identity failed over Z (12 mismatched monomials)`).

## 4. Reproduction of Author Verification Command

Executed the command from `claim/REPRODUCE.md`:
```
python3 claim/verify_slp.py claim/2x8x8_m100_cr423_fv94_cn608_ZT_reduced.json
```
Output (`exit 0`):
```
PASS: claim/2x8x8_m100_cr423_fv94_cn608_ZT_reduced.json | format=2x8x8 m=100 cr=423 (U=92, V=154, W=177) fv=94 cn=608
```
All temporary files created during verification were cleaned up.

pass: true
