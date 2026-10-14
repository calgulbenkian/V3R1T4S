# Run It Yourself

## 1. Verify the Shipped Object (`object/9x13x14_m1039_Z.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/9x13x14_m1039_Z.json
sha256 matches INDEX.csv (bed17451925a1e9a484a2848faae3aca36011203fbd9e3277c73d673a8a57daa)
PASS: object/9x13x14_m1039_Z.json | format=9x13x14 class=Z max_abs=2 rank=1039 | ref(Z)=1050 saved=11 best_overall=1024 valid_ring_upgrade=True
rank 1039 matches INDEX.csv
== Running negative control (mutated entry in u[0] must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/9x13x14_m1039_Z.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -o runs/2026-10-14-0338/attempts/c-evaluator-optimizer/code/zt_flip_reduce runs/2026-10-14-0338/attempts/c-evaluator-optimizer/code/zt_flip_reduce.c
python3 runs/2026-10-14-0338/attempts/representation-absorber/code/upgrade_schemes.py
```
