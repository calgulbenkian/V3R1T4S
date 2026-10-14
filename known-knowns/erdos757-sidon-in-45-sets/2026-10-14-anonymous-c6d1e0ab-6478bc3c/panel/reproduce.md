# REPRODUCE Skeptic Report — Partial Win p1 on Erdos #757 (erdos757-sidon-in-45-sets)

role: reproduce
skeptic: astra
context: subagent
context: subagent (astra)

## 1. Quoted Definitions and Partial Win p1 Criterion

From `claim/target.md` (Statement, Success Criterion, and Partial Win `p1`):
> Let c* be the largest constant such that every (4,5)-set A of reals (every 4-element subset determines at least five distinct values among its six pairwise absolute differences) of size n contains a Sidon subset of size ge c* n. Ma-Tang (arXiv:2602.23282) give 9/17 (about 0.5294) le c* le 4/7 (about 0.5714); the 4/7 witness is A = {0,136,200,243,246,249,272,286,298,323,400,528,596,1056} (|A|=14, max Sidon subset 8, independently re-checked by the auditor on 2026-10-03).
>
> Success means a finite set A of distinct integers with all of the following. (1) Every 4-subset has at least 5 distinct absolute differences, checked exhaustively. (2) The exact maximum Sidon subset size s(A) is certified by two independent exact methods (bitmask branch-and-bound and an ILP that forbids every a+b=c+d, including a=b, i.e. 3-APs). (3) The ratio s/|A|, compared in fractions.Fraction, is STRICTLY SMALLER (direction: min) than the best upper bound on c* shown at verification time... (4) s/|A| ge 9/17; a ratio below 9/17 contradicts a theorem and means a bug, never a claim... (6) The checker reproduces s=8 on the Ma-Tang 14-set as a calibration test.
>
> Partial Wins:
> - p1: A new extremal witness: a (4,5)-set A with |A| NOT a multiple of 14 (e.g. |A| = 21 with s = 12) whose certified exact maximum Sidon subset gives s/|A| exactly equal to the live best ratio (4/7 on 2026-10-03), verified by the same two-method pipeline. Disjoint unions of dilated copies of the Ma-Tang 14-set only reach multiples of 14, so this is a structurally new extremal example.

From `claim/claim.md`:
> We exhibit an explicit 21-element set of integers (|A_21| = 21 not in 14Z):
> A_21 = {0, 1360, 2000, 2430, 2460, 2490, 2720, 2860, 2980, 3230, 4000, 5280, 5960, 9815, 10560, 11223, 11264, 11305, 12631, 13957, 16650}

Mathematical definitions verified:
1. **(4,5)-set property**: For a finite set $A = \{a_0, a_1, \dots, a_{n-1}\} \subset \mathbb{Z}$ with $a_0 \le a_1 - 1$, every 4-element subset $\{x_1, x_2, x_3, x_4\} \subset A$ with $x_1 \le x_2 - 1 \le x_3 - 2 \le x_4 - 3$ satisfies $|\{x_j - x_i : 1 \le i \le j - 1 \le 3\}| \ge 5$.
2. **Sidon ($B_2$) subset**: A subset $S \subseteq A$ is a Sidon set if and only if all $\binom{|S|+1}{2}$ pairwise sums $x + y$ ($x, y \in S$ with $x \le y$) are distinct; equivalently, $S$ contains no three-term arithmetic progression ($x + z = 2y$ with $x \le y - 1 \le z - 2$) and no four-term sum collision ($x + w = y + z$ with $x \le y - 1 \le z - 2 \le w - 3$). The Sidon number is $s(A) = \max\{|S| : S \subseteq A \text{ is Sidon}\}$.

## 2. File Integrity Verification

- **Object File**: `claim/witness_n21_s12.json`
- **Byte size**: `707` bytes
- **SHA-256**: `6478bc3cabcce580910f07fd9e3fee3a15d5b398ba12c9f9f557cfa7af7f2539`
- **Verifier Script**: `claim/verify_erdos757.py` (`15,949` bytes, `432` lines)
- **Claimed Set**: `A_21 = [0, 1360, 2000, 2430, 2460, 2490, 2720, 2860, 2980, 3230, 4000, 5280, 5960, 9815, 10560, 11223, 11264, 11305, 12631, 13957, 16650]`
- **Cardinality**: `|A_21| = 21`, all elements strictly increasing exact integers, `21 mod 14 = 7 != 0`.

## 3. Independent Verification Before Reading Author Code

Before inspecting `claim/verify_erdos757.py`, I wrote and ran an independent Python + compiled C verifier from the mathematical definitions:

1. **Calibration on Ma–Tang's 14-Element Set `A_14`**:
   - Tested `A_14 = [0, 136, 200, 243, 246, 249, 272, 286, 298, 323, 400, 528, 596, 1056]`.
   - Exhaustively checked all $\binom{14}{4} = 1001$ four-element subsets: `0` subsets have fewer than 5 distinct differences (`132` have 5 distinct differences, `869` have 6 distinct differences), confirming `is_45 = True`.
   - Found `12` three-term arithmetic progressions and `0` four-term sum collisions.
   - Exhaustively checked all $2^{14} = 16,384$ subsets: exactly `4,855` subsets are Sidon, the maximum Sidon subset size is `s(A_14) = 8` (attained by `143` distinct Sidon subsets of size 8, and `0` subsets of size 9 or larger), giving `Fraction(8, 14) == Fraction(4, 7)`.
2. **Exhaustive $\binom{21}{4} = 5985$ Verification of the $(4,5)$-Property on `A_21`**:
   - Checked all `5,985` four-element subsets of `A_21` in both Python and C:
     - Subsets with fewer than 5 distinct differences: `bad_4 = 0`
     - Subsets with exactly 5 distinct differences: `diff5 = 342`
     - Subsets with all 6 distinct differences: `diff6 = 5,643`
   - Confirmed `is_45 = True`.
3. **Exhaustive $2^{21} = 2,097,152$ Bitmask Verification of `s(A_21) = 12`**:
   - Evaluated all `2,097,152` subsets of `A_21` in compiled C, testing both absence of conflict hyperedges and direct distinctness of all $\binom{k+1}{2}$ pairwise sums $x + y$ ($x \le y \in S$):
     - Total Sidon subsets of `A_21`: `319,102`
     - Maximum Sidon subset size: `s(A_21) = 12`
     - Number of maximum Sidon subsets of size 12: `1,325`
     - Number of Sidon subsets of size 13 or larger: `0`
   - Directly checked the 12-element witness `S_12 = [0, 1360, 2000, 2430, 2460, 2980, 3230, 5280, 9815, 11223, 11264, 13957]` from `claim/witness_n21_s12.json`: `S_12` is a subset of `A_21` of size 12, and all $\binom{12+1}{2} = 78$ pairwise sums $x + y$ ($x \le y \in S_{12}$) are distinct (`78/78` unique sums).
   - Verified the exact rational ratio: `Fraction(12, 21) == Fraction(4, 7)`, which satisfies `Fraction(4, 7) ge Fraction(9, 17)`.
4. **Re-Derivation of the Proof Steps in `claim/claim.md`**:
   - **19 3-APs and 0 4-Sums**: Independently enumerated all 3-APs and 4-sums in `A_21`, finding `num_4sums = 0` and exactly `19` 3-APs:
     `(0, 1, 6), (0, 2, 10), (0, 8, 12), (0, 11, 14), (1, 12, 14), (2, 3, 7), (2, 5, 8), (3, 4, 5), (4, 6, 8), (4, 9, 10), (5, 7, 9), (6, 10, 11), (8, 13, 20), (12, 17, 20), (13, 14, 17), (13, 15, 18), (15, 16, 17), (16, 19, 20), (17, 18, 19)`.
     These 19 triples match the 19 triples listed in Section 3 of `claim/claim.md` (up to listing order). Their midpoints are a permutation of `{1, 2, ..., 19}` (each interior vertex is the midpoint of a unique 3-AP), and the maximum intersection between any two distinct 3-APs is `1` (confirming $H(A_{21})$ is a linear 3-uniform hypergraph).
   - **Algebraic Block Gluing Proof ($\tau(H(A_{21})) = 9$)**:
     - The 14-element sub-hypergraph on indices `{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14}` equals `10 * A_14` and carries the 12 internal 3-APs of $H(A_{14})$ with minimum transversal number $\tau(H(A_{14})) = 6$.
     - The 8-element block $B_8$ on indices `{12, 13, 15, 16, 17, 18, 19, 20}` (glued at vertex `12`, value `5960`) carries 5 internal 3-APs: `(12, 17, 20), (13, 15, 18), (15, 16, 17), (16, 19, 20), (17, 18, 19)` with $\tau(B_8) = 3$.
     - Removing vertex `12` leaves 4 edges `(13, 15, 18), (15, 16, 17), (16, 19, 20), (17, 18, 19)` on `{13, 15, 16, 17, 18, 19, 20}`, whose minimum transversal size is `2`, with only two size-2 transversals: `{15, 19}` and `{16, 18}` (corresponding to $\{b_1, b_6\}$ and $\{b_2, b_5\}$ in `claim/claim.md`; note a minor index-label typo $T_B = \{b_2, b_4\}$ for $\{b_2, b_5\} = \{16, 18\}$ in the prose of Section 2.2 of `claim/claim.md`, while in both cases $\{b_0, b_3, b_7\} = \{20, 17, 13\}$ is completely missed by both size-2 transversals!).
     - Because $\{13, 17, 20\}$ is disjoint from both size-2 transversals of $B_8 - \{12\}$, the two cross-edges `(8, 13, 20)` and `(13, 14, 17)` cannot both be covered unless either $|T \cap (B_8 \setminus \{12\})| \ge 3$ or both `8` and `14` lie in $T \cap A_{14}$. And if $\{8, 12, 14\} \subseteq T \cap A_{14}$, checking all 143 size-6 minimum transversals of $H(A_{14})$ confirms that every transversal of $H(A_{21})$ has size at least `9`, proving $\tau(H(A_{21})) = 9$ and $s(A_{21}) = 21 - 9 = 12$.
   - **2-Vertex Extension Bound (Section 4.2)**:
     - Verified across all 143 size-6 minimum transversals of $H(A_{14})$ that any two new 3-APs in a 16-element extension eliminate at most `115` transversals if each uses 2 vertices of $A_{14}$, and at most `134` of the `143` transversals if one uses both new vertices and 1 vertex of $A_{14}$, leaving at least $143 - 134 = 9$ surviving size-8 Sidon subsets extendable to size 10.
5. **1-Entry Corruption Negative Tests**:
   - **Corruption Test A** (`A_21[10]` changed from `4000` to `4080`, creating the 4-AP `{0, 1360, 2720, 4080}`):
     - Independent verifier rejected the set (`bad_4 = 2` four-subsets with fewer than 5 distinct differences).
     - Author's `claim/verify_erdos757.py` also rejected the corrupted JSON (`rc = 1`, `is_45: false`, `4-subset (0, 1360, 2720, 4080) has only 3 distinct differences`).
   - **Corruption Test B** (`A_21[20]` changed from `16650` to `16651`, breaking the cross-APs `(8, 13, 20)` and `(12, 17, 20)`):
     - Independent verifier found that `num_3aps` drops from `19` to `16` and `s` increases from `12` to `13` (`s/|A| = 13/21 != 4/7`).

## 4. Reproduction of Author Verification Command

Executed the command from `claim/REPRODUCE.md`:
```
python3 claim/verify_erdos757.py --json claim/witness_n21_s12.json
```
Output (`exit 0`):
```
[CALIBRATION PASS] Ma-Tang A_14: is_45=True, m=12, s1=8, s2=8, s/n=4/7
{
  "label": "claim/witness_n21_s12.json",
  "n": 21,
  "is_45": true,
  "msg_45": "All 5985 4-subsets have >= 5 distinct differences",
  "num_3aps": 19,
  "num_4sums": 0,
  "s_method1": 12,
  "s_method2": 12,
  "s": 12,
  "ratio_str": "4/7",
  "ratio_float": 0.5714285714285714,
  "beats_4_7": false,
  "ties_4_7_non_mult_14": true,
  "witness_sidon": [
    0,
    1360,
    2000,
    2430,
    2460,
    2980,
    3230,
    5280,
    9815,
    11223,
    11264,
    13957
  ]
}
VERIFY_ERDOS757: PASS
```
All temporary C and Python verification files created during the audit were deleted.

pass: true
