# Run It Yourself

## 1. Verify the Shipped Object (`object/15x16x17_r2313_Q.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/15x16x17_r2313_Q.json
sha256 matches INDEX.csv (53e05e6d257401e1089d7ace8d42b7cbde78f8992e90223791fea6c1df50da57)
PASS file=15x16x17_r2313_Q.json format=15x16x17 rank=2313 primes=2 log2_bound=50
rank 2313 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/15x16x17_r2313_Q.json`

From the V3R1T4S workspace root:

```sh
python3 runs/2026-10-14-0425/attempts/representation-absorber/code/cascade_17_18.py
```
