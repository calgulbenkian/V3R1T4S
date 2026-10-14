# Reproduction & Independent Verification Report — Binary Constant-Weight Code `A(27, 8, 10)` Lower Bound `1740`

context: subagent
context: subagent (astra)

## 1. Executive Summary
- **Target**: `constant-weight-codes` (`A(n, d, w)` lower bounds in Brouwer's table)
- **Cell**: `A(27, 8, 10)` (and complement mirror cell `A(27, 8, 17)`)
- **Claimed Lower Bound**: `M = 1740` (strictly beating the live composite bar `1737` by `+3` and Brouwer's `Andw.html` table entry `1728` by `+12`)
- **Claim Level**: `full`
- **Artifact**: `claim/A27_8_10_1740.txt` (`48720` bytes, SHA-256 `bdbf1cf2b34d5a2771172cea5d11fe6abcff25a0de03cc60808796fbe6e0acbe`)
- **Verdict**: **PASS** — Both our independent first-principles verifier (written and executed before reading `claim/verify_cwc.py`) and the author's standalone verifier confirm that `claim/A27_8_10_1740.txt` contains `1740` pairwise distinct binary codewords of length `27` and exact Hamming weight `10`, with minimum pairwise Hamming distance `8 == 8` (`0` pairs below `8` across all `1,512,930` codeword pairs) and `0` collisions among all `208,800` Steiner `t = 7`-subsets. Both verifiers also immediately reject a 2-bit-flipped corrupted copy.

---

## 2. Quoted Definition & Claim from `target.md` and `claim/CLAIM.md`

### 2.1 Mathematical Definition (`target.md`)
  - **Definition**: `A(n, d, w)` is the maximum number of binary words of length `n` and weight `w` with pairwise Hamming distance at least `d`.
  - **Success Criterion**: An explicit list of `M` distinct binary vectors of length `n`, each with Hamming weight exactly `w`, with all pairwise distances at least `d` (`d` even), where `M` is strictly greater than the lower bound shown at verification time in the `(n, d, w)` cell of `https://aeb.win.tue.nl/codes/Andw.html` (also checking the mirror cell `A(n, d, n-w)`), and strictly greater than any value for that cell in `arXiv:2608.13906` (Echols), `arXiv:2607.19550` (Lysenstoen), or prior V3R1T4S records.

### 2.2 Claim Summary (`claim/CLAIM.md`)
  - **Target**: `constant-weight-codes`
  - **Claim Level**: `full` (`+3` over live composite bar `1737`; `+12` over `Andw.html` `1728`)
  - **Artifact**: `A27_8_10_1740.txt` (`1740` binary codewords of length `27`, weight `10`, minimum pairwise Hamming distance `8`)

---

## 3. Step 1 — Independent First-Principles Verification (Executed Before Reading `claim/verify_cwc.py`)

Prior to reading `claim/verify_cwc.py`, we implemented and ran an independent verifier (Python parser + Steiner `t`-subset packing checker + compiled C99 `uint64_t` `__builtin_popcountll` all-pairs distance engine).

### 3.1 Artifact Integrity, Format, Weight & Distinctness
- **File**: `claim/A27_8_10_1740.txt`
- **Byte Size**: `48720` bytes (`1740` lines of `27` ASCII characters plus newline)
- **SHA-256**: `bdbf1cf2b34d5a2771172cea5d11fe6abcff25a0de03cc60808796fbe6e0acbe` (matches `claim/CLAIM.md` exactly)
- **Line & Alphabet Check**: `lines = 1740`, `bad_len = 0`, `bad_chars = 0` (every line has exact length `27` and consists solely of `'0'` and `'1'`).
- **Hamming Weight Check**: `bad_weight = 0` (every codeword has exact Hamming weight `w = 10`).
- **Distinctness Check**: `distinct_M = 1740 == 1740` (zero duplicate codewords).

### 3.2 Independent Steiner `t`-Subset Packing Verification
For constant weight `w = 10` and minimum even Hamming distance `d = 8`, the maximum allowed bitwise overlap between any two distinct codewords is `w - d/2 = 6`. Equivalently, every `t = w - d/2 + 1 = 7`-element subset of the `1`-positions of a codeword must be unique across the entire code (`C(10, 7) = 120` subsets per codeword):
- **Total `t = 7`-subsets**: `208,800`
- **Distinct `t = 7`-subsets**: `208,800`
- **Subset Collisions**: `0`

### 3.3 Exhaustive All-Pairs Hamming Distance Verification
We packed all `1740` codewords into 64-bit unsigned integers (`uint64_t`) and exhaustively evaluated `dist(x, y) = popcount(x ^ y)` across all `M * (M - 1) / 2 = 1,512,930` unordered pairs:
- **Total Pairs Checked**: `1,512,930`
- **Minimum Pairwise Hamming Distance**: `8` (required: at least `8`)
- **Maximum Pairwise Bitwise Overlap**: `6` (required: at most `6`)
- **Violating Pairs (`dist` below `8`)**: `0`
- **Exact Pairwise Distance Histogram**: `{8: 178567, 10: 121676, 12: 676640, 14: 245659, 16: 261670, 18: 24724, 20: 3994}` (`d=8: 178,567, d=10: 121,676, d=12: 676,640, d=14: 245,659, d=16: 261,670, d=18: 24,724, d=20: 3,994`; sum of counts = `1,512,930 == 1,512,930`).

### 3.4 Independent Adversarial Mutation Test
We mutated codeword `1` into a weight-`10` word at Hamming distance `2` (overlap `9`) from codeword `0` by flipping one `'1'` bit and one `'0'` bit of codeword `0`. Re-running our independent C99 all-pairs checker immediately rejected the mutated code (`rc = 1`, `min_dist = 2`, `bad_pairs = 9`).

---

## 4. Step 2 — Audit & Execution of Author's Verifier (`claim/verify_cwc.py`)

After completing our independent verification, we inspected `claim/verify_cwc.py` and ran the reproduction command from `claim/REPRODUCE.md`.

### 4.1 Clean Artifact Execution
- **Command**: `python3 claim/verify_cwc.py claim/A27_8_10_1740.txt 27 8 10`
- **Exit Code**: `0`
- **Output**:
```text
file=A27_8_10_1740.txt sha256=bdbf1cf2b34d5a2771172cea5d11fe6abcff25a0de03cc60808796fbe6e0acbe
F format: lines=1740 claimed_M=1740 bad_lines=0
W weight/distinct: bad_weight=0 distinct=1740
B packing: t=7 subsets=208800 distinct=208800 collisions=0
A all-pairs: words=1740 pairs=1512930 min_distance=8 needat_least_8 bad_pairs=0 histogram={8: 178567, 10: 121676, 12: 676640, 14: 245659, 16: 261670, 18: 24724, 20: 3994}
R record_check: cell=A(27,8,10) M=1740 composite_bar=1737 (Andw=1728, Trophy/PR=1737) strict_beat=True
VERDICT: VALID  A(27,8,10) at_least_ 1740
```

### 4.2 Corrupted Artifact Execution
- **Command**: Ran `claim/verify_cwc.py` on a temporary copy with codeword `1` replaced by a 2-bit flip of codeword `0`
- **Exit Code**: `1` (non-zero rejection)
- **Output**:
```text
file=A27_8_10_1740.txt sha256=9138da0fbafeedaea86b24490ee81836ea850a1befde29bc4f2a8c24fec42165
F format: lines=1740 claimed_M=1740 bad_lines=0
W weight/distinct: bad_weight=0 distinct=1740
B packing: t=7 subsets=208800 distinct=208756 collisions=44
A all-pairs: words=1740 pairs=1512930 min_distance=2 needat_least_8 bad_pairs=9 histogram={2: 1, 6: 8, 8: 178451, 10: 121857, 12: 676311, 14: 245981, 16: 261568, 18: 24762, 20: 3991}
R record_check: cell=A(27,8,10) M=1740 composite_bar=1737 (Andw=1728, Trophy/PR=1737) strict_beat=False
VERDICT: INVALID  A(27,8,10) at_least_ 1740
```

---

## 5. Summary Verification Table

| Check | Method | Scope | Result | Status |
|---|---|---|---|---|
| Artifact SHA-256 & Size | `hashlib.sha256` | `48720` bytes | `bdbf1cf2b34d5a27...` | PASS |
| Format, Length & Weight | Exact ASCII & popcount audit | `1740` words, `n=27, w=10` | `bad_len=0, bad_chars=0, bad_weight=0` | PASS |
| Codeword Distinctness | Set cardinality | `1740` words | `distinct = 1740` | PASS |
| Steiner `t=7`-Subset Packing | Exhaustive `C(10,7)` subsets | `208,800` subsets | `collisions = 0` | PASS |
| Independent All-Pairs Distance | C99 `uint64_t` XOR popcount | All `1,512,930` pairs | `min_dist = 8`, `bad_pairs = 0` | PASS |
| Independent Corruption Test | 2-bit flip on codeword `1` | All `1,512,930` pairs | Rejected (`min_dist = 2, bad_pairs = 9, rc = 1`) | PASS |
| Author Verifier Clean Run | `python3 claim/verify_cwc.py claim/A27_8_10_1740.txt 27 8 10` | Full suite (`F, W, B, A, R`) | `VERDICT: VALID` (`rc = 0`) | PASS |
| Author Verifier Corruption Test | 2-bit flip on codeword `1` | Full suite (`F, W, B, A, R`) | Rejected (`VERDICT: INVALID`, `rc = 1`) | PASS |

pass: true
