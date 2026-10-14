# Lens 1 Preregistration (`attempts/representation-absorber/`)

## 1. Hypothesis & Algebraic Mechanism
We hypothesize that a substantial family of ring gaps in `dronperminov/FastMatrixMultiplication` (both `ZT > Z` and `Z > Q`) arise from **distributive factor folding** and **power-of-2 rank-1 scaling**:
1. **5-to-6 and 3-to-4 Inverse-Distributivity Unfolding on `Z` Schemes (`ZT > Z`)**:
   - In Perminov's bounded-integer (`Z`) schemes with entries in $\{-2, -1, 0, 1, 2\}$, non-ternary terms occur in coupled 5-term clusters $(r_1, r_2, r_3, r_4, r_5)$ where $A[r_1] = s_2 A[r_2] + s_3 A[r_3]$, $B[r_1] = \alpha_3 B[r_3] + \alpha_4 B[r_4]$, and $B[r_2] = \alpha_1 B[r_1] + \alpha_5 B[r_5]$, or 3-term clusters $(r_1, r_2, r_3)$ where $B[r_2] = \alpha_1 B[r_1] + \alpha_3 B[r_3]$.
   - Un-distributing $r_1$ into two rank-1 terms and applying shared-factor flips across the remaining terms in the cluster eliminates all $\pm 2$ coefficients across up to 5 non-ternary terms at a net cost of only **+1 rank per cluster** (converting 5 integer terms into 6 ternary terms, or 3 integer terms into 4 ternary terms).
   - Whenever the number of disjoint clusters plus any residual ternary splits is strictly less than $r_{\text{ZT}} - r_{\text{Z}}$, the resulting 100% ternary (`ZT`) scheme strictly beats $r_{\text{ZT}}$ while staying $\ge r_{\text{Z}} \ge r_{\text{Q}}$.
2. **Rank-1 Scalar Balancing & Fractional Cluster Re-Decomposition on `Q` Schemes (`Z > Q`)**:
   - For `Q` schemes with denominators in $\{2^k\}$, we test whether rank-1 torus scaling $(u_r, v_r, w_r) \mapsto (2^a u_r, 2^b v_r, 2^c w_r)$ ($a+b+c=0$), diagonal basis scaling $A \mapsto D_1 A D_2^{-1}$, or re-decomposing the fractional residual sub-tensor $T_{\text{frac}}$ over $\mathbb{Z}$ produces an integer (`Z`) or ternary (`ZT`) scheme strictly below $r_{\text{Z}}$.
3. **Generalised Unimodular Integer Peeling (`e . f = +-1`) on `ZT` and `Z` Schemes**:
   - We test whether peeling a 1-larger `ZT` or `Z` scheme along unimodular integer vectors $(e, f) \in \{-1, 0, 1\}^d$ with $\langle e, f \rangle = \pm 1$ and absorbing rank-1 terms into the nullspace yields a `ZT` or `Z` scheme strictly below the live `ZT` or `Z` column.

## 2. Verification & Stop Rule
- Every candidate scheme must be verified in exact integer arithmetic over $\mathbb{Z}$ by `verify_z_brent.py` and satisfy all four conditions of `fmm-ternary-integer-ring-upgrade`.
