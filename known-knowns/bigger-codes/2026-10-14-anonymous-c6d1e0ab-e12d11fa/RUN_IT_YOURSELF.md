# Run It Yourself

## 1. Verify the Shipped Object (`object/A56_8_7_4691.txt`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/A56_8_7_4691.txt
sha256 matches INDEX.csv (e12d11fa604fd790d622442b7d96815ed8b129256b45507a9f09bff518cf27b1)
file=A56_8_7_4691.txt sha256=e12d11fa604fd790d622442b7d96815ed8b129256b45507a9f09bff518cf27b1
F format: lines=4691 claimed_M=4691 bad_lines=0
W weight/distinct: bad_weight=0 distinct=4691
B packing: t=4 subsets=164185 distinct=164185 collisions=0
A all-pairs: words=4691 pairs=11000395 min_distance=8 need>=8 bad_pairs=0 histogram={8: 438664, 10: 1820540, 12: 4672305, 14: 4068886}
R record_check: cell=A(56,8,7) M=4691 composite_bar=4685 (Andw=0, Trophy/PR=4685) strict_beat=True
VERDICT: VALID  A(56,8,7) >= 4691
M 4691 matches INDEX.csv
== Running negative control (duplicate/colliding codeword must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/A56_8_7_4691.txt`

From the V3R1T4S workspace root:

```sh
clang -O3 -march=native -pthread -o runs/2026-10-14-0428/attempts/c-evaluator-optimizer/code/cwc_lns runs/2026-10-14-0428/attempts/c-evaluator-optimizer/code/cwc_lns.c
python3 runs/2026-10-14-0428/attempts/c-evaluator-optimizer/code/run_lns_campaign.py
```
