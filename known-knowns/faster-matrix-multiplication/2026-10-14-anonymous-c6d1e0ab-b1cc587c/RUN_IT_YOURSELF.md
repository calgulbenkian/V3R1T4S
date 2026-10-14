# Run It Yourself

## 1. Verify the Shipped Object (`object/3x5x5_m58_cr218_fv70_cn357_ZT_reduced.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/3x5x5_m58_cr218_fv70_cn357_ZT_reduced.json
sha256 matches INDEX.csv (b1cc587cfcd53662a62995834bb546248b177ba2dd46139fddcb726caf2d46ac)
PASS: 3x5x5_m58_cr218_fv70_cn357_ZT_reduced.json | format=3x5x5 m=58 cr=218 (U=52, V=70, W=96) fv=70 cn=357
cr 218 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/3x5x5_m58_cr218_fv70_cn357_ZT_reduced.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -pthread -o runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt.c
python3 runs/2026-10-14-0312/attempts/representation-absorber/code/flip_cse.py
```
