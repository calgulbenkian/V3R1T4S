# REPRODUCE Skeptic Report — Format 4x13x15 Rank 535 (ZT Ring Upgrade)

role: reproduce
skeptic: astra
context: subagent
context: subagent (astra)

## 1. Quoted Definition and Claimed Object

From `claim/CLAIM.md`:
> # Claim: Exact ZT Ring Upgrade for Format (4, 13, 15) at Rank 535
> ## 1. Statement of Claimed Result
> We provide an explicit ternary (ZT, coefficients in {-1, 0, 1}) bilinear matrix multiplication scheme `claim/4x13x15_m535_ZT.json` (`338479` bytes, SHA-256 `937d96a3adc5b64e84e86d8a0d9bc0b7e160f22f00f3ca4af7239abb76a281f2`) for matrix format `(4, 13, 15)` (`4x13x15`) with rank **`535`** over $\mathbb{Z}$.
> - **Target ID**: `fmm-ternary-integer-ring-upgrade`
> - **Matrix Format**: `(4, 13, 15)` (`max(n, m, p) = 15 le 16`, `sorted(n, m, p) != (4, 4, 4)`)
> - **Coefficient Class**: `ZT` (maximum absolute entry `1`)
> - **Claimed Rank**: **`535`**
> - **Live Reference Bounds (`dronperminov/FastMatrixMultiplication` & `MerlijnW70/fmm-schemes`)**:
>   - Live `ZT` rank: `536`
>   - Live `Z` rank: `536`
>   - Live `Q` rank: `520`
>   - Live `fmm_sota.json` best rank: `520`
> - **Improvement**: Saves **`1`** multiplications strictly below the best known `ZT` rank (`535 strictly less than 536`) while satisfying `535 ge 520` (ring upgrade regime).
> ## 2. Exact Bilinear Brent Equations Definition
> Let $(n_1, n_2, n_3) = (4, 13, 15)$. The scheme consists of three integer factor matrices $U \in \mathbb{Z}^{535 \times 52}$, $V \in \mathbb{Z}^{535 \times 195}$, and $W \in \mathbb{Z}^{535 \times 60}$ satisfying the exact integer Brent equations for all $i_1, i_2 \in [n_1], k_1, k_2 \in [n_2], j_1, j_2 \in [n_3]$:
> $$\sum_{r=0}^{535-1} U_{r, (i_1, k_1)} V_{r, (k_2, j_1)} W_{r, (j_2, i_2)} = \delta_{k_1, k_2} \delta_{j_1, j_2} \delta_{i_2, i_1}$$
> over $\mathbb{Z}$ (where $W$ indexes $C^T$ in row-major order $j \cdot n_1 + i$).
> ## 3. Construction Method
> Derived via exact subspace homomorphism substitution (`Q to Z / ZT`) combined with 10 blocks of (2, 4, 5) with equivariant GL(Z) gauge elimination reducing non-ternary triads from 45 to 2, followed by single-factor triad splitting into {-1, 0, 1}.

From `claim/target.md` (Success Criterion):
> Success means an explicit bilinear scheme for a format (n,m,p) with max(n,m,p) le 16 and sorted(n,m,p) != (4,4,4), whose coefficients all lie in {-1,0,1} (ternary, 'ZT') or all in Z (integer), with rank r such that (1) r is STRICTLY LESS (direction: min) than the 'ZT rank' (for a ternary claim) or the 'Z rank' (for an integer claim) listed for that format in dronperminov/FastMatrixMultiplication/master/README.md re-fetched live immediately before claiming; (2) r is GREATER THAN OR EQUAL to the minimum over the live ZT/Z/Q columns for that format and to the live fmm_sota.json rank, i.e. the scheme does NOT beat the overall best rank (a scheme that does is the catalogue target fmm-catalogue-small-format-rank, never both); (3) no scheme of rank le r in the same coefficient class already exists in the live schemes/results/ZT (or /Z) directory of that repository or in MerlijnW70/fmm-schemes; (4) the Brent equations are verified exactly over Z with integer arithmetic (so the scheme is valid over every ring), not merely mod 2.

Mathematical definition of the exact integer Brent equations for format `(n1, n2, n3) = (4, 13, 15)` and rank `r = 535` over `Z`:
For all `i1, i2 in [0, 4)`, `k1, k2 in [0, 13)`, and `j1, j2 in [0, 15)`, with flattened row-major indices `a = i1 * 13 + k1 in [0, 52)`, `b = k2 * 15 + j1 in [0, 195)`, and `c = j2 * 4 + i2 in [0, 60)`:
$$\sum_{q=0}^{534} U_{q, (i_1, k_1)} \, V_{q, (k_2, j_1)} \, W_{q, (j_2, i_2)} = \delta_{k_1, k_2} \, \delta_{j_1, j_2} \, \delta_{i_2, i_1}$$
over `Z`, across all `52 * 195 * 60 = 608400` equations.

## 2. File Integrity Verification

- **Path**: `claim/4x13x15_m535_ZT.json`
- **Byte size**: `338479` bytes
- **SHA-256**: `937d96a3adc5b64e84e86d8a0d9bc0b7e160f22f00f3ca4af7239abb76a281f2` (matches `claim/CLAIM.md` and `claim/REPRODUCE.md` exactly)
- **Dimensions & Rank**: `n = [4, 13, 15]`, `m = 535`, active non-zero rank-1 terms `r = 535`
- **Observed Coefficient Set**: `[-1, 0, 1]` (subset of `{-1, 0, 1}`, `max_abs = 1`, class `ZT`)
- **Nonzero Support**: `nnz(U) = 3917`, `nnz(V) = 7319`, `nnz(W) = 2874` (total `14110` nonzeros)

## 3. Independent Verification Before Reading Author Code

Before inspecting `claim/verify_z_brent.py`, I wrote and ran an independent Python + compiled C verifier from the mathematical definition:

1. **Integrality, Coefficient Class, and Rank Audit**:
   - Parsed `u`, `v`, `w` from `claim/4x13x15_m535_ZT.json`, confirming `len(u) == len(v) == len(w) == 535`, row widths `(52, 195, 60)`, and every entry of exact Python type `int` (not `bool`, `float`, or `str`).
   - Confirmed the exact set of distinct entries is `[-1, 0, 1]` (`max_abs = 1`), strictly within `{-1, 0, 1}` for class `ZT`.
   - Confirmed all `535` rank-1 terms have non-zero `U_q`, `V_q`, and `W_q` vectors (`active_r = 535 == 535`).
2. **Exhaustive Exact Integer Brent Equation Verification**:
   - Evaluated all `52 * 195 * 60 = 608400` Brent equations in exact 64-bit signed integer (`int64_t`) arithmetic in compiled C.
   - Result: `total_eq=608400 bad_eq=0` (`rc = 0`, zero mismatched equations across all `608400` triples).
3. **Exact Integer Matrix Multiplication Check**:
   - Evaluated the bilinear scheme on deterministic full-support integer test matrices `A in Z^{4 x 13}` and `B in Z^{13 x 15}` and compared entrywise with `A * B` over `Z`.
   - Result: `matmul_ok = True` (exact equality across all `60` output entries).
4. **1-Entry Corruption Negative Test**:
   - Perturbed a single non-zero entry `U[0][42]` from `1` to `0`.
   - Independent C+Python verifier rejected the corrupted tensor (`rc = 1`, `total_eq=608400 bad_eq=136`).
   - Author's `claim/verify_z_brent.py` also rejected the corrupted tensor (`rc = 1`, `Brent mismatch at a=42, b=23, c=5: got -1, expected 0`).

## 4. Reproduction of Author Verification Command

Executed the command from `claim/REPRODUCE.md`:
```
python3 claim/verify_z_brent.py claim/4x13x15_m535_ZT.json
```
Output (`exit 0`):
```
PASS: claim/4x13x15_m535_ZT.json | format=4x13x15 class=ZT max_abs=1 rank=535 | ref(ZT)=536 saved=1 best_overall=520 valid_ring_upgrade=True
```
All temporary C and Python verification files created during the audit were deleted.

pass: true
