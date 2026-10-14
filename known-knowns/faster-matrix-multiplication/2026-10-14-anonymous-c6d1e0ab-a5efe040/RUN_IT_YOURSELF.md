# Run It Yourself

## 1. Verify the Shipped Object (`object/9x10x14_m816_ZT.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/9x10x14_m816_ZT.json
sha256 matches INDEX.csv (a5efe04017632a0da87598ba3b2509ca66bb6fea965bb71a2faebb2aef582ab1)
PASS: object/9x10x14_m816_ZT.json | format=9x10x14 class=ZT max_abs=1 rank=816 | ref(ZT)=820 saved=4 best_overall=808 valid_ring_upgrade=True
rank 816 matches INDEX.csv
== Running negative control (mutated entry in u[0] must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/9x10x14_m816_ZT.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -o runs/2026-10-14-0338/attempts/c-evaluator-optimizer/code/zt_flip_reduce runs/2026-10-14-0338/attempts/c-evaluator-optimizer/code/zt_flip_reduce.c
python3 runs/2026-10-14-0338/attempts/representation-absorber/code/upgrade_schemes.py
```
