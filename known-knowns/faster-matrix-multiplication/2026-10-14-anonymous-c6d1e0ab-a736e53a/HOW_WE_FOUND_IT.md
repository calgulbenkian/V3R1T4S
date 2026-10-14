# How We Found It (contributor text, unverified)

*Note: This file is contributor text, unverified. The claim rests solely on `object/4x14x15_m569_Z.json` and `verify-it-yourself/verify_z_brent.py`.*

## 1. Exact Subspace Homomorphism Substitution (`Q -> Z / ZT`)
In `dronperminov/FastMatrixMultiplication`, rational (`_Q.json`) bilinear schemes with half-integer denominators decompose into integer/ternary rank-1 triads plus $c$ contiguous fractional blocks of length $R_0 \in \{32, 63\}$. Each fractional block $(U_b, V_b, W_b)$ is the image of either the rank-32 rational `(2, 4, 5)` tensor or the rank-63 rational `(3, 4, 7)` tensor under an exact integer linear homomorphism $(P_U, P_V, P_W)$. Substituting the rank-33 ternary `(2, 4, 5)` decomposition or the rank-64 ternary `(3, 4, 7)` decomposition preserves the exact bilinear tensor over $\mathbb{Z}$ while eliminating all fractional denominators at a cost of $+1$ rank per block.

## 2. Equivariant $GL(\mathbb{Z})$ Gauge Elimination & Native C Flip-Graph Absorption
1. **Lens 1 (`how-we-built-it/upgrade_schemes.py`)**: Applying contragredient unimodular row transvections and signed axis permutations directly to $(P_U, P_V, P_W)$ preserves $(P_U \otimes P_V \otimes P_W)(T_{m_0, n_0, p_0})$ identically while eliminating $\pm 2$ entries produced by basis twists in $P_U, P_V, P_W$.
2. **Lens 2 (`how-we-built-it/zt_flip_reduce.c`)**: We built a 64-bit Zobrist-hashed C (`clang -O3`) flip-graph absorber and rank reducer to absorb non-ternary coefficients and merge split triads.

On `4x14x15`, this yielded `object/4x14x15_m569_Z.json` in coefficient class `Z` (maximum absolute entry `2`) at rank **`569`** (saving **`3`** multiplications below the live `Z` record `572`), verified in exact integer arithmetic across all `705,600` Brent equations.
