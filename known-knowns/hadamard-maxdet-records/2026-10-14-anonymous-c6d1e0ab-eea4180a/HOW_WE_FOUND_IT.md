# How We Found It (contributor text, unverified)

*Note: This file is contributor text, unverified. The claim rests solely on `object/M105_402299811033982511699641115457655638247621548505385285611140221022215602176.txt` and `verify-it-yourself/verify_maxdet.py`.*

## Method Summary (`n=105`)

We constructed a Hadamard core $H_{104}$ (Paley Class I for $m=104, 108$; Williamson $4 \times 29$ for $m=116$), used our compiled C Iterated Local Search + multi-radius Basin Hopping solver (`how-we-built-it/maxdet_search.c`) to maximize the Hadamard excess $\Sigma(H_m) = \max_{u,c \in \{\pm 1\}^m} u^T H_m c$, and applied bordered Sherman-Morrison rank-1 determinant polishing to obtain the record `105 x 105` `{-1,+1}` matrix `object/M105_402299811033982511699641115457655638247621548505385285611140221022215602176.txt`.
