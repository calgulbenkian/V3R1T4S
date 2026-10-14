# How We Found It (contributor text, unverified)

*Note: This file is contributor text, unverified. The claim rests solely on `object/M117_73659860230620869930312403886045415232575930948902221537499019577403834332848324440116.txt` and `verify-it-yourself/verify_maxdet.py`.*

## Method Summary (`n=117`)

We constructed a Hadamard core $H_{116}$ (Paley Class I for $m=104, 108$; Williamson $4 \times 29$ for $m=116$), used our compiled C Iterated Local Search + multi-radius Basin Hopping solver (`how-we-built-it/maxdet_search.c`) to maximize the Hadamard excess $\Sigma(H_m) = \max_{u,c \in \{\pm 1\}^m} u^T H_m c$, and applied bordered Sherman-Morrison rank-1 determinant polishing to obtain the record `117 x 117` `{-1,+1}` matrix `object/M117_73659860230620869930312403886045415232575930948902221537499019577403834332848324440116.txt`.
