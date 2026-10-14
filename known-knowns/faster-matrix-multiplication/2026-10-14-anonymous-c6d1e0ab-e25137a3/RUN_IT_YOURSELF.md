# Run It Yourself

## 1. Verify the Shipped Object (`object/9x11x14_m889_Z.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/9x11x14_m889_Z.json
sha256 matches INDEX.csv (e25137a39f9a642d3a93ae58337d80703f5e45c2efc48e96207d7e61aeb101e5)
PASS: object/9x11x14_m889_Z.json | format=9x11x14 class=Z max_abs=2 rank=889 | ref(Z)=900 saved=11 best_overall=882 valid_ring_upgrade=True
rank 889 matches INDEX.csv
== Running negative control (mutated entry in u[0] must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/9x11x14_m889_Z.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -o runs/2026-10-14-0338/attempts/c-evaluator-optimizer/code/zt_flip_reduce runs/2026-10-14-0338/attempts/c-evaluator-optimizer/code/zt_flip_reduce.c
python3 runs/2026-10-14-0338/attempts/representation-absorber/code/upgrade_schemes.py
```
