# How We Found It (contributor text, unverified)

*Note: This file is contributor text, unverified. The claim rests solely on `object/15x15x16_r2129_Q.json` and `verify-it-yourself/verify_brent.py`.*

## 1. The $(-6, 1, \dots, 1)$ Hyperplane Fiber & Multi-Step Peeling Cascade
While analyzing the newly committed `17x17x17` (`r = 2723`) and `18x18x18` (`r = 3031`) rational anchors from LITA (Khoruzhii et al., arXiv:2602.12686), we discovered a dense anisotropic hyperplane fiber in `17x17x17`: 169 rank-one terms share the exact hyperplane normal $e = (1, 1, 1, 1, 1, 1, 1, 1, -6, 1, 1, 1, 1, 1, 1, 1, 1) \in \mathbb{Q}^{17}$ paired with $f = e_0 \in \mathbb{Q}^{17}$. Projecting orthogonal to this fiber annihilates 170 multiplications in a single step, yielding `(16, 17, 17)` at rank `2553`.

## 2. Interleaved Rado-Edmonds Matroid Max-Kill Absorption
In `how-we-built-it/cascade_17_18.py` and `how-we-built-it/screen_all.py`, we interleaved hyperplane projections $(e, f)$ with exact rational Rado-Edmonds linear matroid intersection (`matroid_maxkill`) over the Khatri-Rao nullspaces of $(U \odot V, U \odot W, V \odot W)$. Cascading this multi-step peel + matroid absorption pipeline produced `object/15x15x16_r2129_Q.json` for format `(15, 15, 16)` at rank **`2129`** over $\mathbb{Q}$, verified across all `12,960,000` Brent equations.
