# How We Found It (contributor text, unverified)

*Note: This file is contributor text, unverified. The claim rests solely on `object/code_29_114.json` and `verify-it-yourself/verify_spherical.py`.*

## Log-Sum-Exp Homotopy + Riemannian L-BFGS on `(S^(29-1))^114` (`how-we-built-it/spherical_opt.c`)

We warm-started from the public `spherical-codes.org/data/29/114` configuration and ran our multi-threaded C Riemannian L-BFGS + Log-Sum-Exp homotopy solver (`how-we-built-it/spherical_opt.c`, $\beta \in [10^2, 5 \times 10^6]$ with active-pair tangent impulse kicks), reducing the 60-digit normalized maximum pairwise inner product from `0.089759904426` to **`0.0886557493406558116735243`** (`gain = 1.104155e-3`).
