# Run It Yourself

## 1. Verify the Shipped Object (`object/15x17x17_r2463_Q.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/15x17x17_r2463_Q.json
sha256 matches INDEX.csv (a3151b1a973de743875f597a306179204d17a61b3147991c1167e73a7806d7b9)
PASS file=15x17x17_r2463_Q.json format=15x17x17 rank=2463 primes=2 log2_bound=49
rank 2463 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/15x17x17_r2463_Q.json`

From the V3R1T4S workspace root:

```sh
python3 runs/2026-10-14-0425/attempts/representation-absorber/code/cascade_17_18.py
```
