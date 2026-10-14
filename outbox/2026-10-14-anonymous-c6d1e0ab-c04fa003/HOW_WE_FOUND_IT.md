# How We Found It — `[2, 11; 6]`-Mixed Graph on `N = 450` Vertices

*Note: contributor text, unverified (narrative explanation of how the mixed graph was constructed; the machine-verified graph is in `object/mixed_z2_r11_g6_N450.json`).*

## Method Summary
1. **Directed-Collision Exemption in $\operatorname{BiCay}(\mathbb{Z}_M; S, A_0, A_1)$**: In a bipartite bi-Cayley mixed graph on $N = 2M$ vertices, odd cycles cannot occur and mixed 4-cycles occur iff $\Sigma_S = S + S$, $\Sigma_0 = (S + A_0) \cup (A_0 + A_0)$, and $\Sigma_1 = (S + A_1) \cup (A_1 + A_1)$ fail to be pairwise disjoint in $\mathbb{Z}_M$, whereas internal collisions within $\Sigma_0$ or within $\Sigma_1$ correspond to oppositely oriented 2-paths and do not form directed 4-cycles.
2. **Twin-Cluster Sidon Packing (`how-we-built-it/mixed_bicay_sa.c`)**: Choosing $A_0, A_1$ with $a - a' \in S - S$ shrinks $|\Sigma_0|$ and $|\Sigma_1|$ below $2r + 3$, allowing $S = [0, 1, 6, 23, 38, 56, 63, 108, 138, 157, 217], A_0 = [27, 128], A_1 = [104, 205]$ to pack into $\mathbb{Z}_{225}$ ($N = 450$).
