# How We Found It — `ghr-sum-difference-c3a` (`best_k2_m2_finite_cert.json`)

*Note: contributor text, unverified (narrative explanation of how the certificate was constructed; the machine-verified certificate is in `object/best_k2_m2_finite_cert.json`).*

## Method Summary
1. **Lens 1 (`how-we-built-it/deep_k1_polish.cpp`)**: Modulo-$q$ shadowed non-semigroup mask pruning on truncated multiplicative semigroups $\langle G \rangle \cap [0, B]$. When $B < q < 2B + 1$, top mask elements $a \in M \cap [q - B, B]$ whose residue $a \equiv -(q - a) \pmod q$ is already covered at lower or equal weight in $M - M$ can be pruned, shrinking $|M + M|$ while preserving the low-weight difference residue cost distribution $c_k(R)$.
2. **Lens 2 (`how-we-built-it/k2_fine_opt.cpp`)**: Exact $O(q \log q)$ block-length $k = 2$ modulo-$q^2$ residue cost evaluation via $c_2(r_0 + q r_1) = \min(\kappa(r_0) + c_1(r_1),\, \kappa(q - r_0) + c_1((r_1 + 1) \bmod q))$, certifying `best_k2_m2_finite_cert.json` (block length k=2, sum scale m=2, ell=10^16, B=21700, q=25879, |M|=6641 (7 modulo-q shadowed top elements pruned from <{3,4}x{506,508,529}> cap [0,21700])) at $C_{3a} \ge 1.19299096527644796779957337201144650183761204467324$ (`+1.962875e-03` above the published finite-certified record `1.19102809`).
