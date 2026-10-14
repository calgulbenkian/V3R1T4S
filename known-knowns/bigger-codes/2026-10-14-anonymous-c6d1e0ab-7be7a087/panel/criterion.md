# Criterion Skeptic Report: `constant-weight-codes` — `A(53, 8, 7)` Improved to `3992`

context: subagent

## 1. Clause-by-Clause Verification Against `constant-weight-codes` Success Criterion

We audit the claimed binary constant-weight code artifact `claim/A53_8_7_3992.txt` (`215568` bytes, SHA-256 `7be7a08730ebb932aa2700285fab3cfcd0cd464759ca72013f3a238ee3a60a29`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_cwc.py`, against every literal requirement of the `constant-weight-codes` Full Success Criterion:

1. **Explicit list of `M` distinct binary codewords in `{0, 1}^53` (`n` at most 64, even `d` at least 4), each of Hamming weight `w`**:
   - **PASS.** The parameters `(n, d, w) = (53, 8, 7)` satisfy `n = 53` (at most 64), even `d = 8` (at least 4), and `w = 7` in `1..53`. Running `claim/verify_cwc.py` confirms that `claim/A53_8_7_3992.txt` (`215568` bytes, strictly under the `1,000,000`-byte cap) contains `M = 3992` lines (`bad_lines = 0`), each a length-`53` string over `{0, 1}` of exact Hamming weight `w = 7` (`bad_weight = 0`), with all `distinct = 3992` codewords pairwise distinct.
2. **Every pair of distinct codewords has Hamming distance at least `d` (overlap at most `w - d/2 = 3`), verified by two independent routes**:
   - **PASS (Route A — Exhaustive All-Pairs Distance Check)**: Across all `M * (M - 1) / 2 = 7966036` pairs of distinct codewords, the minimum pairwise Hamming distance is `min_distance = 8` (at least `8`), with `bad_pairs = 0` and exact pairwise distance histogram `{8: 403503, 10: 1398836, 12: 3427264, 14: 2736433}`.
   - **PASS (Route B — Steiner `t`-Subset Packing Check)**: For `t = w - d/2 + 1 = 4`, every codeword generates `binom(7, 4) = 35` `t`-subsets of `1`-bit positions, and all `3992 * 35 = 139720` generated `4`-subsets are pairwise distinct (`distinct = 139720`, `collisions = 0`), independently proving that no two codewords share `4` or more `1`-bits.
3. **Code size `M` strictly greater than all live reference sources, `TROPHY_CASE.md`, and open PRs**:
   - **PASS.** Here `M = 3992`. Comparing against all reference sources:
     - Brouwer `Andw.html(53, 8, 7)` and complement `Andw.html(53, 8, 46)`: `3980` (`M = 3992` exceeds `3980` by `+12`).
     - `arXiv:2607.19550`, `arXiv:2608.13906`, `arXiv:2609.35051`: no bound above `3987`.
     - `TROPHY_CASE.md` and open PRs composite bar for `A(53, 8, 7)`: `3987` (`M = 3992` strictly exceeds `3987` by `+5`).
4. **Consistency with theoretical upper bounds `U(n, d, w)`**:
   - **PASS.** The iterated Johnson upper bound is `U_Johnson(53, 8, 7) = 8003` (and the Steiner `t`-packing upper bound is `floor(binom(53, 4) / binom(7, 4)) = 8366`), and `M = 3992` is well below `8003`.
5. **Single Cell & Non-Subsumption Check**:
   - **PASS.** This claim folder covers exclusively cell `A(53, 8, 7)` and achieves a strict improvement over both `Andw.html` (`3980`) and `TROPHY_CASE.md` (`3987`).

## 2. Confirmed Scope

confirmed_scope: Explicit binary constant-weight code in claim/A53_8_7_3992.txt (sha256 7be7a08730ebb932aa2700285fab3cfcd0cd464759ca72013f3a238ee3a60a29, 215568 bytes) establishing A(53, 8, 7) at least 3992 via 3992 distinct binary codewords of length 53 and Hamming weight 7 with minimum pairwise Hamming distance 8 (verified across all 7966036 pairs and 139720 disjoint 4-subsets, below Johnson upper bound 8003), strictly beating Brouwer Andw.html (3980, +12), arXiv:2607.19550/2608.13906/2609.35051, open PRs, and TROPHY_CASE.md (3987, +5).

pass: true
