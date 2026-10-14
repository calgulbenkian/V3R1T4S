# Reproduction & Independent Verification Report — Binary Constant-Weight Code `A(56, 8, 7)` Lower Bound `4691`

context: subagent
context: subagent (astra)

## 1. Executive Summary
- **Target**: `constant-weight-codes` (`A(n, d, w)` lower bounds in Brouwer's table)
- **Cell**: `A(56, 8, 7)` (and complement mirror cell `A(56, 8, 49)`)
- **Claimed Lower Bound**: `M = 4691` (strictly beating the live composite bar `4685` by `+6` and Brouwer's `Andw.html` table entry `4674` by `+17`)
- **Claim Level**: `full`
- **Artifact**: `claim/A56_8_7_4691.txt` (`267387` bytes, SHA-256 `e12d11fa604fd790d622442b7d96815ed8b129256b45507a9f09bff518cf27b1`)
- **Verdict**: **PASS** — Both our independent first-principles verifier (written and executed before reading `claim/verify_cwc.py`) and the author's standalone verifier confirm that `claim/A56_8_7_4691.txt` contains `4691` pairwise distinct binary codewords of length `56` and exact Hamming weight `7`, with minimum pairwise Hamming distance `8 == 8` (`0` pairs below `8` across all `11,000,395` codeword pairs) and `0` collisions among all `164,185` Steiner `t = 4`-subsets. Both verifiers also immediately reject a 2-bit-flipped corrupted copy.

---

## 2. Quoted Definition & Claim from `target.md` and `claim/CLAIM.md`

### 2.1 Mathematical Definition (`target.md`)
  - **Definition**: `A(n, d, w)` is the maximum number of binary words of length `n` and weight `w` with pairwise Hamming distance at least `d`.
  - **Success Criterion**: An explicit list of `M` distinct binary vectors of length `n`, each with Hamming weight exactly `w`, with all pairwise distances at least `d` (`d` even), where `M` is strictly greater than the lower bound shown at verification time in the `(n, d, w)` cell of `https://aeb.win.tue.nl/codes/Andw.html` (also checking the mirror cell `A(n, d, n-w)`), and strictly greater than any value for that cell in `arXiv:2608.13906` (Echols), `arXiv:2607.19550` (Lysenstoen), or prior V3R1T4S records.

### 2.2 Claim Summary (`claim/CLAIM.md`)
  - **Target**: `constant-weight-codes`
  - **Claim Level**: `full` (`+6` over live composite bar `4685`; `+17` over `Andw.html` `4674`)
  - **Artifact**: `A56_8_7_4691.txt` (`4691` binary codewords of length `56`, weight `7`, minimum pairwise Hamming distance `8`)

---

## 3. Step 1 — Independent First-Principles Verification (Executed Before Reading `claim/verify_cwc.py`)

Prior to reading `claim/verify_cwc.py`, we implemented and ran an independent verifier (Python parser + Steiner `t`-subset packing checker + compiled C99 `uint64_t` `__builtin_popcountll` all-pairs distance engine).

### 3.1 Artifact Integrity, Format, Weight & Distinctness
- **File**: `claim/A56_8_7_4691.txt`
- **Byte Size**: `267387` bytes (`4691` lines of `56` ASCII characters plus newline)
- **SHA-256**: `e12d11fa604fd790d622442b7d96815ed8b129256b45507a9f09bff518cf27b1` (matches `claim/CLAIM.md` exactly)
- **Line & Alphabet Check**: `lines = 4691`, `bad_len = 0`, `bad_chars = 0` (every line has exact length `56` and consists solely of `'0'` and `'1'`).
- **Hamming Weight Check**: `bad_weight = 0` (every codeword has exact Hamming weight `w = 7`).
- **Distinctness Check**: `distinct_M = 4691 == 4691` (zero duplicate codewords).

### 3.2 Independent Steiner `t`-Subset Packing Verification
For constant weight `w = 7` and minimum even Hamming distance `d = 8`, the maximum allowed bitwise overlap between any two distinct codewords is `w - d/2 = 3`. Equivalently, every `t = w - d/2 + 1 = 4`-element subset of the `1`-positions of a codeword must be unique across the entire code (`C(7, 4) = 35` subsets per codeword):
- **Total `t = 4`-subsets**: `164,185`
- **Distinct `t = 4`-subsets**: `164,185`
- **Subset Collisions**: `0`

### 3.3 Exhaustive All-Pairs Hamming Distance Verification
We packed all `4691` codewords into 64-bit unsigned integers (`uint64_t`) and exhaustively evaluated `dist(x, y) = popcount(x ^ y)` across all `M * (M - 1) / 2 = 11,000,395` unordered pairs:
- **Total Pairs Checked**: `11,000,395`
- **Minimum Pairwise Hamming Distance**: `8` (required: at least `8`)
- **Maximum Pairwise Bitwise Overlap**: `3` (required: at most `3`)
- **Violating Pairs (`dist` below `8`)**: `0`
- **Exact Pairwise Distance Histogram**: `{8: 438664, 10: 1820540, 12: 4672305, 14: 4068886}` (`d=8: 438,664, d=10: 1,820,540, d=12: 4,672,305, d=14: 4,068,886`; sum of counts = `11,000,395 == 11,000,395`).

### 3.4 Independent Adversarial Mutation Test
We mutated codeword `1` into a weight-`7` word at Hamming distance `2` (overlap `6`) from codeword `0` by flipping one `'1'` bit and one `'0'` bit of codeword `0`. Re-running our independent C99 all-pairs checker immediately rejected the mutated code (`rc = 1`, `min_dist = 2`, `bad_pairs = 8`).

---

## 4. Step 2 — Audit & Execution of Author's Verifier (`claim/verify_cwc.py`)

After completing our independent verification, we inspected `claim/verify_cwc.py` and ran the reproduction command from `claim/REPRODUCE.md`.

### 4.1 Clean Artifact Execution
- **Command**: `python3 claim/verify_cwc.py claim/A56_8_7_4691.txt 56 8 7`
- **Exit Code**: `0`
- **Output**:
```text
file=A56_8_7_4691.txt sha256=e12d11fa604fd790d622442b7d96815ed8b129256b45507a9f09bff518cf27b1
F format: lines=4691 claimed_M=4691 bad_lines=0
W weight/distinct: bad_weight=0 distinct=4691
B packing: t=4 subsets=164185 distinct=164185 collisions=0
A all-pairs: words=4691 pairs=11000395 min_distance=8 needat_least_8 bad_pairs=0 histogram={8: 438664, 10: 1820540, 12: 4672305, 14: 4068886}
R record_check: cell=A(56,8,7) M=4691 composite_bar=4685 (Andw=4674, Trophy/PR=4685) strict_beat=True
VERDICT: VALID  A(56,8,7) at_least_ 4691
```

### 4.2 Corrupted Artifact Execution
- **Command**: Ran `claim/verify_cwc.py` on a temporary copy with codeword `1` replaced by a 2-bit flip of codeword `0`
- **Exit Code**: `1` (non-zero rejection)
- **Output**:
```text
file=A56_8_7_4691.txt sha256=b5f04fe7435b3f35bc36095adedb7bb798018172241379965214cab77d7a72aa
F format: lines=4691 claimed_M=4691 bad_lines=0
W weight/distinct: bad_weight=0 distinct=4691
B packing: t=4 subsets=164185 distinct=164163 collisions=22
A all-pairs: words=4691 pairs=11000395 min_distance=2 needat_least_8 bad_pairs=8 histogram={2: 1, 6: 7, 8: 438621, 10: 1820597, 12: 4672288, 14: 4068881}
R record_check: cell=A(56,8,7) M=4691 composite_bar=4685 (Andw=4674, Trophy/PR=4685) strict_beat=False
VERDICT: INVALID  A(56,8,7) at_least_ 4691
```

---

## 5. Summary Verification Table

| Check | Method | Scope | Result | Status |
|---|---|---|---|---|
| Artifact SHA-256 & Size | `hashlib.sha256` | `267387` bytes | `e12d11fa604fd790...` | PASS |
| Format, Length & Weight | Exact ASCII & popcount audit | `4691` words, `n=56, w=7` | `bad_len=0, bad_chars=0, bad_weight=0` | PASS |
| Codeword Distinctness | Set cardinality | `4691` words | `distinct = 4691` | PASS |
| Steiner `t=4`-Subset Packing | Exhaustive `C(7,4)` subsets | `164,185` subsets | `collisions = 0` | PASS |
| Independent All-Pairs Distance | C99 `uint64_t` XOR popcount | All `11,000,395` pairs | `min_dist = 8`, `bad_pairs = 0` | PASS |
| Independent Corruption Test | 2-bit flip on codeword `1` | All `11,000,395` pairs | Rejected (`min_dist = 2, bad_pairs = 8, rc = 1`) | PASS |
| Author Verifier Clean Run | `python3 claim/verify_cwc.py claim/A56_8_7_4691.txt 56 8 7` | Full suite (`F, W, B, A, R`) | `VERDICT: VALID` (`rc = 0`) | PASS |
| Author Verifier Corruption Test | 2-bit flip on codeword `1` | Full suite (`F, W, B, A, R`) | Rejected (`VERDICT: INVALID`, `rc = 1`) | PASS |

pass: true
