# Criterion Skeptic Report: `erdos757-sidon-in-45-sets` — Partial Win `p1` (`|A| = 21`, `s(A) = 12`, `s(A)/|A| = 4/7`)

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md` (Partial Win `p1`)

We audit the claimed artifact `claim/witness_n21_s12.json` (SHA-256 `6478bc3cabcce580910f07fd9e3fee3a15d5b398ba12c9f9f557cfa7af7f2539`), documented in `claim/claim.md` and `claim/status_record.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_erdos757.py` (SHA-256 `41583510945fed24111e5e0aaf1190ceb4873a490c596beabe14cf9397921f4b`), against every literal clause of Partial Win `p1` and the two-method verification pipeline in `claim/target.md`:

1. **Finite set of distinct integers with cardinality `|A|` NOT a multiple of 14**:
   - **PASS.** `claim/witness_n21_s12.json` defines the explicit sorted 21-element integer set
     `A_21 = [0, 1360, 2000, 2430, 2460, 2490, 2720, 2860, 2980, 3230, 4000, 5280, 5960, 9815, 10560, 11223, 11264, 11305, 12631, 13957, 16650]`.
     All 21 elements are exact distinct Python `int` values, and its cardinality `|A_21| = 21` satisfies `21 mod 14 = 7 != 0` (not a multiple of 14). Because disjoint unions of dilated copies of the Ma-Tang 14-set only reach cardinalities in `14 Z`, `|A_21| = 21` cannot be produced by disjoint union of copies of `A_14`.

2. **Every 4-subset determines at least 5 distinct pairwise absolute differences (checked exhaustively)**:
   - **PASS.** `claim/verify_erdos757.py` checks all `binom(21, 4) = 5985` four-element subsets of `A_21` in exact integer arithmetic (`check_is_45_exhaustive`). Every 4-element subset determines at least 5 distinct values among its 6 pairwise absolute differences (`is_45 = True`). Specifically, `A_21` has `num_4sums = 0` four-term sum collisions (`a + d = b + c` on 4 distinct elements) and `num_3aps = 19` three-term arithmetic progressions (`a + c = 2b`), whose midpoints are bijectively the 19 interior elements indexed `1..19` and which pairwise share at most 1 element (a linear 3-uniform hypergraph).

3. **Exact maximum Sidon subset size `s(A_21) = 12` certified by two independent exact methods**:
   - **PASS.** `claim/verify_erdos757.py` certifies `s(A_21) = 12` by two independent exact algorithms that forbid all `a + b = c + d` (including `a = b`, i.e., all 19 3-APs and all 0 four-sum collisions):
     - **Method 1 (`exact_sidon_method1_bitmask_bnb`)**: Recursive bitmask branch-and-bound with a disjoint 3-AP packing upper bound, returning `s_method1 = 12` and explicit 12-element Sidon witness `S_12 = [0, 1360, 2000, 2430, 2460, 2980, 3230, 5280, 9815, 11223, 11264, 13957]`, which passes direct pairwise-sum distinctness verification (`is_sidon_subset_direct(S_12) == True`, all `12 * 13 / 2 = 78` pairwise sums distinct).
     - **Method 2 (`exact_sidon_method2_dpll_ilp`)**: Independent 0-1 ILP / DPLL minimum hitting-set (transversal) solver with disjoint-packing and max-degree lower bounds over the full conflict hypergraph, certifying minimum transversal size `tau = 9` and `s_method2 = 21 - 9 = 12`.
     - **Independent Exhaustive Subsets Audit**: Direct brute-force inspection of all `binom(21, 13) = 203,490` subsets of size 13 and all `binom(21, 12) = 293,930` subsets of size 12 confirms `0` Sidon subsets of size 13 and `1,325` Sidon subsets of size 12.

4. **Exact rational comparison against live best ratio (`4/7`) and theoretical lower bound (`9/17`)**:
   - **PASS.** In `fractions.Fraction`, `Fraction(12, 21) == Fraction(4, 7)`.
   - Per `claim/status_record.md` (fetched `2026-10-14T03:14:18Z`), the live best upper bound ratio is `4/7` across Ma-Tang (`arXiv:2602.23282`, SHA-256 `d1aace4ca6e952deda0f2dbad7336e7e539b74c2e83eaef5a1954c2c1bd6bc29`), `erdosproblems.com/757` (SHA-256 `9ff4a0a695687fbc4e0ae1188989ae4fdebf1cc682306065fe63576dd5d0471f`), and `teorth/erdosproblems` (SHA-256 `c8fdf1c39dd9299201ab433554e909efa08ccb8c99df859e6a2fe3cd3d6330dc`), where only the 14-element witness `A_14` (and multiples of 14) was previously known at ratio `4/7`.
   - Furthermore, `Fraction(4, 7) = 68/119` is at least `Fraction(9, 17) = 63/119`, consistent with Ma-Tang Theorem 1.6.

5. **Mandatory Calibration on the Ma-Tang 14-Set `A_14`**:
   - **PASS.** `claim/verify_erdos757.py` automatically runs `run_calibration()` on `MA_TANG_14 = [0, 136, 200, 243, 246, 249, 272, 286, 298, 323, 400, 528, 596, 1056]`, verifying `is_45 = True`, `num_3aps = 12`, `s_method1 = 8`, `s_method2 = 8`, and `s/n = 4/7`, as well as negative calibration on `[0, 1, 2, 3]` (`is_45 = False`) and small positive calibration on `[1, 2, 3, 6]` (`is_45 = True, s = 3`).

6. **Claim Level & Non-Subsumption Check**:
   - **PASS.** `claim/claim.md` claims strictly Partial Win `p1` (`partial_win_claim`, `CONFIRMED_PARTIAL`) and explicitly states that it does not claim a full win (`s/|A|` strictly below `4/7`) or partial win `p2`. Notice that the verbatim parenthetical example in `claim/target.md` under `p1` literally reads `(e.g. |A| = 21 with s = 12)`, which `A_21` realizes directly.

## 2. Confirmed Scope

confirmed_scope: Partial Win p1 on erdos757-sidon-in-45-sets is verified by the explicit 21-element integer (4,5)-set A_21 in claim/witness_n21_s12.json (sha256 6478bc3cabcce580910f07fd9e3fee3a15d5b398ba12c9f9f557cfa7af7f2539), whose cardinality 21 is not a multiple of 14, whose (4,5)-set property holds across all 5985 four-subsets, and whose exact maximum Sidon subset size s(A_21) = 12 is certified by two independent exact solvers in claim/verify_erdos757.py (calibrated at s = 8 on the Ma-Tang 14-set), achieving exact rational ratio s(A_21)/|A_21| = 12/21 = 4/7 matching the live best ratio in arXiv:2602.23282 and erdosproblems.com/757.

pass: true
