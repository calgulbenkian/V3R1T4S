# Reproduction & Independent Exact-Arithmetic Verification Report — Frozen Gram Target (`p2`) at Order `n = 49`

context: subagent
context: subagent (astra)

## 1. Executive Summary
- **Target**: `hadamard-maxdet-records` (`Hadamard maximal determinant: new record determinants for orders n not divisible by 4`)
- **Order**: `n = 49 = 7^2` (`n == 1 mod 4`)
- **Claim Level**: `CONFIRMED_PARTIAL` (`p2` — Frozen Gram Target)
- **Artifact**: `claim/G49_p2.json` (`68674` bytes, SHA-256 `cd7ea151cb23cea573fc617f983c2ce21a340dda94ec30baf82c4180c170e347`)
- **Claimed Normalized Gram Determinant**: `sqrt(det(G)) / 2^48 = 116 * 12^23 = 768469522966111493289934848` (strictly exceeding the standing record `96 * 12^23 = 635974777627126753067532288` by `1.208333x`)
- **Verdict**: **PASS** — Both our independent first-principles exact-arithmetic verifier (written and executed before reading `claim/verify_maxdet.py`) and the author's standalone verifier confirm every clause of partial win `p2`: `G` is an `49 x 49` symmetric positive-definite integer matrix (all `49` Sylvester leading principal Bareiss minors strictly positive) with diagonal `49`, valid pairwise/triple mod-4 Gram congruences, `det(G)` strictly exceeding the square of the live record and below the Barba bound, constructive rational congruence `Q * Q^T == G` (`Q_den = 6`) and `P * (49 * I_49) * P^T == G` (`P = Q / 7`, `P_den = 42`), and an explicit `48 x 49` `{-1, +1}` matrix `M0` (`48` at least `n - 2 = 47`) satisfying `M0 * M0^T == G[:48, :48]`. Both verifiers also immediately reject perturbed Gram negative controls (`exit = 1`).

---

## 2. Verbatim `p2` Partial Win Definition & Claim Summary (`claim/target.md` and `claim/CLAIM.md`)

### 2.1 Verbatim `p2` Definition (`claim/target.md`)
  - **Partial Win `p2`**: A frozen Gram target: for an order `n` whose record is below its bound, an explicit symmetric positive-definite integer matrix `G` with diagonal `n`, off-diagonal entries obeying the parity/congruence conditions of Gram matrices of `+-1` matrices of that order, `det G` strictly greater than the square of the live record, and passing the rational (Hasse-Minkowski) equivalence test to `n*I`, all checked exactly; plus at least `n-2` rows of a `+-1` matrix realising the leading principal block of `G`.

### 2.2 Claim Summary (`claim/CLAIM.md`)
  - **Target**: `hadamard-maxdet-records`
  - **Claim Level**: `CONFIRMED_PARTIAL` (`p2`)
  - **Artifact**: `G49_p2.json`
  - **Normalized Gram Determinant**: `sqrt(det G) / 2^48 = 116 * 12^23` (strictly above `96 * 12^23`)
  - **Constructive Rational Congruence**: `Q Q^T = G` (`Q_den = 6`) and `P (49 I_49) P^T = G` (`P_den = 42`), with `48` (at least `n - 2 = 47`) realized `{-1,+1}` rows `M0`.

---

## 3. Step 1 — Independent First-Principles Verification (Executed Before Reading `claim/verify_maxdet.py`)

Before reading `claim/verify_maxdet.py`, we wrote and executed an independent Python exact-arithmetic verifier checking all clauses of `p2`.

### 3.1 Artifact Integrity, Symmetry, Diagonal & Mod-4 Gram Congruences
- **File**: `claim/G49_p2.json` (`68674` bytes, SHA-256 `cd7ea151cb23cea573fc617f983c2ce21a340dda94ec30baf82c4180c170e347`)
- **Symmetry & Diagonal**: `G` is `49 x 49` symmetric (`G[i][j] == G[j][i]`) with `G[i][i] == 49` for all `i in [0, 48]`.
- **Off-Diagonal Congruences**: Upper-triangular off-diagonal entry histogram is `{-3: 8, 1: 1168}` (all off-diagonal entries lie in `{-3, 1}`, satisfying `G[i][j] == 49 == 1 (mod 4)` and `(G[i][j] + G[j][k] + G[k][i] + 49) == 0 (mod 4)` for all triples `(i, j, k)`).

### 3.2 Positive Definiteness, Exact Determinant & Record Comparison
- **Sylvester Leading Principal Minors**: Fraction-free Bareiss elimination without row swaps confirms all `49` leading principal minors `Delta_1, ..., Delta_49` of `G` are strictly positive.
- **Exact Gram Determinant**:
  `sqrt(det(G)) / 2^48 = 116 * 12^23 = 768469522966111493289934848`
- **Strict Improvement Over Live Record**:
  `116 * 12^23 = 768469522966111493289934848` strictly exceeds the standing record `96 * 12^23 = 635974777627126753067532288` by `1.208333x` (`det(G)` is `(1.208333)^2 = 1.460069x` times `(2^48 * D_rec)^2`), while remaining strictly below `B_Barba(49)^2`.

### 3.3 Constructive Rational Equivalence (`Q * Q^T == G` and `P * (49 I_49) * P^T == G`)
- Setting `Q = Q_num / 6`, exact integer matrix multiplication confirms `Q_num * Q_num^T == 36 * G` across all `49 x 49 = 2401` entries.
- Since `n = 49 = 7^2` is an odd square, setting `P = Q_num / 42` (`P_den = 7 * 6 = 42`) gives `P * (49 * I_49) * P^T == Q * Q^T == G` in exact rational arithmetic, constructively certifying Hasse-Minkowski rational equivalence of `G` to `49 * I_49` (and to `I_49`).

### 3.4 Leading Principal Block Realization (`M0 * M0^T == G[:48, :48]`)
- `M0` has dimensions `48 x 49` (`48 == n - 1`, which is at least `n - 2 = 47`), with all `2352` entries in `{-1, +1}`.
- Exact integer matrix multiplication confirms `M0 * M0^T == G[:48, :48]` across all `48 x 48 = 2304` entries.

---

## 4. Step 2 — Audit & Execution of Author's Verifier (`claim/verify_maxdet.py`)

After completing our independent verification, we inspected `claim/verify_maxdet.py` and executed it on `claim/G49_p2.json` and on a corrupted copy.

### 4.1 Clean Artifact Execution
- **Command**: `python3 claim/verify_maxdet.py --gram claim/G49_p2.json`
- **Exit Code**: `0`
- **Output**:
```text
=== Exact Verification of Frozen Gram Target p2 (n=49) ===
Symmetry & mod-4 congruences : PASS (G_ii = 49, all pairwise/triple congruences hold)
Sylvester PD & Bareiss==CRT  : PASS (all 49 leading principal minors above 0)
sqrt(det G) / 2^48        : 768469522966111493289934848 above D_rec = 635974777627126753067532288 (improvement: 1.208333x)
Realized {-1,+1} rows M0     : PASS (48 rows at_least_ n-2 = 47 satisfy M0 M0^T = G[:48,:48])
Constructive Q Q^T == G      : PASS (exact rational matrix with denominator 6)
Constructive P (n I_n) P^T=G : PASS (n=49=7^2, P = Q/7 has denominator 42)
PASS: CONFIRMED_PARTIAL (p2 Frozen Gram Target)
```

### 4.2 Corrupted Artifact Execution
- **Command**: Perturbed `G[0][48]` and `G[48][0]` by `+2` and ran `claim/verify_maxdet.py --gram`
- **Exit Code**: `1` (non-zero rejection)
- **Output**:
```text
FAIL: Mod-4 triple congruence violated at (0,1,48)
```

---

## 5. Summary Verification Table

| Criterion / Check | Method | Scope | Result | Status |
|---|---|---|---|---|
| Artifact SHA-256 & Size | `hashlib.sha256` | `68674` bytes | `cd7ea151cb23cea5...` | PASS |
| Symmetric & Mod-4 Congruences | All pairs & triples | `49 x 49` (`G_ii = 49`) | Off-diag in `{-3, 1}`, mod-4 valid | PASS |
| Positive Definite (Sylvester) | Leading Bareiss minors | `Delta_1, ..., Delta_49` | All `49` leading minors positive | PASS |
| `det(G)` Beats Live Record Squared | Exact Bareiss & CRT | `116 * 12^23` vs `96 * 12^23` | `1.208333x` (`det(G)` below Barba) | PASS |
| Rational Congruence to `49 * I_49` | Exact `P * (49 I_49) * P^T == G` | `49 x 49` (`P_den = 42`) | Exact identity over `Q` | PASS |
| Realized Leading Block `M0` | Exact `M0 * M0^T == G[:48,:48]` | `48 x 49` (`48` at least `47`) | Exact match in `{-1, +1}` | PASS |
| Adversarial Corruption Test | Perturb `G[0][48] += 2` | Independent + `verify_maxdet.py` | Rejected (`rc = 1`) | PASS |

pass: true
