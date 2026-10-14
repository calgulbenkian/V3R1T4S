# Preregistration: Lens 1 (`c-evaluator-optimizer`)

frozen_utc: 2026-10-14T04:35:00Z
target: constant-weight-codes
lens: c-evaluator-optimizer
null_test: not needed because all candidate constant-weight codes are verified deterministically across all M words and all M(M-1)/2 pairs by verify_cwc.py.

## 1. Preregistered Attack Plan

1. **Native Multi-Threaded C Incremental Blocker-Hypergraph LNS Engine (`code/cwc_lns.c`)**:
   - Implement the exact algorithm of `lb_lns_fast3.py` / `lb_lns_inc2.py` in native C (`clang -O3 -march=native -pthread`):
     - Byte-table colex ranking (`rank_t`) and unranking (`unrank_colex`) of weight-$w$ words in $\{0, \dots, n-1\}$.
     - Incremental blocker-count array `cnt[rank]` (`uint16_t` or `uint8_t` with sentinel `SENT` for codewords) updated via support/complement $j$-subset masks ($1 \le j \le r = d/2 - 1$) whenever a codeword is removed or inserted.
     - Exact $t$-subset owner table (`t = w - d/2 + 1`, `owner[sub_rank]`) rebuilt and verified every round to guarantee zero $t$-subset collisions.
     - Parallel (`pthread`) exact bitset branch-and-bound Maximum Independent Set solver (`mis_exact_g` with greedy clique-cover upper bound) over all 1..3-blocker sets, sampled 4-blocker sets, and random connected clusters of the co-blocking graph (`|R| <= rmax`).
2. **Primary Target Cells**:
   - `A(52,8,7)` (warm-start `A52_8_7_3799.txt`, bar `3799`), `A(53,8,7)` (`A53_8_7_3987.txt`, bar `3987`), `A(54,8,7)` (`A54_8_7_4193.txt`, bar `4193`), `A(55,8,7)` (`A55_8_7_4426.txt`, bar `4426`), `A(56,8,7)` (`A56_8_7_4685.txt`, bar `4685`).
   - Shallow `D`-preset cells (`A(26,6,8)`, `A(27,6,9)`, `A(30,8,8)`, `A(51,6,5)`, `A(25,6,12)`, `A(26,6,11)`) and short `P20k` cells (`A(27,8,10)`, `A(35,6,6)`, `A(45,8,7)`, `A(58,6,5)`).
3. **Verification**:
   - Every improved code is written to `results/A{n}_{d}_{w}_{M}.txt` and verified with `verify_cwc.py`.
