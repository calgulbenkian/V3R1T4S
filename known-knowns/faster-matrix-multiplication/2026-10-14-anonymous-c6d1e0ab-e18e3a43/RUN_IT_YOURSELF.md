# Run It Yourself

## 1. Verify the Shipped Object (`object/16x16x17_r2392_Q.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/16x16x17_r2392_Q.json
sha256 matches INDEX.csv (e18e3a43ba7b29da2e9683b93ec8dcfabed75f35c4c6aa515dc8d7f7a4fe183b)
PASS file=16x16x17_r2392_Q.json format=16x16x17 rank=2392 primes=2 log2_bound=51
rank 2392 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/16x16x17_r2392_Q.json`

From the V3R1T4S workspace root:

```sh
python3 runs/2026-10-14-0425/attempts/representation-absorber/code/cascade_17_18.py
```
