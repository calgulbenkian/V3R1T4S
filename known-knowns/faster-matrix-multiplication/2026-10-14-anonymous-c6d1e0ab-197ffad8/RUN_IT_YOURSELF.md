# Run It Yourself

## 1. Verify the Shipped Object (`object/3x4x5_m47_cr159_fv60_cn277_ZT_reduced.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/3x4x5_m47_cr159_fv60_cn277_ZT_reduced.json
sha256 matches INDEX.csv (197ffad82f4cdd3ea6899fe41fc93c1b7c16917cfa5dba26199fe8143c06292d)
PASS: 3x4x5_m47_cr159_fv60_cn277_ZT_reduced.json | format=3x4x5 m=47 cr=159 (U=39, V=46, W=74) fv=60 cn=277
cr 159 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/3x4x5_m47_cr159_fv60_cn277_ZT_reduced.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -pthread -o runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt.c
python3 runs/2026-10-14-0312/attempts/representation-absorber/code/flip_cse.py
```
