# Criterion Skeptic Report: `constant-weight-codes` — `A(56, 8, 7)` Improved to `4691`

context: subagent

## 1. Clause-by-Clause Verification Against `constant-weight-codes` Success Criterion

We audit the claimed binary constant-weight code artifact `claim/A56_8_7_4691.txt` (`267387` bytes, SHA-256 `e12d11fa604fd790d622442b7d96815ed8b129256b45507a9f09bff518cf27b1`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_cwc.py`, against every literal requirement of the `constant-weight-codes` Full Success Criterion:

1. **Explicit list of `M` distinct binary codewords in `{0, 1}^56` (`n` at most 64, even `d` at least 4), each of Hamming weight `w`**:
   - **PASS.** The parameters `(n, d, w) = (56, 8, 7)` satisfy `n = 56` (at most 64), even `d = 8` (at least 4), and `w = 7` in `1..56`. Running `claim/verify_cwc.py` confirms that `claim/A56_8_7_4691.txt` (`267387` bytes, strictly under the `1,000,000`-byte cap) contains `M = 4691` lines (`bad_lines = 0`), each a length-`56` string over `{0, 1}` of exact Hamming weight `w = 7` (`bad_weight = 0`), with all `distinct = 4691` codewords pairwise distinct.
2. **Every pair of distinct codewords has Hamming distance at least `d` (overlap at most `w - d/2 = 3`), verified by two independent routes**:
   - **PASS (Route A — Exhaustive All-Pairs Distance Check)**: Across all `M * (M - 1) / 2 = 11000395` pairs of distinct codewords, the minimum pairwise Hamming distance is `min_distance = 8` (at least `8`), with `bad_pairs = 0` and exact pairwise distance histogram `{8: 438664, 10: 1820540, 12: 4672305, 14: 4068886}`.
   - **PASS (Route B — Steiner `t`-Subset Packing Check)**: For `t = w - d/2 + 1 = 4`, every codeword generates `binom(7, 4) = 35` `t`-subsets of `1`-bit positions, and all `4691 * 35 = 164185` generated `4`-subsets are pairwise distinct (`distinct = 164185`, `collisions = 0`), independently proving that no two codewords share `4` or more `1`-bits.
3. **Code size `M` strictly greater than all live reference sources, `TROPHY_CASE.md`, and open PRs**:
   - **PASS.** Here `M = 4691`. Comparing against all reference sources:
     - Brouwer `Andw.html(56, 8, 7)` and complement `Andw.html(56, 8, 49)`: `4674` (`M = 4691` exceeds `4674` by `+17`).
     - `arXiv:2607.19550`, `arXiv:2608.13906`, `arXiv:2609.35051`: no bound above `4685`.
     - `TROPHY_CASE.md` and open PRs composite bar for `A(56, 8, 7)`: `4685` (`M = 4691` strictly exceeds `4685` by `+6`).
4. **Consistency with theoretical upper bounds `U(n, d, w)`**:
   - **PASS.** The iterated Johnson upper bound is `U_Johnson(56, 8, 7) = 10264` (and the Steiner `t`-packing upper bound is `floor(binom(56, 4) / binom(7, 4)) = 10494`), and `M = 4691` is well below `10264`.
5. **Single Cell & Non-Subsumption Check**:
   - **PASS.** This claim folder covers exclusively cell `A(56, 8, 7)` and achieves a strict improvement over both `Andw.html` (`4674`) and `TROPHY_CASE.md` (`4685`).

## 2. Confirmed Scope

confirmed_scope: Explicit binary constant-weight code in claim/A56_8_7_4691.txt (sha256 e12d11fa604fd790d622442b7d96815ed8b129256b45507a9f09bff518cf27b1, 267387 bytes) establishing A(56, 8, 7) at least 4691 via 4691 distinct binary codewords of length 56 and Hamming weight 7 with minimum pairwise Hamming distance 8 (verified across all 11000395 pairs and 164185 disjoint 4-subsets, below Johnson upper bound 10264), strictly beating Brouwer Andw.html (4674, +17), arXiv:2607.19550/2608.13906/2609.35051, open PRs, and TROPHY_CASE.md (4685, +6).

pass: true
