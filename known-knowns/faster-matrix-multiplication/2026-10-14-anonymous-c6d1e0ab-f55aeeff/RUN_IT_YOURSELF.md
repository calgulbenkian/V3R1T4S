# Run It Yourself

## 1. Verify the Shipped Object (`object/13x14x14_r1541_Q.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/13x14x14_r1541_Q.json
sha256 matches INDEX.csv (f55aeeff8aa61d1b246890045a1122b4564a8a15e179adc4a2e5b8d65943081d)
PASS file=13x14x14_r1541_Q.json format=13x14x14 rank=1541 primes=2 log2_bound=50
rank 1541 matches INDEX.csv
== Running negative control (mutated coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

You can also run the standalone verifier directly:
```sh
python3 verify-it-yourself/verify_brent.py object/13x14x14_r1541_Q.json
```

## 2. How to Rebuild `object/13x14x14_r1541_Q.json`

From the V3R1T4S workspace root:

```sh
python3 runs/2026-10-14-0004/attempts/representation-absorber/code/make_all_remaining_results.py
```
