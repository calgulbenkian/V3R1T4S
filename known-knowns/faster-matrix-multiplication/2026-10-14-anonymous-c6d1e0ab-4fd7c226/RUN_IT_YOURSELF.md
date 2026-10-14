# Run It Yourself

## 1. Verify the Shipped Object (`object/14x16x16_r2119_Q.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/14x16x16_r2119_Q.json
sha256 matches INDEX.csv (4fd7c2264911e65fcc6cf7074e6100202786a5de6c01b85b9ac6572fdf31ba56)
PASS file=14x16x16_r2119_Q.json format=14x16x16 rank=2119 primes=3 log2_bound=65
rank 2119 matches INDEX.csv
== Running negative control (mutated coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

You can also run the standalone verifier directly:
```sh
python3 verify-it-yourself/verify_brent.py object/14x16x16_r2119_Q.json
```

## 2. How to Rebuild `object/14x16x16_r2119_Q.json`

From the V3R1T4S workspace root:

```sh
python3 runs/2026-10-14-0004/attempts/representation-absorber/code/make_all_remaining_results.py
```
