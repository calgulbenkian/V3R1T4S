# Run It Yourself

## 1. Verify the Shipped Object (`object/13x14x15_r1646_Q.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/13x14x15_r1646_Q.json
sha256 matches INDEX.csv (82f6c819ed1d02c0bd1aad307a76b7bea80f2852aeab041132f584c6e1800be2)
PASS file=13x14x15_r1646_Q.json format=13x14x15 rank=1646 primes=2 log2_bound=49
rank 1646 matches INDEX.csv
== Running negative control (mutated coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

You can also run the standalone verifier directly:
```sh
python3 verify-it-yourself/verify_brent.py object/13x14x15_r1646_Q.json
```

## 2. How to Rebuild `object/13x14x15_r1646_Q.json`

From the V3R1T4S workspace root:

```sh
python3 runs/2026-10-14-0004/attempts/representation-absorber/code/make_all_remaining_results.py
```
