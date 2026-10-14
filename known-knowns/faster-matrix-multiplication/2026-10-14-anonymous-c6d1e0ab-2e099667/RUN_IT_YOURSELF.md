# Run It Yourself

## 1. Verify the Shipped Object (`object/4x5x5_m76_cr295_fv113_cn530_ZT_reduced.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/4x5x5_m76_cr295_fv113_cn530_ZT_reduced.json
sha256 matches INDEX.csv (2e09966726d94ad6ade2c53de92b73c0e2f78a2d39d2a4a52f50a0e61eef085d)
PASS: 4x5x5_m76_cr295_fv113_cn530_ZT_reduced.json | format=4x5x5 m=76 cr=295 (U=76, V=89, W=130) fv=113 cn=530
cr 295 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/4x5x5_m76_cr295_fv113_cn530_ZT_reduced.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -pthread -o runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt.c
python3 runs/2026-10-14-0312/attempts/representation-absorber/code/flip_cse.py
```
