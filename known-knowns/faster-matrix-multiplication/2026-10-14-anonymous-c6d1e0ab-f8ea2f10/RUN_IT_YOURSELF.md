# Run It Yourself

## 1. Verify the Shipped Object (`object/4x6x7_m123_cr505_fv237_cn1573_ZT_reduced.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/4x6x7_m123_cr505_fv237_cn1573_ZT_reduced.json
sha256 matches INDEX.csv (f8ea2f1002c2100a61df1ee19be3bf1335a80c1990b2a3d4f3217feebcc52869)
PASS: 4x6x7_m123_cr505_fv237_cn1573_ZT_reduced.json | format=4x6x7 m=123 cr=505 (U=121, V=159, W=225) fv=237 cn=1573
cr 505 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/4x6x7_m123_cr505_fv237_cn1573_ZT_reduced.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -pthread -o runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt.c
python3 runs/2026-10-14-0312/attempts/representation-absorber/code/flip_cse.py
```
