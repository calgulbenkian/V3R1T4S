# Reproduction & Independent Verification Report — Binary Constant-Weight Code `A(52, 8, 7)` Lower Bound `3802`

context: subagent
context: subagent (astra)

## 1. Executive Summary
- **Target**: `constant-weight-codes` (`A(n, d, w)` lower bounds in Brouwer's table)
- **Cell**: `A(52, 8, 7)` (and complement mirror cell `A(52, 8, 45)`)
- **Claimed Lower Bound**: `M = 3802` (strictly beating the live composite bar `3799` by `+3` and Brouwer's `Andw.html` table entry `3797` by `+5`)
- **Claim Level**: `full`
- **Artifact**: `claim/A52_8_7_3802.txt` (`201506` bytes, SHA-256 `4743db7cec4929d05cba257484e8cce16c1f304d94efdb0b82d6870f191e473c`)
- **Verdict**: **PASS** — Both our independent first-principles verifier (written and executed before reading `claim/verify_cwc.py`) and the author's standalone verifier confirm that `claim/A52_8_7_3802.txt` contains `3802` pairwise distinct binary codewords of length `52` and exact Hamming weight `7`, with minimum pairwise Hamming distance `8 == 8` (`0` pairs below `8` across all `7,225,701` codeword pairs) and `0` collisions among all `133,070` Steiner `t = 4`-subsets. Both verifiers also immediately reject a 2-bit-flipped corrupted copy.

---

## 2. Quoted Definition & Claim from `target.md` and `claim/CLAIM.md`

### 2.1 Mathematical Definition (`target.md`)
  - **Definition**: `A(n, d, w)` is the maximum number of binary words of length `n` and weight `w` with pairwise Hamming distance at least `d`.
  - **Success Criterion**: An explicit list of `M` distinct binary vectors of length `n`, each with Hamming weight exactly `w`, with all pairwise distances at least `d` (`d` even), where `M` is strictly greater than the lower bound shown at verification time in the `(n, d, w)` cell of `https://aeb.win.tue.nl/codes/Andw.html` (also checking the mirror cell `A(n, d, n-w)`), and strictly greater than any value for that cell in `arXiv:2608.13906` (Echols), `arXiv:2607.19550` (Lysenstoen), or prior V3R1T4S records.

### 2.2 Claim Summary (`claim/CLAIM.md`)
  - **Target**: `constant-weight-codes`
  - **Claim Level**: `full` (`+3` over live composite bar `3799`; `+5` over `Andw.html` `3797`)
  - **Artifact**: `A52_8_7_3802.txt` (`3802` binary codewords of length `52`, weight `7`, minimum pairwise Hamming distance `8`)

---

## 3. Step 1 — Independent First-Principles Verification (Executed Before Reading `claim/verify_cwc.py`)

Prior to reading `claim/verify_cwc.py`, we implemented and ran an independent verifier (Python parser + Steiner `t`-subset packing checker + compiled C99 `uint64_t` `__builtin_popcountll` all-pairs distance engine).

### 3.1 Artifact Integrity, Format, Weight & Distinctness
- **File**: `claim/A52_8_7_3802.txt`
- **Byte Size**: `201506` bytes (`3802` lines of `52` ASCII characters plus newline)
- **SHA-256**: `4743db7cec4929d05cba257484e8cce16c1f304d94efdb0b82d6870f191e473c` (matches `claim/CLAIM.md` exactly)
- **Line & Alphabet Check**: `lines = 3802`, `bad_len = 0`, `bad_chars = 0` (every line has exact length `52` and consists solely of `'0'` and `'1'`).
- **Hamming Weight Check**: `bad_weight = 0` (every codeword has exact Hamming weight `w = 7`).
- **Distinctness Check**: `distinct_M = 3802 == 3802` (zero duplicate codewords).

### 3.2 Independent Steiner `t`-Subset Packing Verification
For constant weight `w = 7` and minimum even Hamming distance `d = 8`, the maximum allowed bitwise overlap between any two distinct codewords is `w - d/2 = 3`. Equivalently, every `t = w - d/2 + 1 = 4`-element subset of the `1`-positions of a codeword must be unique across the entire code (`C(7, 4) = 35` subsets per codeword):
- **Total `t = 4`-subsets**: `133,070`
- **Distinct `t = 4`-subsets**: `133,070`
- **Subset Collisions**: `0`

### 3.3 Exhaustive All-Pairs Hamming Distance Verification
We packed all `3802` codewords into 64-bit unsigned integers (`uint64_t`) and exhaustively evaluated `dist(x, y) = popcount(x ^ y)` across all `M * (M - 1) / 2 = 7,225,701` unordered pairs:
- **Total Pairs Checked**: `7,225,701`
- **Minimum Pairwise Hamming Distance**: `8` (required: at least `8`)
- **Maximum Pairwise Bitwise Overlap**: `3` (required: at most `3`)
- **Violating Pairs (`dist` below `8`)**: `0`
- **Exact Pairwise Distance Histogram**: `{8: 390656, 10: 1289145, 12: 3118070, 14: 2427830}` (`d=8: 390,656, d=10: 1,289,145, d=12: 3,118,070, d=14: 2,427,830`; sum of counts = `7,225,701 == 7,225,701`).

### 3.4 Independent Adversarial Mutation Test
We mutated codeword `1` into a weight-`7` word at Hamming distance `2` (overlap `6`) from codeword `0` by flipping one `'1'` bit and one `'0'` bit of codeword `0`. Re-running our independent C99 all-pairs checker immediately rejected the mutated code (`rc = 1`, `min_dist = 2`, `bad_pairs = 11`).

---

## 4. Step 2 — Audit & Execution of Author's Verifier (`claim/verify_cwc.py`)

After completing our independent verification, we inspected `claim/verify_cwc.py` and ran the reproduction command from `claim/REPRODUCE.md`.

### 4.1 Clean Artifact Execution
- **Command**: `python3 claim/verify_cwc.py claim/A52_8_7_3802.txt 52 8 7`
- **Exit Code**: `0`
- **Output**:
```text
file=A52_8_7_3802.txt sha256=4743db7cec4929d05cba257484e8cce16c1f304d94efdb0b82d6870f191e473c
F format: lines=3802 claimed_M=3802 bad_lines=0
W weight/distinct: bad_weight=0 distinct=3802
B packing: t=4 subsets=133070 distinct=133070 collisions=0
A all-pairs: words=3802 pairs=7225701 min_distance=8 needat_least_8 bad_pairs=0 histogram={8: 390656, 10: 1289145, 12: 3118070, 14: 2427830}
R record_check: cell=A(52,8,7) M=3802 composite_bar=3799 (Andw=3797, Trophy/PR=3799) strict_beat=True
VERDICT: VALID  A(52,8,7) at_least_ 3802
```

### 4.2 Corrupted Artifact Execution
- **Command**: Ran `claim/verify_cwc.py` on a temporary copy with codeword `1` replaced by a 2-bit flip of codeword `0`
- **Exit Code**: `1` (non-zero rejection)
- **Output**:
```text
file=A52_8_7_3802.txt sha256=7143079faa4361db481920a81a72cac64f273869bc63190b9025c37f324075a8
F format: lines=3802 claimed_M=3802 bad_lines=0
W weight/distinct: bad_weight=0 distinct=3802
B packing: t=4 subsets=133070 distinct=133045 collisions=25
A all-pairs: words=3802 pairs=7225701 min_distance=2 needat_least_8 bad_pairs=11 histogram={2: 1, 6: 10, 8: 390656, 10: 1289244, 12: 3118052, 14: 2427738}
R record_check: cell=A(52,8,7) M=3802 composite_bar=3799 (Andw=3797, Trophy/PR=3799) strict_beat=False
VERDICT: INVALID  A(52,8,7) at_least_ 3802
```

---

## 5. Summary Verification Table

| Check | Method | Scope | Result | Status |
|---|---|---|---|---|
| Artifact SHA-256 & Size | `hashlib.sha256` | `201506` bytes | `4743db7cec4929d0...` | PASS |
| Format, Length & Weight | Exact ASCII & popcount audit | `3802` words, `n=52, w=7` | `bad_len=0, bad_chars=0, bad_weight=0` | PASS |
| Codeword Distinctness | Set cardinality | `3802` words | `distinct = 3802` | PASS |
| Steiner `t=4`-Subset Packing | Exhaustive `C(7,4)` subsets | `133,070` subsets | `collisions = 0` | PASS |
| Independent All-Pairs Distance | C99 `uint64_t` XOR popcount | All `7,225,701` pairs | `min_dist = 8`, `bad_pairs = 0` | PASS |
| Independent Corruption Test | 2-bit flip on codeword `1` | All `7,225,701` pairs | Rejected (`min_dist = 2, bad_pairs = 11, rc = 1`) | PASS |
| Author Verifier Clean Run | `python3 claim/verify_cwc.py claim/A52_8_7_3802.txt 52 8 7` | Full suite (`F, W, B, A, R`) | `VERDICT: VALID` (`rc = 0`) | PASS |
| Author Verifier Corruption Test | 2-bit flip on codeword `1` | Full suite (`F, W, B, A, R`) | Rejected (`VERDICT: INVALID`, `rc = 1`) | PASS |

pass: true
