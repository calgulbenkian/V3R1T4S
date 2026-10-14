# Reproduction & Independent Algebraic Verification Report — Format `(16,18,18)` Rank `2900` over `Q`

context: subagent
context: subagent (astra)

## 1. Executive Summary
- **Target**: `fmm-catalogue-small-format-rank`
- **Format**: `(16, 18, 18)` (multiplying `16 x 18` by `18 x 18` matrices)
- **Claimed Rank over `Q`**: `2900` (previous standing records: `fmm_sota.json` = `2916`, margin `-16`; Lille catalogue = `2916`, margin `-16`; prior V3R1T4S run rank = `2901`, margin `-1`)
- **Claim Category**: `partial_win_claim` — Partial Win p1: beats fmm_sota.json (2916) and Lille HTML (2916) by -16 multiplications
- **Artifact**: `claim/16x18x18_r2900_Q.json` (`241556` bytes, SHA-256 `0975cd66f4a942c0d5fd289c59c7d5a0703e86dee33b40911924de746c679de3`)
- **Verdict**: **PASS** — Both our independent first-principles multi-prime Chinese Remainder Theorem (CRT) and exact `fractions.Fraction` verifier (written and executed prior to inspecting `claim/verify_brent.py`) and the author's standalone verifier confirm `0` errors across all `26,873,856` exact Brent equations over `Q`, with active non-zero rank `r = 2900`. Both verifiers also immediately reject 1-entry corrupted tensors.

---

## 2. Quoted Claim from `claim/CLAIM.md`

  - **Target ID**: `fmm-catalogue-small-format-rank`
  - **Format**: `(16,18,18)`
  - **Claim Level**: `partial_win_claim`
  - **New Exact Rank over Q**: `2900`
  - **Standing Records Beaten**: `fmm_sota.json` = `2916` (margin `-16`), `https://fmm.univ-lille.fr/16x18x18.html` = `2916` (margin `-16`)
  - **Summary**: Partial Win p1: beats fmm_sota.json (2916) and Lille HTML (2916) by -16 multiplications
  - **Scheme Artifact**: `16x18x18_r2900_Q.json` (`241556` bytes, SHA-256: `0975cd66f4a942c0d5fd289c59c7d5a0703e86dee33b40911924de746c679de3`)
  - **Verification**: `python3 verify_brent.py 16x18x18_r2900_Q.json` yields `PASS`

---

## 3. Step 1 — Independent First-Principles Verification (Executed Before Reading `claim/verify_brent.py`)

Before reading `claim/verify_brent.py`, we wrote and executed an independent verifier consisting of a Python `fractions.Fraction` parser/evaluator coupled to a standalone C99 multi-prime CRT Brent-equation engine (`__uint128_t` modular arithmetic).

### 3.1 Artifact Integrity & Structural Audit
- **File**: `claim/16x18x18_r2900_Q.json`
- **Byte Size**: `241556` bytes (matches `claim/CLAIM.md` and `claim/REPRODUCE.md`)
- **SHA-256**: `0975cd66f4a942c0d5fd289c59c7d5a0703e86dee33b40911924de746c679de3` (matches `claim/CLAIM.md`)
- **Header Fields**: `n = [16, 18, 18]`, `m = 2900`, `ring = "Q"`, `encoding = "vocab_rle_b64_v1"`, vocabulary size `633` (`632` distinct non-zero rational values).
- **Decoded Factor Dimensions**:
  - `U`: `2900 x 288` (`256,735` non-zero entries)
  - `V`: `2900 x 324` (`302,854` non-zero entries)
  - `W`: `2900 x 288` (`254,012` non-zero entries)
  - Total non-zero entries across `(U, V, W)`: `813,601`
- **Active Rank Check**: All `2900` rank-1 triples `(U_q, V_q, W_q)` for `q in [0, 2900-1]` are non-zero in all three factors (`active_r = 2900 == 2900`).

### 3.2 Exact Multi-Prime CRT Verification of All `26,873,856` Brent Equations
For cyclic trace indexing `a = i1*18 + k1 in [0, 288)`, `b = k2*18 + j1 in [0, 324)`, `c = j2*16 + i2 in [0, 288)`, the exact bilinear Brent equations over `Q` are:
`sum_{q=0}^{2900-1} U[q, a] * V[q, b] * W[q, c] == [k1 == k2] * [j1 == j2] * [i2 == i1]`.

- **Denominator LCM**: `L = 242020800`
- **Term Magnitude Sum Bound**: `ceil(S_bound) = 18022`
- **CRT Reconstruction Bound**: `2 * L * (ceil(S_bound) + 1) = 8723881756800`
- **Independent Primes Used**: `P in [2147483647, 2147483629]` with product `prod(P) = 4611685975477714963`, which strictly exceeds `2 * L * (ceil(S_bound) + 1)` and is coprime to `L`.
- **Clean Artifact Result**: `bad_eq = 0` across all `26,873,856` equations modulo every prime `P`. By the Chinese Remainder Theorem, every Brent equation holds identically over `Q`.
- **Exact `fractions.Fraction` Matrix Multiplication Check**: Evaluated `C_scheme` on deterministic full-support rational matrices `A in Q^{16 x 18}` (`A_{i,k} = (7*(i+1) + 3*(k+1))/5`) and `B in Q^{18 x 18}` (`B_{k,j} = (11*(k+1) - 2*(j+1))/7`) in exact `fractions.Fraction` arithmetic; verified `C_scheme == A * B` entrywise (`matmul_ok = True`).
- **Adversarial Corruption Check**: Perturbed a single non-zero entry `U[0, 0]` by `+1` and re-ran our independent verifier; it immediately rejected the tensor with `bad_eq = 48` violated Brent equations (`rc = 1`).

---

## 4. Step 2 — Audit & Execution of Author's Verifier (`claim/verify_brent.py`)

After completing our independent verification, we inspected `claim/verify_brent.py` and executed the exact reproduction command from `claim/REPRODUCE.md`.

### 4.1 Code Audit of `claim/verify_brent.py`
- Parses every rational coefficient into an exact `fractions.Fraction(p, q)` (rejecting booleans, malformed RLE tokens, width mismatches, and unmerged runs).
- Computes exact row denominator LCMs `du, dv, dw`, global `L = lcm_k(du*dv*dw)`, and scaled numerator bound `S`, then selects odd primes below `2^30` coprime to all denominators until `prod(primes)` strictly exceeds `2 * L * (S + 1)`.
- Compiles an inline C99 checker (`cc -O3`) that evaluates all `(n1*n2)*(n2*n3)*(n3*n1)` Brent equations modulo each prime and checks `row[c] % p == exp`.

### 4.2 Execution on Clean & Corrupted Artifacts
- **Clean Artifact Command**: `python3 claim/verify_brent.py claim/16x18x18_r2900_Q.json`
  - **Exit Code**: `0`
  - **Stdout**: `PASS file=16x18x18_r2900_Q.json format=16x18x18 rank=2900 primes=3 log2_bound=71`
- **1-Entry Corrupted Artifact Command**: Executed `claim/verify_brent.py` on a temporary copy with `vocab[1]` perturbed by `+999`
  - **Exit Code**: `1` (non-zero rejection)
  - **Stdout**: `FAIL prime=1073741789 a=0 b=9 c=0 got=154951641 exp=0`

---

## 5. Summary Verification Table

| Check | Method | Scope | Result | Status |
|---|---|---|---|---|
| Artifact SHA-256 & Size | `hashlib.sha256` | `241556` bytes | `0975cd66f4a942c0...` | PASS |
| Active Rank over `Q` | Non-zero `(U_q, V_q, W_q)` count | `q in [0, 2900-1]` | `2900 == 2900` | PASS |
| Independent Exact Brent CRT | C99 `__uint128_t` mod `[2147483647, 2147483629]` |All `26,873,856` equations | `bad_eq = 0` (`L = 242020800`) | PASS |
| Independent Exact `Fraction` Matmul | `fractions.Fraction` over `Q` | `16 x 18` by `18 x 18` | Exact match (`0` discrepancies) | PASS |
| Independent Corruption Test | Perturb `U[0, 0] += 1` |All `26,873,856` equations | Rejected (`bad_eq = 48`, `rc = 1`) | PASS |
| Author Verifier Clean Run | `python3 claim/verify_brent.py claim/16x18x18_r2900_Q.json` |All `26,873,856` equations | `PASS file=16x18x18_r2900_Q.json format=16x18x18 rank=2900 primes=3 log2_bound=71` (`rc = 0`) | PASS |
| Author Verifier Corruption Test | Perturb `vocab[1]` by `+999` |All `26,873,856` equations | Rejected (`FAIL prime=1073741789 a=0 b=9 c=0 got=154951641 exp=0`, `rc = 1`) | PASS |

pass: true
