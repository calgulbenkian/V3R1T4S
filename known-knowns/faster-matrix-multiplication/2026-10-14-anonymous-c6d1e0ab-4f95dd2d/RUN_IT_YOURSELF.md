# Run It Yourself

## 1. Verify the Shipped Object (`object/5x5x6_m110_cr451_fv202_cn1208_ZT_reduced.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/5x5x6_m110_cr451_fv202_cn1208_ZT_reduced.json
sha256 matches INDEX.csv (4f95dd2dbee2b93b8c8e102b863438193c7d6a5b899fcd0ec5a35661c115cd5d)
PASS: 5x5x6_m110_cr451_fv202_cn1208_ZT_reduced.json | format=5x5x6 m=110 cr=451 (U=119, V=124, W=208) fv=202 cn=1208
cr 451 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/5x5x6_m110_cr451_fv202_cn1208_ZT_reduced.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -pthread -o runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt.c
python3 runs/2026-10-14-0312/attempts/representation-absorber/code/flip_cse.py
```
