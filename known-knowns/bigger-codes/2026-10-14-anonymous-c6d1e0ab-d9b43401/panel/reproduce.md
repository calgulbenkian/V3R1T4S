# Reproduction & Independent Verification Report — Binary Constant-Weight Code `A(54, 8, 7)` Lower Bound `4204`

context: subagent
context: subagent (astra)

## 1. Executive Summary
- **Target**: `constant-weight-codes` (`A(n, d, w)` lower bounds in Brouwer's table)
- **Cell**: `A(54, 8, 7)` (and complement mirror cell `A(54, 8, 47)`)
- **Claimed Lower Bound**: `M = 4204` (strictly beating the live composite bar `4193` by `+11` and Brouwer's `Andw.html` table entry `4173` by `+31`)
- **Claim Level**: `full`
- **Artifact**: `claim/A54_8_7_4204.txt` (`231220` bytes, SHA-256 `d9b4340171c56a0ddc034dcb31cb4f568eb9c8e2fecddbb3a1871a0722356fca`)
- **Verdict**: **PASS** — Both our independent first-principles verifier (written and executed before reading `claim/verify_cwc.py`) and the author's standalone verifier confirm that `claim/A54_8_7_4204.txt` contains `4204` pairwise distinct binary codewords of length `54` and exact Hamming weight `7`, with minimum pairwise Hamming distance `8 == 8` (`0` pairs below `8` across all `8,834,706` codeword pairs) and `0` collisions among all `147,140` Steiner `t = 4`-subsets. Both verifiers also immediately reject a 2-bit-flipped corrupted copy.

---

## 2. Quoted Definition & Claim from `target.md` and `claim/CLAIM.md`

### 2.1 Mathematical Definition (`target.md`)
  - **Definition**: `A(n, d, w)` is the maximum number of binary words of length `n` and weight `w` with pairwise Hamming distance at least `d`.
  - **Success Criterion**: An explicit list of `M` distinct binary vectors of length `n`, each with Hamming weight exactly `w`, with all pairwise distances at least `d` (`d` even), where `M` is strictly greater than the lower bound shown at verification time in the `(n, d, w)` cell of `https://aeb.win.tue.nl/codes/Andw.html` (also checking the mirror cell `A(n, d, n-w)`), and strictly greater than any value for that cell in `arXiv:2608.13906` (Echols), `arXiv:2607.19550` (Lysenstoen), or prior V3R1T4S records.

### 2.2 Claim Summary (`claim/CLAIM.md`)
  - **Target**: `constant-weight-codes`
  - **Claim Level**: `full` (`+11` over live composite bar `4193`; `+31` over `Andw.html` `4173`)
  - **Artifact**: `A54_8_7_4204.txt` (`4204` binary codewords of length `54`, weight `7`, minimum pairwise Hamming distance `8`)

---

## 3. Step 1 — Independent First-Principles Verification (Executed Before Reading `claim/verify_cwc.py`)

Prior to reading `claim/verify_cwc.py`, we implemented and ran an independent verifier (Python parser + Steiner `t`-subset packing checker + compiled C99 `uint64_t` `__builtin_popcountll` all-pairs distance engine).

### 3.1 Artifact Integrity, Format, Weight & Distinctness
- **File**: `claim/A54_8_7_4204.txt`
- **Byte Size**: `231220` bytes (`4204` lines of `54` ASCII characters plus newline)
- **SHA-256**: `d9b4340171c56a0ddc034dcb31cb4f568eb9c8e2fecddbb3a1871a0722356fca` (matches `claim/CLAIM.md` exactly)
- **Line & Alphabet Check**: `lines = 4204`, `bad_len = 0`, `bad_chars = 0` (every line has exact length `54` and consists solely of `'0'` and `'1'`).
- **Hamming Weight Check**: `bad_weight = 0` (every codeword has exact Hamming weight `w = 7`).
- **Distinctness Check**: `distinct_M = 4204 == 4204` (zero duplicate codewords).

### 3.2 Independent Steiner `t`-Subset Packing Verification
For constant weight `w = 7` and minimum even Hamming distance `d = 8`, the maximum allowed bitwise overlap between any two distinct codewords is `w - d/2 = 3`. Equivalently, every `t = w - d/2 + 1 = 4`-element subset of the `1`-positions of a codeword must be unique across the entire code (`C(7, 4) = 35` subsets per codeword):
- **Total `t = 4`-subsets**: `147,140`
- **Distinct `t = 4`-subsets**: `147,140`
- **Subset Collisions**: `0`

### 3.3 Exhaustive All-Pairs Hamming Distance Verification
We packed all `4204` codewords into 64-bit unsigned integers (`uint64_t`) and exhaustively evaluated `dist(x, y) = popcount(x ^ y)` across all `M * (M - 1) / 2 = 8,834,706` unordered pairs:
- **Total Pairs Checked**: `8,834,706`
- **Minimum Pairwise Hamming Distance**: `8` (required: at least `8`)
- **Maximum Pairwise Bitwise Overlap**: `3` (required: at most `3`)
- **Violating Pairs (`dist` below `8`)**: `0`
- **Exact Pairwise Distance Histogram**: `{8: 420462, 10: 1522822, 12: 3790819, 14: 3100603}` (`d=8: 420,462, d=10: 1,522,822, d=12: 3,790,819, d=14: 3,100,603`; sum of counts = `8,834,706 == 8,834,706`).

### 3.4 Independent Adversarial Mutation Test
We mutated codeword `1` into a weight-`7` word at Hamming distance `2` (overlap `6`) from codeword `0` by flipping one `'1'` bit and one `'0'` bit of codeword `0`. Re-running our independent C99 all-pairs checker immediately rejected the mutated code (`rc = 1`, `min_dist = 2`, `bad_pairs = 7`).

---

## 4. Step 2 — Audit & Execution of Author's Verifier (`claim/verify_cwc.py`)

After completing our independent verification, we inspected `claim/verify_cwc.py` and ran the reproduction command from `claim/REPRODUCE.md`.

### 4.1 Clean Artifact Execution
- **Command**: `python3 claim/verify_cwc.py claim/A54_8_7_4204.txt 54 8 7`
- **Exit Code**: `0`
- **Output**:
```text
file=A54_8_7_4204.txt sha256=d9b4340171c56a0ddc034dcb31cb4f568eb9c8e2fecddbb3a1871a0722356fca
F format: lines=4204 claimed_M=4204 bad_lines=0
W weight/distinct: bad_weight=0 distinct=4204
B packing: t=4 subsets=147140 distinct=147140 collisions=0
A all-pairs: words=4204 pairs=8834706 min_distance=8 needat_least_8 bad_pairs=0 histogram={8: 420462, 10: 1522822, 12: 3790819, 14: 3100603}
R record_check: cell=A(54,8,7) M=4204 composite_bar=4193 (Andw=4173, Trophy/PR=4193) strict_beat=True
VERDICT: VALID  A(54,8,7) at_least_ 4204
```

### 4.2 Corrupted Artifact Execution
- **Command**: Ran `claim/verify_cwc.py` on a temporary copy with codeword `1` replaced by a 2-bit flip of codeword `0`
- **Exit Code**: `1` (non-zero rejection)
- **Output**:
```text
file=A54_8_7_4204.txt sha256=13620f250dd145e94c81e94f07699ef7b245c774c9d2c52f2153ae29788cab01
F format: lines=4204 claimed_M=4204 bad_lines=0
W weight/distinct: bad_weight=0 distinct=4204
B packing: t=4 subsets=147140 distinct=147119 collisions=21
A all-pairs: words=4204 pairs=8834706 min_distance=2 needat_least_8 bad_pairs=7 histogram={2: 1, 6: 6, 8: 420454, 10: 1522997, 12: 3790846, 14: 3100402}
R record_check: cell=A(54,8,7) M=4204 composite_bar=4193 (Andw=4173, Trophy/PR=4193) strict_beat=False
VERDICT: INVALID  A(54,8,7) at_least_ 4204
```

---

## 5. Summary Verification Table

| Check | Method | Scope | Result | Status |
|---|---|---|---|---|
| Artifact SHA-256 & Size | `hashlib.sha256` | `231220` bytes | `d9b4340171c56a0d...` | PASS |
| Format, Length & Weight | Exact ASCII & popcount audit | `4204` words, `n=54, w=7` | `bad_len=0, bad_chars=0, bad_weight=0` | PASS |
| Codeword Distinctness | Set cardinality | `4204` words | `distinct = 4204` | PASS |
| Steiner `t=4`-Subset Packing | Exhaustive `C(7,4)` subsets | `147,140` subsets | `collisions = 0` | PASS |
| Independent All-Pairs Distance | C99 `uint64_t` XOR popcount | All `8,834,706` pairs | `min_dist = 8`, `bad_pairs = 0` | PASS |
| Independent Corruption Test | 2-bit flip on codeword `1` | All `8,834,706` pairs | Rejected (`min_dist = 2, bad_pairs = 7, rc = 1`) | PASS |
| Author Verifier Clean Run | `python3 claim/verify_cwc.py claim/A54_8_7_4204.txt 54 8 7` | Full suite (`F, W, B, A, R`) | `VERDICT: VALID` (`rc = 0`) | PASS |
| Author Verifier Corruption Test | 2-bit flip on codeword `1` | Full suite (`F, W, B, A, R`) | Rejected (`VERDICT: INVALID`, `rc = 1`) | PASS |

pass: true
