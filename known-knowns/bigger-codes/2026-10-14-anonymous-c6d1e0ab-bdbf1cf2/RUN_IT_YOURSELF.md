# Run It Yourself

## 1. Verify the Shipped Object (`object/A27_8_10_1740.txt`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/A27_8_10_1740.txt
sha256 matches INDEX.csv (bdbf1cf2b34d5a2771172cea5d11fe6abcff25a0de03cc60808796fbe6e0acbe)
file=A27_8_10_1740.txt sha256=bdbf1cf2b34d5a2771172cea5d11fe6abcff25a0de03cc60808796fbe6e0acbe
F format: lines=1740 claimed_M=1740 bad_lines=0
W weight/distinct: bad_weight=0 distinct=1740
B packing: t=7 subsets=208800 distinct=208800 collisions=0
A all-pairs: words=1740 pairs=1512930 min_distance=8 need>=8 bad_pairs=0 histogram={8: 178567, 10: 121676, 12: 676640, 14: 245659, 16: 261670, 18: 24724, 20: 3994}
R record_check: cell=A(27,8,10) M=1740 composite_bar=1737 (Andw=0, Trophy/PR=1737) strict_beat=True
VERDICT: VALID  A(27,8,10) >= 1740
M 1740 matches INDEX.csv
== Running negative control (duplicate/colliding codeword must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/A27_8_10_1740.txt`

From the V3R1T4S workspace root:

```sh
clang -O3 -march=native -pthread -o runs/2026-10-14-0428/attempts/c-evaluator-optimizer/code/cwc_lns runs/2026-10-14-0428/attempts/c-evaluator-optimizer/code/cwc_lns.c
python3 runs/2026-10-14-0428/attempts/c-evaluator-optimizer/code/run_lns_campaign.py
```
