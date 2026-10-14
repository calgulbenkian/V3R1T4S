# Reproduction & Independent Algebraic Verification Report — Format `(14,16,17)` Rank `2261` over `Q`

context: subagent
context: subagent (astra)

## 1. Executive Summary
- **Target**: `fmm-catalogue-small-format-rank`
- **Format**: `(14, 16, 17)` (multiplying `14 x 16` by `16 x 17` matrices)
- **Claimed Rank over `Q`**: `2261` (previous standing records: `fmm_sota.json` = `2306`, margin `-45`; Lille catalogue = `2306`, margin `-45`; prior V3R1T4S run rank = `2262`, margin `-1`)
- **Claim Category**: `partial_win_claim` — Partial Win p1: beats fmm_sota.json (2306) and Lille HTML (2306) by -45 multiplications
- **Artifact**: `claim/14x16x17_r2261_Q.json` (`734551` bytes, SHA-256 `9daa4b495e91e98bb5da76cff692af959885766b07e33042b353e7ea94de7b3d`)
- **Verdict**: **PASS** — Both our independent first-principles multi-prime Chinese Remainder Theorem (CRT) and exact `fractions.Fraction` verifier (written and executed prior to inspecting `claim/verify_brent.py`) and the author's standalone verifier confirm `0` errors across all `14,500,864` exact Brent equations over `Q`, with active non-zero rank `r = 2261`. Both verifiers also immediately reject 1-entry corrupted tensors.

---

## 2. Quoted Claim from `claim/CLAIM.md`

  - **Target ID**: `fmm-catalogue-small-format-rank`
  - **Format**: `(14,16,17)`
  - **Claim Level**: `partial_win_claim`
  - **New Exact Rank over Q**: `2261`
  - **Standing Records Beaten**: `fmm_sota.json` = `2306` (margin `-45`), `https://fmm.univ-lille.fr/14x16x17.html` = `2306` (margin `-45`)
  - **Summary**: Partial Win p1: beats fmm_sota.json (2306) and Lille HTML (2306) by -45 multiplications
  - **Scheme Artifact**: `14x16x17_r2261_Q.json` (`734551` bytes, SHA-256: `9daa4b495e91e98bb5da76cff692af959885766b07e33042b353e7ea94de7b3d`)
  - **Verification**: `python3 verify_brent.py 14x16x17_r2261_Q.json` yields `PASS`

---

## 3. Step 1 — Independent First-Principles Verification (Executed Before Reading `claim/verify_brent.py`)

Before reading `claim/verify_brent.py`, we wrote and executed an independent verifier consisting of a Python `fractions.Fraction` parser/evaluator coupled to a standalone C99 multi-prime CRT Brent-equation engine (`__uint128_t` modular arithmetic).

### 3.1 Artifact Integrity & Structural Audit
- **File**: `claim/14x16x17_r2261_Q.json`
- **Byte Size**: `734551` bytes (matches `claim/CLAIM.md` and `claim/REPRODUCE.md`)
- **SHA-256**: `9daa4b495e91e98bb5da76cff692af959885766b07e33042b353e7ea94de7b3d` (matches `claim/CLAIM.md`)
- **Header Fields**: `n = [14, 16, 17]`, `m = 2261`, `ring = "Q"`, `encoding = "vocab_rle_v1"`, vocabulary size `327` (`326` distinct non-zero rational values).
- **Decoded Factor Dimensions**:
  - `U`: `2261 x 224` (`75,240` non-zero entries)
  - `V`: `2261 x 272` (`44,878` non-zero entries)
  - `W`: `2261 x 238` (`57,950` non-zero entries)
  - Total non-zero entries across `(U, V, W)`: `178,068`
- **Active Rank Check**: All `2261` rank-1 triples `(U_q, V_q, W_q)` for `q in [0, 2261-1]` are non-zero in all three factors (`active_r = 2261 == 2261`).

### 3.2 Exact Multi-Prime CRT Verification of All `14,500,864` Brent Equations
For cyclic trace indexing `a = i1*16 + k1 in [0, 224)`, `b = k2*17 + j1 in [0, 272)`, `c = j2*14 + i2 in [0, 238)`, the exact bilinear Brent equations over `Q` are:
`sum_{q=0}^{2261-1} U[q, a] * V[q, b] * W[q, c] == [k1 == k2] * [j1 == j2] * [i2 == i1]`.

- **Denominator LCM**: `L = 50400`
- **Term Magnitude Sum Bound**: `ceil(S_bound) = 190952`
- **CRT Reconstruction Bound**: `2 * L * (ceil(S_bound) + 1) = 19248062400`
- **Independent Primes Used**: `P in [2147483647, 2147483629]` with product `prod(P) = 4611685975477714963`, which strictly exceeds `2 * L * (ceil(S_bound) + 1)` and is coprime to `L`.
- **Clean Artifact Result**: `bad_eq = 0` across all `14,500,864` equations modulo every prime `P`. By the Chinese Remainder Theorem, every Brent equation holds identically over `Q`.
- **Exact `fractions.Fraction` Matrix Multiplication Check**: Evaluated `C_scheme` on deterministic full-support rational matrices `A in Q^{14 x 16}` (`A_{i,k} = (7*(i+1) + 3*(k+1))/5`) and `B in Q^{16 x 17}` (`B_{k,j} = (11*(k+1) - 2*(j+1))/7`) in exact `fractions.Fraction` arithmetic; verified `C_scheme == A * B` entrywise (`matmul_ok = True`).
- **Adversarial Corruption Check**: Perturbed a single non-zero entry `U[0, 0]` by `+1` and re-ran our independent verifier; it immediately rejected the tensor with `bad_eq = 174` violated Brent equations (`rc = 1`).

---

## 4. Step 2 — Audit & Execution of Author's Verifier (`claim/verify_brent.py`)

After completing our independent verification, we inspected `claim/verify_brent.py` and executed the exact reproduction command from `claim/REPRODUCE.md`.

### 4.1 Code Audit of `claim/verify_brent.py`
- Parses every rational coefficient into an exact `fractions.Fraction(p, q)` (rejecting booleans, malformed RLE tokens, width mismatches, and unmerged runs).
- Computes exact row denominator LCMs `du, dv, dw`, global `L = lcm_k(du*dv*dw)`, and scaled numerator bound `S`, then selects odd primes below `2^30` coprime to all denominators until `prod(primes)` strictly exceeds `2 * L * (S + 1)`.
- Compiles an inline C99 checker (`cc -O3`) that evaluates all `(n1*n2)*(n2*n3)*(n3*n1)` Brent equations modulo each prime and checks `row[c] % p == exp`.

### 4.2 Execution on Clean & Corrupted Artifacts
- **Clean Artifact Command**: `python3 claim/verify_brent.py claim/14x16x17_r2261_Q.json`
  - **Exit Code**: `0`
  - **Stdout**: `PASS file=14x16x17_r2261_Q.json format=14x16x17 rank=2261 primes=2 log2_bound=50`
- **1-Entry Corrupted Artifact Command**: Executed `claim/verify_brent.py` on a temporary copy with `vocab[1]` perturbed by `+999`
  - **Exit Code**: `1` (non-zero rejection)
  - **Stdout**: `FAIL prime=1073741789 a=0 b=0 c=0 got=931891160 exp=1`

---

## 5. Summary Verification Table

| Check | Method | Scope | Result | Status |
|---|---|---|---|---|
| Artifact SHA-256 & Size | `hashlib.sha256` | `734551` bytes | `9daa4b495e91e98b...` | PASS |
| Active Rank over `Q` | Non-zero `(U_q, V_q, W_q)` count | `q in [0, 2261-1]` | `2261 == 2261` | PASS |
| Independent Exact Brent CRT | C99 `__uint128_t` mod `[2147483647, 2147483629]` |All `14,500,864` equations | `bad_eq = 0` (`L = 50400`) | PASS |
| Independent Exact `Fraction` Matmul | `fractions.Fraction` over `Q` | `14 x 16` by `16 x 17` | Exact match (`0` discrepancies) | PASS |
| Independent Corruption Test | Perturb `U[0, 0] += 1` |All `14,500,864` equations | Rejected (`bad_eq = 174`, `rc = 1`) | PASS |
| Author Verifier Clean Run | `python3 claim/verify_brent.py claim/14x16x17_r2261_Q.json` |All `14,500,864` equations | `PASS file=14x16x17_r2261_Q.json format=14x16x17 rank=2261 primes=2 log2_bound=50` (`rc = 0`) | PASS |
| Author Verifier Corruption Test | Perturb `vocab[1]` by `+999` |All `14,500,864` equations | Rejected (`FAIL prime=1073741789 a=0 b=0 c=0 got=931891160 exp=1`, `rc = 1`) | PASS |

pass: true
