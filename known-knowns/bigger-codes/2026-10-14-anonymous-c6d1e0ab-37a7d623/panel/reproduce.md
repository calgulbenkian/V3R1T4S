# Reproduction & Independent Verification Report — Binary Constant-Weight Code `A(55, 8, 7)` Lower Bound `4431`

context: subagent
context: subagent (astra)

## 1. Executive Summary
- **Target**: `constant-weight-codes` (`A(n, d, w)` lower bounds in Brouwer's table)
- **Cell**: `A(55, 8, 7)` (and complement mirror cell `A(55, 8, 48)`)
- **Claimed Lower Bound**: `M = 4431` (strictly beating the live composite bar `4426` by `+5` and Brouwer's `Andw.html` table entry `4417` by `+14`)
- **Claim Level**: `full`
- **Artifact**: `claim/A55_8_7_4431.txt` (`248136` bytes, SHA-256 `37a7d62321644d15eb6d70962893f7fbbd59bb36b10230f74ac56902f21dc158`)
- **Verdict**: **PASS** — Both our independent first-principles verifier (written and executed before reading `claim/verify_cwc.py`) and the author's standalone verifier confirm that `claim/A55_8_7_4431.txt` contains `4431` pairwise distinct binary codewords of length `55` and exact Hamming weight `7`, with minimum pairwise Hamming distance `8 == 8` (`0` pairs below `8` across all `9,814,665` codeword pairs) and `0` collisions among all `155,085` Steiner `t = 4`-subsets. Both verifiers also immediately reject a 2-bit-flipped corrupted copy.

---

## 2. Quoted Definition & Claim from `target.md` and `claim/CLAIM.md`

### 2.1 Mathematical Definition (`target.md`)
  - **Definition**: `A(n, d, w)` is the maximum number of binary words of length `n` and weight `w` with pairwise Hamming distance at least `d`.
  - **Success Criterion**: An explicit list of `M` distinct binary vectors of length `n`, each with Hamming weight exactly `w`, with all pairwise distances at least `d` (`d` even), where `M` is strictly greater than the lower bound shown at verification time in the `(n, d, w)` cell of `https://aeb.win.tue.nl/codes/Andw.html` (also checking the mirror cell `A(n, d, n-w)`), and strictly greater than any value for that cell in `arXiv:2608.13906` (Echols), `arXiv:2607.19550` (Lysenstoen), or prior V3R1T4S records.

### 2.2 Claim Summary (`claim/CLAIM.md`)
  - **Target**: `constant-weight-codes`
  - **Claim Level**: `full` (`+5` over live composite bar `4426`; `+14` over `Andw.html` `4417`)
  - **Artifact**: `A55_8_7_4431.txt` (`4431` binary codewords of length `55`, weight `7`, minimum pairwise Hamming distance `8`)

---

## 3. Step 1 — Independent First-Principles Verification (Executed Before Reading `claim/verify_cwc.py`)

Prior to reading `claim/verify_cwc.py`, we implemented and ran an independent verifier (Python parser + Steiner `t`-subset packing checker + compiled C99 `uint64_t` `__builtin_popcountll` all-pairs distance engine).

### 3.1 Artifact Integrity, Format, Weight & Distinctness
- **File**: `claim/A55_8_7_4431.txt`
- **Byte Size**: `248136` bytes (`4431` lines of `55` ASCII characters plus newline)
- **SHA-256**: `37a7d62321644d15eb6d70962893f7fbbd59bb36b10230f74ac56902f21dc158` (matches `claim/CLAIM.md` exactly)
- **Line & Alphabet Check**: `lines = 4431`, `bad_len = 0`, `bad_chars = 0` (every line has exact length `55` and consists solely of `'0'` and `'1'`).
- **Hamming Weight Check**: `bad_weight = 0` (every codeword has exact Hamming weight `w = 7`).
- **Distinctness Check**: `distinct_M = 4431 == 4431` (zero duplicate codewords).

### 3.2 Independent Steiner `t`-Subset Packing Verification
For constant weight `w = 7` and minimum even Hamming distance `d = 8`, the maximum allowed bitwise overlap between any two distinct codewords is `w - d/2 = 3`. Equivalently, every `t = w - d/2 + 1 = 4`-element subset of the `1`-positions of a codeword must be unique across the entire code (`C(7, 4) = 35` subsets per codeword):
- **Total `t = 4`-subsets**: `155,085`
- **Distinct `t = 4`-subsets**: `155,085`
- **Subset Collisions**: `0`

### 3.3 Exhaustive All-Pairs Hamming Distance Verification
We packed all `4431` codewords into 64-bit unsigned integers (`uint64_t`) and exhaustively evaluated `dist(x, y) = popcount(x ^ y)` across all `M * (M - 1) / 2 = 9,814,665` unordered pairs:
- **Total Pairs Checked**: `9,814,665`
- **Minimum Pairwise Hamming Distance**: `8` (required: at least `8`)
- **Maximum Pairwise Bitwise Overlap**: `3` (required: at most `3`)
- **Violating Pairs (`dist` below `8`)**: `0`
- **Exact Pairwise Distance Histogram**: `{8: 438298, 10: 1656042, 12: 4196975, 14: 3523350}` (`d=8: 438,298, d=10: 1,656,042, d=12: 4,196,975, d=14: 3,523,350`; sum of counts = `9,814,665 == 9,814,665`).

### 3.4 Independent Adversarial Mutation Test
We mutated codeword `1` into a weight-`7` word at Hamming distance `2` (overlap `6`) from codeword `0` by flipping one `'1'` bit and one `'0'` bit of codeword `0`. Re-running our independent C99 all-pairs checker immediately rejected the mutated code (`rc = 1`, `min_dist = 2`, `bad_pairs = 8`).

---

## 4. Step 2 — Audit & Execution of Author's Verifier (`claim/verify_cwc.py`)

After completing our independent verification, we inspected `claim/verify_cwc.py` and ran the reproduction command from `claim/REPRODUCE.md`.

### 4.1 Clean Artifact Execution
- **Command**: `python3 claim/verify_cwc.py claim/A55_8_7_4431.txt 55 8 7`
- **Exit Code**: `0`
- **Output**:
```text
file=A55_8_7_4431.txt sha256=37a7d62321644d15eb6d70962893f7fbbd59bb36b10230f74ac56902f21dc158
F format: lines=4431 claimed_M=4431 bad_lines=0
W weight/distinct: bad_weight=0 distinct=4431
B packing: t=4 subsets=155085 distinct=155085 collisions=0
A all-pairs: words=4431 pairs=9814665 min_distance=8 needat_least_8 bad_pairs=0 histogram={8: 438298, 10: 1656042, 12: 4196975, 14: 3523350}
R record_check: cell=A(55,8,7) M=4431 composite_bar=4426 (Andw=4417, Trophy/PR=4426) strict_beat=True
VERDICT: VALID  A(55,8,7) at_least_ 4431
```

### 4.2 Corrupted Artifact Execution
- **Command**: Ran `claim/verify_cwc.py` on a temporary copy with codeword `1` replaced by a 2-bit flip of codeword `0`
- **Exit Code**: `1` (non-zero rejection)
- **Output**:
```text
file=A55_8_7_4431.txt sha256=fe25a5ab43d8c68f7a0c11f012248fc27abc402254c45f2872a2d69163ef00a7
F format: lines=4431 claimed_M=4431 bad_lines=0
W weight/distinct: bad_weight=0 distinct=4431
B packing: t=4 subsets=155085 distinct=155063 collisions=22
A all-pairs: words=4431 pairs=9814665 min_distance=2 needat_least_8 bad_pairs=8 histogram={2: 1, 6: 7, 8: 438294, 10: 1656196, 12: 4196991, 14: 3523176}
R record_check: cell=A(55,8,7) M=4431 composite_bar=4426 (Andw=4417, Trophy/PR=4426) strict_beat=False
VERDICT: INVALID  A(55,8,7) at_least_ 4431
```

---

## 5. Summary Verification Table

| Check | Method | Scope | Result | Status |
|---|---|---|---|---|
| Artifact SHA-256 & Size | `hashlib.sha256` | `248136` bytes | `37a7d62321644d15...` | PASS |
| Format, Length & Weight | Exact ASCII & popcount audit | `4431` words, `n=55, w=7` | `bad_len=0, bad_chars=0, bad_weight=0` | PASS |
| Codeword Distinctness | Set cardinality | `4431` words | `distinct = 4431` | PASS |
| Steiner `t=4`-Subset Packing | Exhaustive `C(7,4)` subsets | `155,085` subsets | `collisions = 0` | PASS |
| Independent All-Pairs Distance | C99 `uint64_t` XOR popcount | All `9,814,665` pairs | `min_dist = 8`, `bad_pairs = 0` | PASS |
| Independent Corruption Test | 2-bit flip on codeword `1` | All `9,814,665` pairs | Rejected (`min_dist = 2, bad_pairs = 8, rc = 1`) | PASS |
| Author Verifier Clean Run | `python3 claim/verify_cwc.py claim/A55_8_7_4431.txt 55 8 7` | Full suite (`F, W, B, A, R`) | `VERDICT: VALID` (`rc = 0`) | PASS |
| Author Verifier Corruption Test | 2-bit flip on codeword `1` | Full suite (`F, W, B, A, R`) | Rejected (`VERDICT: INVALID`, `rc = 1`) | PASS |

pass: true
