# How We Found It (contributor text, unverified)

*Note: This file is contributor text, unverified. The claim rests solely on `object/code_29_145.json` and `verify-it-yourself/verify_spherical.py`.*

## Log-Sum-Exp Homotopy + Riemannian L-BFGS on `(S^(29-1))^145` (`how-we-built-it/spherical_opt.c`)

We warm-started from the public `spherical-codes.org/data/29/145` configuration and ran our multi-threaded C Riemannian L-BFGS + Log-Sum-Exp homotopy solver (`how-we-built-it/spherical_opt.c`, $\beta \in [10^2, 5 \times 10^6]$ with active-pair tangent impulse kicks), reducing the 60-digit normalized maximum pairwise inner product from `0.110701844288` to **`0.1106960891058149669538693`** (`gain = 5.755182e-6`).
