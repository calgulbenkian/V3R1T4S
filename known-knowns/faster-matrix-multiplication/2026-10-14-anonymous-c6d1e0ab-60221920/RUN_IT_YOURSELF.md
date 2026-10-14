# Run It Yourself

## 1. Verify the Shipped Object (`object/4x5x6_m90_cr374_fv179_cn1008_ZT_reduced.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/4x5x6_m90_cr374_fv179_cn1008_ZT_reduced.json
sha256 matches INDEX.csv (60221920dc02e9a5198d6df81dbafa70f481f0367db9600fe418b21dc220584a)
PASS: 4x5x6_m90_cr374_fv179_cn1008_ZT_reduced.json | format=4x5x6 m=90 cr=374 (U=86, V=114, W=174) fv=179 cn=1008
cr 374 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/4x5x6_m90_cr374_fv179_cn1008_ZT_reduced.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -pthread -o runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt.c
python3 runs/2026-10-14-0312/attempts/representation-absorber/code/flip_cse.py
```
