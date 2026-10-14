# Reproduction & Independent Verification Report

role: reproduce
context: subagent
target_id: fmm-catalogue-small-format-rank
claimed_object: claim/13x15x15_r1763_Q.json
claimed_sha256: 710c8ff6593f7c6e578a9ae83b4d7083ed5381db72fd734e614a3108d7c87465
claimed_rank: 1763

## 1. Quoted Definition from `claim/CLAIM.md`

Verbatim from `claim/CLAIM.md` (lines 12–20):

> In `claim/13x15x15_r1763_Q.json`:
> - `n = [13, 15, 15]`, `m = 1763`, `ring = "Q"`, `encoding = "sparse_flat_pairs"`.
> - `u`, `v`, `w` are lists of $r = 1763$ rows corresponding to dense vectors $u_k \in \mathbb{Q}^{13 \cdot 15}$, $v_k \in \mathbb{Q}^{15 \cdot 15}$, $w_k \in \mathbb{Q}^{15 \cdot 13}$, where each row in `sparse_flat_pairs` is `[idx_0, val_0, idx_1, val_1, ...]` listing the strictly increasing 0-based flat indices and non-zero rational values (`int` or `"p/q"`).
> - Index mapping (Perminov/Lille convention):
>   - $u_k[i_1 \cdot 15 + j_1] \leftrightarrow A_{i_1, j_1}$ ($0 \le i_1 < 13$, $0 \le j_1 < 15$)
>   - $v_k[j_2 \cdot 15 + l_2] \leftrightarrow B_{j_2, l_2}$ ($0 \le j_2 < 15$, $0 \le l_2 < 15$)
>   - $w_k[l_3 \cdot 13 + i_3] \leftrightarrow C_{i_3, l_3}$ ($0 \le l_3 < 15$, $0 \le i_3 < 13$)
> - The Brent equations over $\mathbb{Q}$ state that for all $0 \le i_1, i_3 < 13$, $0 \le j_1, j_2 < 15$, $0 \le l_2, l_3 < 15$:
>   $$\sum_{k=0}^{r-1} u_k[i_1 \cdot 15 + j_1] \cdot v_k[j_2 \cdot 15 + l_2] \cdot w_k[l_3 \cdot 13 + i_3] = \delta_{i_1, i_3} \delta_{j_1, j_2} \delta_{l_2, l_3}.$$

## 2. Independent Verification (Written and Executed Before Reading `claim/verify_brent.py`)

Before inspecting `claim/verify_brent.py`, we wrote and ran three independent verifiers directly from the mathematical specification in `claim/CLAIM.md`:

### 2.1 File Integrity, Structural Schema, and Denominator Analysis
- **SHA-256 of `claim/13x15x15_r1763_Q.json`**: `710c8ff6593f7c6e578a9ae83b4d7083ed5381db72fd734e614a3108d7c87465` (matches `claim/CLAIM.md` and `claim/REPRODUCE.md` identically).
- **Header metadata**: `n = [13, 15, 15]`, `m = 1763`, `ring = "Q"`, `encoding = "sparse_flat_pairs"`.
- **Factor arrays**: `len(u) = 1763`, `len(v) = 1763`, `len(w) = 1763`. Every row of `u`, `v`, `w` has positive even length, strictly increasing 0-based indices within bounds (`[0, 195)` for `u`, `[0, 225)` for `v`, `[0, 195)` for `w`), and non-zero rational coefficients parsed via `fractions.Fraction`. All $1763$ rank-one terms are non-zero in all three factors.
- **Denominators and CRT Bound**:
  - Distinct entry denominators in `u`, `v`, `w`: `{1, 2, 5, 10, 16, 17, 20, 25, 34, 50, 80, 85, 100, 170, 200, 272, 320, 400, 640, 680, 1088, 1360, 3200, 5440}`.
  - Maximum absolute numerator across all entries: $11,142$.
  - For each term $k$, let $d_k = d_{u,k} d_{v,k} d_{w,k}$ be the product of the row denominator LCMs of $u_k, v_k, w_k$. The global LCM over all $k \in \{0, \dots, 1762\}$ is $L = \operatorname{lcm}_k(d_k) = 54,400 = 2^7 \cdot 5^2 \cdot 17$.
  - The unscaled sum of maximum term magnitudes is $S = \sum_{k=0}^{1762} (\max_\alpha |u_k[\alpha]|)(\max_\beta |v_k[\beta]|)(\max_\gamma |w_k[\gamma]|) \approx 46,811.451140$ ($\lceil S \rceil = 46,812$).
  - After clearing denominators by $L = 54,400$, any integer residual in the $8,555,625$ equations is bounded in magnitude by $L(S + 1) \le 2,546,627,200$, so $2 L (S + 1) \le 5,093,254,400 \approx 2^{32.25}$.

### 2.2 Exact `fractions.Fraction` Bilinear Evaluation on Random Rational Matrices
- Generated $5$ independent pairs of dense random rational matrices $A \in \mathbb{Q}^{13 \times 15}$ and $B \in \mathbb{Q}^{15 \times 15}$ with entries in $\{-7/5, \dots, 7/5\}$ (seed `20261014`).
- Computed $C_{\text{scheme}}[l_3 \cdot 13 + i_3] = \sum_{k=0}^{1762} \left(\sum_{\alpha} u_k[\alpha] A[\alpha]\right) \left(\sum_{\beta} v_k[\beta] B[\beta]\right) w_k[l_3 \cdot 13 + i_3]$ in exact `fractions.Fraction` arithmetic and compared every entry against the exact matrix product $\sum_{j=0}^{14} A_{i_3, j} B_{j, l_3}$.
- **Result**: `Exact fractions.Fraction random matrix multiplication test (5 trials): PASS` ($0$ discrepancies across all $5 \times 195 = 975$ output entries).

### 2.3 Exhaustive Full-Tensor Check Over All $8,555,625$ Brent Equations (Exact Integer & Independent Multi-Prime CRT)
- **Method A (Exact integer full-tensor check without modular reduction)**:
  - Scaled each row $u_k$ by $d_{u,k}$, $v_k$ by $d_{v,k}$, and $w_k$ by $L / (d_{u,k} d_{v,k})$ to obtain exact integer matrices $U_{\text{int}}, V_{\text{int}}, W_{\text{int}}$.
  - Evaluated $\sum_{k=0}^{1762} U_{\text{int}}[k, \alpha] V_{\text{int}}[k, \beta] W_{\text{int}}[k, \gamma]$ in exact 128-bit signed integer arithmetic (`__int128`) across all $195 \times 225 \times 195 = 8,555,625$ triples $(\alpha, \beta, \gamma)$, verifying that every diagonal triple ($2,925$ triples with $i_1 = i_3, j_1 = j_2, l_2 = l_3$) equals $L = 54,400$ and every off-diagonal triple ($8,552,700$ triples) equals $0$.
  - **Result**: `EXACT_AND_MOD_PASS total_eqs=8555625 nonzero_eqs=2925`.
- **Method B (Direct modular full-tensor check from rational entries)**:
  - Reduced every rational entry $p/q$ directly via $p \cdot q^{-1} \bmod p_m$ for three independent 31-bit primes $p_1 = 2147483647$, $p_2 = 2147483629$, $p_3 = 2147483587$, whose product is $p_1 p_2 p_3 \approx 9.90 \times 10^{27} \approx 2^{93}$, exceeding $2 L (S + 1) \approx 5.09 \times 10^9$ by more than $18$ orders of magnitude.
  - Evaluated all $8,555,625$ Brent equations modulo each prime independently.
  - **Result**:
    - `DIRECT_MOD_PASS prime=2147483647 eqs=8555625`
    - `DIRECT_MOD_PASS prime=2147483629 eqs=8555625`
    - `DIRECT_MOD_PASS prime=2147483587 eqs=8555625`
- All temporary C source, binary, and data files created during independent verification were deleted immediately after execution.

## 3. Execution of Author's Verifier (`claim/verify_brent.py`)

We inspected `claim/verify_brent.py` and ran the exact reproduction command from `claim/REPRODUCE.md`:

```sh
python3 claim/verify_brent.py claim/13x15x15_r1763_Q.json
```

Output:
```text
PASS file=13x15x15_r1763_Q.json format=13x15x15 rank=1763 primes=2 log2_bound=48
```

This matches the expected output in `claim/REPRODUCE.md` character-for-character.

pass: true
