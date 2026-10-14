# Reproduction & Independent Algebraic Verification Report — Format `(15,16,17)` Rank `2313` over `Q`

context: subagent
context: subagent (astra)

## 1. Executive Summary
- **Target**: `fmm-catalogue-small-format-rank`
- **Format**: `(15, 16, 17)` (multiplying `15 x 16` by `16 x 17` matrices)
- **Claimed Rank over `Q`**: `2313` (previous standing records: `fmm_sota.json` = `2448`, margin `-135`; Lille catalogue = `2448`, margin `-135`; prior V3R1T4S run rank = `2314`, margin `-1`)
- **Claim Category**: `partial_win_claim` — Partial Win p1: beats fmm_sota.json (2448) and Lille HTML (2448) by -135 multiplications
- **Artifact**: `claim/15x16x17_r2313_Q.json` (`751346` bytes, SHA-256 `53e05e6d257401e1089d7ace8d42b7cbde78f8992e90223791fea6c1df50da57`)
- **Verdict**: **PASS** — Both our independent first-principles multi-prime Chinese Remainder Theorem (CRT) and exact `fractions.Fraction` verifier (written and executed prior to inspecting `claim/verify_brent.py`) and the author's standalone verifier confirm `0` errors across all `16,646,400` exact Brent equations over `Q`, with active non-zero rank `r = 2313`. Both verifiers also immediately reject 1-entry corrupted tensors.

---

## 2. Quoted Claim from `claim/CLAIM.md`

  - **Target ID**: `fmm-catalogue-small-format-rank`
  - **Format**: `(15,16,17)`
  - **Claim Level**: `partial_win_claim`
  - **New Exact Rank over Q**: `2313`
  - **Standing Records Beaten**: `fmm_sota.json` = `2448` (margin `-135`), `https://fmm.univ-lille.fr/15x16x17.html` = `2448` (margin `-135`)
  - **Summary**: Partial Win p1: beats fmm_sota.json (2448) and Lille HTML (2448) by -135 multiplications
  - **Scheme Artifact**: `15x16x17_r2313_Q.json` (`751346` bytes, SHA-256: `53e05e6d257401e1089d7ace8d42b7cbde78f8992e90223791fea6c1df50da57`)
  - **Verification**: `python3 verify_brent.py 15x16x17_r2313_Q.json` yields `PASS`

---

## 3. Step 1 — Independent First-Principles Verification (Executed Before Reading `claim/verify_brent.py`)

Before reading `claim/verify_brent.py`, we wrote and executed an independent verifier consisting of a Python `fractions.Fraction` parser/evaluator coupled to a standalone C99 multi-prime CRT Brent-equation engine (`__uint128_t` modular arithmetic).

### 3.1 Artifact Integrity & Structural Audit
- **File**: `claim/15x16x17_r2313_Q.json`
- **Byte Size**: `751346` bytes (matches `claim/CLAIM.md` and `claim/REPRODUCE.md`)
- **SHA-256**: `53e05e6d257401e1089d7ace8d42b7cbde78f8992e90223791fea6c1df50da57` (matches `claim/CLAIM.md`)
- **Header Fields**: `n = [15, 16, 17]`, `m = 2313`, `ring = "Q"`, `encoding = "vocab_rle_v1"`, vocabulary size `246` (`245` distinct non-zero rational values).
- **Decoded Factor Dimensions**:
  - `U`: `2313 x 240` (`58,598` non-zero entries)
  - `V`: `2313 x 272` (`45,935` non-zero entries)
  - `W`: `2313 x 255` (`50,799` non-zero entries)
  - Total non-zero entries across `(U, V, W)`: `155,332`
- **Active Rank Check**: All `2313` rank-1 triples `(U_q, V_q, W_q)` for `q in [0, 2313-1]` are non-zero in all three factors (`active_r = 2313 == 2313`).

### 3.2 Exact Multi-Prime CRT Verification of All `16,646,400` Brent Equations
For cyclic trace indexing `a = i1*16 + k1 in [0, 240)`, `b = k2*17 + j1 in [0, 272)`, `c = j2*15 + i2 in [0, 255)`, the exact bilinear Brent equations over `Q` are:
`sum_{q=0}^{2313-1} U[q, a] * V[q, b] * W[q, c] == [k1 == k2] * [j1 == j2] * [i2 == i1]`.

- **Denominator LCM**: `L = 50400`
- **Term Magnitude Sum Bound**: `ceil(S_bound) = 119381`
- **CRT Reconstruction Bound**: `2 * L * (ceil(S_bound) + 1) = 12033705600`
- **Independent Primes Used**: `P in [2147483647, 2147483629]` with product `prod(P) = 4611685975477714963`, which strictly exceeds `2 * L * (ceil(S_bound) + 1)` and is coprime to `L`.
- **Clean Artifact Result**: `bad_eq = 0` across all `16,646,400` equations modulo every prime `P`. By the Chinese Remainder Theorem, every Brent equation holds identically over `Q`.
- **Exact `fractions.Fraction` Matrix Multiplication Check**: Evaluated `C_scheme` on deterministic full-support rational matrices `A in Q^{15 x 16}` (`A_{i,k} = (7*(i+1) + 3*(k+1))/5`) and `B in Q^{16 x 17}` (`B_{k,j} = (11*(k+1) - 2*(j+1))/7`) in exact `fractions.Fraction` arithmetic; verified `C_scheme == A * B` entrywise (`matmul_ok = True`).
- **Adversarial Corruption Check**: Perturbed a single non-zero entry `U[0, 0]` by `+1` and re-ran our independent verifier; it immediately rejected the tensor with `bad_eq = 126` violated Brent equations (`rc = 1`).

---

## 4. Step 2 — Audit & Execution of Author's Verifier (`claim/verify_brent.py`)

After completing our independent verification, we inspected `claim/verify_brent.py` and executed the exact reproduction command from `claim/REPRODUCE.md`.

### 4.1 Code Audit of `claim/verify_brent.py`
- Parses every rational coefficient into an exact `fractions.Fraction(p, q)` (rejecting booleans, malformed RLE tokens, width mismatches, and unmerged runs).
- Computes exact row denominator LCMs `du, dv, dw`, global `L = lcm_k(du*dv*dw)`, and scaled numerator bound `S`, then selects odd primes below `2^30` coprime to all denominators until `prod(primes)` strictly exceeds `2 * L * (S + 1)`.
- Compiles an inline C99 checker (`cc -O3`) that evaluates all `(n1*n2)*(n2*n3)*(n3*n1)` Brent equations modulo each prime and checks `row[c] % p == exp`.

### 4.2 Execution on Clean & Corrupted Artifacts
- **Clean Artifact Command**: `python3 claim/verify_brent.py claim/15x16x17_r2313_Q.json`
  - **Exit Code**: `0`
  - **Stdout**: `PASS file=15x16x17_r2313_Q.json format=15x16x17 rank=2313 primes=2 log2_bound=50`
- **1-Entry Corrupted Artifact Command**: Executed `claim/verify_brent.py` on a temporary copy with `vocab[1]` perturbed by `+999`
  - **Exit Code**: `1` (non-zero rejection)
  - **Stdout**: `FAIL prime=1073741789 a=0 b=0 c=0 got=134211023 exp=1`

---

## 5. Summary Verification Table

| Check | Method | Scope | Result | Status |
|---|---|---|---|---|
| Artifact SHA-256 & Size | `hashlib.sha256` | `751346` bytes | `53e05e6d257401e1...` | PASS |
| Active Rank over `Q` | Non-zero `(U_q, V_q, W_q)` count | `q in [0, 2313-1]` | `2313 == 2313` | PASS |
| Independent Exact Brent CRT | C99 `__uint128_t` mod `[2147483647, 2147483629]` |All `16,646,400` equations | `bad_eq = 0` (`L = 50400`) | PASS |
| Independent Exact `Fraction` Matmul | `fractions.Fraction` over `Q` | `15 x 16` by `16 x 17` | Exact match (`0` discrepancies) | PASS |
| Independent Corruption Test | Perturb `U[0, 0] += 1` |All `16,646,400` equations | Rejected (`bad_eq = 126`, `rc = 1`) | PASS |
| Author Verifier Clean Run | `python3 claim/verify_brent.py claim/15x16x17_r2313_Q.json` |All `16,646,400` equations | `PASS file=15x16x17_r2313_Q.json format=15x16x17 rank=2313 primes=2 log2_bound=50` (`rc = 0`) | PASS |
| Author Verifier Corruption Test | Perturb `vocab[1]` by `+999` |All `16,646,400` equations | Rejected (`FAIL prime=1073741789 a=0 b=0 c=0 got=134211023 exp=1`, `rc = 1`) | PASS |

pass: true
