# Reproduction & Independent Verification Report — Binary Constant-Weight Code `A(53, 8, 7)` Lower Bound `3992`

context: subagent
context: subagent (astra)

## 1. Executive Summary
- **Target**: `constant-weight-codes` (`A(n, d, w)` lower bounds in Brouwer's table)
- **Cell**: `A(53, 8, 7)` (and complement mirror cell `A(53, 8, 46)`)
- **Claimed Lower Bound**: `M = 3992` (strictly beating the live composite bar `3987` by `+5` and Brouwer's `Andw.html` table entry `3980` by `+12`)
- **Claim Level**: `full`
- **Artifact**: `claim/A53_8_7_3992.txt` (`215568` bytes, SHA-256 `7be7a08730ebb932aa2700285fab3cfcd0cd464759ca72013f3a238ee3a60a29`)
- **Verdict**: **PASS** — Both our independent first-principles verifier (written and executed before reading `claim/verify_cwc.py`) and the author's standalone verifier confirm that `claim/A53_8_7_3992.txt` contains `3992` pairwise distinct binary codewords of length `53` and exact Hamming weight `7`, with minimum pairwise Hamming distance `8 == 8` (`0` pairs below `8` across all `7,966,036` codeword pairs) and `0` collisions among all `139,720` Steiner `t = 4`-subsets. Both verifiers also immediately reject a 2-bit-flipped corrupted copy.

---

## 2. Quoted Definition & Claim from `target.md` and `claim/CLAIM.md`

### 2.1 Mathematical Definition (`target.md`)
  - **Definition**: `A(n, d, w)` is the maximum number of binary words of length `n` and weight `w` with pairwise Hamming distance at least `d`.
  - **Success Criterion**: An explicit list of `M` distinct binary vectors of length `n`, each with Hamming weight exactly `w`, with all pairwise distances at least `d` (`d` even), where `M` is strictly greater than the lower bound shown at verification time in the `(n, d, w)` cell of `https://aeb.win.tue.nl/codes/Andw.html` (also checking the mirror cell `A(n, d, n-w)`), and strictly greater than any value for that cell in `arXiv:2608.13906` (Echols), `arXiv:2607.19550` (Lysenstoen), or prior V3R1T4S records.

### 2.2 Claim Summary (`claim/CLAIM.md`)
  - **Target**: `constant-weight-codes`
  - **Claim Level**: `full` (`+5` over live composite bar `3987`; `+12` over `Andw.html` `3980`)
  - **Artifact**: `A53_8_7_3992.txt` (`3992` binary codewords of length `53`, weight `7`, minimum pairwise Hamming distance `8`)

---

## 3. Step 1 — Independent First-Principles Verification (Executed Before Reading `claim/verify_cwc.py`)

Prior to reading `claim/verify_cwc.py`, we implemented and ran an independent verifier (Python parser + Steiner `t`-subset packing checker + compiled C99 `uint64_t` `__builtin_popcountll` all-pairs distance engine).

### 3.1 Artifact Integrity, Format, Weight & Distinctness
- **File**: `claim/A53_8_7_3992.txt`
- **Byte Size**: `215568` bytes (`3992` lines of `53` ASCII characters plus newline)
- **SHA-256**: `7be7a08730ebb932aa2700285fab3cfcd0cd464759ca72013f3a238ee3a60a29` (matches `claim/CLAIM.md` exactly)
- **Line & Alphabet Check**: `lines = 3992`, `bad_len = 0`, `bad_chars = 0` (every line has exact length `53` and consists solely of `'0'` and `'1'`).
- **Hamming Weight Check**: `bad_weight = 0` (every codeword has exact Hamming weight `w = 7`).
- **Distinctness Check**: `distinct_M = 3992 == 3992` (zero duplicate codewords).

### 3.2 Independent Steiner `t`-Subset Packing Verification
For constant weight `w = 7` and minimum even Hamming distance `d = 8`, the maximum allowed bitwise overlap between any two distinct codewords is `w - d/2 = 3`. Equivalently, every `t = w - d/2 + 1 = 4`-element subset of the `1`-positions of a codeword must be unique across the entire code (`C(7, 4) = 35` subsets per codeword):
- **Total `t = 4`-subsets**: `139,720`
- **Distinct `t = 4`-subsets**: `139,720`
- **Subset Collisions**: `0`

### 3.3 Exhaustive All-Pairs Hamming Distance Verification
We packed all `3992` codewords into 64-bit unsigned integers (`uint64_t`) and exhaustively evaluated `dist(x, y) = popcount(x ^ y)` across all `M * (M - 1) / 2 = 7,966,036` unordered pairs:
- **Total Pairs Checked**: `7,966,036`
- **Minimum Pairwise Hamming Distance**: `8` (required: at least `8`)
- **Maximum Pairwise Bitwise Overlap**: `3` (required: at most `3`)
- **Violating Pairs (`dist` below `8`)**: `0`
- **Exact Pairwise Distance Histogram**: `{8: 403503, 10: 1398836, 12: 3427264, 14: 2736433}` (`d=8: 403,503, d=10: 1,398,836, d=12: 3,427,264, d=14: 2,736,433`; sum of counts = `7,966,036 == 7,966,036`).

### 3.4 Independent Adversarial Mutation Test
We mutated codeword `1` into a weight-`7` word at Hamming distance `2` (overlap `6`) from codeword `0` by flipping one `'1'` bit and one `'0'` bit of codeword `0`. Re-running our independent C99 all-pairs checker immediately rejected the mutated code (`rc = 1`, `min_dist = 2`, `bad_pairs = 7`).

---

## 4. Step 2 — Audit & Execution of Author's Verifier (`claim/verify_cwc.py`)

After completing our independent verification, we inspected `claim/verify_cwc.py` and ran the reproduction command from `claim/REPRODUCE.md`.

### 4.1 Clean Artifact Execution
- **Command**: `python3 claim/verify_cwc.py claim/A53_8_7_3992.txt 53 8 7`
- **Exit Code**: `0`
- **Output**:
```text
file=A53_8_7_3992.txt sha256=7be7a08730ebb932aa2700285fab3cfcd0cd464759ca72013f3a238ee3a60a29
F format: lines=3992 claimed_M=3992 bad_lines=0
W weight/distinct: bad_weight=0 distinct=3992
B packing: t=4 subsets=139720 distinct=139720 collisions=0
A all-pairs: words=3992 pairs=7966036 min_distance=8 needat_least_8 bad_pairs=0 histogram={8: 403503, 10: 1398836, 12: 3427264, 14: 2736433}
R record_check: cell=A(53,8,7) M=3992 composite_bar=3987 (Andw=3980, Trophy/PR=3987) strict_beat=True
VERDICT: VALID  A(53,8,7) at_least_ 3992
```

### 4.2 Corrupted Artifact Execution
- **Command**: Ran `claim/verify_cwc.py` on a temporary copy with codeword `1` replaced by a 2-bit flip of codeword `0`
- **Exit Code**: `1` (non-zero rejection)
- **Output**:
```text
file=A53_8_7_3992.txt sha256=e30fffe22137df72c2c5f88cc6551cf9c993d1dc65e48749ab41fcbfd5ad031a
F format: lines=3992 claimed_M=3992 bad_lines=0
W weight/distinct: bad_weight=0 distinct=3992
B packing: t=4 subsets=139720 distinct=139699 collisions=21
A all-pairs: words=3992 pairs=7966036 min_distance=2 needat_least_8 bad_pairs=7 histogram={2: 1, 6: 6, 8: 403498, 10: 1398907, 12: 3427133, 14: 2736491}
R record_check: cell=A(53,8,7) M=3992 composite_bar=3987 (Andw=3980, Trophy/PR=3987) strict_beat=False
VERDICT: INVALID  A(53,8,7) at_least_ 3992
```

---

## 5. Summary Verification Table

| Check | Method | Scope | Result | Status |
|---|---|---|---|---|
| Artifact SHA-256 & Size | `hashlib.sha256` | `215568` bytes | `7be7a08730ebb932...` | PASS |
| Format, Length & Weight | Exact ASCII & popcount audit | `3992` words, `n=53, w=7` | `bad_len=0, bad_chars=0, bad_weight=0` | PASS |
| Codeword Distinctness | Set cardinality | `3992` words | `distinct = 3992` | PASS |
| Steiner `t=4`-Subset Packing | Exhaustive `C(7,4)` subsets | `139,720` subsets | `collisions = 0` | PASS |
| Independent All-Pairs Distance | C99 `uint64_t` XOR popcount | All `7,966,036` pairs | `min_dist = 8`, `bad_pairs = 0` | PASS |
| Independent Corruption Test | 2-bit flip on codeword `1` | All `7,966,036` pairs | Rejected (`min_dist = 2, bad_pairs = 7, rc = 1`) | PASS |
| Author Verifier Clean Run | `python3 claim/verify_cwc.py claim/A53_8_7_3992.txt 53 8 7` | Full suite (`F, W, B, A, R`) | `VERDICT: VALID` (`rc = 0`) | PASS |
| Author Verifier Corruption Test | 2-bit flip on codeword `1` | Full suite (`F, W, B, A, R`) | Rejected (`VERDICT: INVALID`, `rc = 1`) | PASS |

pass: true
