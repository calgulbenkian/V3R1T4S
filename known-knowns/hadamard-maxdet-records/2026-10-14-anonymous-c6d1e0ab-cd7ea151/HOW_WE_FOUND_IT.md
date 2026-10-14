# How We Found It (contributor text, unverified)

*Note: This file is contributor text, unverified. The claim rests solely on `object/G49_p2.json` and `verify-it-yourself/verify_maxdet.py`.*

## Method Summary (`n=49(p2)`)

Using our Rank-1 Right-Kernel Absorber over $\mathbb{Q}$ (`how-we-built-it/frozen_gram_builder.py`), we constructed `n - 1 = 48` explicit `{-1,+1}` rows `M0` realizing the leading principal block of the symmetric positive-definite integer Gram target `G` of order `n = 49` and produced the exact rational congruence certificate `Q` (`Q Q^T = G` and `P (49 I_49) P^T = G` with `P = Q / 7`).
