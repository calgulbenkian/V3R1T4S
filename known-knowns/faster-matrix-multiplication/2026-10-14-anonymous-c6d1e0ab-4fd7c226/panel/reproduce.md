# REPRODUCE Skeptic Report — Format 14x16x16 Rank 2119 over Q

role: reproduce
skeptic: astra
context: subagent
context: subagent (astra)

## 1. Quoted Definition and Claimed Object

From `claim/CLAIM.md`:
> Object: claim/14x16x16_r2119_Q.json (SHA-256 4fd7c2264911e65fcc6cf7074e6100202786a5de6c01b85b9ac6572fdf31ba56)
> Format: 14x16x16, Ring: Q, Rank: 2119, Total Brent equations: 12902400

From `claim/target.md` (Success Criterion):
> Success means an explicit bilinear scheme (U, V, W coefficient matrices or an equivalent list of rank-one terms) for a format (n,m,p) with max(n,m,p) le 16 and sorted(n,m,p) not in {(3,3,3),(4,4,4)}, whose number of rank-one terms r is STRICTLY LESS (direction: min) than ALL of: the rank listed for the sorted format in fmm_sota.json, the rank on fmm.univ-lille.fr, the minimum over the ZT/Z/Q columns for that format in Perminov's README.md, and the lowest rank for that format in MerlijnW70/fmm-schemes (every one re-fetched live immediately before claiming; the scheme beats the minimum over all four). The scheme must be verified in exact arithmetic (integers/fractions, or mod p for GF(p)) over the ring it claims...

Mathematical definition of the Brent equations for format `(n1, n2, n3) = (14, 16, 16)` and rank `r = 2119` over `Q`:
For every triple of flattened matrix indices `a = i1 * n2 + j1` in `[0, n1*n2)`, `b = j2 * n3 + l2` in `[0, n2*n3)`, and `c = l3 * n1 + i3` in `[0, n3*n1)`:
$$\sum_{k=0}^{r-1} u_{k,a} \, v_{k,b} \, w_{k,c} = \delta_{i_1, i_3} \, \delta_{j_1, j_2} \, \delta_{l_2, l_3}$$
Note on equation count: `claim/CLAIM.md` lists `Total Brent equations: 12902400` in its header line, which is a prose arithmetic typo (`225 * 256 * 224` instead of `224 * 256 * 224`); the exact number of Brent equations for `(14, 16, 16)` is `(14 * 16) * (16 * 16) * (16 * 14) = 224 * 256 * 224 = 12,845,056`, all of which are verified below.

## 2. File Integrity Verification

- **Path**: `claim/14x16x16_r2119_Q.json`
- **Byte size**: `905,718` bytes
- **SHA-256**: `4fd7c2264911e65fcc6cf7074e6100202786a5de6c01b85b9ac6572fdf31ba56` (matches `claim/CLAIM.md` exactly)
- **Encoding**: `vocab_rle_v1`, `n = [14, 16, 16]`, `m = 2119`, `ring = "Q"`
- **Nonzero support**: `nnz(U) = 159,793`, `nnz(V) = 191,937`, `nnz(W) = 157,952` (total `509,682` nonzeros across `2,119` non-empty rank-one factors).

## 3. Independent Verification Before Reading Author Code

Before inspecting `claim/verify_brent.py`, I wrote and ran an independent Python + compiled C verifier from the mathematical definition:

1. **Decoding & Structural Audit**:
   - Decoded `vocab_rle_v1` for `u`, `v`, `w`, confirming `len(u) == len(v) == len(w) == 2119`, every RLE string expanding to exact width `224`, `256`, `224` respectively, and every factor `k in [0, 2119)` non-zero.
   - Parsed every rational vocabulary entry as an exact reduced `(numerator, denominator)` integer pair.
2. **CRT Bound Derivation**:
   - Across all `k in [0, 2119)`, the least common multiple of all product denominators `den(u_{k,a}) * den(v_{k,b}) * den(w_{k,c})` is `L = 29,030,400`.
   - The sum of maximum term magnitudes is `S = sum_{k=0}^{2118} max_a |u_{k,a}| max_b |v_{k,b}| max_c |w_{k,c}| = 373,229,652,922 / 29,030,400 approx 12,856.5109`.
   - The theoretical CRT bound is `2 * L * (S + 1) = 746,517,366,644 approx 7.4652 * 10^11`.
   - Using two independent primes `p1 = 2147483647` and `p2 = 2147483629` (both coprime to `L = 29,030,400`), their product `p1 * p2 = 4,611,685,995,379,913,963 approx 4.6117 * 10^18` strictly exceeds `2 * L * (S + 1)` by more than 6 orders of magnitude.
3. **Exhaustive Brent Equation Check**:
   - Evaluated all `224 * 256 * 224 = 12,845,056` Brent equations modulo `p1` and `p2` using `__uint128_t` accumulation.
   - Result: `total_eq=12845056 bad_eq=0` (`exit 0`). By the Chinese Remainder Theorem, all `12,845,056` Brent equations hold identically over `Q`.
4. **Exact Rational Matrix Multiplication Check**:
   - Constructed deterministic full-support rational test matrices `A in Q^{14 x 16}` and `B in Q^{16 x 16}` using Python `fractions.Fraction`.
   - Computed `C_scheme` via the `2,119` bilinear products and compared entrywise with `A * B` in exact `fractions.Fraction` arithmetic.
   - Result: `exact_Q_matmul = True` (exact zero residual across all `14 * 16 = 224` entries).
5. **1-Entry Corruption Negative Test**:
   - Perturbed a single entry of `U[0]` (`U[0][0]` changed to a different vocabulary entry).
   - Independent verifier rejected the corrupted tensor (`rc = 1`, `bad_eq = 48`).
   - Author's `claim/verify_brent.py` also rejected the corrupted tensor (`rc = 1`, `FAIL prime=1073741789 a=0 b=0 c=15 got=290805067 exp=0`, and also rejects unmerged RLE corruptions with `rc = 1`).

## 4. Reproduction of Author Verification Command

Executed the command from `claim/REPRODUCE.md`:
```
python3 claim/verify_brent.py claim/14x16x16_r2119_Q.json
```
Output (`exit 0`):
```
PASS file=14x16x16_r2119_Q.json format=14x16x16 rank=2119 primes=3 log2_bound=65
```
All temporary C source and binary files created during verification were cleaned up.

pass: true
