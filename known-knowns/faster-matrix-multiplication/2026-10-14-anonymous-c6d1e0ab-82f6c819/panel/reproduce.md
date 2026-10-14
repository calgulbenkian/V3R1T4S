# REPRODUCE Skeptic Report — Format 13x14x15 Rank 1646 over Q

role: reproduce
skeptic: astra
context: subagent
context: subagent (astra)

## 1. Quoted Definition and Claimed Object

From `claim/CLAIM.md`:
> Object: claim/13x14x15_r1646_Q.json (SHA-256 82f6c819ed1d02c0bd1aad307a76b7bea80f2852aeab041132f584c6e1800be2)
> Format: 13x14x15, Ring: Q, Rank: 1646, Total Brent equations: 7452900

From `claim/target.md` (Success Criterion):
> Success means an explicit bilinear scheme (U, V, W coefficient matrices or an equivalent list of rank-one terms) for a format (n,m,p) with max(n,m,p) le 16 and sorted(n,m,p) not in {(3,3,3),(4,4,4)}, whose number of rank-one terms r is STRICTLY LESS (direction: min) than ALL of: the rank listed for the sorted format in fmm_sota.json, the rank on fmm.univ-lille.fr, the minimum over the ZT/Z/Q columns for that format in Perminov's README.md, and the lowest rank for that format in MerlijnW70/fmm-schemes (every one re-fetched live immediately before claiming; the scheme beats the minimum over all four). The scheme must be verified in exact arithmetic (integers/fractions, or mod p for GF(p)) over the ring it claims...

Mathematical definition of the Brent equations for format `(n1, n2, n3) = (13, 14, 15)` and rank `r = 1646` over `Q`:
For every triple of flattened matrix indices `a = i1 * n2 + j1` in `[0, n1*n2)`, `b = j2 * n3 + l2` in `[0, n2*n3)`, and `c = l3 * n1 + i3` in `[0, n3*n1)`:
$$\sum_{k=0}^{r-1} u_{k,a} \, v_{k,b} \, w_{k,c} = \delta_{i_1, i_3} \, \delta_{j_1, j_2} \, \delta_{l_2, l_3}$$
The total number of Brent equations is `(13 * 14) * (14 * 15) * (15 * 13) = 182 * 210 * 195 = 7,452,900`.

## 2. File Integrity Verification

- **Path**: `claim/13x14x15_r1646_Q.json`
- **Byte size**: `739,277` bytes
- **SHA-256**: `82f6c819ed1d02c0bd1aad307a76b7bea80f2852aeab041132f584c6e1800be2` (matches `claim/CLAIM.md` exactly)
- **Encoding**: `sparse_flat_pairs`, `n = [13, 14, 15]`, `m = 1646`, `ring = "Q"`
- **Nonzero support**: `nnz(U) = 38,917`, `nnz(V) = 30,838`, `nnz(W) = 34,141` (total `103,896` nonzeros across `1,646` non-empty rank-one factors).

## 3. Independent Verification Before Reading Author Code

Before inspecting `claim/verify_brent.py`, I wrote and ran an independent Python + compiled C verifier from the mathematical definition:

1. **Decoding & Structural Audit**:
   - Decoded `sparse_flat_pairs` for `u`, `v`, `w`, confirming `len(u) == len(v) == len(w) == 1646`, all indices within `[0, 182)`, `[0, 210)`, `[0, 195)`, and every factor `k in [0, 1646)` non-zero.
   - Parsed every rational coefficient as an exact reduced `(numerator, denominator)` integer pair.
2. **CRT Bound Derivation**:
   - Across all `k in [0, 1646)`, the least common multiple of all product denominators `den(u_{k,a}) * den(v_{k,b}) * den(w_{k,c})` is `L = 54,400`.
   - The sum of maximum term magnitudes is `S = sum_{k=0}^{1645} max_a |u_{k,a}| max_b |v_{k,b}| max_c |w_{k,c}| = 3,255,968,430 / 54,400 approx 59,852.3608`.
   - The theoretical CRT bound is `2 * L * (S + 1) = 6,512,045,660 approx 6.5120 * 10^9` (and even with an extra factor of `L`, `2 * L * (L * S + 1) = 354,249,473,984,000 approx 3.5425 * 10^14`).
   - Using two independent primes `p1 = 2147483647` and `p2 = 2147483629` (both coprime to `L = 54,400`), their product `p1 * p2 = 4,611,685,995,379,913,963 approx 4.6117 * 10^18` strictly exceeds `2 * L * (S + 1)` by nearly 9 orders of magnitude.
3. **Exhaustive Brent Equation Check**:
   - Evaluated all `182 * 210 * 195 = 7,452,900` Brent equations modulo `p1` and `p2` using `__uint128_t` accumulation.
   - Result: `total_eq=7452900 bad_eq=0` (`exit 0`). By the Chinese Remainder Theorem, all `7,452,900` Brent equations hold identically over `Q`.
4. **Exact Rational Matrix Multiplication Check**:
   - Constructed deterministic full-support rational test matrices `A in Q^{13 x 14}` and `B in Q^{14 x 15}` using Python `fractions.Fraction`.
   - Computed `C_scheme` via the `1,646` bilinear products and compared entrywise with `A * B` in exact `fractions.Fraction` arithmetic.
   - Result: `exact_Q_matmul = True` (exact zero residual across all `13 * 15 = 195` entries).
5. **1-Entry Corruption Negative Test**:
   - Perturbed a single entry of `U[0]` (`U[0][0] -> U[0][0] + 1`).
   - Independent verifier rejected the corrupted tensor (`rc = 1`, `bad_eq = 114`).
   - Author's `claim/verify_brent.py` also rejected the corrupted tensor (`rc = 1`, `FAIL prime=1073741789 a=0 b=2 c=6 got=1073741788 exp=0`).

## 4. Reproduction of Author Verification Command

Executed the command from `claim/REPRODUCE.md`:
```
python3 claim/verify_brent.py claim/13x14x15_r1646_Q.json
```
Output (`exit 0`):
```
PASS file=13x14x15_r1646_Q.json format=13x14x15 rank=1646 primes=2 log2_bound=49
```
All temporary C source and binary files created during verification were cleaned up.

pass: true
