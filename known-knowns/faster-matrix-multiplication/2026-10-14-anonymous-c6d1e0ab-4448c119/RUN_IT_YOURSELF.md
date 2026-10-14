# Run It Yourself

## 1. Verify the Shipped Object (`object/4x5x7_m104_cr395_fv161_cn931_ZT_reduced.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/4x5x7_m104_cr395_fv161_cn931_ZT_reduced.json
sha256 matches INDEX.csv (4448c119d128c8be762c29223b43d7486bd9bb7acc9633d9d6fd23110445aa72)
PASS: 4x5x7_m104_cr395_fv161_cn931_ZT_reduced.json | format=4x5x7 m=104 cr=395 (U=96, V=116, W=183) fv=161 cn=931
cr 395 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/4x5x7_m104_cr395_fv161_cn931_ZT_reduced.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -pthread -o runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt.c
python3 runs/2026-10-14-0312/attempts/representation-absorber/code/flip_cse.py
```
