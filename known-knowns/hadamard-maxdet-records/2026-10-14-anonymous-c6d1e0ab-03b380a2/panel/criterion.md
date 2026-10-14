# CRITERION Skeptic Report: `hadamard-maxdet-records` — Order `n = 81` Partial Win `p2` (Frozen Gram Target)

context: subagent
confirmed_scope: Verified that claim/G81_p2.json (192,478 bytes, SHA-256 03b380a2074785deac39cb19b68c0853cd52ea469f7b848600cc756df42c8992) defines a valid Partial Win p2 (Frozen Gram Target) at order n = 81 consisting of an 81x81 symmetric positive-definite integer Gram matrix G with diagonal 81, valid pairwise and triple mod-4 congruences, exact normalized root-determinant sqrt(det G) / 2^80 = 252 * 20^39 = 138538465099776000000000000000000000000000000000000000 strictly beating the live record 196 * 20^39 = 107752139522048000000000000000000000000000000000000000, constructive exact rational congruence P (81 I_81) P^T = G (and Q Q^T = G), and 80 realized {-1,+1} rows M0 matching the leading 80x80 principal block of G.

## 1. Clause-by-Clause Verification of Partial Win `p2` Against `claim/target.md`

### 1.1 Order Eligibility ($n = 81$ Record Strictly Below Bound)
- $n = 81 \equiv 1 \pmod 4$. The standing record at $n = 81$ is $D_{\text{rec}}(81) = 196 \cdot 20^{39} = 107752139522048000000000000000000000000000000000000000$, which is strictly below the Barba bound $\lfloor \sqrt{161} \cdot 20^{40} \rfloor = 139520956558491744061508097600984010074074880169671590$ because $2n - 1 = 161 = 7 \cdot 23$ is not a square.

### 1.2 Symmetry, Diagonal, and Mod-4 Gram Congruences
- Verified $G$ is an explicit $81 \times 81$ symmetric integer matrix with $G_{ii} = 81$ for all $1 \le i \le 81$.
- Every off-diagonal entry $G_{ij}$ ($i \ne j$) satisfies $G_{ij} \equiv 81 \equiv 1 \pmod 2$ (specifically, the leading $80 \times 80$ block has $G_{ij} = 1$ for $i \ne j$, and the $81$-st border row/column has $72$ entries equal to $+1$ and $8$ entries equal to $-3$), and every triple $(i, j, k)$ satisfies $G_{ij} + G_{jk} + G_{ki} + 81 \equiv 0 \pmod 4$.

### 1.3 Positive Definiteness & Determinant Strictly Above Live Record Squared
- All $81$ leading principal Bareiss minors $\Delta_1, \dots, \Delta_{81}$ of $G$ are strictly positive (Sylvester's criterion).
- Exact integer $\det(G)$ verified identically via fraction-free Bareiss elimination, Chinese Remainder Theorem modular determinants, and exact `fractions.Fraction` Gaussian elimination:
  $$\det(G) = \left(2^{80} \cdot 252 \cdot 20^{39}\right)^2, \quad \frac{\sqrt{\det G}}{2^{80}} = 252 \cdot 20^{39} = 138538465099776000000000000000000000000000000000000000.$$
- $\det(G)$ is strictly greater than the square of the live record $(2^{80} \cdot 196 \cdot 20^{39})^2$ (ratio $252 / 196 = 9 / 7 \approx 1.285714\times$ in root-determinant, $(9/7)^2 \approx 1.653061\times$ in $\det G$), and does not exceed $B(81)^2 = 161 \cdot 80^{80}$.

### 1.4 Exact Rational (Hasse-Minkowski) Equivalence to $81 I_{81}$
- **Hasse-Minkowski invariants**: Verified that $\det(G) / 81^{81} = (2^{80} \cdot 252 \cdot 20^{39} / 9^{81})^2$ is a nonzero rational square and that the $p$-adic Hasse invariant of $G$ equals the $p$-adic Hasse invariant of $81 I_{81}$ (and $I_{81}$) at $p = 2$ and every odd prime dividing $2 \cdot 81 \cdot \det(G)$.
- **Constructive rational congruence**: Verified in exact integer arithmetic that $Q = Q_{\text{num}} / 10$ (`Q_den = 10`) satisfies $Q Q^T = G$ (`Q_num @ Q_num^T == 100 * G`), and since $81 = 9^2$, setting $P = Q / 9 = Q_{\text{num}} / 90$ (`P_den = 90`) satisfies $P (81 I_{81}) P^T = G$ identically.

### 1.5 Realized Leading Principal Block ($k = 80 \ge n - 2 = 79$ Rows)
- Verified that `M0` in `claim/G81_p2.json` is an explicit $80 \times 81$ matrix with all entries in $\{-1, +1\}$ ($80 = n - 1 \ge n - 2 = 79$ rows) satisfying $M_0 M_0^T = G_{1..80, 1..80}$ identically.

## 2. Verdict
All literal clauses of Partial Win `p2` (Frozen Gram Target) in `claim/target.md` are satisfied.

pass: true
