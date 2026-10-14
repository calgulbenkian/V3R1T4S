# Criterion Skeptic Report: `constant-weight-codes` — `A(45, 8, 7)` Improved to `1910`

context: subagent

## 1. Clause-by-Clause Verification Against `constant-weight-codes` Success Criterion

We audit the claimed binary constant-weight code artifact `claim/A45_8_7_1910.txt` (`87860` bytes, SHA-256 `e9a786a8af3ad130a62167977ca106c4f1ffc99d134f798959fafb319e21c966`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_cwc.py`, against every literal requirement of the `constant-weight-codes` Full Success Criterion:

1. **Explicit list of `M` distinct binary codewords in `{0, 1}^45` (`n` at most 64, even `d` at least 4), each of Hamming weight `w`**:
   - **PASS.** The parameters `(n, d, w) = (45, 8, 7)` satisfy `n = 45` (at most 64), even `d = 8` (at least 4), and `w = 7` in `1..45`. Running `claim/verify_cwc.py` confirms that `claim/A45_8_7_1910.txt` (`87860` bytes, strictly under the `1,000,000`-byte cap) contains `M = 1910` lines (`bad_lines = 0`), each a length-`45` string over `{0, 1}` of exact Hamming weight `w = 7` (`bad_weight = 0`), with all `distinct = 1910` codewords pairwise distinct.
2. **Every pair of distinct codewords has Hamming distance at least `d` (overlap at most `w - d/2 = 3`), verified by two independent routes**:
   - **PASS (Route A — Exhaustive All-Pairs Distance Check)**: Across all `M * (M - 1) / 2 = 1823095` pairs of distinct codewords, the minimum pairwise Hamming distance is `min_distance = 8` (at least `8`), with `bad_pairs = 0` and exact pairwise distance histogram `{8: 142038, 10: 385326, 12: 785387, 14: 510344}`.
   - **PASS (Route B — Steiner `t`-Subset Packing Check)**: For `t = w - d/2 + 1 = 4`, every codeword generates `binom(7, 4) = 35` `t`-subsets of `1`-bit positions, and all `1910 * 35 = 66850` generated `4`-subsets are pairwise distinct (`distinct = 66850`, `collisions = 0`), independently proving that no two codewords share `4` or more `1`-bits.
3. **Code size `M` strictly greater than all live reference sources, `TROPHY_CASE.md`, and open PRs**:
   - **PASS.** Here `M = 1910`. Comparing against all reference sources:
     - Brouwer `Andw.html(45, 8, 7)` and complement `Andw.html(45, 8, 38)`: `1904` (`M = 1910` exceeds `1904` by `+6`).
     - `arXiv:2607.19550`, `arXiv:2608.13906`, `arXiv:2609.35051`: no bound above `1907`.
     - `TROPHY_CASE.md` and open PRs composite bar for `A(45, 8, 7)`: `1907` (`M = 1910` strictly exceeds `1907` by `+3`).
4. **Consistency with theoretical upper bounds `U(n, d, w)`**:
   - **PASS.** The iterated Johnson upper bound is `U_Johnson(45, 8, 7) = 4050` (and the Steiner `t`-packing upper bound is `floor(binom(45, 4) / binom(7, 4)) = 4257`), and `M = 1910` is well below `4050`.
5. **Single Cell & Non-Subsumption Check**:
   - **PASS.** This claim folder covers exclusively cell `A(45, 8, 7)` and achieves a strict improvement over both `Andw.html` (`1904`) and `TROPHY_CASE.md` (`1907`).

## 2. Confirmed Scope

confirmed_scope: Explicit binary constant-weight code in claim/A45_8_7_1910.txt (sha256 e9a786a8af3ad130a62167977ca106c4f1ffc99d134f798959fafb319e21c966, 87860 bytes) establishing A(45, 8, 7) at least 1910 via 1910 distinct binary codewords of length 45 and Hamming weight 7 with minimum pairwise Hamming distance 8 (verified across all 1823095 pairs and 66850 disjoint 4-subsets, below Johnson upper bound 4050), strictly beating Brouwer Andw.html (1904, +6), arXiv:2607.19550/2608.13906/2609.35051, open PRs, and TROPHY_CASE.md (1907, +3).

pass: true
