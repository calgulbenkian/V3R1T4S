# Criterion Skeptic Report: `constant-weight-codes` — `A(52, 8, 7)` Improved to `3802`

context: subagent

## 1. Clause-by-Clause Verification Against `constant-weight-codes` Success Criterion

We audit the claimed binary constant-weight code artifact `claim/A52_8_7_3802.txt` (`201506` bytes, SHA-256 `4743db7cec4929d05cba257484e8cce16c1f304d94efdb0b82d6870f191e473c`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_cwc.py`, against every literal requirement of the `constant-weight-codes` Full Success Criterion:

1. **Explicit list of `M` distinct binary codewords in `{0, 1}^52` (`n` at most 64, even `d` at least 4), each of Hamming weight `w`**:
   - **PASS.** The parameters `(n, d, w) = (52, 8, 7)` satisfy `n = 52` (at most 64), even `d = 8` (at least 4), and `w = 7` in `1..52`. Running `claim/verify_cwc.py` confirms that `claim/A52_8_7_3802.txt` (`201506` bytes, strictly under the `1,000,000`-byte cap) contains `M = 3802` lines (`bad_lines = 0`), each a length-`52` string over `{0, 1}` of exact Hamming weight `w = 7` (`bad_weight = 0`), with all `distinct = 3802` codewords pairwise distinct.
2. **Every pair of distinct codewords has Hamming distance at least `d` (overlap at most `w - d/2 = 3`), verified by two independent routes**:
   - **PASS (Route A — Exhaustive All-Pairs Distance Check)**: Across all `M * (M - 1) / 2 = 7225701` pairs of distinct codewords, the minimum pairwise Hamming distance is `min_distance = 8` (at least `8`), with `bad_pairs = 0` and exact pairwise distance histogram `{8: 390656, 10: 1289145, 12: 3118070, 14: 2427830}`.
   - **PASS (Route B — Steiner `t`-Subset Packing Check)**: For `t = w - d/2 + 1 = 4`, every codeword generates `binom(7, 4) = 35` `t`-subsets of `1`-bit positions, and all `3802 * 35 = 133070` generated `4`-subsets are pairwise distinct (`distinct = 133070`, `collisions = 0`), independently proving that no two codewords share `4` or more `1`-bits.
3. **Code size `M` strictly greater than all live reference sources, `TROPHY_CASE.md`, and open PRs**:
   - **PASS.** Here `M = 3802`. Comparing against all reference sources:
     - Brouwer `Andw.html(52, 8, 7)` and complement `Andw.html(52, 8, 45)`: `3797` (`M = 3802` exceeds `3797` by `+5`).
     - `arXiv:2607.19550`, `arXiv:2608.13906`, `arXiv:2609.35051`: no bound above `3799`.
     - `TROPHY_CASE.md` and open PRs composite bar for `A(52, 8, 7)`: `3799` (`M = 3802` strictly exceeds `3799` by `+3`).
4. **Consistency with theoretical upper bounds `U(n, d, w)`**:
   - **PASS.** The iterated Johnson upper bound is `U_Johnson(52, 8, 7) = 7577` (and the Steiner `t`-packing upper bound is `floor(binom(52, 4) / binom(7, 4)) = 7735`), and `M = 3802` is well below `7577`.
5. **Single Cell & Non-Subsumption Check**:
   - **PASS.** This claim folder covers exclusively cell `A(52, 8, 7)` and achieves a strict improvement over both `Andw.html` (`3797`) and `TROPHY_CASE.md` (`3799`).

## 2. Confirmed Scope

confirmed_scope: Explicit binary constant-weight code in claim/A52_8_7_3802.txt (sha256 4743db7cec4929d05cba257484e8cce16c1f304d94efdb0b82d6870f191e473c, 201506 bytes) establishing A(52, 8, 7) at least 3802 via 3802 distinct binary codewords of length 52 and Hamming weight 7 with minimum pairwise Hamming distance 8 (verified across all 7225701 pairs and 133070 disjoint 4-subsets, below Johnson upper bound 7577), strictly beating Brouwer Andw.html (3797, +5), arXiv:2607.19550/2608.13906/2609.35051, open PRs, and TROPHY_CASE.md (3799, +3).

pass: true
