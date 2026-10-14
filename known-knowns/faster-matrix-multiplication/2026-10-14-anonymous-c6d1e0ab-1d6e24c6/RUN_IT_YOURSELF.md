# Run It Yourself

## 1. Verify the Shipped Object (`object/5x5x7_m127_cr525_fv245_cn1602_ZT_reduced.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/5x5x7_m127_cr525_fv245_cn1602_ZT_reduced.json
sha256 matches INDEX.csv (1d6e24c6edebc809e6d6cfa7a3ecfec0f9b00550ebcf92c3289d510eb1f091fd)
PASS: 5x5x7_m127_cr525_fv245_cn1602_ZT_reduced.json | format=5x5x7 m=127 cr=525 (U=127, V=150, W=248) fv=245 cn=1602
cr 525 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/5x5x7_m127_cr525_fv245_cn1602_ZT_reduced.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -pthread -o runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt.c
python3 runs/2026-10-14-0312/attempts/representation-absorber/code/flip_cse.py
```
