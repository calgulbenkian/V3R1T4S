# REPRODUCE Skeptic Report — Format 13x13x14 Rank 1499 over Q

role: reproduce
skeptic: astra
context: subagent
context: subagent (astra)

## 1. Quoted Definition and Claimed Object

From `claim/CLAIM.md`:
> Object: claim/13x13x14_r1499_Q.json (SHA-256 d6ed9de8a92340b0c420c42344c915b8232853aef5ecee342fef7fa0c558a5f3)
> Format: 13x13x14, Ring: Q, Rank: 1499, Total Brent equations: 6147282

From `claim/target.md` (Success Criterion):
> Success means an explicit bilinear scheme (U, V, W coefficient matrices or an equivalent list of rank-one terms) for a format (n,m,p) with max(n,m,p) le 16 and sorted(n,m,p) not in {(3,3,3),(4,4,4)}, whose number of rank-one terms r is STRICTLY LESS (direction: min) than ALL of: the rank listed for the sorted format in fmm_sota.json, the rank on fmm.univ-lille.fr, the minimum over the ZT/Z/Q columns for that format in Perminov's README.md, and the lowest rank for that format in MerlijnW70/fmm-schemes (every one re-fetched live immediately before claiming; the scheme beats the minimum over all four). The scheme must be verified in exact arithmetic (integers/fractions, or mod p for GF(p)) over the ring it claims...

Mathematical definition of the Brent equations for format `(n1, n2, n3) = (13, 13, 14)` and rank `r = 1499` over `Q`:
For every triple of flattened matrix indices `a = i1 * n2 + j1` in `[0, n1*n2)`, `b = j2 * n3 + l2` in `[0, n2*n3)`, and `c = l3 * n1 + i3` in `[0, n3*n1)`:
$$\sum_{k=0}^{r-1} u_{k,a} \, v_{k,b} \, w_{k,c} = \delta_{i_1, i_3} \, \delta_{j_1, j_2} \, \delta_{l_2, l_3}$$
Note on equation count: `claim/CLAIM.md` lists `Total Brent equations: 6147282` in its header line, which is a prose arithmetic typo; the exact number of Brent equations for `(13, 13, 14)` is `(13 * 13) * (13 * 14) * (14 * 13) = 169 * 182 * 182 = 5,597,956`, all of which are verified below.

## 2. File Integrity Verification

- **Path**: `claim/13x13x14_r1499_Q.json`
- **Byte size**: `832,267` bytes
- **SHA-256**: `d6ed9de8a92340b0c420c42344c915b8232853aef5ecee342fef7fa0c558a5f3` (matches `claim/CLAIM.md` exactly)
- **Encoding**: `sparse_flat_pairs`, `n = [13, 13, 14]`, `m = 1499`, `ring = "Q"`
- **Nonzero support**: `nnz(U) = 35,048`, `nnz(V) = 46,772`, `nnz(W) = 37,609` (total `119,429` nonzeros across `1,499` non-empty rank-one factors).

## 3. Independent Verification Before Reading Author Code

Before inspecting `claim/verify_brent.py`, I wrote and ran an independent Python + compiled C verifier from the mathematical definition:

1. **Decoding & Structural Audit**:
   - Decoded `sparse_flat_pairs` for `u`, `v`, `w`, confirming `len(u) == len(v) == len(w) == 1499`, all indices within `[0, 169)`, `[0, 182)`, `[0, 182)`, and every factor `k in [0, 1499)` non-zero.
   - Parsed every rational coefficient as an exact reduced `(numerator, denominator)` integer pair.
2. **CRT Bound Derivation**:
   - Across all `k in [0, 1499)`, the least common multiple of all product denominators `den(u_{k,a}) * den(v_{k,b}) * den(w_{k,c})` is `L = 54,400`.
   - The sum of maximum term magnitudes is `S = sum_{k=0}^{1498} max_a |u_{k,a}| max_b |v_{k,b}| max_c |w_{k,c}| = 6,150,690,391 / 54,400 approx 113,064.1616`.
   - The theoretical CRT bound is `2 * L * (S + 1) = 12,301,489,582 approx 1.2301 * 10^10` (and even with an extra factor of `L`, `2 * L * (L * S + 1) = 669,195,223,340,800 approx 6.6920 * 10^14`).
   - Using two independent primes `p1 = 2147483647` and `p2 = 2147483629` (both coprime to `L = 54,400`), their product `p1 * p2 = 4,611,685,995,379,913,963 approx 4.6117 * 10^18` strictly exceeds `2 * L * (S + 1)` by more than 8 orders of magnitude.
3. **Exhaustive Brent Equation Check**:
   - Evaluated all `169 * 182 * 182 = 5,597,956` Brent equations modulo `p1` and `p2` using `__uint128_t` accumulation.
   - Result: `total_eq=5597956 bad_eq=0` (`exit 0`). By the Chinese Remainder Theorem, all `5,597,956` Brent equations hold identically over `Q`.
4. **Exact Rational Matrix Multiplication Check**:
   - Constructed deterministic full-support rational test matrices `A in Q^{13 x 13}` and `B in Q^{13 x 14}` using Python `fractions.Fraction`.
   - Computed `C_scheme` via the `1,499` bilinear products and compared entrywise with `A * B` in exact `fractions.Fraction` arithmetic.
   - Result: `exact_Q_matmul = True` (exact zero residual across all `13 * 14 = 182` entries).
5. **1-Entry Corruption Negative Test**:
   - Perturbed a single entry of `U[0]` (`U[0][0] -> U[0][0] + 1`).
   - Independent verifier rejected the corrupted tensor (`rc = 1`, `bad_eq = 68`).
   - Author's `claim/verify_brent.py` also rejected the corrupted tensor (`rc = 1`, `FAIL prime=1073741789 a=0 b=1 c=13 got=2 exp=1`).

## 4. Reproduction of Author Verification Command

Executed the command from `claim/REPRODUCE.md`:
```
python3 claim/verify_brent.py claim/13x13x14_r1499_Q.json
```
Output (`exit 0`):
```
PASS file=13x13x14_r1499_Q.json format=13x13x14 rank=1499 primes=2 log2_bound=50
```
All temporary C source and binary files created during verification were cleaned up.

pass: true
