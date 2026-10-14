# Run It Yourself

## 1. Verify the Shipped Object (`object/7x8x15_m570_Z.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/7x8x15_m570_Z.json
sha256 matches INDEX.csv (9f0a232de00ce5220d75097b9af6986f97d81932fa3e3718e1291d426f4caede)
PASS: object/7x8x15_m570_Z.json | format=7x8x15 class=Z max_abs=2 rank=570 | ref(Z)=571 saved=1 best_overall=557 valid_ring_upgrade=True
rank 570 matches INDEX.csv
== Running negative control (mutated entry in u[0] must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/7x8x15_m570_Z.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -o runs/2026-10-14-0338/attempts/c-evaluator-optimizer/code/zt_flip_reduce runs/2026-10-14-0338/attempts/c-evaluator-optimizer/code/zt_flip_reduce.c
python3 runs/2026-10-14-0338/attempts/representation-absorber/code/upgrade_schemes.py
```
