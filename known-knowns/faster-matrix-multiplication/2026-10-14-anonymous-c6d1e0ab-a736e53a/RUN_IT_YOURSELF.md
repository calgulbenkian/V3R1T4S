# Run It Yourself

## 1. Verify the Shipped Object (`object/4x14x15_m569_Z.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/4x14x15_m569_Z.json
sha256 matches INDEX.csv (a736e53a74f68425c0211816e0972faf8c027d4845885509b530644e9f64c52b)
PASS: object/4x14x15_m569_Z.json | format=4x14x15 class=Z max_abs=2 rank=569 | ref(Z)=572 saved=3 best_overall=557 valid_ring_upgrade=True
rank 569 matches INDEX.csv
== Running negative control (mutated entry in u[0] must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/4x14x15_m569_Z.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -o runs/2026-10-14-0338/attempts/c-evaluator-optimizer/code/zt_flip_reduce runs/2026-10-14-0338/attempts/c-evaluator-optimizer/code/zt_flip_reduce.c
python3 runs/2026-10-14-0338/attempts/representation-absorber/code/upgrade_schemes.py
```
