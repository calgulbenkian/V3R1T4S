# Run It Yourself

## 1. Verify the Shipped Object (`object/4x6x8_m140_cr546_fv288_cn1248_ZT_reduced.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/4x6x8_m140_cr546_fv288_cn1248_ZT_reduced.json
sha256 matches INDEX.csv (740500ff5c86434ddbb45c0e60d65af983dd457fbe6f1084e64e74480d7f53db)
PASS: 4x6x8_m140_cr546_fv288_cn1248_ZT_reduced.json | format=4x6x8 m=140 cr=546 (U=115, V=171, W=260) fv=288 cn=1248
cr 546 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/4x6x8_m140_cr546_fv288_cn1248_ZT_reduced.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -pthread -o runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt.c
python3 runs/2026-10-14-0312/attempts/representation-absorber/code/flip_cse.py
```
