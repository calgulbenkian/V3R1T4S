# Reproduction & Independent Verification Report — Binary Constant-Weight Code `A(35, 6, 6)` Lower Bound `2218`

context: subagent
context: subagent (astra)

## 1. Executive Summary
- **Target**: `constant-weight-codes` (`A(n, d, w)` lower bounds in Brouwer's table)
- **Cell**: `A(35, 6, 6)` (and complement mirror cell `A(35, 6, 29)`)
- **Claimed Lower Bound**: `M = 2218` (strictly beating the live composite bar `2217` by `+1` and Brouwer's `Andw.html` table entry `2209` by `+9`)
- **Claim Level**: `full`
- **Artifact**: `claim/A35_6_6_2218.txt` (`79848` bytes, SHA-256 `dd2eb057e40bc19bbd7f6a2838681200d6d55b4018e9b01a62082c35822e413e`)
- **Verdict**: **PASS** — Both our independent first-principles verifier (written and executed before reading `claim/verify_cwc.py`) and the author's standalone verifier confirm that `claim/A35_6_6_2218.txt` contains `2218` pairwise distinct binary codewords of length `35` and exact Hamming weight `6`, with minimum pairwise Hamming distance `6 == 6` (`0` pairs below `6` across all `2,458,653` codeword pairs) and `0` collisions among all `33,270` Steiner `t = 4`-subsets. Both verifiers also immediately reject a 2-bit-flipped corrupted copy.

---

## 2. Quoted Definition & Claim from `target.md` and `claim/CLAIM.md`

### 2.1 Mathematical Definition (`target.md`)
  - **Definition**: `A(n, d, w)` is the maximum number of binary words of length `n` and weight `w` with pairwise Hamming distance at least `d`.
  - **Success Criterion**: An explicit list of `M` distinct binary vectors of length `n`, each with Hamming weight exactly `w`, with all pairwise distances at least `d` (`d` even), where `M` is strictly greater than the lower bound shown at verification time in the `(n, d, w)` cell of `https://aeb.win.tue.nl/codes/Andw.html` (also checking the mirror cell `A(n, d, n-w)`), and strictly greater than any value for that cell in `arXiv:2608.13906` (Echols), `arXiv:2607.19550` (Lysenstoen), or prior V3R1T4S records.

### 2.2 Claim Summary (`claim/CLAIM.md`)
  - **Target**: `constant-weight-codes`
  - **Claim Level**: `full` (`+1` over live composite bar `2217`; `+9` over `Andw.html` `2209`)
  - **Artifact**: `A35_6_6_2218.txt` (`2218` binary codewords of length `35`, weight `6`, minimum pairwise Hamming distance `6`)

---

## 3. Step 1 — Independent First-Principles Verification (Executed Before Reading `claim/verify_cwc.py`)

Prior to reading `claim/verify_cwc.py`, we implemented and ran an independent verifier (Python parser + Steiner `t`-subset packing checker + compiled C99 `uint64_t` `__builtin_popcountll` all-pairs distance engine).

### 3.1 Artifact Integrity, Format, Weight & Distinctness
- **File**: `claim/A35_6_6_2218.txt`
- **Byte Size**: `79848` bytes (`2218` lines of `35` ASCII characters plus newline)
- **SHA-256**: `dd2eb057e40bc19bbd7f6a2838681200d6d55b4018e9b01a62082c35822e413e` (matches `claim/CLAIM.md` exactly)
- **Line & Alphabet Check**: `lines = 2218`, `bad_len = 0`, `bad_chars = 0` (every line has exact length `35` and consists solely of `'0'` and `'1'`).
- **Hamming Weight Check**: `bad_weight = 0` (every codeword has exact Hamming weight `w = 6`).
- **Distinctness Check**: `distinct_M = 2218 == 2218` (zero duplicate codewords).

### 3.2 Independent Steiner `t`-Subset Packing Verification
For constant weight `w = 6` and minimum even Hamming distance `d = 6`, the maximum allowed bitwise overlap between any two distinct codewords is `w - d/2 = 3`. Equivalently, every `t = w - d/2 + 1 = 4`-element subset of the `1`-positions of a codeword must be unique across the entire code (`C(6, 4) = 15` subsets per codeword):
- **Total `t = 4`-subsets**: `33,270`
- **Distinct `t = 4`-subsets**: `33,270`
- **Subset Collisions**: `0`

### 3.3 Exhaustive All-Pairs Hamming Distance Verification
We packed all `2218` codewords into 64-bit unsigned integers (`uint64_t`) and exhaustively evaluated `dist(x, y) = popcount(x ^ y)` across all `M * (M - 1) / 2 = 2,458,653` unordered pairs:
- **Total Pairs Checked**: `2,458,653`
- **Minimum Pairwise Hamming Distance**: `6` (required: at least `6`)
- **Maximum Pairwise Bitwise Overlap**: `3` (required: at most `3`)
- **Violating Pairs (`dist` below `6`)**: `0`
- **Exact Pairwise Distance Histogram**: `{6: 133550, 8: 523436, 10: 1087173, 12: 714494}` (`d=6: 133,550, d=8: 523,436, d=10: 1,087,173, d=12: 714,494`; sum of counts = `2,458,653 == 2,458,653`).

### 3.4 Independent Adversarial Mutation Test
We mutated codeword `1` into a weight-`6` word at Hamming distance `2` (overlap `5`) from codeword `0` by flipping one `'1'` bit and one `'0'` bit of codeword `0`. Re-running our independent C99 all-pairs checker immediately rejected the mutated code (`rc = 1`, `min_dist = 2`, `bad_pairs = 4`).

---

## 4. Step 2 — Audit & Execution of Author's Verifier (`claim/verify_cwc.py`)

After completing our independent verification, we inspected `claim/verify_cwc.py` and ran the reproduction command from `claim/REPRODUCE.md`.

### 4.1 Clean Artifact Execution
- **Command**: `python3 claim/verify_cwc.py claim/A35_6_6_2218.txt 35 6 6`
- **Exit Code**: `0`
- **Output**:
```text
file=A35_6_6_2218.txt sha256=dd2eb057e40bc19bbd7f6a2838681200d6d55b4018e9b01a62082c35822e413e
F format: lines=2218 claimed_M=2218 bad_lines=0
W weight/distinct: bad_weight=0 distinct=2218
B packing: t=4 subsets=33270 distinct=33270 collisions=0
A all-pairs: words=2218 pairs=2458653 min_distance=6 needat_least_6 bad_pairs=0 histogram={6: 133550, 8: 523436, 10: 1087173, 12: 714494}
R record_check: cell=A(35,6,6) M=2218 composite_bar=2217 (Andw=2209, Trophy/PR=2217) strict_beat=True
VERDICT: VALID  A(35,6,6) at_least_ 2218
```

### 4.2 Corrupted Artifact Execution
- **Command**: Ran `claim/verify_cwc.py` on a temporary copy with codeword `1` replaced by a 2-bit flip of codeword `0`
- **Exit Code**: `1` (non-zero rejection)
- **Output**:
```text
file=A35_6_6_2218.txt sha256=392c960cd6534b2b22005939c079eb4573a137a3dbf9e38d96a8f1565f10a1b7
F format: lines=2218 claimed_M=2218 bad_lines=0
W weight/distinct: bad_weight=0 distinct=2218
B packing: t=4 subsets=33270 distinct=33262 collisions=8
A all-pairs: words=2218 pairs=2458653 min_distance=2 needat_least_6 bad_pairs=4 histogram={2: 1, 4: 3, 6: 133509, 8: 523390, 10: 1087205, 12: 714545}
R record_check: cell=A(35,6,6) M=2218 composite_bar=2217 (Andw=2209, Trophy/PR=2217) strict_beat=False
VERDICT: INVALID  A(35,6,6) at_least_ 2218
```

---

## 5. Summary Verification Table

| Check | Method | Scope | Result | Status |
|---|---|---|---|---|
| Artifact SHA-256 & Size | `hashlib.sha256` | `79848` bytes | `dd2eb057e40bc19b...` | PASS |
| Format, Length & Weight | Exact ASCII & popcount audit | `2218` words, `n=35, w=6` | `bad_len=0, bad_chars=0, bad_weight=0` | PASS |
| Codeword Distinctness | Set cardinality | `2218` words | `distinct = 2218` | PASS |
| Steiner `t=4`-Subset Packing | Exhaustive `C(6,4)` subsets | `33,270` subsets | `collisions = 0` | PASS |
| Independent All-Pairs Distance | C99 `uint64_t` XOR popcount | All `2,458,653` pairs | `min_dist = 6`, `bad_pairs = 0` | PASS |
| Independent Corruption Test | 2-bit flip on codeword `1` | All `2,458,653` pairs | Rejected (`min_dist = 2, bad_pairs = 4, rc = 1`) | PASS |
| Author Verifier Clean Run | `python3 claim/verify_cwc.py claim/A35_6_6_2218.txt 35 6 6` | Full suite (`F, W, B, A, R`) | `VERDICT: VALID` (`rc = 0`) | PASS |
| Author Verifier Corruption Test | 2-bit flip on codeword `1` | Full suite (`F, W, B, A, R`) | Rejected (`VERDICT: INVALID`, `rc = 1`) | PASS |

pass: true
