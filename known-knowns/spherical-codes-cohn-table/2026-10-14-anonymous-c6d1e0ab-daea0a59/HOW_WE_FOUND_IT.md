# How We Found It (contributor text, unverified)

*Note: This file is contributor text, unverified. The claim rests solely on `object/code_26_232.json` and `verify-it-yourself/verify_spherical.py`.*

## Log-Sum-Exp Homotopy + Riemannian L-BFGS on `(S^(26-1))^232` (`how-we-built-it/spherical_opt.c`)

We warm-started from the public `spherical-codes.org/data/26/232` configuration and ran our multi-threaded C Riemannian L-BFGS + Log-Sum-Exp homotopy solver (`how-we-built-it/spherical_opt.c`, $\beta \in [10^2, 5 \times 10^6]$ with active-pair tangent impulse kicks), reducing the 60-digit normalized maximum pairwise inner product from `0.161911811246` to **`0.1619070097691030503945036`** (`gain = 4.801477e-6`).
