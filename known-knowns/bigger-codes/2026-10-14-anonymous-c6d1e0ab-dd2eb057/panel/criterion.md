# Criterion Skeptic Report: `constant-weight-codes` — `A(35, 6, 6)` Improved to `2218`

context: subagent

## 1. Clause-by-Clause Verification Against `constant-weight-codes` Success Criterion

We audit the claimed binary constant-weight code artifact `claim/A35_6_6_2218.txt` (`79848` bytes, SHA-256 `dd2eb057e40bc19bbd7f6a2838681200d6d55b4018e9b01a62082c35822e413e`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_cwc.py`, against every literal requirement of the `constant-weight-codes` Full Success Criterion:

1. **Explicit list of `M` distinct binary codewords in `{0, 1}^35` (`n` at most 64, even `d` at least 4), each of Hamming weight `w`**:
   - **PASS.** The parameters `(n, d, w) = (35, 6, 6)` satisfy `n = 35` (at most 64), even `d = 6` (at least 4), and `w = 6` in `1..35`. Running `claim/verify_cwc.py` confirms that `claim/A35_6_6_2218.txt` (`79848` bytes, strictly under the `1,000,000`-byte cap) contains `M = 2218` lines (`bad_lines = 0`), each a length-`35` string over `{0, 1}` of exact Hamming weight `w = 6` (`bad_weight = 0`), with all `distinct = 2218` codewords pairwise distinct.
2. **Every pair of distinct codewords has Hamming distance at least `d` (overlap at most `w - d/2 = 3`), verified by two independent routes**:
   - **PASS (Route A — Exhaustive All-Pairs Distance Check)**: Across all `M * (M - 1) / 2 = 2458653` pairs of distinct codewords, the minimum pairwise Hamming distance is `min_distance = 6` (at least `6`), with `bad_pairs = 0` and exact pairwise distance histogram `{6: 133550, 8: 523436, 10: 1087173, 12: 714494}`.
   - **PASS (Route B — Steiner `t`-Subset Packing Check)**: For `t = w - d/2 + 1 = 4`, every codeword generates `binom(6, 4) = 15` `t`-subsets of `1`-bit positions, and all `2218 * 15 = 33270` generated `4`-subsets are pairwise distinct (`distinct = 33270`, `collisions = 0`), independently proving that no two codewords share `4` or more `1`-bits.
3. **Code size `M` strictly greater than all live reference sources, `TROPHY_CASE.md`, and open PRs**:
   - **PASS.** Here `M = 2218`. Comparing against all reference sources:
     - Brouwer `Andw.html(35, 6, 6)` and complement `Andw.html(35, 6, 29)`: `2209` (`M = 2218` exceeds `2209` by `+9`).
     - `arXiv:2607.19550`, `arXiv:2608.13906`, `arXiv:2609.35051`: no bound above `2217`.
     - `TROPHY_CASE.md` and open PRs composite bar for `A(35, 6, 6)`: `2217` (`M = 2218` strictly exceeds `2217` by `+1`).
4. **Consistency with theoretical upper bounds `U(n, d, w)`**:
   - **PASS.** The iterated Johnson upper bound is `U_Johnson(35, 6, 6) = 3249` (and the Steiner `t`-packing upper bound is `floor(binom(35, 4) / binom(6, 4)) = 3490`), and `M = 2218` is well below `3249`.
5. **Single Cell & Non-Subsumption Check**:
   - **PASS.** This claim folder covers exclusively cell `A(35, 6, 6)` and achieves a strict improvement over both `Andw.html` (`2209`) and `TROPHY_CASE.md` (`2217`).

## 2. Confirmed Scope

confirmed_scope: Explicit binary constant-weight code in claim/A35_6_6_2218.txt (sha256 dd2eb057e40bc19bbd7f6a2838681200d6d55b4018e9b01a62082c35822e413e, 79848 bytes) establishing A(35, 6, 6) at least 2218 via 2218 distinct binary codewords of length 35 and Hamming weight 6 with minimum pairwise Hamming distance 6 (verified across all 2458653 pairs and 33270 disjoint 4-subsets, below Johnson upper bound 3249), strictly beating Brouwer Andw.html (2209, +9), arXiv:2607.19550/2608.13906/2609.35051, open PRs, and TROPHY_CASE.md (2217, +1).

pass: true
