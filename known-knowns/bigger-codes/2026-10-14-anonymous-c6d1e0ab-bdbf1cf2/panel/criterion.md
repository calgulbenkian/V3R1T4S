# Criterion Skeptic Report: `constant-weight-codes` — `A(27, 8, 10)` Improved to `1740`

context: subagent

## 1. Clause-by-Clause Verification Against `constant-weight-codes` Success Criterion

We audit the claimed binary constant-weight code artifact `claim/A27_8_10_1740.txt` (`48720` bytes, SHA-256 `bdbf1cf2b34d5a2771172cea5d11fe6abcff25a0de03cc60808796fbe6e0acbe`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_cwc.py`, against every literal requirement of the `constant-weight-codes` Full Success Criterion:

1. **Explicit list of `M` distinct binary codewords in `{0, 1}^27` (`n` at most 64, even `d` at least 4), each of Hamming weight `w`**:
   - **PASS.** The parameters `(n, d, w) = (27, 8, 10)` satisfy `n = 27` (at most 64), even `d = 8` (at least 4), and `w = 10` in `1..27`. Running `claim/verify_cwc.py` confirms that `claim/A27_8_10_1740.txt` (`48720` bytes, strictly under the `1,000,000`-byte cap) contains `M = 1740` lines (`bad_lines = 0`), each a length-`27` string over `{0, 1}` of exact Hamming weight `w = 10` (`bad_weight = 0`), with all `distinct = 1740` codewords pairwise distinct.
2. **Every pair of distinct codewords has Hamming distance at least `d` (overlap at most `w - d/2 = 6`), verified by two independent routes**:
   - **PASS (Route A — Exhaustive All-Pairs Distance Check)**: Across all `M * (M - 1) / 2 = 1512930` pairs of distinct codewords, the minimum pairwise Hamming distance is `min_distance = 8` (at least `8`), with `bad_pairs = 0` and exact pairwise distance histogram `{8: 178567, 10: 121676, 12: 676640, 14: 245659, 16: 261670, 18: 24724, 20: 3994}`.
   - **PASS (Route B — Steiner `t`-Subset Packing Check)**: For `t = w - d/2 + 1 = 7`, every codeword generates `binom(10, 7) = 120` `t`-subsets of `1`-bit positions, and all `1740 * 120 = 208800` generated `7`-subsets are pairwise distinct (`distinct = 208800`, `collisions = 0`), independently proving that no two codewords share `7` or more `1`-bits.
3. **Code size `M` strictly greater than all live reference sources, `TROPHY_CASE.md`, and open PRs**:
   - **PASS.** Here `M = 1740`. Comparing against all reference sources:
     - Brouwer `Andw.html(27, 8, 10)` and complement `Andw.html(27, 8, 17)`: `1728` (`M = 1740` exceeds `1728` by `+12`).
     - `arXiv:2607.19550`, `arXiv:2608.13906`, `arXiv:2609.35051`: no bound above `1737`.
     - `TROPHY_CASE.md` and open PRs composite bar for `A(27, 8, 10)`: `1737` (`M = 1740` strictly exceeds `1737` by `+3`).
4. **Consistency with theoretical upper bounds `U(n, d, w)`**:
   - **PASS.** The iterated Johnson upper bound is `U_Johnson(27, 8, 10) = 7020` (and the Steiner `t`-packing upper bound is `floor(binom(27, 7) / binom(10, 7)) = 7400`), and `M = 1740` is well below `7020`.
5. **Single Cell & Non-Subsumption Check**:
   - **PASS.** This claim folder covers exclusively cell `A(27, 8, 10)` and achieves a strict improvement over both `Andw.html` (`1728`) and `TROPHY_CASE.md` (`1737`).

## 2. Confirmed Scope

confirmed_scope: Explicit binary constant-weight code in claim/A27_8_10_1740.txt (sha256 bdbf1cf2b34d5a2771172cea5d11fe6abcff25a0de03cc60808796fbe6e0acbe, 48720 bytes) establishing A(27, 8, 10) at least 1740 via 1740 distinct binary codewords of length 27 and Hamming weight 10 with minimum pairwise Hamming distance 8 (verified across all 1512930 pairs and 208800 disjoint 7-subsets, below Johnson upper bound 7020), strictly beating Brouwer Andw.html (1728, +12), arXiv:2607.19550/2608.13906/2609.35051, open PRs, and TROPHY_CASE.md (1737, +3).

pass: true
