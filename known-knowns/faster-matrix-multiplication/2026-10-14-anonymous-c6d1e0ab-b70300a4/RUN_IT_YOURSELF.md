# Run It Yourself

## 1. Verify the Shipped Object (`object/14x17x17_r2403_Q.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/14x17x17_r2403_Q.json
sha256 matches INDEX.csv (b70300a45b0a9ae1de0ce9196b43e1c546a49f072943d9f90c139e2686c7ebb9)
PASS file=14x17x17_r2403_Q.json format=14x17x17 rank=2403 primes=2 log2_bound=50
rank 2403 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/14x17x17_r2403_Q.json`

From the V3R1T4S workspace root:

```sh
python3 runs/2026-10-14-0425/attempts/representation-absorber/code/cascade_17_18.py
```
