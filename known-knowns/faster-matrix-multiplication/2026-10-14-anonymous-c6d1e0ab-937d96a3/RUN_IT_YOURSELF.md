# Run It Yourself

## 1. Verify the Shipped Object (`object/4x13x15_m535_ZT.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/4x13x15_m535_ZT.json
sha256 matches INDEX.csv (937d96a3adc5b64e84e86d8a0d9bc0b7e160f22f00f3ca4af7239abb76a281f2)
PASS: object/4x13x15_m535_ZT.json | format=4x13x15 class=ZT max_abs=1 rank=535 | ref(ZT)=536 saved=1 best_overall=520 valid_ring_upgrade=True
rank 535 matches INDEX.csv
== Running negative control (mutated entry in u[0] must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/4x13x15_m535_ZT.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -o runs/2026-10-14-0338/attempts/c-evaluator-optimizer/code/zt_flip_reduce runs/2026-10-14-0338/attempts/c-evaluator-optimizer/code/zt_flip_reduce.c
python3 runs/2026-10-14-0338/attempts/representation-absorber/code/upgrade_schemes.py
```
