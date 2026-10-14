# Run It Yourself

## 1. Verify the Shipped Object (`object/14x16x17_r2261_Q.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/14x16x17_r2261_Q.json
sha256 matches INDEX.csv (9daa4b495e91e98bb5da76cff692af959885766b07e33042b353e7ea94de7b3d)
PASS file=14x16x17_r2261_Q.json format=14x16x17 rank=2261 primes=2 log2_bound=50
rank 2261 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/14x16x17_r2261_Q.json`

From the V3R1T4S workspace root:

```sh
python3 runs/2026-10-14-0425/attempts/representation-absorber/code/cascade_17_18.py
```
