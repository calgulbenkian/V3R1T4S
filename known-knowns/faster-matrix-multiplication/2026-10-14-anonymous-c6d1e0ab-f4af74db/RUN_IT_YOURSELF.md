# Run It Yourself

## 1. Verify the Shipped Object (`object/16x17x18_r2850_Q.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/16x17x18_r2850_Q.json
sha256 matches INDEX.csv (f4af74db369b2724e4ee67c937c5f66381994bfaf4fbfde4cce65da43d330773)
PASS file=16x17x18_r2850_Q.json format=16x17x18 rank=2850 primes=3 log2_bound=71
rank 2850 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/16x17x18_r2850_Q.json`

From the V3R1T4S workspace root:

```sh
python3 runs/2026-10-14-0425/attempts/representation-absorber/code/cascade_17_18.py
```
