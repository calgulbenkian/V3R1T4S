# Run It Yourself

## 1. Verify the Shipped Object (`object/A53_8_7_3992.txt`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/A53_8_7_3992.txt
sha256 matches INDEX.csv (7be7a08730ebb932aa2700285fab3cfcd0cd464759ca72013f3a238ee3a60a29)
file=A53_8_7_3992.txt sha256=7be7a08730ebb932aa2700285fab3cfcd0cd464759ca72013f3a238ee3a60a29
F format: lines=3992 claimed_M=3992 bad_lines=0
W weight/distinct: bad_weight=0 distinct=3992
B packing: t=4 subsets=139720 distinct=139720 collisions=0
A all-pairs: words=3992 pairs=7966036 min_distance=8 need>=8 bad_pairs=0 histogram={8: 403503, 10: 1398836, 12: 3427264, 14: 2736433}
R record_check: cell=A(53,8,7) M=3992 composite_bar=3987 (Andw=0, Trophy/PR=3987) strict_beat=True
VERDICT: VALID  A(53,8,7) >= 3992
M 3992 matches INDEX.csv
== Running negative control (duplicate/colliding codeword must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/A53_8_7_3992.txt`

From the V3R1T4S workspace root:

```sh
clang -O3 -march=native -pthread -o runs/2026-10-14-0428/attempts/c-evaluator-optimizer/code/cwc_lns runs/2026-10-14-0428/attempts/c-evaluator-optimizer/code/cwc_lns.c
python3 runs/2026-10-14-0428/attempts/c-evaluator-optimizer/code/run_lns_campaign.py
```
