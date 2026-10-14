# REPRODUCE Skeptic Report — Format 9x11x14 Rank 889 (Z Ring Upgrade)

role: reproduce
skeptic: astra
context: subagent
context: subagent (astra)

## 1. Quoted Definition and Claimed Object

From `claim/CLAIM.md`:
> # Claim: Exact Z Ring Upgrade for Format (9, 11, 14) at Rank 889
> ## 1. Statement of Claimed Result
> We provide an explicit integer (Z, coefficients in {-2, -1, 0, 1, 2}) bilinear matrix multiplication scheme `claim/9x11x14_m889_Z.json` (`693112` bytes, SHA-256 `e25137a39f9a642d3a93ae58337d80703f5e45c2efc48e96207d7e61aeb101e5`) for matrix format `(9, 11, 14)` (`9x11x14`) with rank **`889`** over $\mathbb{Z}$.
> - **Target ID**: `fmm-ternary-integer-ring-upgrade`
> - **Matrix Format**: `(9, 11, 14)` (`max(n, m, p) = 14 le 16`, `sorted(n, m, p) != (4, 4, 4)`)
> - **Coefficient Class**: `Z` (maximum absolute entry `2`)
> - **Claimed Rank**: **`889`**
> - **Live Reference Bounds (`dronperminov/FastMatrixMultiplication` & `MerlijnW70/fmm-schemes`)**:
>   - Live `ZT` rank: `900`
>   - Live `Z` rank: `900`
>   - Live `Q` rank: `882`
>   - Live `fmm_sota.json` best rank: `882`
> - **Improvement**: Saves **`11`** multiplications strictly below the best known `Z` rank (`889 strictly less than 900`) while satisfying `889 ge 882` (ring upgrade regime).
> ## 2. Exact Bilinear Brent Equations Definition
> Let $(n_1, n_2, n_3) = (9, 11, 14)$. The scheme consists of three integer factor matrices $U \in \mathbb{Z}^{889 \times 99}$, $V \in \mathbb{Z}^{889 \times 154}$, and $W \in \mathbb{Z}^{889 \times 126}$ satisfying the exact integer Brent equations for all $i_1, i_2 \in [n_1], k_1, k_2 \in [n_2], j_1, j_2 \in [n_3]$:
> $$\sum_{r=0}^{889-1} U_{r, (i_1, k_1)} V_{r, (k_2, j_1)} W_{r, (j_2, i_2)} = \delta_{k_1, k_2} \delta_{j_1, j_2} \delta_{i_2, i_1}$$
> over $\mathbb{Z}$ (where $W$ indexes $C^T$ in row-major order $j \cdot n_1 + i$).
> ## 3. Construction Method
> Derived via exact subspace homomorphism substitution (`Q to Z / ZT`) combined with 4 blocks of (3, 4, 7) with equivariant GL(Z) gauge elimination.

From `claim/target.md` (Success Criterion):
> Success means an explicit bilinear scheme for a format (n,m,p) with max(n,m,p) le 16 and sorted(n,m,p) != (4,4,4), whose coefficients all lie in {-1,0,1} (ternary, 'ZT') or all in Z (integer), with rank r such that (1) r is STRICTLY LESS (direction: min) than the 'ZT rank' (for a ternary claim) or the 'Z rank' (for an integer claim) listed for that format in dronperminov/FastMatrixMultiplication/master/README.md re-fetched live immediately before claiming; (2) r is GREATER THAN OR EQUAL to the minimum over the live ZT/Z/Q columns for that format and to the live fmm_sota.json rank, i.e. the scheme does NOT beat the overall best rank (a scheme that does is the catalogue target fmm-catalogue-small-format-rank, never both); (3) no scheme of rank le r in the same coefficient class already exists in the live schemes/results/ZT (or /Z) directory of that repository or in MerlijnW70/fmm-schemes; (4) the Brent equations are verified exactly over Z with integer arithmetic (so the scheme is valid over every ring), not merely mod 2.

Mathematical definition of the exact integer Brent equations for format `(n1, n2, n3) = (9, 11, 14)` and rank `r = 889` over `Z`:
For all `i1, i2 in [0, 9)`, `k1, k2 in [0, 11)`, and `j1, j2 in [0, 14)`, with flattened row-major indices `a = i1 * 11 + k1 in [0, 99)`, `b = k2 * 14 + j1 in [0, 154)`, and `c = j2 * 9 + i2 in [0, 126)`:
$$\sum_{q=0}^{888} U_{q, (i_1, k_1)} \, V_{q, (k_2, j_1)} \, W_{q, (j_2, i_2)} = \delta_{k_1, k_2} \, \delta_{j_1, j_2} \, \delta_{i_2, i_1}$$
over `Z`, across all `99 * 154 * 126 = 1920996` equations.

## 2. File Integrity Verification

- **Path**: `claim/9x11x14_m889_Z.json`
- **Byte size**: `693112` bytes
- **SHA-256**: `e25137a39f9a642d3a93ae58337d80703f5e45c2efc48e96207d7e61aeb101e5` (matches `claim/CLAIM.md` and `claim/REPRODUCE.md` exactly)
- **Dimensions & Rank**: `n = [9, 11, 14]`, `m = 889`, active non-zero rank-1 terms `r = 889`
- **Observed Coefficient Set**: `[-2, -1, 0, 1, 2]` (subset of `{-2, -1, 0, 1, 2}`, `max_abs = 2`, class `Z`)
- **Nonzero Support**: `nnz(U) = 11217`, `nnz(V) = 9529`, `nnz(W) = 6520` (total `27266` nonzeros)

## 3. Independent Verification Before Reading Author Code

Before inspecting `claim/verify_z_brent.py`, I wrote and ran an independent Python + compiled C verifier from the mathematical definition:

1. **Integrality, Coefficient Class, and Rank Audit**:
   - Parsed `u`, `v`, `w` from `claim/9x11x14_m889_Z.json`, confirming `len(u) == len(v) == len(w) == 889`, row widths `(99, 154, 126)`, and every entry of exact Python type `int` (not `bool`, `float`, or `str`).
   - Confirmed the exact set of distinct entries is `[-2, -1, 0, 1, 2]` (`max_abs = 2`), strictly within `{-2, -1, 0, 1, 2}` for class `Z`.
   - Confirmed all `889` rank-1 terms have non-zero `U_q`, `V_q`, and `W_q` vectors (`active_r = 889 == 889`).
2. **Exhaustive Exact Integer Brent Equation Verification**:
   - Evaluated all `99 * 154 * 126 = 1920996` Brent equations in exact 64-bit signed integer (`int64_t`) arithmetic in compiled C.
   - Result: `total_eq=1920996 bad_eq=0` (`rc = 0`, zero mismatched equations across all `1920996` triples).
3. **Exact Integer Matrix Multiplication Check**:
   - Evaluated the bilinear scheme on deterministic full-support integer test matrices `A in Z^{9 x 11}` and `B in Z^{11 x 14}` and compared entrywise with `A * B` over `Z`.
   - Result: `matmul_ok = True` (exact equality across all `126` output entries).
4. **1-Entry Corruption Negative Test**:
   - Perturbed a single non-zero entry `U[0][39]` from `1` to `0`.
   - Independent C+Python verifier rejected the corrupted tensor (`rc = 1`, `total_eq=1920996 bad_eq=400`).
   - Author's `claim/verify_z_brent.py` also rejected the corrupted tensor (`rc = 1`, `Brent mismatch at a=39, b=0, c=9: got 1, expected 0`).

## 4. Reproduction of Author Verification Command

Executed the command from `claim/REPRODUCE.md`:
```
python3 claim/verify_z_brent.py claim/9x11x14_m889_Z.json
```
Output (`exit 0`):
```
PASS: claim/9x11x14_m889_Z.json | format=9x11x14 class=Z max_abs=2 rank=889 | ref(Z)=900 saved=11 best_overall=882 valid_ring_upgrade=True
```
All temporary C and Python verification files created during the audit were deleted.

pass: true
