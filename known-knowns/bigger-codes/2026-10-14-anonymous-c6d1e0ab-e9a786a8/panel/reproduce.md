# Reproduction & Independent Verification Report — Binary Constant-Weight Code `A(45, 8, 7)` Lower Bound `1910`

context: subagent
context: subagent (astra)

## 1. Executive Summary
- **Target**: `constant-weight-codes` (`A(n, d, w)` lower bounds in Brouwer's table)
- **Cell**: `A(45, 8, 7)` (and complement mirror cell `A(45, 8, 38)`)
- **Claimed Lower Bound**: `M = 1910` (strictly beating the live composite bar `1907` by `+3` and Brouwer's `Andw.html` table entry `1904` by `+6`)
- **Claim Level**: `full`
- **Artifact**: `claim/A45_8_7_1910.txt` (`87860` bytes, SHA-256 `e9a786a8af3ad130a62167977ca106c4f1ffc99d134f798959fafb319e21c966`)
- **Verdict**: **PASS** — Both our independent first-principles verifier (written and executed before reading `claim/verify_cwc.py`) and the author's standalone verifier confirm that `claim/A45_8_7_1910.txt` contains `1910` pairwise distinct binary codewords of length `45` and exact Hamming weight `7`, with minimum pairwise Hamming distance `8 == 8` (`0` pairs below `8` across all `1,823,095` codeword pairs) and `0` collisions among all `66,850` Steiner `t = 4`-subsets. Both verifiers also immediately reject a 2-bit-flipped corrupted copy.

---

## 2. Quoted Definition & Claim from `target.md` and `claim/CLAIM.md`

### 2.1 Mathematical Definition (`target.md`)
  - **Definition**: `A(n, d, w)` is the maximum number of binary words of length `n` and weight `w` with pairwise Hamming distance at least `d`.
  - **Success Criterion**: An explicit list of `M` distinct binary vectors of length `n`, each with Hamming weight exactly `w`, with all pairwise distances at least `d` (`d` even), where `M` is strictly greater than the lower bound shown at verification time in the `(n, d, w)` cell of `https://aeb.win.tue.nl/codes/Andw.html` (also checking the mirror cell `A(n, d, n-w)`), and strictly greater than any value for that cell in `arXiv:2608.13906` (Echols), `arXiv:2607.19550` (Lysenstoen), or prior V3R1T4S records.

### 2.2 Claim Summary (`claim/CLAIM.md`)
  - **Target**: `constant-weight-codes`
  - **Claim Level**: `full` (`+3` over live composite bar `1907`; `+6` over `Andw.html` `1904`)
  - **Artifact**: `A45_8_7_1910.txt` (`1910` binary codewords of length `45`, weight `7`, minimum pairwise Hamming distance `8`)

---

## 3. Step 1 — Independent First-Principles Verification (Executed Before Reading `claim/verify_cwc.py`)

Prior to reading `claim/verify_cwc.py`, we implemented and ran an independent verifier (Python parser + Steiner `t`-subset packing checker + compiled C99 `uint64_t` `__builtin_popcountll` all-pairs distance engine).

### 3.1 Artifact Integrity, Format, Weight & Distinctness
- **File**: `claim/A45_8_7_1910.txt`
- **Byte Size**: `87860` bytes (`1910` lines of `45` ASCII characters plus newline)
- **SHA-256**: `e9a786a8af3ad130a62167977ca106c4f1ffc99d134f798959fafb319e21c966` (matches `claim/CLAIM.md` exactly)
- **Line & Alphabet Check**: `lines = 1910`, `bad_len = 0`, `bad_chars = 0` (every line has exact length `45` and consists solely of `'0'` and `'1'`).
- **Hamming Weight Check**: `bad_weight = 0` (every codeword has exact Hamming weight `w = 7`).
- **Distinctness Check**: `distinct_M = 1910 == 1910` (zero duplicate codewords).

### 3.2 Independent Steiner `t`-Subset Packing Verification
For constant weight `w = 7` and minimum even Hamming distance `d = 8`, the maximum allowed bitwise overlap between any two distinct codewords is `w - d/2 = 3`. Equivalently, every `t = w - d/2 + 1 = 4`-element subset of the `1`-positions of a codeword must be unique across the entire code (`C(7, 4) = 35` subsets per codeword):
- **Total `t = 4`-subsets**: `66,850`
- **Distinct `t = 4`-subsets**: `66,850`
- **Subset Collisions**: `0`

### 3.3 Exhaustive All-Pairs Hamming Distance Verification
We packed all `1910` codewords into 64-bit unsigned integers (`uint64_t`) and exhaustively evaluated `dist(x, y) = popcount(x ^ y)` across all `M * (M - 1) / 2 = 1,823,095` unordered pairs:
- **Total Pairs Checked**: `1,823,095`
- **Minimum Pairwise Hamming Distance**: `8` (required: at least `8`)
- **Maximum Pairwise Bitwise Overlap**: `3` (required: at most `3`)
- **Violating Pairs (`dist` below `8`)**: `0`
- **Exact Pairwise Distance Histogram**: `{8: 142038, 10: 385326, 12: 785387, 14: 510344}` (`d=8: 142,038, d=10: 385,326, d=12: 785,387, d=14: 510,344`; sum of counts = `1,823,095 == 1,823,095`).

### 3.4 Independent Adversarial Mutation Test
We mutated codeword `1` into a weight-`7` word at Hamming distance `2` (overlap `6`) from codeword `0` by flipping one `'1'` bit and one `'0'` bit of codeword `0`. Re-running our independent C99 all-pairs checker immediately rejected the mutated code (`rc = 1`, `min_dist = 2`, `bad_pairs = 9`).

---

## 4. Step 2 — Audit & Execution of Author's Verifier (`claim/verify_cwc.py`)

After completing our independent verification, we inspected `claim/verify_cwc.py` and ran the reproduction command from `claim/REPRODUCE.md`.

### 4.1 Clean Artifact Execution
- **Command**: `python3 claim/verify_cwc.py claim/A45_8_7_1910.txt 45 8 7`
- **Exit Code**: `0`
- **Output**:
```text
file=A45_8_7_1910.txt sha256=e9a786a8af3ad130a62167977ca106c4f1ffc99d134f798959fafb319e21c966
F format: lines=1910 claimed_M=1910 bad_lines=0
W weight/distinct: bad_weight=0 distinct=1910
B packing: t=4 subsets=66850 distinct=66850 collisions=0
A all-pairs: words=1910 pairs=1823095 min_distance=8 needat_least_8 bad_pairs=0 histogram={8: 142038, 10: 385326, 12: 785387, 14: 510344}
R record_check: cell=A(45,8,7) M=1910 composite_bar=1907 (Andw=1904, Trophy/PR=1907) strict_beat=True
VERDICT: VALID  A(45,8,7) at_least_ 1910
```

### 4.2 Corrupted Artifact Execution
- **Command**: Ran `claim/verify_cwc.py` on a temporary copy with codeword `1` replaced by a 2-bit flip of codeword `0`
- **Exit Code**: `1` (non-zero rejection)
- **Output**:
```text
file=A45_8_7_1910.txt sha256=8945487707818cc9215069a2f792242cb2aa88d750607d79c530f7f34cc599af
F format: lines=1910 claimed_M=1910 bad_lines=0
W weight/distinct: bad_weight=0 distinct=1910
B packing: t=4 subsets=66850 distinct=66827 collisions=23
A all-pairs: words=1910 pairs=1823095 min_distance=2 needat_least_8 bad_pairs=9 histogram={2: 1, 6: 8, 8: 142025, 10: 385315, 12: 785386, 14: 510360}
R record_check: cell=A(45,8,7) M=1910 composite_bar=1907 (Andw=1904, Trophy/PR=1907) strict_beat=False
VERDICT: INVALID  A(45,8,7) at_least_ 1910
```

---

## 5. Summary Verification Table

| Check | Method | Scope | Result | Status |
|---|---|---|---|---|
| Artifact SHA-256 & Size | `hashlib.sha256` | `87860` bytes | `e9a786a8af3ad130...` | PASS |
| Format, Length & Weight | Exact ASCII & popcount audit | `1910` words, `n=45, w=7` | `bad_len=0, bad_chars=0, bad_weight=0` | PASS |
| Codeword Distinctness | Set cardinality | `1910` words | `distinct = 1910` | PASS |
| Steiner `t=4`-Subset Packing | Exhaustive `C(7,4)` subsets | `66,850` subsets | `collisions = 0` | PASS |
| Independent All-Pairs Distance | C99 `uint64_t` XOR popcount | All `1,823,095` pairs | `min_dist = 8`, `bad_pairs = 0` | PASS |
| Independent Corruption Test | 2-bit flip on codeword `1` | All `1,823,095` pairs | Rejected (`min_dist = 2, bad_pairs = 9, rc = 1`) | PASS |
| Author Verifier Clean Run | `python3 claim/verify_cwc.py claim/A45_8_7_1910.txt 45 8 7` | Full suite (`F, W, B, A, R`) | `VERDICT: VALID` (`rc = 0`) | PASS |
| Author Verifier Corruption Test | 2-bit flip on codeword `1` | Full suite (`F, W, B, A, R`) | Rejected (`VERDICT: INVALID`, `rc = 1`) | PASS |

pass: true
