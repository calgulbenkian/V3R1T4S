# Run It Yourself

## 1. Verify the Shipped Object (`object/A45_8_7_1910.txt`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/A45_8_7_1910.txt
sha256 matches INDEX.csv (e9a786a8af3ad130a62167977ca106c4f1ffc99d134f798959fafb319e21c966)
file=A45_8_7_1910.txt sha256=e9a786a8af3ad130a62167977ca106c4f1ffc99d134f798959fafb319e21c966
F format: lines=1910 claimed_M=1910 bad_lines=0
W weight/distinct: bad_weight=0 distinct=1910
B packing: t=4 subsets=66850 distinct=66850 collisions=0
A all-pairs: words=1910 pairs=1823095 min_distance=8 need>=8 bad_pairs=0 histogram={8: 142038, 10: 385326, 12: 785387, 14: 510344}
R record_check: cell=A(45,8,7) M=1910 composite_bar=1907 (Andw=0, Trophy/PR=1907) strict_beat=True
VERDICT: VALID  A(45,8,7) >= 1910
M 1910 matches INDEX.csv
== Running negative control (duplicate/colliding codeword must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/A45_8_7_1910.txt`

From the V3R1T4S workspace root:

```sh
clang -O3 -march=native -pthread -o runs/2026-10-14-0428/attempts/c-evaluator-optimizer/code/cwc_lns runs/2026-10-14-0428/attempts/c-evaluator-optimizer/code/cwc_lns.c
python3 runs/2026-10-14-0428/attempts/c-evaluator-optimizer/code/run_lns_campaign.py
```
