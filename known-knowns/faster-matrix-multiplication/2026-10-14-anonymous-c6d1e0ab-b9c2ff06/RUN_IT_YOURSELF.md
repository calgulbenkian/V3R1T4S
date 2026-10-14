# Run It Yourself

## 1. Verify the Shipped Object (`object/15x15x17_r2257_Q.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/15x15x17_r2257_Q.json
sha256 matches INDEX.csv (b9c2ff0681dca344541f2bb281f4fc6e7ebd9e3762160ba1a29f58a814f2d8af)
PASS file=15x15x17_r2257_Q.json format=15x15x17 rank=2257 primes=2 log2_bound=50
rank 2257 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/15x15x17_r2257_Q.json`

From the V3R1T4S workspace root:

```sh
python3 runs/2026-10-14-0425/attempts/representation-absorber/code/cascade_17_18.py
```
