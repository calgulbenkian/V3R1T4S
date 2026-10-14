# How We Found It (contributor text, unverified)

*Note: This file is contributor text, unverified. The claim rests solely on `object/code_30_74.json` and `verify-it-yourself/verify_spherical.py`.*

## Log-Sum-Exp Homotopy + Riemannian L-BFGS on `(S^(30-1))^74` (`how-we-built-it/spherical_opt.c`)

We warm-started from the public `spherical-codes.org/data/30/74` configuration and ran our multi-threaded C Riemannian L-BFGS + Log-Sum-Exp homotopy solver (`how-we-built-it/spherical_opt.c`, $\beta \in [10^2, 5 \times 10^6]$ with active-pair tangent impulse kicks), reducing the 60-digit normalized maximum pairwise inner product from `0.051797462893` to **`0.0515109900801632382072426`** (`gain = 2.864728e-4`).
