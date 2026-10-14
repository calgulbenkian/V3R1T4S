# How We Found It (contributor text, unverified)

*Note: This file is contributor text, unverified. The claim rests solely on `object/14x14x15_r1715_Q.json` and `verify-it-yourself/verify_brent.py`.*

## 1. The Brief and Observation
Earlier V3R1T4S runs (2026-10-08 through 2026-10-12) discovered that applying a generalised one-slice restriction ("peeling" along a non-coordinate direction pair $(e, f)$ with $\langle e, f \rangle \ne 0$) to LITA's square schemes (`14x14x14:1593`, `15x15x15:1977`, `16x16x16:2236`), followed by single-support nullspace absorption (`maxkill.py`), yielded five record rational schemes (`14x15x15:1842`, `13x14x14:1558`, `15x16x16:2180`, `14x14x15:1716`, `13x14x15:1677`).

Two structural gaps remained in that pipeline:
1. `maxkill.py` filtered the RREF left nullspace $C \in \mathbb{Q}^{d \times r}$ of a factor pairing $(Y \otimes Z)$ down to columns with support size $1$ (`|supp(c_k)| == 1`), ignoring multi-support "hub" columns (`|supp(c_k)| >= 2`) that share projective rays.
2. Secondary peels from the newly absorbed schemes (`14x15x15:1842` and `15x16x16:2180`)—and non-greedy axis orderings where absorption precedes or alternates with peeling—had not been systematically cascaded with exact multi-round `(uv, uw, vw)` matroid absorption.

## 2. What Failed (Lens 2: `c-evaluator-optimizer`)
We built a compiled native C (`clang -O3`) evaluator (`lookahead_peel_c.py`) to test whether choosing a *non-greedy* peel direction $(e, f)$ with slightly smaller immediate dead count $z$ could unlock a larger post-peel pairing nullspace (`r - z - 2*nullity`), and whether any of the base schemes admitted direct 2-term collinearity reductions or 3-term cyclic flip triangles (`u_i || u_j, v_j || v_k, w_k || w_i`). Across 48 candidate peels, trading $1$ peel kill ($z \to z - 1$) merely left one rank-1 fiber term unpeeled, increasing the post-peel pairing nullity by $+1$ (`r_peel - nullity` invariant) without creating any new size-2 ray cluster. All 7 base schemes also had zero 2-term collinearity reductions and zero 3-term cyclic flip triangles.

## 3. What Worked (Lens 1: `representation-absorber`)
We built `how-we-built-it/screen_all.py` and `how-we-built-it/build_and_cascade.py`, combining:
1. **C-Accelerated 3-Prime CRT Khatri-Rao Nullspace Extraction**: Random projections modulo three 31-bit primes (`2147483629`, `2147483587`, `2147483579`), exact RREF in C, CRT + rational reconstruction to $\mathbb{Q}$, and exact `fractions.Fraction` certification of every nullspace basis row.
2. **Rado–Edmonds Matroid Max-Kill (`matroid_maxkill`)**: Every column $k$ with non-zero nullspace vector $c_k \in \mathbb{Q}^d$ is projectively normalized by its first non-zero coordinate $c_{s_0, k}$ into a ray cluster $(c_k / c_{s_0, k}, x_k / c_{s_0, k})$. A greedy Rado–Edmonds linear system solver selects the heaviest independent ray clusters (plus any affine-circuit dependent clusters) to construct the optimal shift matrix $\Zeta \in \mathbb{Q}^{d \times d_X}$.

Applying our 3-prime CRT Khatri-Rao nullspace extractor and Rado-Edmonds matroid max-kill solver to `14x14x15_r1716_Q.json` uncovers an overlooked 1-dimensional $(U \otimes V)$ left-nullspace dependency whose $W$-factor shift annihilates $1$ rank-one term ($1716 \to 1715$, beating the `1789` public bar by $74$ and improving the `1716` Trophy Case record by $1$).
