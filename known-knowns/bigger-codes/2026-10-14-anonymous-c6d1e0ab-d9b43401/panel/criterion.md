# Criterion Skeptic Report: `constant-weight-codes` — `A(54, 8, 7)` Improved to `4204`

context: subagent

## 1. Clause-by-Clause Verification Against `constant-weight-codes` Success Criterion

We audit the claimed binary constant-weight code artifact `claim/A54_8_7_4204.txt` (`231220` bytes, SHA-256 `d9b4340171c56a0ddc034dcb31cb4f568eb9c8e2fecddbb3a1871a0722356fca`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_cwc.py`, against every literal requirement of the `constant-weight-codes` Full Success Criterion:

1. **Explicit list of `M` distinct binary codewords in `{0, 1}^54` (`n` at most 64, even `d` at least 4), each of Hamming weight `w`**:
   - **PASS.** The parameters `(n, d, w) = (54, 8, 7)` satisfy `n = 54` (at most 64), even `d = 8` (at least 4), and `w = 7` in `1..54`. Running `claim/verify_cwc.py` confirms that `claim/A54_8_7_4204.txt` (`231220` bytes, strictly under the `1,000,000`-byte cap) contains `M = 4204` lines (`bad_lines = 0`), each a length-`54` string over `{0, 1}` of exact Hamming weight `w = 7` (`bad_weight = 0`), with all `distinct = 4204` codewords pairwise distinct.
2. **Every pair of distinct codewords has Hamming distance at least `d` (overlap at most `w - d/2 = 3`), verified by two independent routes**:
   - **PASS (Route A — Exhaustive All-Pairs Distance Check)**: Across all `M * (M - 1) / 2 = 8834706` pairs of distinct codewords, the minimum pairwise Hamming distance is `min_distance = 8` (at least `8`), with `bad_pairs = 0` and exact pairwise distance histogram `{8: 420462, 10: 1522822, 12: 3790819, 14: 3100603}`.
   - **PASS (Route B — Steiner `t`-Subset Packing Check)**: For `t = w - d/2 + 1 = 4`, every codeword generates `binom(7, 4) = 35` `t`-subsets of `1`-bit positions, and all `4204 * 35 = 147140` generated `4`-subsets are pairwise distinct (`distinct = 147140`, `collisions = 0`), independently proving that no two codewords share `4` or more `1`-bits.
3. **Code size `M` strictly greater than all live reference sources, `TROPHY_CASE.md`, and open PRs**:
   - **PASS.** Here `M = 4204`. Comparing against all reference sources:
     - Brouwer `Andw.html(54, 8, 7)` and complement `Andw.html(54, 8, 47)`: `4173` (`M = 4204` exceeds `4173` by `+31`).
     - `arXiv:2607.19550`, `arXiv:2608.13906`, `arXiv:2609.35051`: no bound above `4193`.
     - `TROPHY_CASE.md` and open PRs composite bar for `A(54, 8, 7)`: `4193` (`M = 4204` strictly exceeds `4193` by `+11`).
4. **Consistency with theoretical upper bounds `U(n, d, w)`**:
   - **PASS.** The iterated Johnson upper bound is `U_Johnson(54, 8, 7) = 8447` (and the Steiner `t`-packing upper bound is `floor(binom(54, 4) / binom(7, 4)) = 9035`), and `M = 4204` is well below `8447`.
5. **Single Cell & Non-Subsumption Check**:
   - **PASS.** This claim folder covers exclusively cell `A(54, 8, 7)` and achieves a strict improvement over both `Andw.html` (`4173`) and `TROPHY_CASE.md` (`4193`).

## 2. Confirmed Scope

confirmed_scope: Explicit binary constant-weight code in claim/A54_8_7_4204.txt (sha256 d9b4340171c56a0ddc034dcb31cb4f568eb9c8e2fecddbb3a1871a0722356fca, 231220 bytes) establishing A(54, 8, 7) at least 4204 via 4204 distinct binary codewords of length 54 and Hamming weight 7 with minimum pairwise Hamming distance 8 (verified across all 8834706 pairs and 147140 disjoint 4-subsets, below Johnson upper bound 8447), strictly beating Brouwer Andw.html (4173, +31), arXiv:2607.19550/2608.13906/2609.35051, open PRs, and TROPHY_CASE.md (4193, +11).

pass: true
