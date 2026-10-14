# CRITERION Skeptic Assessment: `ghr-sum-difference-c3a`

context: subagent
confirmed_scope: Verified that the finite-depth base-q block certificates in claim/best_k2_m2_finite_cert.json (SHA-256 a4be363d511abedbd64b9d99599e6d72572fe7423b96b63cce20e9e1b431e71b, k=2, m=2, ell=10^16, B=21700, q=25879, mask size 6641, certified lower bound 1.19299096527644796779957337201144650183761204467324), claim/best_k2_finite_cert.json (SHA-256 88a8597a3f644e9ea00bdd76269ce69e5c367e9eeaddab9c1a8d3594d8750b1d, k=2, m=1, ell=10^16, B=21700, q=25879, mask size 6641, certified lower bound 1.19298973462186362590382529754753993070825527359705), and claim/deep_k1_cert.json (SHA-256 f66848137f7f749bc2305b5fcca464507273d02a515a0e1174050714adf0da17, k=1, m=1, ell=10^13, B=19572, q=30295, mask size 3889, certified lower bound 1.19229311147308833018077611662264204140088149782869) literally satisfy Partial Win p1 of ghr-sum-difference-c3a by strictly improving the published finite-certified lower bound 1.19102809 (Kleinwaks 2026b, Zenodo 19363795) by +0.001962875276, +0.001961644621, and +0.001265021473 respectively (all far exceeding the 1e-7 threshold).

## 1. Literal Problem Statement & Acceptance Criteria Audit

From `claim/target.md`, the target is the Gyarmati–Hennecart–Ruzsa (2003) sum-difference constant:
$$C_{3a} = \sup_{|A| \ge 2} \frac{\log |A - A|}{\log |A + A|}$$
over finite integer sets $A \subset \mathbb{Z}$ with at least 2 elements.

`claim/target.md` defines two distinct tiers of success:
1. **Full Win**: Strictly improve the best known unconditional asymptotic limit lower bound `1.19519192` (Kleinwaks 2026b, Zenodo 19363795, logged 2026-04-01 on `teorth/optimizationproblems` `constants/3a.md`) by at least `1e-7` (reaching at least `1.19519202`).
2. **Partial Win (`p1`)**: Strictly improve the best published *finite-certified* (finite-depth base-$q$ concatenation without taking the asymptotic limit as depth approaches infinity) lower bound `1.19102809` (Kleinwaks 2026b, Zenodo 19363795, logged 2026-04-01) by at least `1e-7` (reaching at least `1.19102819`) with an explicit digit mask $M \subseteq \{0, \dots, B\}$, modulus $q$, finite concatenation depth, and exact multinomial/polynomial certificate.

### Honest Framing Check
- `claim/CLAIM.md` explicitly declares **Claim Type: Partial Win (`p1`)** and transparently states in its "Relation to the Unconditional Limit Record" section that none of the three finite-depth certificates exceed the unconditional asymptotic limit record `1.19519192`.
- `claim/verify_c3a.py` explicitly outputs `"beats_limit_record_1_19519192": false`, `"beats_finite_record_1_19102809": true`, and `"beats_finite_record_by_1e7": true` for all three certificates. There is no conflation between Partial Win `p1` and Full Win.

---

## 2. Independent Verification of Certificates & SHA-256 Digests

Running `shasum -a 256` and `python3 verify_c3a.py best_k2_m2_finite_cert.json best_k2_finite_cert.json deep_k1_cert.json` inside `claim/` exited with code `0` and confirmed every digest and 50-digit lower bound reported in `claim/CLAIM.md` and `claim/REPRODUCE.md`:

| Certificate File | SHA-256 Digest | Parameters ($k, m, \ell, B, q, |M|$) | Certified 50-Digit Lower Bound $\theta_{\mathrm{finite}}$ | Margin Above `1.19102809` | Beats `p1` Threshold (`1.19102819`)? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `claim/best_k2_m2_finite_cert.json` | `a4be363d511abedbd64b9d99599e6d72572fe7423b96b63cce20e9e1b431e71b` | $k=2, m=2, \ell=10^{16}, B=21700, q=25879, |M|=6641$ | `1.19299096527644796779957337201144650183761204467324` | `+0.001962875276...` ($19,628\times 10^{-7}$) | Yes (`true`) |
| `claim/best_k2_finite_cert.json` | `88a8597a3f644e9ea00bdd76269ce69e5c367e9eeaddab9c1a8d3594d8750b1d` | $k=2, m=1, \ell=10^{16}, B=21700, q=25879, |M|=6641$ | `1.19298973462186362590382529754753993070825527359705` | `+0.001961644621...` ($19,616\times 10^{-7}$) | Yes (`true`) |
| `claim/deep_k1_cert.json` | `f66848137f7f749bc2305b5fcca464507273d02a515a0e1174050714adf0da17` | $k=1, m=1, \ell=10^{13}, B=19572, q=30295, |M|=3889$ | `1.19229311147308833018077611662264204140088149782869` | `+0.001265021473...` ($12,650\times 10^{-7}$) | Yes (`true`) |

The verifier script `claim/verify_c3a.py` (SHA-256 `a77dca2bb66f2ee32310c8276fd15e72236e28089f2718b5935b6e289f50d651`) also confirmed `"methods_agree": true` across all three certificates.

---

## 3. Mathematical Audit of the Finite-Depth Construction & Bound

We audited `claim/CLAIM.md` and `claim/verify_c3a.py` to ensure there are no hidden asymptotic assumptions, uncertified carry collisions, or optimistic rounding directions:

1. **Valid Base-$q$ Representation & Witness Costs**:
   - In all three certificates, the mask $M \subseteq \{0, 1, \dots, B\}$ satisfies $0 \in M$, $B \in M$, and the base $q$ satisfies $B + 1 \le q \le 2B$ ($q = 25879$ for $B = 21700$, and $q = 30295$ for $B = 19572$). Because every digit in $M$ lies in $[0, q-1]$, base-$q$ expansion of any $N$-digit tuple in $M^N$ is unique.
   - `claim/verify_c3a.py` constructs the single-digit sum support $M + M \subseteq [0, 2B]$ and single-digit minimum witness sum table $\kappa(d) = \min\{a + b : a, b \in M, a - b = d\}$ via two independent algorithms (`combinatorial_tables_method1` and `combinatorial_tables_method2`) and explicitly checks witness validity $a \in M, b \in M, a - b = d, a + b = \kappa(d)$ for every $d \in [0, B]$.
   - For $k$-digit blocks ($k \in \{1, 2\}$), `block_difference_costs_method1` and `block_difference_costs_method2` independently compute the minimum digit sum $c_{\mathrm{no}}^{(k)}(r)$ for representing each block difference $r \in \{1, \dots, q^k - 1\}$ without outer borrow, and define the canonical dual-pair cost $c_{\mathrm{canon}}^{(k)}(r) = \min(c_{\mathrm{no}}^{(k)}(r), c_{\mathrm{no}}^{(k)}(q^k - r))$.

2. **Exact Injectivity of Block Differences in $\mathbb{Z}$ (`nh = 0`)**:
   - In all three certificates, $q$ is odd ($25879$ and $30295$), so $q^k$ is odd and there is no non-zero self-inverse residue $r \equiv -r \pmod{q^k}$ (`nh = 0`).
   - For each dual pair $\{r, q^k - r\}$ ($1 \le r \le (q^k - 1)/2$) with finite cost, picking the representative $r^* \in \{r, q^k - r\}$ achieving $c_{\mathrm{no}}^{(k)}(r^*) = c_{\mathrm{canon}}^{(k)}(r)$ gives a $k$-digit witness pair $(u^{(r)}, v^{(r)}) \in M^k \times M^k$ with integer block difference $u^{(r)} - v^{(r)} = +r^*$ and swapped block difference $v^{(r)} - u^{(r)} = -r^* \equiv q^k - r^* \pmod{q^k}$.
   - Because $0$, $+r^* \bmod q^k$, and $(-r^*) \bmod q^k = q^k - r^*$ are pairwise distinct residues modulo $q^k$ across all dual pairs, the map $(D_0, \dots, D_{\ell-1}) \mapsto \sum_{i=0}^{\ell-1} D_i q^{ki} \in \mathbb{Z}$ is strictly injective: reducing modulo $q^k$ uniquely identifies $D_0 \bmod q^k$ and hence $D_0 \in \mathbb{Z}$, and induction on $i = 0, \dots, \ell - 1$ uniquely recovers every block difference $D_i$.
   - Furthermore, every valid multiset permutation with $n_r$ blocks of $(u^{(r)}, v^{(r)})$, $n_r$ blocks of $(v^{(r)}, u^{(r)})$, and $n_0 = \ell - \sum 2 n_r$ zero blocks produces $u, v \in U_\ell$ having identical total base-$q$ digit sum $\sum_{j=0}^{k\ell-1} u_j = \sum_{j=0}^{k\ell-1} v_j = \sum_{\{r, q^k - r\}} n_r c_{\mathrm{canon}}^{(k)}(r) = L$.
   - Consequently, $|U_\ell - U_\ell|$ is bounded below by the exact multinomial count $D_{\mathrm{block}}(\ell) = \frac{\ell!}{n_0! \prod_{\{r, q^k - r\}} (n_r!)^2}$.

3. **Rigorous Sum-Side Upper Bound & Outward Directed Rounding**:
   - Every sum $u + u' \in U_\ell + U_\ell$ has $N = k\ell$ base-$q$ digit sums $s_j = u_j + u'_j \in M + M$ with total sum $\sum_{j=0}^{N-1} s_j = 2L$.
   - For $m = 1$ (`claim/best_k2_finite_cert.json` and `claim/deep_k1_cert.json`), Rankin's bound gives $|U_\ell + U_\ell| \le x^{-2L} P_+(x)^N$ where $P_+(x) = \sum_{s \in M+M} x^s$.
   - For $m = 2$ (`claim/best_k2_m2_finite_cert.json`), the carry-state automaton in `claim/verify_c3a.py` sums $x^{\text{cost}}$ over both outgoing carry states (`c0` for $m$-digit block sums in $[0, q^m - 1]$ and `c1` for $m$-digit block sums in $[q^m, 2q^m - 1]$), bounding the generating polynomial of all achievable $m$-digit block integer sums $S_i = s_{2i} + s_{2i+1} q$ from above by $W_2(x)$, so $|U_\ell + U_\ell| \le x^{-2L} W_2(x)^{N/2}$.
   - All logarithms of factorials use exact integer multiplication for $n \le 2000$ and the rigorous Robbins (1955) two-sided Stirling bounds enclosing $\ln(n!) - \left((n+\frac{1}{2})\ln n - n + \ln\sqrt{2\pi}\right)$ within $[\frac{1}{12n+1}, \frac{1}{12n}]$ for $n \ge 2001$, with `ROUND_FLOOR` (`ctx_lo`) for lower bounds and `ROUND_CEILING` (`ctx_hi`) for upper bounds, evaluated independently at 80-digit and 105-digit precision (agreeing to more than 60 decimal places).

## 4. Verdict

All three certificates in `claim/` literally and rigorously satisfy the Partial Win (`p1`) acceptance criteria of `ghr-sum-difference-c3a`.

pass: true
