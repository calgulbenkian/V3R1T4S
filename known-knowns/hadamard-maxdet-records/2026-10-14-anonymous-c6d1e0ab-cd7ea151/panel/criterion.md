# CRITERION Skeptic Report: `hadamard-maxdet-records` — Order `n = 49` Partial Win `p2` (Frozen Gram Target)

context: subagent
confirmed_scope: Verified that claim/G49_p2.json (68,674 bytes, SHA-256 cd7ea151cb23cea573fc617f983c2ce21a340dda94ec30baf82c4180c170e347) defines a valid Partial Win p2 (Frozen Gram Target) at order n = 49 consisting of a 49x49 symmetric positive-definite integer Gram matrix G with diagonal 49, valid pairwise and triple mod-4 congruences, exact normalized root-determinant sqrt(det G) / 2^48 = 116 * 12^23 = 768469522966111493289934848 strictly beating the live record 96 * 12^23 = 635974777627126753067532288, constructive exact rational congruence P (49 I_49) P^T = G (and Q Q^T = G), and 48 realized {-1,+1} rows M0 matching the leading 48x48 principal block of G.

## 1. Clause-by-Clause Verification of Partial Win `p2` Against `claim/target.md`

### 1.1 Order Eligibility ($n = 49$ Record Strictly Below Bound)
- $n = 49 \equiv 1 \pmod 4$. The standing record at $n = 49$ is $D_{\text{rec}}(49) = 96 \cdot 12^{23} = 635974777627126753067532288$, which is strictly below the Barba bound $\lfloor \sqrt{97} \cdot 12^{24} \rfloor = 782952897108359985090801151$ because $2n - 1 = 97$ is prime.

### 1.2 Symmetry, Diagonal, and Mod-4 Gram Congruences
- Verified $G$ is an explicit $49 \times 49$ symmetric integer matrix with $G_{ii} = 49$ for all $1 \le i \le 49$.
- Every off-diagonal entry $G_{ij}$ ($i \ne j$) satisfies $G_{ij} \equiv 49 \equiv 1 \pmod 2$ (specifically, the leading $48 \times 48$ block has $G_{ij} = 1$ for $i \ne j$, and the $49$-th border row/column has $40$ entries equal to $+1$ and $8$ entries equal to $-3$), and every triple $(i, j, k)$ satisfies $G_{ij} + G_{jk} + G_{ki} + 49 \equiv 0 \pmod 4$.

### 1.3 Positive Definiteness & Determinant Strictly Above Live Record Squared
- All $49$ leading principal Bareiss minors $\Delta_1, \dots, \Delta_{49}$ of $G$ are strictly positive (Sylvester's criterion).
- Exact integer $\det(G)$ verified identically via fraction-free Bareiss elimination, Chinese Remainder Theorem modular determinants, and exact `fractions.Fraction` Gaussian elimination:
  $$\det(G) = \left(2^{48} \cdot 116 \cdot 12^{23}\right)^2, \quad \frac{\sqrt{\det G}}{2^{48}} = 116 \cdot 12^{23} = 768469522966111493289934848.$$
- $\det(G)$ is strictly greater than the square of the live record $(2^{48} \cdot 96 \cdot 12^{23})^2$ (ratio $116 / 96 = 29 / 24 \approx 1.208333\times$ in root-determinant, $(29/24)^2 \approx 1.460069\times$ in $\det G$), and does not exceed $B(49)^2 = 97 \cdot 48^{48}$.

### 1.4 Exact Rational (Hasse-Minkowski) Equivalence to $49 I_{49}$
- **Hasse-Minkowski invariants**: Verified that $\det(G) / 49^{49} = (2^{48} \cdot 116 \cdot 12^{23} / 7^{49})^2$ is a nonzero rational square and that the $p$-adic Hasse invariant of $G$ equals the $p$-adic Hasse invariant of $49 I_{49}$ (and $I_{49}$) at $p = 2$ and every odd prime dividing $2 \cdot 49 \cdot \det(G)$.
- **Constructive rational congruence**: Verified in exact integer arithmetic that $Q = Q_{\text{num}} / 6$ (`Q_den = 6`) satisfies $Q Q^T = G$ (`Q_num @ Q_num^T == 36 * G`), and since $49 = 7^2$, setting $P = Q / 7 = Q_{\text{num}} / 42$ (`P_den = 42`) satisfies $P (49 I_{49}) P^T = G$ identically.

### 1.5 Realized Leading Principal Block ($k = 48 \ge n - 2 = 47$ Rows)
- Verified that `M0` in `claim/G49_p2.json` is an explicit $48 \times 49$ matrix with all entries in $\{-1, +1\}$ ($48 = n - 1 \ge n - 2 = 47$ rows) satisfying $M_0 M_0^T = G_{1..48, 1..48}$ identically.

## 2. Verdict
All literal clauses of Partial Win `p2` (Frozen Gram Target) in `claim/target.md` are satisfied.

pass: true
