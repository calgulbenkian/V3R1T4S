# How We Found It (contributor text, unverified)

*Note: This file is contributor text, unverified. The claim rests solely on `object/A52_8_7_3802.txt` and `verify-it-yourself/verify_cwc.py`.*

## 1. Incremental Multi-Threaded C Blocker-Hypergraph LNS (`how-we-built-it/cwc_lns.c`)
We ported the blocker-hypergraph large-neighborhood search (LNS) algorithm from `known-knowns/bigger-codes/how-we-built-it/` to an 8-thread native C (`clang -O3 -march=native -pthread`) engine (`how-we-built-it/cwc_lns.c`) that maintains the exact blocker count `int16_t cnt[C(n,w)]` incrementally via atomic updates across $t$-subset neighborhoods ($t = w - d/2 + 1 = 4$) and solves degree-weighted maximum independent set (`w_v = (n+1) + deg_R(v)`) over conflict clusters up to `KB = 4, rmax = 12`.

## 2. Degree-Balanced Coordinate Relabeling (`how-we-built-it/shortening_and_delsarte.py`)
In Lens 2, auditing coordinate degrees on the `d = 8, w = 7` seeds revealed a severe coordinate-degree imbalance on `bit 0`, which biased lexicographic $t$-subset cluster indexing. Combining degree-sorted coordinate relabeling with our incremental C LNS engine pushed `A(52, 8, 7)` from `3799` to **`3802`** (`+3` over `TROPHY_CASE.md` and `+5` over `Andw.html`), verified exhaustively across all `7,225,701` codeword pairs.
