# REPRODUCE Skeptic Report — Gyarmati–Hennecart–Ruzsa Sum-Difference Constant $C_{3a}$

- context: subagent
- context: subagent (astra)
- quarry: `ghr-sum-difference-c3a`
- claim_level: `partial_win_claim` (`Partial Win p1`: finite-certified lower bound improvements over $1.19102809$)

## 1. Quoted Mathematical Definitions and Finite-Depth Certificate Formulas

From `claim/target.md` and `claim/CLAIM.md`:
1. **Gyarmati–Hennecart–Ruzsa Sum-Difference Constant $C_{3a}$**:
   $$C_{3a} = \sup_{|A| \ge 2} \frac{\log |A - A|}{\log |A + A|},$$
   where the supremum ranges over all finite subsets $A \subset \mathbb{Z}$ with $|A| \ge 2$.
   - Published finite-certified lower bound record prior to this claim (Kleinwaks 2026b, Zenodo 19363795, logged 2026-04-01 on `teorth/optimizationproblems` `constants/3a.md`):
     $$C_{3a} \ge 1.19102809 \quad (1.19102809427254007200970237949767346144249893230453).$$
2. **Finite-Depth Controlled-Carry Block Certificate Lower Bound (Propositions 1, 2, and 3 of Kleinwaks 2026b)**:
   - Given a finite integer digit mask $M \subset [0, B] \cap \mathbb{Z}$ with $0 \in M$ and $\max(M) = B$, an odd integer base $q \in [B+1, 2B]$ (`q % 2 == 1`, so there are no non-zero self-inverse elements modulo $q^k$, i.e. `nh = 0`), a block length $k \in \{1, 2\}$, a sum-carry block length $m \in \{1, 2\}$, a block count $\ell \ge 1$ ($N = k\ell$ total base-$q$ digits, divisible by $m$), and a Boltzmann parameter $x \in (0, 1)$:
   - Define the single-digit positive difference minimum cost $\kappa(d) = \min\{a + b : a, b \in M,\, a - b = d\}$ for $d \in [0, B]$ (with $\kappa(0) = 0$ and $\kappa(d) = +\infty$ if $d \notin M - M$), and the modulo-$q$ residue cost $c_1(r) = \min(\kappa(r), \kappa(q - r))$ for $r \in [1, q-1]$ ($c_1(0) = 0$).
   - For $k = 2$, each residue $R = r_0 + q r_1 \in [0, q^2 - 1]$ has exact minimum two-digit block cost
     $$c_2(r_0 + q r_1) = \begin{cases} c_1(r_1) & \text{if } r_0 = 0, \\ \min\big(\kappa(r_0) + c_1(r_1),\; \kappa(q - r_0) + c_1((r_1 + 1) \bmod q)\big) & \text{if } r_0 \in [1, q-1]. \end{cases}$$
   - Let $H_k(c) = |\{R \in \mathbb{Z}/q^k\mathbb{Z} : c_k(R) = c\}|$ be the exact residue cost multiplicity histogram and $\text{om}(c) = H_k(c)/2$ for $c \ge 1$ be the negation-orbit multiplicity on $(\mathbb{Z}/q^k\mathbb{Z}) \setminus \{0\}$. With $Z_k(x) = \sum_{c \ge 0} H_k(c) x^c$, the exact integer orbit type counts and weight bound are
     $$n_R(c) = \left\lfloor \ell \cdot \frac{x^c}{Z_k(x)} \right\rfloor, \qquad n_0 = \ell - \sum_{c \ge 1} 2\,\text{om}(c)\,n_R(c), \qquad L = \sum_{c \ge 1} \text{om}(c)\,n_R(c)\,c.$$
   - By base-$q^k$ injectivity on distinct residue witnesses and the multinomial theorem on balanced witness orbits, $|U_\ell - U_\ell| \ge D_\ell$ where
     $$\ln D_\ell = \ln(\ell!) - \ln(n_0!) - \sum_{c \ge 1} 2\,\text{om}(c)\,\ln(n_R(c)!).$$
   - On the sumset side, $|U_\ell + U_\ell| \le S_\ell = W_m(x)^{N/m} x^{-2L}$, where $W_1(x) = P_+(x) = \sum_{s \in M+M} x^s$ for $m = 1$, and $W_2(x)$ is the exact two-step base-$q$ carry-automaton transfer polynomial for $m = 2$, giving $\ln S_\ell = (N/m) \ln W_m(x) - 2L \ln x$.
   - By Proposition 1 (interval gluing / dilation to $V_\ell = 2U_\ell$ with $4\max(U_\ell) + 1 \le 4 q^{k\ell}$), the resulting explicit finite set $A \subset \mathbb{Z}_{\ge 0}$ satisfies:
     $$C_{3a} \ge 1 + \frac{\ln D_\ell - \ln S_\ell}{k\ell \ln q + \ln 4}.$$

## 2. Independent Verification Before Reading `claim/verify_c3a.py`

Before inspecting `claim/verify_c3a.py`, we wrote and executed an independent Python verifier at 110-digit `decimal.Decimal` precision using 1D integer bitsets (`bs` and `bs_sum`) that:
1. Verified all structural invariants on `claim/best_k2_m2_finite_cert.json`, `claim/best_k2_finite_cert.json`, and `claim/deep_k1_cert.json`:
   - `0 in M`, `max(M) == B`, all elements of `M` are strictly increasing integers in $[0, B]$, $B + 1 \le q \le 2B$, and `q % 2 == 1` (`nh == 0`).
   - Confirmed $|M| = 6641$, $\sum_{a \in M} a = 110153923$, $|M + M| = 42914$ for `claim/best_k2_m2_finite_cert.json` and `claim/best_k2_finite_cert.json` ($B = 21700, q = 25879$).
   - Confirmed $|M| = 3889$, $\sum_{a \in M} a = 58264195$, $|M + M| = 22200$ for `claim/deep_k1_cert.json` ($B = 19572, q = 30295$).
2. Recomputed $\kappa(d) = \min\{2b + d : b \in M,\, b + d \in M\}$ via bitset lowest-set-bit extraction (`common = bs & (bs // 2**r)`) and independently reconstructed the complete $k = 2$ residue cost histogram across all $q^2 = 25879^2 = 669,722,641$ residues in $\mathbb{Z}/q^2\mathbb{Z}$ by grouping the $24,519$ distinct $(c_1(r_1), c_1((r_1 + 1) \bmod q))$ pairs:
   - `Independent hist matches JSON cost_histogram: True`
   - `Total reachable residues in Z/q^2Z: 669722641 out of q^2 = 669722641` (all $20,218$ non-zero cost buckets match `cost_histogram` in both $k = 2$ JSON certificates identically).
3. Evaluated $Z_k(x)$, $n_R(c)$, $n_0$, $L$, the Stirling-Bernoulli lower bound on $\ln D_\ell$, the carry-automaton upper bound on $\ln S_\ell$, and the 50-digit lower bound on $C_{3a}$ at 110-digit precision, reproducing every single digit of all three claimed bounds:
   - `claim/best_k2_m2_finite_cert.json` ($k=2, m=2, \ell=10^{16}$): `n0 = 32819948656`, `L = 98800205183398657643`, $C_{3a} \ge \mathbf{1.19299096527644796779957337201144650183761204467324}$.
   - `claim/best_k2_finite_cert.json` ($k=2, m=1, \ell=10^{16}$): `n0 = 32819948656`, `L = 98800205183398657643`, $C_{3a} \ge \mathbf{1.19298973462186362590382529754753993070825527359705}$.
   - `claim/deep_k1_cert.json` ($k=1, m=1, \ell=10^{13}$): `n0 = 16097580574`, `L = 53828044944368725`, $C_{3a} \ge \mathbf{1.19229311147308833018077611662264204140088149782869}$.

## 3. Execution of `claim/verify_c3a.py` and Negative Corruption Tests

1. **Direct Execution of `claim/verify_c3a.py`**:
   Running `python3 claim/verify_c3a.py claim/best_k2_m2_finite_cert.json claim/best_k2_finite_cert.json claim/deep_k1_cert.json` completed in $\approx 6$ seconds with exit code `0`, reporting `"methods_agree": true`, `"nh": 0`, `"beats_finite_record_1_19102809": true`, and `"beats_finite_record_by_1e7": true` on all three certificates, matching our independent 110-digit verifier to all 50 decimal places.
2. **Negative Corruption Tests**:
   - **Mask Corruption ($M[1]: 1518 \to 1519$ in `claim/best_k2_m2_finite_cert.json`)**: Both our independent histogram check and `claim/verify_c3a.py` rejected the corrupted certificate (`exit code 1`, `ValueError: cost_histogram failed exact O(q log q) moment & modular polynomial verification`).
   - **Bound Corruption (`certified_lower_bound_50d` last digit $9 \to 0$ in `claim/deep_k1_cert.json`)**: Rejected with `exit code 1` (`ValueError: certified_lower_bound_50d mismatch: 1.19229311147308833018077611662264204140088149782870 vs 1.19229311147308833018077611662264204140088149782869`).
   - All temporary files created during testing were deleted immediately.

pass: true
