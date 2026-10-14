# Run It Yourself

## 1. Verify the Shipped Object (`object/16x18x18_r2900_Q.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/16x18x18_r2900_Q.json
sha256 matches INDEX.csv (0975cd66f4a942c0d5fd289c59c7d5a0703e86dee33b40911924de746c679de3)
PASS file=16x18x18_r2900_Q.json format=16x18x18 rank=2900 primes=3 log2_bound=71
rank 2900 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/16x18x18_r2900_Q.json`

From the V3R1T4S workspace root:

```sh
python3 runs/2026-10-14-0425/attempts/representation-absorber/code/cascade_17_18.py
```
