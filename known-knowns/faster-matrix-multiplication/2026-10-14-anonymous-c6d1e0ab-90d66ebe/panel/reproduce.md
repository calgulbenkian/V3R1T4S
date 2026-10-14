# REPRODUCE Skeptic Report — Format 2x4x8 Rank 51 SLP in 187 Reduced Additions over Z

role: reproduce
skeptic: astra
context: subagent
context: subagent (astra)

## 1. Quoted Definition and Claimed Object

From `claim/CLAIM.md`:
> # Claim: Format `(2, 4, 8)` Rank 51 Straight-Line Program in 187 Additions over `Z`
> - **Target**: `fmm-additive-complexity-records`
> - **Format**: `(2, 4, 8)` (`2x4x8`)
> - **Rank**: `m = 51` (matches the best rank in `fmm_sota.json`)
> - **Ring**: `Z` (ternary straight-line program, coefficients in `{-1, 1}`)
> - **Claimed Reduced Additions (`cr`)**: `187` (`fv = 62` fresh variables, `cn = 354` naive additions)
> - **Previous Best (`addition_reduced_ZT`)**: `188` (`2x4x8_m51_cr188_cn354_ZT_reduced.json`, margin `-1`)
> - **Other Sources**: `reduced_known.json` = `none`, `matmulcatalog` `adds` = `+354`, `fmm.univ-lille.fr/2x4x8.html` = no complexity variant listed
> - **Object File**: `claim/2x4x8_m51_cr187_fv62_cn354_ZT_reduced.json`
> ## Definition Verified
> Every linear form in `u_fresh`, `u`, `v_fresh`, `v`, `w_fresh`, `w` is an acyclic sum/difference of already-computed quantities with coefficients in `{-1, 1}` (each binary `+/-` counted as 1 addition; negation is free), and the expanded bilinear forms compute the exact matrix product $C = A B$ over $\mathbb{Z}$ across all $n_1 n_2 n_3 n_1 n_2 n_3$ monomials.

From `claim/target.md` (Success Criterion):
> Success means an explicit straight-line program (list of linear forms over the inputs, r products, and linear forms producing the outputs) for a format (n,m,p) with max(n,m,p) le 8 and rank r equal to the best rank listed for that format in fmm_sota.json (re-fetched live), that (1) is verified symbolically to compute the full product A*B exactly over Z, and (2) uses a number of additions/subtractions STRICTLY LESS (direction: min) than the smallest reduced addition count for that format and rank in Perminov's live repository (the addition_reduced_ZT scheme file for the format, reduced_known.json, README and CHANGELOG) re-fetched live immediately before claiming, counted under Perminov's 'reduced' convention (each binary +/- between already-computed quantities counts one; multiplication by -1 is free; multiplication by any other scalar is not allowed in a ternary SLP), AND below any lower count published for that format and rank on the live Lille per-format page's cited complexity variant and in matmulcatalog's live COVERAGE.md 'adds' column.

Mathematical definition of the straight-line program (SLP) and Brent equations for format `(n1, n2, n3) = (2, 4, 8)` and rank `m = 51` over `Z`:
- In each section (`U` with `na = 8` inputs, `V` with `nb = 32` inputs, `W` with `m = 51` product inputs), intermediate variables in `u_fresh`, `v_fresh`, `w_fresh` and output linear forms in `u`, `v`, `w` are linear combinations `sum_t c_t * var[idx_t]` with ternary coefficients `c_t in {-1, 1}`, strictly prior indices `idx_t` (acyclic DAG), and distinct `idx_t` within each form.
- Each linear form `f` of length `len(f) ge 1` contributes `len(f) - 1` binary additions/subtractions to the reduced addition count `cr`.
- Upon expanding the DAGs to basis matrices `U in Z^{51 x 8}`, `V in Z^{51 x 32}`, `W in Z^{16 x 51}`, all `8 * 32 * 16 = 4096` Brent equations over `Z` must hold identically:
$$\sum_{k=0}^{50} U_{k, i_1 n_2 + j_1} \, V_{k, j_2 n_3 + l_2} \, W_{l_3 n_1 + i_3, k} = \delta_{i_1, i_3} \, \delta_{j_1, j_2} \, \delta_{l_2, l_3}$$

## 2. File Integrity Verification

- **Path**: `claim/2x4x8_m51_cr187_fv62_cn354_ZT_reduced.json`
- **Byte size**: `23291` bytes
- **SHA-256**: `90d66ebee7ee850df3b63def31ba158745a7eb6c74b3a38d651aebf514bdf388`
- **Dimensions & Rank**: `n = [2, 4, 8]`, `m = 51`, `z2 = false`
- **Declared Complexity**: `reduced = 187`, `naive = 354`

## 3. Independent Verification Before Reading Author Code

Before inspecting `claim/verify_slp.py`, I wrote and ran an independent Python SLP verifier from the mathematical definition:

1. **DAG Acyclicity, Ternary Coefficient, and Disjointness Audit**:
   - Verified that every term in `u_fresh` (`15` forms), `u` (`51` forms), `v_fresh` (`25` forms), `v` (`51` forms), `w_fresh` (`22` forms), and `w` (`16` forms) has integer coefficient strictly in `{-1, 1}`, references only strictly earlier variable indices within its own section (`0 le idx le var_id - 1`), has no duplicate variable indices within any single linear form, and shares no variables across `U`, `V`, `W`.
2. **Independent Addition and Fresh-Variable Count**:
   - Recounted reduced additions `cr = sum(len(form) - 1)`:
     - `cr(U) = 38` (`fv(U) = 15`)
     - `cr(V) = 71` (`fv(V) = 25`)
     - `cr(W) = 78` (`fv(W) = 22`)
     - **Total reduced additions**: `cr = 38 + 71 + 78 = 187` (matches claimed `cr = 187` exactly).
     - **Total fresh variables**: `fv = 15 + 25 + 22 = 62` (matches claimed `fv = 62` exactly).
   - Recounted expanded nonzeros and naive additions `cn = sum(max(0, nnz(row) - 1))`:
     - `nnz(U) = 123` (`cn(U) = 72`), `nnz(V) = 216` (`cn(V) = 165`), `nnz(W) = 133` (`cn(W) = 117`).
     - **Total naive additions**: `cn = 72 + 165 + 117 = 354` (matches claimed `cn = 354` exactly).
3. **Exhaustive Symbolic Brent Equation Verification over Z**:
   - Expanded all linear forms over `Z` and checked all `8 * 32 * 16 = 4096` Brent equations over `Z`.
   - Result: `total_eq = 4096`, `bad_eq = 0` (zero error on every bilinear monomial over `Z`).
4. **Step-by-Step Integer Matrix Multiplication Check**:
   - Evaluated the straight-line program step-by-step on deterministic integer matrices `A in Z^{2 x 4}` (`A_{i,j} = 3^{i n_2 + j} + (i+1)(j+2)`) and `B in Z^{4 x 8}` (`B_{j,l} = 5^{j n_3 + l} + (j+2)(l+3)`).
   - Confirmed that the step-by-step SLP output `C_SLP` equals `A * B` entrywise over `Z` across all `16` output entries (`matmul_ok = True`).
5. **1-Entry Corruption Negative Test**:
   - Flipped a single coefficient sign in `u[0][0]` (`value -> -value`).
   - Independent verifier rejected the corrupted SLP (`bad_eq = 6` mismatched Brent equations, `matmul_ok = False`).
   - Author's `claim/verify_slp.py` also rejected the corrupted SLP (`rc = 1`, `FAIL: claim/2x4x8_m51_cr187_fv62_cn354_ZT_reduced.json (corrupted) | Symbolic bilinear identity failed over Z (6 mismatched monomials)`).

## 4. Reproduction of Author Verification Command

Executed the command from `claim/REPRODUCE.md`:
```
python3 claim/verify_slp.py claim/2x4x8_m51_cr187_fv62_cn354_ZT_reduced.json
```
Output (`exit 0`):
```
PASS: claim/2x4x8_m51_cr187_fv62_cn354_ZT_reduced.json | format=2x4x8 m=51 cr=187 (U=38, V=71, W=78) fv=62 cn=354
```
All temporary files created during verification were cleaned up.

pass: true
