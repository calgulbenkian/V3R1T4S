# How We Found It — `[154, 11, 97]_4` Linear Code

*Note: contributor text, unverified (narrative explanation of how the generator matrix was constructed; the machine-verified generator matrix is in `object/win_q4_n154_k11_d97.json`).*

## Method Summary
1. **Lens 1 (`how-we-built-it/qc_search.c`)**: Quasi-cyclic / quasi-twisted (`QC/QT`) polynomial ideal search combined with Zero-Divisor CRT Lifting and Coset-Weighted Construction X over $\mathbb{F}_4[x]/(x^m - 1)$.
2. **Lens 2 (`how-we-built-it/bklc_opt.c`)**: Critical-Word Histogram Smart Puncturing inside the circulant blocks and Full-Space Hitting-Set Extension minimizing the minimum-weight codeword shell $A_d$.
