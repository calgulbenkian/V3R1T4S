# Run It Yourself

## 1. Verify the Shipped Object (`object/16x17x17_r2553_Q.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/16x17x17_r2553_Q.json
sha256 matches INDEX.csv (b078e93d7574b8328b1cf8f865170e2d8c337ccf09b1c8b29d13462a89481540)
PASS file=16x17x17_r2553_Q.json format=16x17x17 rank=2553 primes=2 log2_bound=50
rank 2553 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/16x17x17_r2553_Q.json`

From the V3R1T4S workspace root:

```sh
python3 runs/2026-10-14-0425/attempts/representation-absorber/code/cascade_17_18.py
```
