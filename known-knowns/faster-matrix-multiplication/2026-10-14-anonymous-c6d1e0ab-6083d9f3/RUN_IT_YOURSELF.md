# Run It Yourself

## 1. Verify the Shipped Object (`object/4x13x15_m533_Z.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/4x13x15_m533_Z.json
sha256 matches INDEX.csv (6083d9f3d15c408b83094f0d8d2f48ce60ecb549856051182174e92f00aa5596)
PASS: object/4x13x15_m533_Z.json | format=4x13x15 class=Z max_abs=2 rank=533 | ref(Z)=536 saved=3 best_overall=520 valid_ring_upgrade=True
rank 533 matches INDEX.csv
== Running negative control (mutated entry in u[0] must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/4x13x15_m533_Z.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -o runs/2026-10-14-0338/attempts/c-evaluator-optimizer/code/zt_flip_reduce runs/2026-10-14-0338/attempts/c-evaluator-optimizer/code/zt_flip_reduce.c
python3 runs/2026-10-14-0338/attempts/representation-absorber/code/upgrade_schemes.py
```
