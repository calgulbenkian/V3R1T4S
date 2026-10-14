# Reproduction & Independent Exact-Arithmetic Verification Report — Frozen Gram Target (`p2`) at Order `n = 81`

context: subagent
context: subagent (astra)

## 1. Executive Summary
- **Target**: `hadamard-maxdet-records` (`Hadamard maximal determinant: new record determinants for orders n not divisible by 4`)
- **Order**: `n = 81 = 9^2` (`n == 1 mod 4`)
- **Claim Level**: `CONFIRMED_PARTIAL` (`p2` — Frozen Gram Target)
- **Artifact**: `claim/G81_p2.json` (`192478` bytes, SHA-256 `03b380a2074785deac39cb19b68c0853cd52ea469f7b848600cc756df42c8992`)
- **Claimed Normalized Gram Determinant**: `sqrt(det(G)) / 2^80 = 252 * 20^39 = 138538465099776000000000000000000000000000000000000000` (strictly exceeding the standing record `196 * 20^39 = 107752139522048000000000000000000000000000000000000000` by `1.285714x`)
- **Verdict**: **PASS** — Both our independent first-principles exact-arithmetic verifier (written and executed before reading `claim/verify_maxdet.py`) and the author's standalone verifier confirm every clause of partial win `p2`: `G` is an `81 x 81` symmetric positive-definite integer matrix (all `81` Sylvester leading principal Bareiss minors strictly positive) with diagonal `81`, valid pairwise/triple mod-4 Gram congruences, `det(G)` strictly exceeding the square of the live record and below the Barba bound, constructive rational congruence `Q * Q^T == G` (`Q_den = 10`) and `P * (81 * I_81) * P^T == G` (`P = Q / 9`, `P_den = 90`), and an explicit `80 x 81` `{-1, +1}` matrix `M0` (`80` at least `n - 2 = 79`) satisfying `M0 * M0^T == G[:80, :80]`. Both verifiers also immediately reject perturbed Gram negative controls (`exit = 1`).

---

## 2. Verbatim `p2` Partial Win Definition & Claim Summary (`claim/target.md` and `claim/CLAIM.md`)

### 2.1 Verbatim `p2` Definition (`claim/target.md`)
  - **Partial Win `p2`**: A frozen Gram target: for an order `n` whose record is below its bound, an explicit symmetric positive-definite integer matrix `G` with diagonal `n`, off-diagonal entries obeying the parity/congruence conditions of Gram matrices of `+-1` matrices of that order, `det G` strictly greater than the square of the live record, and passing the rational (Hasse-Minkowski) equivalence test to `n*I`, all checked exactly; plus at least `n-2` rows of a `+-1` matrix realising the leading principal block of `G`.

### 2.2 Claim Summary (`claim/CLAIM.md`)
  - **Target**: `hadamard-maxdet-records`
  - **Claim Level**: `CONFIRMED_PARTIAL` (`p2`)
  - **Artifact**: `G81_p2.json`
  - **Normalized Gram Determinant**: `sqrt(det G) / 2^80 = 252 * 20^39` (strictly above `196 * 20^39`)
  - **Constructive Rational Congruence**: `Q Q^T = G` (`Q_den = 10`) and `P (81 I_81) P^T = G` (`P_den = 90`), with `80` (at least `n - 2 = 79`) realized `{-1,+1}` rows `M0`.

---

## 3. Step 1 — Independent First-Principles Verification (Executed Before Reading `claim/verify_maxdet.py`)

Before reading `claim/verify_maxdet.py`, we wrote and executed an independent Python exact-arithmetic verifier checking all clauses of `p2`.

### 3.1 Artifact Integrity, Symmetry, Diagonal & Mod-4 Gram Congruences
- **File**: `claim/G81_p2.json` (`192478` bytes, SHA-256 `03b380a2074785deac39cb19b68c0853cd52ea469f7b848600cc756df42c8992`)
- **Symmetry & Diagonal**: `G` is `81 x 81` symmetric (`G[i][j] == G[j][i]`) with `G[i][i] == 81` for all `i in [0, 80]`.
- **Off-Diagonal Congruences**: Upper-triangular off-diagonal entry histogram is `{-3: 8, 1: 3232}` (all off-diagonal entries lie in `{-3, 1}`, satisfying `G[i][j] == 81 == 1 (mod 4)` and `(G[i][j] + G[j][k] + G[k][i] + 81) == 0 (mod 4)` for all triples `(i, j, k)`).

### 3.2 Positive Definiteness, Exact Determinant & Record Comparison
- **Sylvester Leading Principal Minors**: Fraction-free Bareiss elimination without row swaps confirms all `81` leading principal minors `Delta_1, ..., Delta_81` of `G` are strictly positive.
- **Exact Gram Determinant**:
  `sqrt(det(G)) / 2^80 = 252 * 20^39 = 138538465099776000000000000000000000000000000000000000`
- **Strict Improvement Over Live Record**:
  `252 * 20^39 = 138538465099776000000000000000000000000000000000000000` strictly exceeds the standing record `196 * 20^39 = 107752139522048000000000000000000000000000000000000000` by `1.285714x` (`det(G)` is `(1.285714)^2 = 1.65306x` times `(2^80 * D_rec)^2`), while remaining strictly below `B_Barba(81)^2`.

### 3.3 Constructive Rational Equivalence (`Q * Q^T == G` and `P * (81 I_81) * P^T == G`)
- Setting `Q = Q_num / 10`, exact integer matrix multiplication confirms `Q_num * Q_num^T == 100 * G` across all `81 x 81 = 6561` entries.
- Since `n = 81 = 9^2` is an odd square, setting `P = Q_num / 90` (`P_den = 9 * 10 = 90`) gives `P * (81 * I_81) * P^T == Q * Q^T == G` in exact rational arithmetic, constructively certifying Hasse-Minkowski rational equivalence of `G` to `81 * I_81` (and to `I_81`).

### 3.4 Leading Principal Block Realization (`M0 * M0^T == G[:80, :80]`)
- `M0` has dimensions `80 x 81` (`80 == n - 1`, which is at least `n - 2 = 79`), with all `6480` entries in `{-1, +1}`.
- Exact integer matrix multiplication confirms `M0 * M0^T == G[:80, :80]` across all `80 x 80 = 6400` entries.

---

## 4. Step 2 — Audit & Execution of Author's Verifier (`claim/verify_maxdet.py`)

After completing our independent verification, we inspected `claim/verify_maxdet.py` and executed it on `claim/G81_p2.json` and on a corrupted copy.

### 4.1 Clean Artifact Execution
- **Command**: `python3 claim/verify_maxdet.py --gram claim/G81_p2.json`
- **Exit Code**: `0`
- **Output**:
```text
=== Exact Verification of Frozen Gram Target p2 (n=81) ===
Symmetry & mod-4 congruences : PASS (G_ii = 81, all pairwise/triple congruences hold)
Sylvester PD & Bareiss==CRT  : PASS (all 81 leading principal minors above 0)
sqrt(det G) / 2^80        : 138538465099776000000000000000000000000000000000000000 above D_rec = 107752139522048000000000000000000000000000000000000000 (improvement: 1.285714x)
Realized {-1,+1} rows M0     : PASS (80 rows at_least_ n-2 = 79 satisfy M0 M0^T = G[:80,:80])
Constructive Q Q^T == G      : PASS (exact rational matrix with denominator 10)
Constructive P (n I_n) P^T=G : PASS (n=81=9^2, P = Q/9 has denominator 90)
PASS: CONFIRMED_PARTIAL (p2 Frozen Gram Target)
```

### 4.2 Corrupted Artifact Execution
- **Command**: Perturbed `G[0][80]` and `G[80][0]` by `+2` and ran `claim/verify_maxdet.py --gram`
- **Exit Code**: `1` (non-zero rejection)
- **Output**:
```text
FAIL: Mod-4 triple congruence violated at (0,1,80)
```

---

## 5. Summary Verification Table

| Criterion / Check | Method | Scope | Result | Status |
|---|---|---|---|---|
| Artifact SHA-256 & Size | `hashlib.sha256` | `192478` bytes | `03b380a2074785de...` | PASS |
| Symmetric & Mod-4 Congruences | All pairs & triples | `81 x 81` (`G_ii = 81`) | Off-diag in `{-3, 1}`, mod-4 valid | PASS |
| Positive Definite (Sylvester) | Leading Bareiss minors | `Delta_1, ..., Delta_81` | All `81` leading minors positive | PASS |
| `det(G)` Beats Live Record Squared | Exact Bareiss & CRT | `252 * 20^39` vs `196 * 20^39` | `1.285714x` (`det(G)` below Barba) | PASS |
| Rational Congruence to `81 * I_81` | Exact `P * (81 I_81) * P^T == G` | `81 x 81` (`P_den = 90`) | Exact identity over `Q` | PASS |
| Realized Leading Block `M0` | Exact `M0 * M0^T == G[:80,:80]` | `80 x 81` (`80` at least `79`) | Exact match in `{-1, +1}` | PASS |
| Adversarial Corruption Test | Perturb `G[0][80] += 2` | Independent + `verify_maxdet.py` | Rejected (`rc = 1`) | PASS |

pass: true
